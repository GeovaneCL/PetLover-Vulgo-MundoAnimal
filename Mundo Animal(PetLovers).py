import time 

#(FUNÇÕES)

# Função para por caractéries em volta de um print desejado
def inha(msg):
    tam = len(msg) + 4
    print("=" * tam)
    print(f'  {msg}  ')
    print("=" * tam)


# Função para mostrar as opções do Menu Principal
def mostrar_menu():
    time.sleep(1)
    print("\n[MENU INICIAL]\n")
    print('\n[1. Usuários [ADM]')
    print('[2. Clientes]')
    print('[3. Pets]')
    print('[4. Serviços]')
    print('[5. Sair]')

# Função para por tempo de execução no print desejado
def sleep(rint):
    time.sleep(1)
    print(F'{rint}')

# Função para mostrar as opções de usuários
def ADM():
    time.sleep(1)
    print("\n((Usuários [ADMIN]))\n")
    print('\n|1. Cadastrar Usuário|')
    print('|2. Atualizar|')
    print('|3. Apagar|')
    print('|4. Consultar|')
    print('|5. Voltar ao Menu|')

# Função para mostrar as opções de Cliente
def mostrar_client():
    
    sleep("Escolha uma opção...")
    time.sleep(1)
    print("\n|1. Cadastrar Cliente|")
    print("|2. Atualizar dados|")
    print("|3. Apagar Cliente[ADMIN]|")
    print("|4. Consultar Clientes|")
    print("|5. Voltar ao Menu Principal|")

# Função para mostrar as opções de Pets
def mostrar_pets():
    
    sleep("Escolha uma opção...")
    time.sleep(1)
    print("\n|1. Cadastrar Pet|")
    print("|2. Atualizar Pet|")
    print("|3. Apagar Pet [ADMIN]|")
    print("|4. Consultar Pets|")
    print("|5. Voltar ao Menu Principal|")

# Função para mostrar as opções de Serviços
def mostrar_servicos():
    sleep("Escolha uma opção...")
    time.sleep(1)
    print("\n|1. Cadastrar Serviço|")
    print("|2. Atualizar Serviço|")
    print("|3. Apagar Serviço [ADMIN]|")
    print("|4. Consultar Serviços|")
    print("|5. Voltar ao Menu Principal|")






#/////.......................................................................................................................................................\\\\\





#(ALL O PERCURÇO DESSE PROGRAMA É FEITO APENAS PELO ADM!!!)


usuarios = []

useruser =[]

while True:
    login = False

    if len(usuarios)==0: #Criando Login de ADM 
        time.sleep(1)

        inha("Crie seu Login de admistrador.")
        time.sleep(1)
        nome= input('Digite seu Nome: ')
        cpf = input('\nDigite seu CPF: ')
        senha = input('\nSenha: ')
        geren = '1'

        if geren =="1":   
            print('\nVoçê é ADM!')
        login= True
         
        usuarios.append([nome,cpf,senha,geren])
        
        login = True
       
        if any(nome == usuario[0] for usuario in usuarios):
            
            print(f"..."*9)
            sleep("Login de Verificação!")
            print(f"..."*9)
            continue
        
        login =True    
    
    else:
        nome = input('Digite seu nome: ')
        
        cpf = input('\nDigite o seu CPF: ')

        senha = input('\nDigite sua senha: ')
 
        for i in range (len(usuarios)):
 
            if nome ==usuarios[i][0]:
  
                if cpf == usuarios[i][1]:
 
                    if senha == usuarios [i][2]:
                        time.sleep(2)
                        print('\n')
                        inha('BEM VINDO AO MUNDO ANIMAL!!!')
                        login = True
                        break
    if login :
        
        break
    else:
            print(f'~'*30)
            print('Usuários ou senha inválidos!')
            print(f'~'*30)







#/////.......................................................................................................................................................\\\\\








user= [] 
clientes= [] 
pets=[]
servicos =[]   

