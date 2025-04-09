import os 

nome=input('nome do arquivo\n')

if os.path.exists(nome):
    print("sim")

    with open(nome,'r') as arquivo:
        dados = ''

        while True:
            bloco = arquivo.read(4096)
            if not bloco:
                break
            dados += bloco

        caracteres = len(dados)
        palavras = len(dados.split())
        print(caracteres,palavras)
        #numero de ocorrencias

else:
    print("nao")    