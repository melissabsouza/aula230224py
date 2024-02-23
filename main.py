from pprint import pprint

# arquivo = open("./exemplo.txt")

# texto = arquivo.read()

# texto = arquivo.readlines()
# texto = arquivo.readline()

# for line in arquivo:
#     print(line)

# with open("./exemplo.txt") as file:
#     for line in arquivo:
#         print(line)

# with open("arquivo-escrita.txt", "w") as f:
#
#      f.write('oi')
#
# with open("exemplo.txt", "r+") as f:
#      texto = f.read()
#      f.write("\nNovalinha")


arquivo = open("./exemplo.txt")
texto = arquivo.readlines()

conta_letras = {}
conta_palavras = {}

for linha in texto:
     palavras = linha.split()

     for palavra in palavras:
           conta_palavras[palavra] = conta_palavras.get(palavra, 0) + 1

           for letra in palavra: 
                 conta_letras[letra] = conta_letras.get(letra,0) + 1




# pprint(conta_letras)
# pprint(conta_palavras)

max_palavras = [None, 0]
max_char= [None, 0]

for palavra, count in conta_palavras.items():
      if max_palavras[1] < count:
            max_palavras= [palavra, count]

for char, count in conta_letras.items():
      if max_char[1] < count:
            max_char= [char, count]

print(max_palavras)
print(max_char)

with open("result.txt", "w")as f:
     f.write(f"palavra mais frequente: {max_palavras[0]}\n")
     f.write(f"frequencia: {max_palavras[1]}\n")
     f.write(f"letra frequente: {max_char[0]}\n")
     f.write(f"frequencia: {max_char[1]}\n")


      
      

# for letra in texto:

#      letra
#      # conta_letras[letra] = conta_letras.get(letra,0) + 1

#      print(conta_letras)
