import matplotlib
import numpy as np
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sympy import *
from PySide2.QtCore import Qt

matplotlib.use('Qt5Agg')  # Render to PySide/PyQt Canvas

from equation_parsing import translate


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=600, height=600, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))
        fig.suptitle('f(x)', fontsize=14, fontweight='bold')
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('f(x)')
        self.axes.text(0.5, 0.5, 'Please, Enter an Equation and Hit Plot\ne.g. exp(x) or x^2 or sin(x)',
                       verticalalignment='center', horizontalalignment='center',
                       transform=self.axes.transAxes,
                       color='blue', fontsize=32)
        super(Canvas, self).__init__(fig)


class Form(QFormLayout):
    def __init__(self):
        super(Form, self).__init__()

        # generate the canvas to display the plot
        self.canvas = Canvas()
        pixmap = QPixmap("logo.png")
        self.Title = QLabel()
        self.Title.setMargin(20)
        self.Title.setPixmap(pixmap)
        self.Title.setAlignment(Qt.AlignHCenter)
        # add input field with label
        self.label = QLabel('f(x) =')
        self.input_field = QLineEdit()
        # Add a button
        self.button = QPushButton("Plot")
        self.button.setMaximumWidth(200)
        self.button.clicked.connect(lambda: self.onClicked())

        self.window = QWidget()

        self.horiz_layout = QHBoxLayout()
        self.horiz_layout.addWidget(self.label)
        self.horiz_layout.addWidget(self.input_field)
        self.horiz_layout.addWidget(self.button)
        self.horiz_layout.setContentsMargins(100, 5, 100, 5)

        self.horiz_layout2 = QHBoxLayout()
        self.xlim1 = QLineEdit()
        self.xlim1.setValidator(QIntValidator())
        self.xlim1.setAlignment(Qt.AlignLeft)

        self.xlim1_label = QLabel('x: from')

        self.xlim2 = QLineEdit()
        self.xlim2.setValidator(QIntValidator())
        self.xlim2.setAlignment(Qt.AlignLeft)

        self.xlim2_label = QLabel('to')

        self.horiz_layout2.addWidget(self.xlim1_label)
        self.horiz_layout2.addWidget(self.xlim1)
        self.horiz_layout2.addWidget(self.xlim2_label)
        self.horiz_layout2.addWidget(self.xlim2)

        self.horiz_layout2.setContentsMargins(400, 5, 400, 5)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.Title)
        self.layout.addLayout(self.horiz_layout)
        self.layout.addLayout(self.horiz_layout2)
        self.layout.addWidget(self.canvas)
        self.window.setLayout(self.layout)

    def show(self):
        self.window.show()

    def onClicked(self):
        print("clicked")
        equation = self.input_field.text()
        x1, x2 = self.xlim1.text(), self.xlim2.text()
        if equation != '':
            if x1 == '' and x2 == '':
                x_vals, y_vals = self.generate_data(equation)
            else:
                x_vals, y_vals = self.generate_data(equation, int(x1), int(x2))
            print(x_vals, y_vals)
            try:
                self.canvas.axes.cla()  # Clear the canvas.
                self.canvas.axes.plot(x_vals, y_vals, "r")
                # Trigger the canvas to update and redraw.
                self.canvas.axes.set_xlabel('x')
                self.canvas.axes.set_ylabel('f(x)')
                self.canvas.draw()
            except Exception as e:
                self.handle_error('wrong equation')
        else:
            self.handle_error('empty equation')

    def parse_equation(self, eq=None):
        try:
            if eq is None:
                eq = self.input_field.text()
            return translate(eq)
        except Exception as e:
            self.handle_error('parse')

    def generate_data(self, eq=None, x1=0, x2=10):
        try:
            x = symbols('x')
            y = self.parse_equation(eq)
            lam_x = lambdify(x, y, modules=['numpy'])
            x_vals = np.linspace(x1, x2)
            y_vals = lam_x(x_vals)
            return x_vals, y_vals
        except Exception as e:
            self.handle_error('wrong equation')

    def handle_error(self, err):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        msg.setText("Error")
        msg.setInformativeText(str(err))
        msg.setWindowTitle("Error")
        msg.setDetailedText(
            "Hint: \nthe equation must be a function of (x) \ne.g. x^2 or sin(x) or ln(x) or exp(x)")
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()
