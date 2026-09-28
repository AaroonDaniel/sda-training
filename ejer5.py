#Obtener la representacion inversa de una cadena de caracteres

palabra = input('Ingrese la palabra: ')

tam = len(palabra)
c = tam -1;
nueva = ''
for i in range(tam):
    nueva = nueva + palabra[c]
    c-=1
print(nueva)