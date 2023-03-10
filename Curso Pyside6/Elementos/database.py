import pandas as pd
import sqlite3

cnx = sqlite3.connect('banco.db')

data = pd.DataFrame( [
            ['001', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['002', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['003', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['004', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['005', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['006', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['007', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['008', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['009', 'R$100,00','R$ 18,00','R$ 5,00'],
        ],columns=['Notas','Valor', 'icms', 'ipi'])

data.to_sql('notas', con= cnx)        