import sys
from PySide2.QtWidgets import (QMainWindow, QApplication, QTableView,
                               QFrame, QVBoxLayout, QPushButton,QLineEdit)
from PySide2.QtCore import Qt, QSize
from PySide2.QtSql import QSqlDatabase, QSqlTableModel

import re

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("banco.db")
db.open()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(600,400))
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)
        
        self.model.setTable("notas")
        #self.model.setSort(1,Qt.DescendingOrder)
        #self.model.setSort(1,Qt.AscendingOrder)
        #self.model.removeColumns(0,1)
        #self.model.removeColumns(3,1)
        
        colunas = ['index', 'ipi']
        
        for c in colunas:
            id = self.model.fieldIndex(c)
            self.model.removeColumns(id, 1)
        
        self.model.select()
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    
        self.filtro = QLineEdit()
        self.btn_alterar = QPushButton("alterar valoes")

        layout = QVBoxLayout()
        layout.addWidget(self.filtro) 
        layout.addWidget(self.table)
        layout.addWidget(self.btn_alterar)
        
        container = QFrame()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        self.btn_alterar.clicked.connect(self.alterar_dados)
        self.filtro.textChanged.connect(self.filtrar_nota)
        
               
    def alterar_dados(self):
        
        self.model.submitAll()
        
    def reverter(self):    
        self.model.revertAll()
        
    def filtrar_nota(self, s):
        s = re.sub('[\W_]+','',s)
        filter_str = f'Notas LIKE "%{s}%"'
        self.model.setFilter(filter_str)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
