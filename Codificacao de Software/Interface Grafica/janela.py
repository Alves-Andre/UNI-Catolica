import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

def muda_valor_universidade():
    texto.setText(texto.text() + " Universidade Federal do Tocantins")
    texto.adjustSize()
    botao1.setText("Eu fui clicado")

def muda_valor():
    texto_digitado = entrada_texto.text()
    texto.setText(texto_digitado)

def somar():
    valor1 = entrada_texto.text()
    valor2 = entrada_texto2.text()
    soma = int(valor1) + int(valor2)
    resultado.setText("Resultado: " + str(soma))
    resultado.adjustSize()

app = QApplication(sys.argv) #objeto para criar a aplicação

janela = QWidget()
janela.resize(800,600)
janela.setWindowTitle("Titulo do meu programa")

texto = QLabel("Número 1", janela)
texto.move(20, 120) # posicionando a label na tela

entrada_texto = QLineEdit("", janela)
entrada_texto.setGeometry(20,140,200,20)

texto2 = QLabel("Número 2", janela)
texto2.move(20, 160) # posicionando a label na tela
entrada_texto2 = QLineEdit("", janela)
entrada_texto2.setGeometry(20,180,200,20)

resultado = QLabel("Resultado: ", janela)
resultado.move(20, 200) # posicionando a label na tela

botao1 = QPushButton("Somar", janela)
botao1.setGeometry(20,220,80,40)
botao1.setStyleSheet('background-color:grey; color:white')

botao1.clicked.connect(somar)

janela.show()
app.exec()



