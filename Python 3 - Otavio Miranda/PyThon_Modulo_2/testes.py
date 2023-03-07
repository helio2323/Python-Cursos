caminho = 'D:\\VSCode\\Python\\'
arquivo = 'infsTest.txt'

caminho_arquivo = caminho + arquivo

arquivo = open(caminho_arquivo, 'w')

arquivo.close()

print(caminho_arquivo)