while True:
            login = False
            mostrar_menu()
            
            menu = input("\nDigite o número correspondente: ")




            if geren =="1":
                
                if menu == '1' and geren =='1': # Menu de Usuários
  
                    sleep("Você escolheu Usuários...")
                    ADM()
                    user = input("\nDigite o número correspondente: ")
 
                    while True:
                        login = False
                        if user =='1': # Cadastrar dados do usuário
                            sleep("Cadastrar Usuário...")

                            if len(useruser)>=0:

                                time.sleep(1)

                                inha("Crie seu Login...")
                                nomeuser= input('Digite seu nome: ')
                                cpfuser = input('\nDigite seu CPF: ')
                                senhauser = input('\nSenha: ')
                                gerenuser ='2'
                                
                                if gerenuser == "2":
                                    print('\nVoçê é Usuário!')
                                    
                                                               
                                else :
                                    break
                                login = True
                                
                                
                                for i in range(len(useruser)):
                                    
                                    if nomeuser ==useruser[i][0]:
                                        
                                        if cpfuser == useruser[i][1]:
                                            
                                            if senhauser== useruser [i][2]:
                                                print(' ')
                                
                                
                                useruser.append([nomeuser,cpfuser,senhauser,gerenuser])
                                print("Usuário cadastrado com sucesso!")
                                continuar= False
                                # Pergunta se deseja cadastrar outro
                                continuar = input("\nDeseja cadastrar outro usuário? (s/n): ")
                                
                                if continuar == 's' or continuar == 'S':
                                    login =True
                                      
                                else :
                                    break
                                


                                    
                        elif user == '2':  # Atualizar dados do usuário
                            
                            time.sleep(1)
                            
                            inha('Atualizar dados...')
                            nomeuser = input("Digite o nome de login do usuário que deseja atualizar: ")

                            for usuario in useruser:

                                if usuario[0] == nomeuser:

                                    novo_nome = input(f"Digite o novo nome ou(Deixe em branco para manter '{usuario[0]}'): ")
                                    nova_cpf = input(f"Digite o novo CPF ou(Deixe em branco para manter): ")
                                    nova_senha = input(f"Digite a nova senha ou(Deixe em branco para manter a atual): ")

                                    if novo_nome: 
                                        usuario[0] = novo_nome
                                    if nova_cpf:
                                        usuario[1] = nova_cpf
                                    if nova_senha:
                                        usuario[2] = nova_senha
                                    
                                    print(f"Usuário '{usuario[0]}' atualizado com sucesso!")
                                    
                                    print('\n')
                                    break
                            break
                            


                        elif user == '3':  # Apagar usuário

                            time.sleep(1)
                            inha("Apagar usuário...")
                            nomeuser = input('Digite o nome de usuário que deseja apagar: ')

                            for usuario in useruser:

                                if usuario[0] == nomeuser:
                                    
                                    useruser.remove(usuario)
                                    print(f"Usuário '{nomeuser}' apagado com sucesso!")

                                else:
                                    print(" ")    
                            break
                               



                        elif user == '4':  # Consultar usuários

                            time.sleep(1)
                            inha("Consultar usuários...")

                            if useruser:
                                
                                for usuario in useruser:

                                    print(f"Nome: {usuario[0]}, CPF: {usuario[1]}, Senha: {usuario[2]}, Gerenciamento: Usuário")
                                break    
                            else:
                                print("Nenhum usuário cadastrado.")
                                break

                        elif user == '5':  # Voltar ao menu principal

                            sleep("Voltando ao Menu principal...")
                            break
                        
                        else:
                            print("Opção inválida! Tente novamente.")







