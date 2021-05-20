import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from calculator import Ui_MainWindow
from enum import Enum

class Operation(Enum):
    plus = 1
    minus = 2
    mul = 3
    div = 4
    power = 5

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.calculator = Ui_MainWindow()
        self.calculator.setupUi(self)
        self.init_calc()

    def init_calc(self):
        self.calculator.plus_btn.clicked.connect(lambda: self.Operation(Operation.plus))
        self.calculator.minus_btn.clicked.connect(lambda: self.Operation(Operation.minus))
        self.calculator.multipl_btn.clicked.connect(lambda: self.Operation(Operation.mul))
        self.calculator.division_btn.clicked.connect(lambda: self.Operation(Operation.div))
        self.calculator.power_btn.clicked.connect(lambda: self.Operation(Operation.power))

    def Operation(self, operation):
        try:
            arg1 = float(self.calculator.first_lineEdit.text())
            arg2 = float(self.calculator.second_lineEdit.text())
            result = 0
            if(operation == Operation.plus):
                result = arg1 + arg2
            if(operation == Operation.minus):
                result = arg1 - arg2
            if(operation == Operation.mul):
                result = arg1 * arg2
            if(operation == Operation.div):
                result = arg1 / arg2
            if(operation == Operation.power):
                result = pow(arg1, arg2)
            self.calculator.result_lineEdit.setText(str(result))
        except Exception:
            self.calculator.result_lineEdit.setText('Invalid arguments')



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()  
