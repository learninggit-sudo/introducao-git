import os 

nome=input('nome do arquivo: ')


#teste pica das galaxia receba
if os.path.exists(nome):

    with open(nome,'r') as arquivo:
        dados = ''

        while True:
            bloco = arquivo.read(4096)
            if not bloco:
                break
            dados += bloco

        caracteres = len(dados)
        palavras = len(dados.split())
        print(f"\nquantiadde de caracteres: {caracteres} \nquantidade de palavras : {palavras}\n")
        #numero de ocorrencias
        contagem = {}
        lista_palavras= dados.split()
        quantidade_palavras =len(lista_palavras)

        for palavra in lista_palavras:
            if palavras in contagem:
                contagem[palavra] += 1
            else:
                contagem[palavra] = 1
        
        print("repetições de palavras:")
        for palavra, quantidade in contagem.items():
            print(f'{palavra}: {quantidade}')
else:
    print("O arquivo não existe.")    