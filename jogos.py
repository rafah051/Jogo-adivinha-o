import forca
import jogoadivinhacao

print("************************************")
print('********Escolha o seu jogo!*********')
print("************************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

#CRIANDO A CONDIÇÃO

if(jogo == 1):
    print('Jogando jogo Forca')
    forca.jogar_forca()
else:
    print('Jogando jogo da Adivinhação')
    jogoadivinhacao.jogar_adivinhação()