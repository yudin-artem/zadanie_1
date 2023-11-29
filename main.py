import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QApplication


class coffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        self.model = QSqlTableModel(self, db)
        self.model.setTable('coffee')
        self.model.select()

        self.view.setModel(self.model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = coffee()
    ex.show()
    sys.exit(app.exec())