#/////.......................................................................................................................................................\\\\\








                if menu == '2' and geren == '1':   #Menu Clientes

                    sleep("Você escolheu Clientes...")
                    mostrar_client()

                    cliente_opcao = input("\nDigite o número correspondente: ")

                    if cliente_opcao == '1':  # Cadastrar cliente

                        while True:
                            clientlogin= False
                            sleep("Cadastrar Cliente...")
                           
                            time.sleep(1)
                            inha("Crie seu Login de Cliente...")
                            
                            nomecliente = input('Digite o Nome do Cliente: ')
                            cpfcliente = input('\nDigite o CPF do Cliente: ')
                            telefonecliente = input('\nDigite o telefone do Cliente: ')
                            emailcliente = input('\nDigite o email do Cliente: ')                            
                            nopets = input('\nDigite o Nome do seu Pet: ')

                            clientes.append([nomecliente, cpfcliente, telefonecliente, emailcliente,nopets])
                            
                            print(f"Cliente {nomecliente} cadastrado com sucesso!")
                            
                            continuarcl = input("\nDeseja cadastrar outro cliente opção? (s/n): ")

                            if continuarcl == 's' or continuarcl == 'S':
                                    clientlogin = True
                                    
                                      
                            else :
                                    break





                    elif cliente_opcao == '2':  # Atualizar cliente

                        time.sleep(1)
                        sleep("Atualizar dados do Cliente...")
                        nomecliente = input("Digite o Nome do Cliente que deseja atualizar: ")

                        for cliente in clientes:

                            if cliente[0] == nomecliente:

                                novo_nome = input(f"\nNovo Nome ou(Deixe em branco para manter '{cliente[0]}'): ")
                                novo_cpf = input(f"\nNovo CPF ou(Deixe em branco para manter): ")
                                novo_telefone = input(f"\nNovo telefone ou(Deixe em branco para manter): ")
                                novo_email = input(f"\nNovo email ou(Deixe em branco para manter): ")
                                
                                novo_nomepet = input(f"\nNovo Nome do Pet ou(Deixe em branco para manter): ")

                                if novo_nome:
                                    cliente[0] = novo_nome
                                if novo_cpf:
                                    cliente[1] = novo_cpf
                                if novo_telefone: 
                                    cliente[2] = novo_telefone
                                if novo_email:
                                    cliente[3] = novo_email                              
                                if novo_nomepet:
                                    cliente[4] = novo_nomepet

                                print(f"Cliente '{cliente[0]}' atualizado com sucesso!")
                                break
                        else:
                            print("Cliente não encontrado!")
                        


                            

                    elif cliente_opcao == '3':  # Apagar cliente

                        time.sleep(1)
                        
                        sleep("Apagar cliente...")


                        nomecliente = input("Digite o Nome do Cliente que deseja apagar: ")

                        for cliente in clientes:

                            if cliente[0] == nomecliente:
                                clientes.remove(cliente)
                                print(f"Cliente '{nomecliente}' apagado com sucesso!")
                                login=True

                        else:    
                            print("")
                            




                    elif cliente_opcao == '4':  # Consultar clientes

                        time.sleep(1)
                        sleep("Consultar Clientes...")

                        if clientes:

                            for cliente in clientes:
                                    print(f"Nome: {cliente[0]}, CPF: {cliente[1]}, Telefone: {cliente[2]}, Email: {cliente[3]},, Nome Pet: {cliente[4]}")
                                    
                            
                        else:
                            print("Nenhum Cliente cadastrado.")
                            




                    elif cliente_opcao == '5':  # Voltar ao menu principal
                         sleep("Voltando ao Menu principal...")  
                         login=True
                         
                    else:
                        print("Opção inválida! Tente novamente.")







 #/////.......................................................................................................................................................\\\\\








                if menu == '3'and geren =='1': # Menu Pets

                    sleep("Você escolheu Pets...")
                    mostrar_pets()

                    pet_opcao = input("\nDigite o número correspondente: ")

                    if pet_opcao == '1':  # Cadastrar pet

                        while True:
                            login=False

                            sleep("Cadastrar Pet...")
                            time.sleep(1)
                            inha("Crie o cadastro do seu Pet...")
                            nocliente = input("\nDigite o nome do Dono: ")
                            nomepet = input('\nDigite o nome do Pet: ')
                            tipopet = input('\nDigite o tipo do Pet (Cachorro, Gato, etc.): ')
                            

                            pets.append([nomepet, tipopet, nocliente])

                            print(f"Pet {nomepet} cadastrado com sucesso!")

                            continuar_pet = input("\nDeseja cadastrar outro pet? (s/n): ")

                            if continuar_pet == 's' or continuar_pet == 'S':
                                login=True

                            else:
                                break





                    elif pet_opcao == '2':  # Atualizar pet

                        time.sleep(1)
                        sleep("Atualizar dados do Pet...")
                        nomepet = input("Digite o Nome do Pet que deseja atualizar: ")
                        
                        for pet in pets:

                            if pet[0] == nomepet:

                                novo_nomepet = input(f"\nNovo Nome do PET ou(Deixe em branco para manter '{pet[0]}'): ")
                                novo_tipopet = input(f"\nNovo Tipo de PET ou(Deixe em branco para manter '{pet[1]}'): ")
                                novo_donopet = input(f"\nNovo Nome do Dono ou(Deixe em branco para manter '{pet[2]}'): ")

                                if novo_nomepet:
                                    pet[0] = novo_nomepet
                                if novo_tipopet:
                                    pet[1] = novo_tipopet
                                if novo_donopet: 
                                    pet[2] = novo_donopet

                                print(f"Pet '{pet[0]}' atualizado com sucesso!")
                                break
                        else:
                            print("Pet não encontrado!")

                    elif pet_opcao == '3':  # Apagar pet

                        time.sleep(1)
                        sleep("Apagar Pet...")
                        nomepet = input("Digite o nome do Pet que deseja apagar: ")

                        for pet in pets:

                            if pet[0] == nomepet:
                                pets.remove(pet)
                                print(f"Pet '{nomepet}' apagado com sucesso!")
                                login=True
                        else:
                            print(" ")





                    elif pet_opcao == '4':  # Consultar Pets

                        time.sleep(1)
                        sleep("Consultar Pets...")
                        
                        if pets:

                            for pet in pets:
                                print(f"Nome PET: {pet[0]}, Tipo: {pet[1]}, Nome Dono: {pet[2]}")
                        else:
                            print("Nenhum Pet cadastrado.")

                    elif pet_opcao == '5':  # Voltar ao Menu Principal

                        sleep("Voltando ao Menu principal...")
                        login = True

                    else:
                        print("Opção inválida! Tente novamente.")







