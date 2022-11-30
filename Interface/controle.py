# Codigo Principal
from PyQt5 import uic, QtWidgets
import mysql.connector
import uteis

banco = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    database='cadastro'
)


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    c = ''
    if formulario.radioButton.isChecked():
        print(f'Categoria: Alimentos')
        c = 'Alimentos'
    elif formulario.radioButton_2.isChecked():
        print(f'Categoria: Eletronicos')
        c = 'Eletronicos'
    elif formulario.radioButton_3.isChecked():
        print(f'Categoria: Móveis')
        c = 'Moveis'
    else:
        print('Categoria: Outros')
        c = 'Outros'

    print(f'Codigo: {linha1}')
    print(f'Descrição: {linha2}')
    print(f'Preço: R${linha3}')

    #if uteis.arqExiste(a):
    #    print('Arquivo encontrado com sucesso!')
    #else:
    #    uteis.CriarArquvivo(a)
    #uteis.escrever(a, linha1, linha2, linha3, c)

    cursor = banco.cursor()
    comando_sql = f"INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s, %s, %s, %s)"
    dados = (str(linha1), str(linha2), str(linha3), c)
    cursor.execute(comando_sql, dados)
    banco.commit()


#a = 'cadastro.txt'
app = QtWidgets.QApplication([])
formulario = uic.loadUi("CadastroProduto.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
