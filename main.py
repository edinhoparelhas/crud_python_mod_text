from model import *
from povoar import *
from menu import *
#login == 1
#senha==1

nome= "CLINIC CONTROL"
cnpj="55.238.976/0001-33"
endereco="Rua José Cavalcante Nº 177 Parelhas RN"
empresa=Empresa(nome,cnpj,endereco)
povoar(empresa)
print (f"\n\n{empresa}\n\n")
cont=2
while cont >= 0:
    login=input("login:")
    senha=input("senha: ")
    if login != "1" or senha !="1":
        print ("\nlogin ou senha incorreto")
        resp =input("desja continuar (s/n): ")
        if resp !="s":
            break
        else:
            print(f"\nvocê tem mais {cont} tentativas\n ")
            cont-=1
    else:
        while True: 
            print (f"\n\n{empresa}")
            print(MENU_PRINCIPAL)
            opcao=input("digite a opção: ")
            if opcao==SAIR:
                break
            elif opcao==ACESSAR_FUNCIONARIO:
                while True:
                    print (f"\n\n{empresa}")
                    print(MENU_FUNCIONARIO)
                    opcao=input("digite a opção: ")

                    if opcao==SAIR:
                        break
                    elif opcao==CADASTRAR_FUNCIONARIO:
                        print(' CADASTRAR FUNCIONARIOS')
                        print(MENU_CADAST_FUNC)
                        opcao=input("digite a opção: ")
                        if opcao==SAIR:
                            break
                        elif opcao==MEDICO:
                            crm=input('CRM: ')
                            medico=empresa.get_medico_crm(crm)
                            if medico!=None:
                                print('já existe um cadastro para esse CRM')
                            else:
                                nome=input('NOME: ')
                                telefone=input('TELEFONE: ')
                                nome_especializ=input('ESPECIALIZAÇÃO: ')
                                ano_conclusao=input("ANO DE CONCLUSÃO: ")
                                especialidade=Especialidade_medica(nome_especializ,ano_conclusao)
                                medico=Medico(crm,nome,telefone,especialidade)
                                medico=empresa.cadastrar_medico(medico)
                                print('medico cadastrado com sucesso')

                        elif opcao==FUNCIONARIO_LIMPEZA:
                            rg=input('RG: ')
                            funcionario_limpeza=empresa.get_func_limpeza(rg)
                            if funcionario_limpeza!=None:
                                print('já existe um cadastro para esse rg')
                            else:
                                nome=input('NOME: ')
                                telefone=input('TELEFONE: ')
                                rua=input("RUA: ")
                                cidade=input("CIDADE: ")
                                estado=input("ESTADO: ")
                                endereco=End_func_limpeza (rua,cidade,estado)
                                funcionario_limpeza=Func_limpeza(rg,nome,telefone,endereco)
                                medico=empresa.cadastrar_func_limpeza(funcionario_limpeza)
                                print('funcionario cadastrado com sucesso')

                        elif opcao==FUNCIONARIO_ATEND:
                            rg=input('RG: ')
                            func_atend=empresa.get_func_atendimento(rg)
                            if func_atend!=None:
                                print('já existe um cadastro para esse rg')
                            else:
                                nome=input('NOME: ')
                                telefone=input('TELEFONE: ')
                                curso=input('CURSO: ')
                                ano=input('ANO: ')
                                faculdade=input('FACULDADE: ')
                                titulo=input('TITULO: ')
                                especialidade= Especialidade_func_atendimento (curso,ano,faculdade,titulo)
                                rua=input("RUA: ")
                                cidade=input("CIDADE: ")
                                estado=input("ESTADO: ")
                                endereco= End_func_atendimento (rua,cidade,estado)
                                funcionario_atend=Func_atendimento(rg,nome,telefone,especialidade,endereco)
                                funcionario_atend=empresa.cadastrar_func_atendimento(funcionario_atend)
                                print('funcionario cadastrado com sucesso')
                    elif opcao==ALTERAR_DADOS_FUNCIONARIO:
                        print(MENU_CADAST_FUNC)
                        opcao=input("digite a opção: ")
                        if opcao==SAIR:
                            break
                        elif opcao==MEDICO:
                            print('ALTERAR MEDICO')
                            crm=input('digite o CRM do medico: ')
                            medico = empresa.get_medico_crm(crm)
                            if medico == None:
                                print("crm não encontrado")
                            else:
                                novo_nome=input('NOME: ')
                                novo_telefone=input('TELEFONE: ')
                                nome_especializ=input('ESPECIALIZAÇÃO: ')
                                ano_conclusao=input("ANO DE CONCLUSÃO: ")
                                nova_especializ= Especialidade_medica (nome_especializ,ano_conclusao)
                                empresa.alterar_medico(crm,novo_nome,novo_telefone,nova_especializ)
                                print('medico alterado com sucesso') 
                        elif opcao==FUNCIONARIO_LIMPEZA:
                            print('ALTERAÇÃO DE FUNC. LIMPEZA')
                            rg=input('digite o rg do funcionario: ')
                            func_limp = empresa.get_func_limpeza(rg)
                            if func_limp == None:
                                print("rg não encontrado")
                            else:
                                novo_nome=input('NOME: ')
                                novo_telefone=input('TELEFONE: ')
                                rua=input('RUA: ')
                                cidade=input('CIDADE: ')
                                estado=input('ESTADO: ')
                                novo_endereco=End_func_limpeza(rua,cidade,estado)
                                empresa.alterar_func_limpeza(rg,novo_nome,novo_telefone,novo_endereco)
                                print('funcionario alterado com sucesso') 
                        elif opcao==FUNCIONARIO_ATEND:
                            print('ALTERAÇÃO DE FUNC. ATENDIMENTO ')
                            rg=input('digite o rg do funcionario: ')
                            func_atend = empresa.get_func_atendimento(rg)
                            if func_atend == None:
                                print("rg não encontrado")
                            else:
                                novo_nome=input('NOME: ')
                                novo_telefone=input('TELEFONE: ')
                                nome_curso=input("CURSO: ")
                                ano_conclusao=input("ANO CONCLUSÃO: ")
                                faculdade=input("FACULDADE: ")
                                titulo=input("TITULO: ")
                                nova_especialidade=Especialidade_func_atendimento(nome_curso,ano_conclusao,faculdade,titulo)
                                rua=input('RUA: ')
                                cidade=input('CIDADE: ')
                                estado=input('ESTADO: ')
                                novo_endereco=End_func_atendimento(rua,cidade,estado)
                                empresa.alterar_func_atendimento(rg,novo_nome,novo_telefone,nova_especialidade,novo_endereco)
                                print('funcionário alterado com sucesso') 
                    elif opcao==REMOVER_FUNCIONARIO:
                        print(MENU_CADAST_FUNC)
                        opcao=input("digite a opção: ")
                        if opcao==SAIR:
                            break
                        elif opcao==MEDICO:
                            print('REMOVER MÉDICO')
                            crm=input('digite o CRM para remoção do medico: ')
                            verif=empresa.remover_medico(crm)
                            if verif== True:
                                print('medico removido com sucesso')
                            else:
                                print('CRM não encontrado')
                        elif opcao==FUNCIONARIO_LIMPEZA:
                            print('REMOVER FUNC. LIMPEZA')
                            rg=input('digite o rg para remoção do funcionário: ')
                            verif=empresa.remover_func_limpeza(rg)
                            if verif== True:
                                print('funcionário removido com sucesso')
                            else:
                                print('RG não encontrado')

                        elif opcao==FUNCIONARIO_ATEND:
                            print('REMOVER FUNC. ATENDIMENTO')
                            rg=input('digite o rg para remoção do funcionário: ')
                            verif=empresa.remover_func_atendimento(rg)
                            if verif== True:
                                print('funcionario removido com sucesso')
                            else:
                                print('RG não encontrado')
                    elif opcao==LISTA_FUNCIONARIOS_ATIVOS:
                        print(MENU_CADAST_FUNC)
                        opcao=input("digite a opção: ")
                        if opcao==SAIR:
                            break
                        elif opcao == MEDICO:
                            print('LISTA DE MÉDICOS ATIVOS')
                            medicos=empresa.medico_ativo()
                            for medico in medicos:
                                print(F"Dr.{medico.nome}")
                                print("------------------")
                        elif opcao==FUNCIONARIO_LIMPEZA:
                            print('LISTA DE FUNCIONARIOS DA LIMPEZA ATIVOS')
                            funcionarios_limp=empresa.func_limp_ativo()
                            for func_limp in funcionarios_limp:
                                print(func_limp.nome)
                                print("------------------")

                        elif opcao==FUNCIONARIO_ATEND:
                            print('LISTA DE FUNCIONARIOS DO ATENDIMENTO ATIVOS')
                            funcionarios_atend=empresa.func_atend_ativo()
                            for func_atend in funcionarios_atend:
                                print(func_atend.nome)
                                print("------------------")
                    elif opcao==LISTA_FUNCIONARIOS_INATIVOS:
                        print(MENU_CADAST_FUNC)
                        opcao=input("digite a opção: ")
                        if opcao==SAIR:
                            break
                        elif opcao == MEDICO:
                            print('LISTA DE MÉDICOS INATIVOS')
                            medicos=empresa.medico_inativo()
                            for medico in medicos:
                                print(medico.nome)
                                print("------------------")

                        elif opcao==FUNCIONARIO_LIMPEZA:
                            print('LISTA DE FUNCIONARIOS DA LIMPEZA INATIVOS')
                            funcionarios_limp=empresa.func_limp_inativo()
                            for func_limp in funcionarios_limp:
                                print(func_limp.nome)
                                print("------------------")

                        elif opcao==FUNCIONARIO_ATEND:
                            print('LISTA DE FUNCIONARIOS DO ATENDIMENTO INATIVOS')
                            funcionarios_atend=empresa.func_atend_inativo()
                            for func_atend in funcionarios_atend:
                                print(func_atend.nome)
                                print("------------------")
                    elif opcao==DADOS_FUNCIONARIO:
                        print(MENU_CADAST_FUNC)
                        opcao=input("digite a opção: ")
                        if opcao==SAIR:
                            break
                        elif opcao==MEDICO:
                            print("DADOS DO MEDICO")
                            crm=input('digite o CRM do medico: ')
                            medico=empresa.get_medico_crm(crm)
                            if medico==None or medico.ativo==False:
                                print ('CRM não encontrado')
                            else:
                                if medico.crm==crm:
                                    print(medico)
                        elif opcao==FUNCIONARIO_LIMPEZA:
                            print("DADOS DO FUNC. LIMPEZA")
                            rg=input('digite o rg do funcionario: ')
                            func_limp=empresa.get_func_limpeza(rg)
                            if func_limp==None or func_limp.ativo==False:
                                print ('rg não encontrado')
                            else:
                                if func_limp.rg==rg:
                                    print(func_limp)

                        elif opcao==FUNCIONARIO_ATEND:
                            print("DADOS DO FUNC. ATENDIMENTO")
                            rg=input('digite o rg do funcionario: ')
                            func_atend=empresa.get_func_atendimento(rg)
                            if func_atend==None or func_atend.ativo==False:
                                print ('rg não encontrado')
                            else:
                                if func_atend.rg==rg:
                                    print(func_atend)
                    else:
                        print("opção invalida")          
            elif opcao==ACESSAR_CLIENTE:
                while True:
                    print (f"\n\n{empresa}")
                    print(MENU_CLIENTE)
                    opcao=input("digite a opção: ")

                    if opcao==SAIR:
                        break
                    elif opcao==CADASTRAR_CLIENTE:
                        print('CADASTRO DE CLIENTE')
                        rg=input('RG: ')
                        cliente=empresa.get_cliente(rg)
                        if cliente!=None:
                            print('já existe um cadastro para esse rg')
                        else:
                            nome=input('NOME: ')
                            telefone=input('TELEFONE: ')
                            rua=input('RUA: ')
                            cidade=input('CIDADE: ')
                            estado=input('ESTADO: ')
                            email=input("EMAIL: ")
                            endereco_cliente=Endereco_cliente(rua,cidade,estado)
                            cliente=Cliente(rg,nome,telefone,endereco_cliente,email)
                            cliente=empresa.cadastrar_cliente(cliente)
                            print('cliente cadastrado com sucesso')
                    elif opcao==ALTERAR_DADOS_CLIENTE:
                        print('ALTERAÇÃO DE CLIENTE')
                        rg=input('digite o rg do cliente: ')
                        cliente = empresa.get_cliente(rg)
                        if cliente == None:
                            print("rg não encontrado")
                        else:
                            novo_nome=input('NOVO NOME: ')
                            novo_telefone=input('NOVO TELEFONE: ')
                            rua=input('RUA: ')
                            cidade=input('CIDADE: ')
                            estado=input('ESTADO: ')
                            novo_endereco=Endereco_cliente(rua,cidade,estado)
                            empresa.alterar_cliente(rg,novo_nome,novo_telefone,novo_endereco)
                            print('cliente alterado com sucesso')           
                    elif opcao==REMOVER_CLIENTE:
                        print('REMOVER CLIENTE')
                        rg=input('digite o rg para remoção do cliente: ')
                        verif=empresa.remover_cliente(rg)
                        if verif==True:
                            print('cliente removido com sucesso')
                        else:
                            print('rg não encontrado')
                    elif opcao == LISTA_CLIENTES_ATIVOS:
                        print('LISTA DE CLIENTES ATIVOS')
                        clientes=empresa.cliente_ativo()
                        for cliente in clientes:
                            print(cliente.nome)
                            print("------------------")
                    elif opcao == LISTA_CLIENTES_INATIVOS:
                        print('LISTA DE CLIENTES INATIVOS')
                        clientes=empresa.cliente_inativo()
                        for cliente in clientes:
                            print(cliente.nome)
                            print("------------------")
                    elif opcao==DADOS_CLIENTE:
                        print("CLIENTE")
                        rg=input('digite o rg do cliente: ')
                        cliente=empresa.get_cliente(rg)
                        if cliente==None or cliente.ativo==False:
                            print ('cpf não encontrado')
                        else:
                            if cliente.rg==rg:
                                print(cliente)
                    else:
                        print("opção invalida")
            elif opcao==ACESSAR_CONVENIO:
                while True:
                    print (f"\n\n{empresa}")
                    print(MENU_CONVENIO)
                    opcao=input("digite a opção: ")
                    if opcao==SAIR:
                        break
                    elif opcao==CADASTRAR_CONVENIO:
                        print("CADASTRO DE CONVÊNIO")
                        sigla=input("SIGLA: ")
                        convenio=empresa.get_convenio(sigla)
                        if convenio!= None:
                            print("convenio já existente")
                        else:
                            nome_conv=input("NOME DO CONVÊNIO: ")
                            telefone=input("TELEFONE: ")
                            convenio=Convenio(sigla,nome_conv,telefone)
                            empresa.cadastrar_convenio(convenio)
                            print("convênio cadastrado com sucesso")
                    elif opcao==ALTERAR_CONVENIO:
                        print("ALTERAR CONVÊNIO")
                        sigla=input("digite a sigla do convênio: ")
                        convenio=empresa.get_convenio(sigla)
                        if convenio==None:
                            print("sigla não encontrada")
                        else:
                            nova_sigla=input("SIGLA: ")
                            novo_nome=input("NOME CONVÊNIO: ")
                            novo_telefone=input("TELEFONE: ")
                            convenio=Convenio(nova_sigla,novo_nome,novo_telefone)
                            empresa.alterar_convenio(sigla,nova_sigla,novo_nome,novo_telefone)
                            print ("convênio alterado com sucesso")
                    elif opcao==REMOVER_CONVENIO:
                        print("REMOVER CONVÊNIO")
                        sigla=input("digite a sigla do convênio para remover: ")
                        verif=empresa.remover_convenio(sigla)
                        if verif==False:
                            print("sigla não encontrada")
                        else:
                            print("Convênio removido com sucesso")
                    elif opcao==LISTA_CONVENIO:
                        print("LISTA DOS CONVÊNIO")
                        convenios=empresa.convenio_ativo()
                        for convenio in convenios:
                            print(convenio.nome)
                            print("..........")
                    elif opcao==LISTA_CONVENIO_INATIVOS:
                        print("LISTA DOS CONVÊNIO INATIVOS")
                        convenios=empresa.convenio_inativo()
                        for convenio in convenios:
                            print(convenio.nome)
                            print("..........")
                    elif opcao == DADOS_CONVENIO:
                        print("DADOS DO CONVÊNIO")
                        sigla=input("digite a sigla do convênio: ")
                        convenio=empresa.get_convenio(sigla)
                        if convenio==None or convenio.ativo==False:
                            print("convenio não encontrado")
                        else: 
                            print(convenio)
            elif opcao==AGENDAR_ATENDIMENTO:
                print (f"\n\n{empresa}")
                print(MENU_AGENDAMENTO)
                opcao=input("digite a opção: ")
                if opcao==SAIR:
                    break
                elif opcao==AGENDAR:
                    while True:
                    
                        print("AGENDAMENTO POR CONVÊNIO (1) ")
                        print("AGENDAMENTO SEM CONVÊNIO (2)")
                        print("para sair digite 0")
                        resp=input("qual o agendamento: ")
                        if resp=="0":
                            break
                        elif resp == "1":
                            data=input("DATA: ")
                            horario=float(input("HORARIO: "))
                            agend=empresa.get_agendamento_convenio(data,horario)
                            if agend !=None:
                                print("data e horario já está agendado")
                            else:
                                rg= input("RG:")
                                cliente=empresa.get_cliente(rg)
                                if cliente!=None:
                                    print(cliente) 
                                    sigla=input("CONVÊNIO: ")
                                    convenio=empresa.get_convenio(sigla)
                                    if convenio!=None:
                                        print(convenio)
                                        espec=input("ESPECIALIDADE: ")
                                        for medico in convenio.lista_medicos_convenio:
                                            if medico.especialidade!=espec:
                                               print ("especialidade não faz parte do convênio\n")
                                            else:
                                                print (f"Dr.{medico.nome}")
                                                print(medico.especialidade)
                                                agendamento=Agendamento_convenio(data,horario,cliente,convenio,medico)
                                                agendamento=empresa.cadastrar_agendamento_convenio(agendamento)
                                                print ("agendamento realizado com sucesso")
                                                email=Email(cliente.email)
                                                email=empresa.cadastrar_email(email)
                                                print("email enviado com sucesso")
                                    else:
                                        print ("convenio não faz parte da dessa empresa")
                                else:
                                    print("rg nao cadastrado")
                                    break
                        elif resp=="2":
                            data=input("DATA: ")
                            horario=float(input("HORARIO: "))
                            agend=empresa.get_agendamento_nao_conveniado(data,horario)
                            if agend!=None:
                                print("data e horario já está agendado")
                            else:
                                rg= input("RG:")
                                cliente=empresa.get_cliente(rg)
                                if cliente!=None:
                                    print(cliente) 
                                    nome_especialidade=input ("ESPECIALIDADE: ")
                                    medico=empresa.get_medico_especialidade(nome_especialidade)
                                    if medico!=None:
                                        print (f"Dr.{medico.nome}")
                                        print(medico.especialidade)
                                        agendamento=Agendamento_nao_conveniado(data,horario,cliente,medico)
                                        agendamento=empresa.cadastrar_agendamento(agendamento)
                                        print ("agendamento realizado com sucesso")
                                        email=Email(cliente.email)
                                        email=empresa.cadastrar_email(email)
                                        print("email enviado com sucesso")
                                    else:
                                        print("não existe essa especialidade nessa empresa")        
                                
                                else:
                                    print("rg nao cadastrado")
                                    break
                        
                        else:
                            print("opcão invalida")
                elif opcao==ALTERAR_AGENDAMENTO_CONVENIO:
                    data=input("DATA: ")
                    horario=float(input("HORARIO: "))
                    agendamento=empresa.get_agendamento_convenio(data,horario)
                    if agendamento!=None:
                        print("ALTERAR AGENDAMENTO CONVÊNIO")
                        nova_data=input("alterar data: ")
                        novo_horario=input("alterar horario: ")
                        empresa.alterar_agendamento_convenio(agendamento,nova_data,novo_horario)
                        print ("agendamento alterado com sucesso")
                        email=Email(cliente.email)
                        email=empresa.cadastrar_email(email)
                        print("email enviado com sucesso")
                    else:
                        print ("não existe agendamento para essa data/hora")
                elif opcao==ALTERAR_AGENDAMENTO_NAO_CONVENIADO:
                    data=input("DATA: ")
                    horario=float(input("HORARIO: "))
                    agendamento=empresa.get_agendamento_nao_conveniado(data,horario)
                    if agendamento!=None:
                        print("ALTERAR AGENDAMENTO NÃO CONVÊNIO")
                        nova_data=input("alterar data: ")
                        novo_horario=input("alterar horario: ")
                        empresa.alterar_agendamento_nao_conveniado(agendamento,nova_data,novo_horario)
                        print ("agendamento alterado com sucesso")
                        email=Email(cliente.email)
                        email=empresa.cadastrar_email(email)
                        print("email enviado com sucesso")
                    else:
                        print ("não existe agendamento para essa data/hora")
                elif opcao==REMOVER_AGENDAMENTO_CONVENIO:
                    print ("REMOVER AGENDAMENTO CONVÊNIO")
                    data=input("data do agendammento: ")
                    horario=float(input("horario do agendamento: "))
                    verif=empresa.remover_agendamento_convenio(data,horario)
                    if verif!=False:
                        print ("agendamento removido com sucesso")
                    else:
                        print("não existe agendamento para essa data/hora")              
                elif opcao==REMOVER_AGENDAMENTO_NAO_CONVENIADO:
                    print ("REMOVER AGENDAMENTO NÃO CONVÊNIADO")
                    data=input("data do agendammento: ")
                    horario=float(input("horario do agendamento: "))
                    verif=empresa.remover_agendamento_nao_conveniado(data,horario)
                    if verif!=False:
                        print ("agendamento removido com sucesso")
                    else:
                        print("não existe agendamento para essa dataa/hora")    
                elif opcao==LISTA_AGENDAMENTOS_CONVENIO_ATIVOS:
                    print('LISTA DE AGENDAMENTOS CONVENIO ATIVOS')
                    agendamentos=empresa.agendamento_convenio_ativo()
                    for agendamento in agendamentos:
                        print(agendamento)
                        print("------------------")
                elif opcao==LISTA_AGENDAMENTOS_ATIVOS_NAO_CONVENIADOS:
                    print('LISTA DE AGENDAMENTOS NÃO CONVENIADOS ATIVOS')
                    agendamentos=empresa.agendamento_ativo()
                    for agendamento in agendamentos:
                        print(agendamento)
                        print("------------------")
                elif opcao == DADOS_AGENDAMENTO_CONVENIO:
                    print("AGENDAMENTO POR CONVÊNIO")
                    data=input('digite a data do agendamento: ')
                    horario=float(input ("digite o horario agendado: "))
                    agendamento=empresa.get_agendamento_convenio(data,horario)
                    if agendamento!=None:
                        print(agendamento)
                    else:
                        print ('nenhum agendamento confirmado para essa data/hora')
                elif opcao == DADOS_AGENDAMENTO_NAO_CONVENIADO:
                    print("AGENDAMENTO NÃO CONVÊNIADO")
                    data=input('digite a data do agendamento: ')
                    horario=float(input ("digite o horario agendado: "))
                    agendamento=empresa.get_agendamento_nao_conveniado(data,horario)
                    if agendamento!=None:
                        print(agendamento)
                    else:
                        print ('nenhum agendamento confirmado para essa data/hora')
                else:
                    print("opção invalida")
            else:
                print("opção invalida")

        