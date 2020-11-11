import getpass
import sys
from time import sleep
usuario = getpass.getuser()
print ("------------------------------------------------------------------ \n")
print ("Criptografia \n")
print("------------------------------------------------------------------- \n")



#recebe a chave de critografia e valida
chave = 31


base = 'abcdefghijklmnopqrstuvwxyz!@#$_ '

#escolhe o modo
modo = str(input("Deseja encriptar(e) ou descriptar(d)? \n Digite sua opção com 'e' ou 'd': " ))
             

#insere o texto final
cripto =' '

    #escolhe o modo
if (modo == 'e' ) :
    #insere e formata o texto
    text= input("Digite o texto a ser criptografado\n")
    text = text.lower()

    for word in text:
                #encontra o numero da posição dp word na base
        posicion = base.find(word)

            #soma a chave á posição
        posicion += chave

            # se a posição for maior que a base ira calcular a diferença
        if(posicion > len(base)):
            posicion = posicion - len(base)

    #concatena a o word encontrado           
        cripto = cripto + base[posicion]

elif (modo == 'd'):
    #insere e formata o texto
    text= input("Digite o texto a ser criptografado\n")
    text = text.lower()
        # contador do texto
            # recebe o word da posição
            #condição se o word estiver contido na base
    for word in text:
            #encontra a posição
        posicion = base.find(word)
            #subtrai a chave
        posicion -= chave
            #condicional se a posição foi menor que 0
        if posicion < 0:
            # subtrai o valor absoluto da base para encontrar a posição
            posicion = len(base)- abs(posicion)

    #resultado            
        cripto = cripto + base[posicion]   

if (modo == 'e'):
    arquivo = open("C:\\Users\\" + usuario + "\\Desktop\\Criptografia.txt", "w")
    arquivo.write("Mensagem: "+ cripto)
    print("Arquivo .txt criado na area de trabalho")
    

if (modo == 'd'):
    arquivo = open("C:\\Users\\" + usuario + "\\Desktop\\Descriptografia.txt", "w")
    arquivo.write("Mensagem: "+ cripto)
    print("Arquivo .txt criado na area de trabalho")

#da para o usuario a chance de finalizar o programa
saida = input("Aperte qualquer tecla para sair do sistema")
while cripto == True:
    sys.exit()
   











