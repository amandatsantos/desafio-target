#5 Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

print("--"*30,"\n")

entrada_usuario = input("digite frase/palavra para ser convertida: ")

string_converte = ''

for x in range(len(entrada_usuario)-1,-1, -1):
    string_converte += entrada_usuario[x]

print(f"\nconversão da entrada ->  {entrada_usuario}  :  {string_converte}\n")
print("--"*30,"\n")