print(30 * "=", "VETOR INICIAL", 30 *"=")
el=[-9,-8,-7,-6,-5,-4,-3.-2,-1,0,1,2,3,4,5,6,7,8,9,10,11]

print(el)

contador1=0
contador2=19
cl=0

while cl<10:
    aux=el[contador1]
    el[contador1]=el[contador2]
    el[contador2]=aux
    contador1=contador1+1
    contador2=contador2-1
    cl=cl+1
    
el2=[]
for i in range(len(el)):
    el2.append(el[i])
print(31 * "=", "NOVO VETOR", 32 *"=")
print (el2)
print(75 * "=")
print(27 * "=", "POSIÇÂO DOS VETORES", 27 *"=")
print("N[0] = {}\nN[1] = {}\nN[2] = {}\nN[3] = {}\nN[4] = {}  ".format(el2[0],el2[1],el2[2],el2[3],el2[4]))
print("N[5] = {}\nN[6] = {}\nN[7] = {}\nN[8] = {}\nN[9] = {}\nN[10] = {}".format(el2[5],el2[6],el2[7],el2[8],el2[9],el2[10]))
print("N[11] = {}\nN[12] = {}\nN[13] = {}\nN[14] = {}\nN[15] = {}".format(el2[11],el2[12],el2[13],el2[14],el2[15]))
print("N[16] = {}\nN[17] = {}\nN[18] = {}\nN[19] = {}".format(el2[16],el2[17],el2[18],el2[19]))
print(75 * "=")
