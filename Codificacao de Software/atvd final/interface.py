import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app = QApplication(sys.argv) #objeto para criar a aplicação

inicial = QWidget()
inicial.resize(480,720)
inicial.setWindowTitle("ANDRBANK")

# texto = QLabel("", inicial)
# texto.move(20, 120) # posicionando a label na tela

# entrada_texto = QLineEdit("", inicial)
# entrada_texto.setGeometry(20,140,200,20)

# texto2 = QLabel("Número 2", inicial)
# texto2.move(20, 160) # posicionando a label na tela
# entrada_texto2 = QLineEdit("", inicial)
# entrada_texto2.setGeometry(20,180,200,20)

# resultado = QLabel("Resultado: ", inicial)
# resultado.move(20, 200) # posicionando a label na tela

botao1 = QPushButton("ENTRAR", inicial)
botao1.setGeometry(190,550,100,40)
botao1.setStyleSheet('background-color:purple; color:white; font-size: 20px; border-radius: 20px;')


inicial.show()
app.exec()



