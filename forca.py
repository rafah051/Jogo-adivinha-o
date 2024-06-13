def jogar_forca():

    print('*********************************')
    print('Bem vindo, ao JOGO FORCA')
    print('*********************************')
    #Definir qual a palavra secreta
    palavraSecreta = "morango"
    
    letras_acertadas = ['_','_','_','_','_','_','_']

    enforcou = False
    acertou = False

    #Enquanto o jogador não se "enforcar" E não acertar a palavra, faça algo
    while(not enforcou and not acertou):
        
        chute = input ('Qual a letra?')
        chute = chute.strip()

        index = 0 
        for letra in palavraSecreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1 
        print(letras_acertadas)
        print("Jogando....")


    print("Fim de jogo!")
if(__name__ == "__main__"):
    jogar_forca()