#/////.......................................................................................................................................................\\\\\








                if menu == '4'and geren =='1': # Menu Serviços

                    sleep("Você escolheu Serviços...")
                    mostrar_servicos()

                    servicoopcao = input("\nDigite o número correspondente: ")

                    if servicoopcao == '1':  # Cadastrar serviço
                        
                        while True:
                            login=False
                            sleep("Cadastrar Serviço...")
                            time.sleep(1)
                            inha("Crie o cadastro do seu Serviço...")
                            
                            
                            nome_servico = input('\nDigite o Nome do Serviço: ')
                            nommecliente = input("\nDigite o Nome do Cliente: ")
                            descricao_servico = input('\nDigite a Descrição do Serviço: ')
                            diagenda = input("\n Digite a data de Agendamento: ")
                            preco_servico = input('\nDigite o preço do Serviço: ')
                            pagosn= input("\nJá foi pago? (s/n): ")

                            if pagosn =='s' or pagosn =="S":
                                pagosn ='SIM'
                            elif pagosn !="s" and pagosn !="S":
                                pagosn="NÃO"
                                

                            servicos.append([nome_servico,nommecliente, descricao_servico, diagenda,preco_servico,pagosn])

                            print(f"Serviço {nome_servico} cadastrado com sucesso!")

                            continuar_servico = input("\nDeseja cadastrar outro serviço? (s/n): ")

                            if continuar_servico == 's' or continuar_servico == 'S':
                                login = True
                                
                            else:
                                break





                    elif servicoopcao == '2':  # Atualizar serviço

                        time.sleep(1)
                        sleep("Atualizar dados do Serviço...")
                        nomecliennte = input("Digite o Nome  do Cliente: ")

                        for servico in servicos:

                            if servico[1] == nomecliennte:
                                novo_nome = input(f"\nNovo Nome do Serviço ou(Deixe em branco para manter '{servico[0]}'): ")
                                novo_nomme_cliente = input(f"\nDigite o Nome  do Cliente(Deixe em branco para manter'{servico[1]}'): ")
                                nova_descricao = input(f"\nNova Descrição ou(Deixe em branco para manter '{servico[2]}'): ")
                                novo_diagenda = input(f"\nNova Data de Agendamento ou(Deixe em branco para manter '{servico[3]}'): ")
                                novo_preco = input(f"\nNovo preço ou(Deixe em branco para manter '{servico[4]}'): ")
                                novopagosn = input(f"\nJá foi pago? (s/n)ou(Deixe em branco para manter '{servico[5]}'): ")

                                if novo_nomme_cliente: 
                                    servico[1] = novo_nomme_cliente
                                if novo_nome:
                                    servico[0] = novo_nome
                                if nova_descricao:
                                    servico[2] = nova_descricao
                                if novo_diagenda:
                                    servico[3] = novo_diagenda
                                if novo_preco:
                                    servico[4] = novo_preco
                                if novopagosn:
                                    servico[5] = novopagosn
                                

                                print(f"Serviço '{servico[0]}' atualizado com sucesso!")
                                break
                        else:
                            print("Serviço não encontrado!")





                    elif servicoopcao == '3':  # Apagar serviço

                        time.sleep(1)
                        sleep("Apagar Serviço...")
                        nomme_cliente = input("Digite o Nome do Cliente: ")

                        for servico in servicos:

                            if servico[1] == nomme_cliente:
                                servicos.remove(servico)
                                print(f"Serviço '{nommecliente}' apagado com sucesso!")
                                break
                        else:
                            print("Serviço não encontrado!")





                    elif servicoopcao == '4':  # Consultar serviços

                        time.sleep(1)
                        sleep("Consultar Serviços...")
                        if servicos:
                            for servico in servicos:
                                print(f"\nNome do Cliente: {servico[1]}\n Serviço: {servico[0]}\n Descrição: {servico[2]}\n Agendamento para: {servico[3]}\n Preço do Serviço: {servico[4]}\n Status de Pagamento: {servico[5]} ")
                                print('\t')
                        else:
                            print("Nenhum serviço cadastrado.")





                    elif servicoopcao == '5':  # Voltar ao Menu Principal

                        sleep("Voltando ao Menu principal...")
                        login = True

                    else:
                        print("Opção inválida! Tente novamente.")







