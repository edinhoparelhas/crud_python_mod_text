from model import *

def povoar(empresa):
    

    
    endereco_client1 = Endereco_cliente("Rua Stanislau","Caico","RN")
    endereco_client2 = Endereco_cliente("Rua Sverino Sobrinho","Parelhas","RN")
    endereco_client3= Endereco_cliente('Rua Natanael Rodrigues','Patos','PB')

    end_func_atend1 = End_func_atendimento("Rua Stanislau","Caico","RN")
    end_func_atend2 = End_func_atendimento("Rua Sverino Sobrinho","Parelhas","RN")
    end_func_atend3= End_func_atendimento('Rua Natanael Rodrigues','Patos','PB')

    end_func_limp1 = End_func_limpeza("Rua Stanislau","Caico","RN")
    end_func_limp2 = End_func_limpeza("Rua Sverino Sobrinho","Parelhas","RN")
    end_func_limp3= End_func_limpeza('Rua Natanael Rodrigues','Patos','PB')

    espec_func_atend1 = Especialidade_func_atendimento("ADM",2022,"MAURICIO DE NASSAU","especialização")
    espec_func_atend2 = Especialidade_func_atendimento("enfermagem",2000,"Unopar","doutorado")
    espec_func_atend3 = Especialidade_func_atendimento("tec enfermagem",2022,"Mauricio de Baturité","especialização")

    email1=Email("edinho@gmail.com")
    email2=Email("ana@gmail.com")
    email3=Email("matheus@gmail.com")

    cliente1=Cliente('777','Luiz',"(84)99667746",endereco_client1,email1)
    cliente2=Cliente("555","Ana ","(84)99665846",endereco_client2,email2)
    cliente3=Cliente("444","Matheus","(88)99664578",endereco_client3,email3)

    func_limp1 = Func_limpeza("123","Ojuara","9999999",end_func_limp1)
    func_limp2 = Func_limpeza("456","Maria", "88888", end_func_limp2)
    func_limp3 = Func_limpeza("789","Serafina","777777", end_func_limp3)

    func_atend1 = Func_atendimento("111","Tairon","9999999",espec_func_atend1, end_func_atend1)
    func_atend2 = Func_atendimento("222","Lurdes", "88888", espec_func_atend2, end_func_atend2)
    func_atend3 = Func_atendimento("333","Luzia","777777", espec_func_atend3, end_func_atend3)

    medico1=Medico("1","Ricardo","(87)64875236","cardiologista")
    medico2=Medico("2","Antonio","(85)64875236","ginecologista")
    medico3=Medico("3","Tadeu","(81)63375236","nutricionista")  
    medico4=Medico("4","Vanessa","(87)64875236","cardiologista")
    medico5=Medico("5","Robson","(85)64875236","odontologo")
    medico6=Medico("6","Arthur","(81)63375236","urologista")

    convenio1=Convenio("tci","tratamento cardiologico infantil","(83)99885522")
    convenio2=Convenio("tgar","tratamento gestantes auto risco","(88)99852563")
    convenio3=Convenio("unimed","Unidade Medica","(85)99776644")

    empresa.cadastrar_medico(medico1)
    empresa.cadastrar_medico(medico2)
    empresa.cadastrar_medico(medico3)
    empresa.cadastrar_medico(medico4)
    empresa.cadastrar_medico(medico5)
    empresa.cadastrar_medico(medico6)

    empresa.cadastrar_cliente(cliente1)
    empresa.cadastrar_cliente(cliente2)
    empresa.cadastrar_cliente(cliente3)

    empresa.cadastrar_func_limpeza(func_limp1)
    empresa.cadastrar_func_limpeza(func_limp2)
    empresa.cadastrar_func_limpeza(func_limp3)

    empresa.cadastrar_func_atendimento(func_atend1)
    empresa.cadastrar_func_atendimento(func_atend2)
    empresa.cadastrar_func_atendimento(func_atend3)

    empresa.cadastrar_convenio(convenio1)
    empresa.cadastrar_convenio(convenio2)
    empresa.cadastrar_convenio(convenio3)


    hospital1=Hospital("HU","campina grande")
    hospital2=Hospital("maternidade CLIPS","campina grande")
    hospital3=Hospital("INCOR","patos")

    convenio1.cadastrar_hospital(hospital2)
    convenio1.cadastrar_hospital(hospital3)
    convenio2.cadastrar_hospital(hospital1)
    convenio2.cadastrar_hospital(hospital3)
    convenio3.cadastrar_hospital(hospital1)
    convenio3.cadastrar_hospital(hospital2)

    convenio1.cadastrar_medico_conveniado(medico3)
    convenio1.cadastrar_medico_conveniado(medico1)
    convenio2.cadastrar_medico_conveniado(medico2)
    convenio2.cadastrar_medico_conveniado(medico4)
    convenio3.cadastrar_medico_conveniado(medico6)
    convenio3.cadastrar_medico_conveniado(medico5)

    
    
    agend_convenio1=Agendamento_convenio(20,10.00,cliente1,convenio3,medico5)
    agend_convenio2=Agendamento_convenio(21,10.30,cliente2,convenio2,medico2)
    agend_convenio3=Agendamento_convenio(22,11.00,cliente3,convenio1,medico1)
    
    empresa.cadastrar_agendamento_convenio(agend_convenio1)
    empresa.cadastrar_agendamento_convenio(agend_convenio2)
    empresa.cadastrar_agendamento_convenio(agend_convenio3)

    agend_sem_convenio1=Agendamento_nao_conveniado(23,10.00,cliente1,medico3)
    agend_sem_convenio2=Agendamento_nao_conveniado(24,10.30,cliente2,medico4)
    agend_sem_convenio3=Agendamento_nao_conveniado(25,11.00,cliente3,medico6)

    empresa.cadastrar_agendamento(agend_sem_convenio1)
    empresa.cadastrar_agendamento(agend_sem_convenio2)
    empresa.cadastrar_agendamento(agend_sem_convenio3)


    
    

    
    