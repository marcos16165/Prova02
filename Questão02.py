print(95* "=")
lista2=[10, 20, 1, 3, 4, 3, 9, 8, 9, 10, 200, 40, 30, 25, 10, 9, 37, 19, 28, 10, 28, 22, 10, 102, 317]
print(lista2)
print(95* "=")

menor=10
maior=10
for i in range(len(lista2)):
    if lista2[i]>maior:
        maior=lista2[i]
    elif lista2[i]<menor:
        menor=lista2[i]

for i in range(len(lista2)):
    if lista2[i]==maior:
        print ("Maior número: {}".format(lista2[i]))
        print ("Índice do maior número: [{}]".format(i))

for i in range(len(lista2)):
    if lista2[i]==menor:
        print ("Menor número: {}".format(lista2[i]))
        print ("Índice do menor número: [{}]".format(i))

#Media        
def media(lista2):
    soma=0
    for i in lista2:
        soma=i+soma
        m=soma/len(lista2)
    return m
print ("A média é: {}".format(media(lista2)))

pad=0
for x in lista2:
    p=(x-media(lista2))**2
    pad+=p/(len(lista2)-1)
print("O desvio padrão é: {:.2f}".format(pad**0.5))
print(95* "=")
