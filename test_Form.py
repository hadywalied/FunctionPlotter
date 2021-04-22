import sys
import unittest
from unittest import TestCase

import pytest
from PySide2 import QtCore
from PySide2.QtTest import QTest
from PySide2.QtWidgets import *
from pytestqt import *
from pytestqt.plugin import qtbot

from Form import *

app = QApplication()


class FormTest(TestCase):
    def setUp(self) -> None:
        self.form = Form()

    def setEquationToX(self):
        """Set all the elements for plotting f(x) = x"""
        self.form.input_field.setText('x')
        self.form.xlim1.setText(-10)
        self.form.xlim2.setText(10)

    def test_checkTheLabelsAreShowingCorrectly(self):
        assert self.form.label.text() == "f(x) ="
        assert self.form.xlim1_label.text() == 'x: from'
        assert self.form.xlim2_label.text() == 'to'

    def test_ButtonClickOnInputX(self):
        """test the plotting of f(x)=x"""
        self.form.input_field.clear()
        QTest.keyClicks(self.form.input_field, "x")
        assert self.form.input_field.text() == "x"
        QTest.mouseClick(self.form.button, QtCore.Qt.LeftButton)
        assert self.form.canvas.figure is not None

    def test_ButtonClickOnInput_e_of_x(self):
        """test the plotting of f(x)=e(x)"""
        self.form.input_field.clear()
        QTest.keyClicks(self.form.input_field, "e(x)")
        assert self.form.input_field.text() == "e(x)"
        QTest.mouseClick(self.form.button, QtCore.Qt.LeftButton)
        assert self.form.msg.text() == 'Error'


if __name__ == "__main__":
    unittest.main()
