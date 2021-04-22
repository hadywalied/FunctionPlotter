import sys
from PySide2 import *
from Form import *


def main():
    app = QApplication()
    app.setApplicationDisplayName("Function Plotter")
    app.setStyle("fusion")

    form = Form()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
