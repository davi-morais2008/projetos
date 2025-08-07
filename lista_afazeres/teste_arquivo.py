# cria o arquivo - x
# f = open("C:/Users/SENAI/Desktop/projetos/teste2.txt", "x")

# imprime o que contem no arquvio
# with open("C:/Users/SENAI/Desktop/projetos/teste.txt") as f:
#     print(f.read())

# escreve no arquivo - a
with open("C:/Users/SENAI/Desktop/projetos/teste.txt", "w") as f:
    f.write("Escrevendo no arquivo\n")


# escreve e substitui o que continha no arquivo - w
with open("C:/Users/SENAI/Desktop/projetos/teste.txt", "a") as f:
    f.write("Adcionando")