#/////.......................................................................................................................................................\\\\\








                if menu == '5'and geren =='1':
                    sleep("Saindo do programa...")
                    exit()  # Cortar o programa de vez
                else:
                    print("") 





            
            """             
            1 Cadastros     CHECK V

            1.1 Usuários (Administrador)    CHECK V
                1.1.1 Cadastrar novo usuário    CHECK  V
                1.1.2 Atualizar dados    CHECK V
                1.1.3 Apagar     CHECK V
                1.1.4 Consultar     CHECK V
                1.1.5 Voltar ao Menu Cadastros  CHECK V

            1.2 Clientes    CHECK V
                1.2.1 Cadastrar novo cliente    CHECK V
                1.2.2 Atualizar  CHECK V
                1.2.3 Apagar (Administrador)    CHECK V
                1.2.4 Consultar  CHECK V
                1.2.5 Voltar ao Menu Cadastros  CHECK V

            1.3 Pets        CHECK V
                1.3.1 Cadastrar novo pet     CHECK V
                1.3.2 Atualizar     CHECK V
                1.3.3 Apagar (Administrador)     CHECK V
                1.3.4 Consultar  CHECK V
                1.3.5 Voltar ao Menu Cadastros  CHECK V

            1.4 Serviços    CHECK V
                1.4.1 Cadastrar novo serviço (Administrador)    CHECK V
                1.4.2 Atualizar (Administrador)  CHECK V
                1.4.3 Apagar (Administrador)     CHECK V
                1.4.4 Consultar     CHECK V
                1.4.5 Voltar ao Menu Cadastros   CHECK V

            1.5 Voltar ao Menu Principal     CHECK  V 

            
                                                    
            """