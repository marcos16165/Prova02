print("INSIRA A PRIMEIRA MATRIZ 4X4")
print(40 * "-")

x11, x12, x13, x14 = [int(m) for m in input("Digite elementos linha1:\n").split()]

x21, x22, x23, x24 = [int(m) for m in input("Digite elementos linha2:\n").split()]

x31, x32, x33, x34 = [int(m) for m in input("Digite elementos linha3:\n").split()]

x41, x42, x43, x44 = [int(m) for m in input("Digite elementos linha4:\n").split()]
print(40 * "-")
print("INSIRA A SEGUNDA MATRIZ 4X4")
print(40 * "-")

y11, y12, y13, y14 =[int(m) for m in input("Digite elementos linha1:\n").split()]

y21, y22, y23, y24 =[int(m) for m in input("Digite elementos linha2:\n").split()]

y31, y32, y33, y34 =[int(m) for m in input("Digite elementos linha3:\n").split()]

y41, y42, y43, y44 =[int(m) for m in input("Digite elementos linha4:\n").split()]

print("RESULTADO DA SOMA")
print(40 * "-")
print("  {}  {}  {}  {}   ".format(x11+y11, x12+y12, x13+y13, x14+y14))
print("  {}  {}  {}  {}   ".format(x21+y21, x22+y22, x23+y23, x24+y24))
print("  {}  {}  {}  {}   ".format(x31+y31, x32+y32, x33+y33, x34+y34))
print("  {}  {}  {}  {}   ".format(x41+y41, x42+y42, x43+y43, x44+y44))
print(40 * "-")
