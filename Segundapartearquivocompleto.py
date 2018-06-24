def cadastro(n, e, l, s, t):
    return{"nome": n,
           "email": e,
           "login": l,
           "senha": s,
           "tipo": t}

def cadastro2(n, e):
    return{"nome": n,
           "email": e}

def adicionar(u, l):
    l.append(u)
    return l


def mostre_lista(l):
    for m in l:
        print(40 * "=")
        for k, v in m.items():
            print("{}: {}".format(k.capitalize(),v))

    print(40 * "=")

#Sistema de login
    
def autenticar(l,s):
    resposta = False
    for x in lista_alunos:
        if x["login"] == l:
            if x["senha"] == s:
                resposta = True
                return resposta, "Login realizado com sucesso"
            else:
                return resposta, "Senha incorreta"
    return resposta, "Login incorreto"


def autenticar2(l,s):
    resposta = False
    for x in lista_professor:
        if x["login"] == l:
            if x["senha"] == s:
                resposta = True
                return resposta, "Login realizado com sucesso"
            else:
                return resposta, "Senha incorreta"
    return resposta, "Login incorreto"        
        
def read_integer(*,m=''):
    i = int(input(m))
    return i
    
def read_string(*,m=''):
    s = str(input(m))
    return s
                    

def login_aluno():
    l = read_string(m="Entre com o login: ")
    s = read_string(m="Entre com a senha: ")
    r,m = autenticar(l,s)
    print(m)
    return r
def login_professor():
    l = read_string(m="Entre com o login: ")
    s = read_string(m="Entre com a senha: ")
    r,m = autenticar2(l,s)
    print(m)
    return r

#-----------------------------------------

#idiomas
def cadastro_idiomas(i):
    return{"idioma": i}

    
#listas ------------------------------------------------------------------------------
lista_alunos2 = [{'nome': 'Sara','email': 'sara@gmail.com'}]

lista_professores2 = [{'nome': 'Levy','email': 'levy@gmail.com'}]

dados_prof = []
meus_idiomas = []
lista_alunos = [{'nome': 'Sara','email': 'sara@gmail.com','login': 'sara', 'senha': '123', "tipo" : "aluno"}]
lista_professor = [{'nome': 'Levy','email': 'levy@gmail.com','login': 'levy', 'senha': '1234', "tipo" : "professor"}]


#opções de verificação --------------------------------------------------------------------------
print()
print(10* "*=*", "SISTEMA PARA CADASTRO DE USUÁRIO", 10* "*=*")
print()
while True:
    print("---------- MENU INÍCIO ----------")
    op = input("""
1 - Cadastrar usuário
2 - Login
3 - Mostrar a lista de alunos
4 - Mostrar a lista de professores
Digite sua opção: """)

    if op == '3':
        print()
        print("---------- LISTA DE ALUNOS ----------")
        print()
        mostre_lista(lista_alunos2)

    if op == '4':
        print()
        print("---------- LISTA DE PROFESSORES ----------")
        print()
        mostre_lista(lista_professores2)
        
# cadastro ----------------------------------------------------
    if op == '1':
        print()
        print("---------- CADASTRO DE USUÁRIO ----------")
        print()
        nome = str(input("Digite seu nome: "))
        email = input("Digite seu E-mail: ")
        login = input("Digite o login que deseja cadastrar: ")
        senha = input("Digite a senha: ")
        tipo = int(input("""
1 - Para cadastrar-se como professor
2 - Para cadastrar-se como aluno
Digite sua opção: """))
        
        if tipo != 1 and tipo !=2:
            print("Opção invalida")
    
        
        if tipo == 1:
            adicionar(cadastro(nome,email,login,senha,"professor"), lista_professor)
            adicionar(cadastro2(nome,email),lista_professores2)
            print("Cadastro realizado")

        if tipo == 2:
            adicionar(cadastro(nome,email,login,senha,"aluno"), lista_alunos)
            adicionar(cadastro2(nome,email),lista_alunos2)
            print("Cadastro realizado")
        print()
        
        

# Login  ------------------------------------------------------------------------


    if op == '2':
        
        print()
        print("---------- LOGAR NO SISTEMA ----------")
        print()
        escolha = input("""
1 - Logar como aluno
2 - Logar como professor
Escolha uma opção: """)

# Opcoes do aluno ---------------------------------------------------------
        if escolha == '1':
            if login_aluno() == True:
                while True:
                    print()
                    print("---------- MENU ALUNO ----------")
                    op2 = input("""
1 - Pode cadastrar e consultar os idiomas que deseja estudar
2 - Pode cadastrar e consultar o horário e o dia que melhor pode frequentar a escola
3 - Pode cadastrar e consultar o local (cidade e estado) onde pretende realizar o curso
4 - Sair
Digite sua opção: """)

# idiomas           
                    if op2 == '1':
                        print()
                        print("---------- IDIOMAS ----------")
                        opcoes = input("""
1 - Para se cadastar no idioma
2 - Para mostrar lista de idiomas já cadastrados
Digite sua opção: """)
                    
                        if opcoes == '1':
                            op3 = input("""
1 - Inglês                     
2 - Francês          
Digite sua opção:  """)
                        
                        
                            if op3 == '1':
                                adicionar({"Idioma":"Inglês"}, meus_idiomas)
                            if op3 == '2':
                                adicionar({"Idioma":"Francês"}, meus_idiomas)
                        
                            
                        if opcoes == '2':
                            mostre_lista(meus_idiomas)

# horario

                    if op2== '2':
                        print()
                        print("---------- HORÁRIOS ----------")
                        opcoes1 = input("""
1 - Para se cadastar horário
2 - Para mostrar horário
Digite sua opção: """)


                        if opcoes1 == '1':
                            op4 = input("""
----------------------------------------------------------------------------------------------------------------------------------
| 1) Inglês:                                                    | 2) Francês:                                                    |
|                                                               |                                                                |
| 1) Turma A: Quarta - 10:50/12:30 hs e Sexta - 7:00/10:30 hs   | 1) Turma A: Terça - 15:00/17:00 hs e Sexta - 9:00/11:30 hs     |
| 2) Turma B: Segunda - 7:00/10:30 hs e Quinta - 10:50/12:30 hs | 2) Turma B: Quarta - 8:50/12:00 hs e Quinta - 11:00/12:30 hs   |
----------------------------------------------------------------------------------------------------------------------------------
Digite sua opção: """)

                        
                            if op4 == '1':
                                cursoi = input("""
1 - Turma A de Inglês
2 - Turma B de Inglês
Escolha uma turma: """)
                                print()
                                print("Matrícula efetuada!")
                                print(20* "-")
                            
                                if cursoi == '1':
                                    adicionar({"horario":"Turma A Inglês"}, meus_idiomas)
                                if cursoi == '2':
                                    adicionar({"horario":"Turma B Inglês"}, meus_idiomas)



                            if op4 == '2':
                                cursof = input("""
1 - Turma A de Francês 
2 - Turma B de Francês
Escolha uma turma: """)
                                print()
                                print("Matrícula efetuada!")
                                print(20* "-")
                            
                                if cursoi == '1':
                                    adicionar({"horario":"Turma A Francês "}, meus_idiomas)
                                if cursoi == '2':
                                    adicionar({"horario":"Turma B Francês "}, meus_idiomas)

                        if opcoes1 == '2':
                            mostre_lista(meus_idiomas)


    # Local

                    if op2 == "3":
                        print()
                        print("---------- LOCAL ----------")
                        opcoes2 = input("""
1 - Para cadastrar local
2 - Para mostrar local
Digite sua opção: """)
                    
                        if opcoes2 == '1':
                            op5 = input("""
1 - Mossoró - RN                   
2 - Russas - CE
Digite sua opção:  """)

                            if op5 == '1':
                                adicionar({"local":"Mossoró - RN"}, meus_idiomas)

                            if op5 == '2':
                                adicionar({"local":"Russas - CE"}, meus_idiomas)

                        if opcoes2 == '2':
                             mostre_lista(meus_idiomas)
                             
                    if op2 == '4':
                        break                            
            
## opcoes de professor -----------------------------------------------------------------------------------------
        if escolha == '2':
            if login_professor() == True:
                while True:
                    print()
                    print("---------- MENU PROFESSOR ----------")
                    prof = input("""
1 - cadastrar notas de aluno 
2 - Número de faltas dos alunos 
3 - As disciplinas que ministra
4 - Sair
Digite sua opção: """)
                    if prof == '4':
                        break

# notas aluno          
                    if prof == '1':
                        print()
                        print("---------- CADASTRO DE NOTAS ----------")
                        print()
                        nomalu = input("Aluno: ")
                        notalu = input("Nota: ")
                        adicionar({"Aluno":nomalu, "Nota": notalu}, dados_prof)
                        mostre_lista(dados_prof)

#faltas
                    if prof == '2':
                        print()
                        print("---------- FALTAS DOS ALUNOS ----------")
                        print()
                        nomalu = input("Aluno: ")
                        faalu = input("Falta: ")
                        adicionar({"Aluno":nomalu, "Falta": faalu}, dados_prof)
                        mostre_lista(dados_prof)
                        
#diciplinas ministradas
                        
                    if prof == '3':
                        print()
                        print("---------- DISCIPLINAS MINISTRADAS ----------")
                        print()
                        ministra = input("Disciplina: ")
                        
                        adicionar({"Disciplina": ministra}, dados_prof)
                        mostre_lista(dados_prof)


                    
                
       

