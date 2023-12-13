class Empresa:

    def __init__(self, nome, cnpj,endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco=endereco
        self.lista_func_limpeza = []
        self.lista_func_atendimento=[]
        self.lista_clientes = []
        self.lista_medicos=[]
        self.lista_convenios=[]
        self.lista_agendamentos=[]
        self.lista_agendamento_convenios=[]
        self.lista_emails=[]

    def __str__(self):
        return f"NOME EMPRESA: {self.nome}\nCNPJ: {self.cnpj}\nENDEREÇO: {self.endereco}"

    def get_func_limpeza(self, rg):
        for func_limpeza in self.lista_func_limpeza:
            if func_limpeza.rg == rg:
                return func_limpeza
        return None
    
    def get_func_atendimento(self, rg):
        for func_atendimento in self.lista_func_atendimento:
            if func_atendimento.rg == rg:
                return func_atendimento
        return None

    def get_cliente(self, rg):
        for cliente in self.lista_clientes:
            if cliente.rg == rg:
                return cliente
        return None

    def get_medico_crm(self, crm):
        for medico in self.lista_medicos:
            if medico.crm == crm:
                return medico
        return None 
    
    def get_medico_especialidade(self, especialidade):
        for medico in self.lista_medicos:
            if medico.especialidade == especialidade:
                return medico
        return None 

    def get_convenio(self, sigla):
        for convenio in self.lista_convenios:
            if convenio.sigla == sigla:
                return convenio
        return None 
    
    def get_agendamento_convenio(self,data,horario):
        for agendamento in self.lista_agendamento_convenios:
            if agendamento.data == data and agendamento.horario == horario:
                return agendamento
        return None

    def get_agendamento_nao_conveniado(self,data,horario):
        for agendamento in self.lista_agendamentos:
            if agendamento.data == data and agendamento.horario == horario:
                return agendamento
        return None

    def cadastrar_cliente(self,cliente):
        self.lista_clientes.append(cliente)
        return cliente
  
    def alterar_cliente(self,rg,novo_nome,novo_telefone,novo_endereco):
        cliente=self.get_cliente(rg)
        if cliente!=None:
            cliente.nome=novo_nome
            cliente.telefone=novo_telefone
            cliente.endereco_cliente=novo_endereco
            return True
        return False

    def remover_cliente(self,rg):
        cliente=self.get_cliente(rg)
        if cliente!=None:
            cliente.ativo=False
            return  True
        return False
    
    def cliente_ativo(self):
        clientes=[]
        for cliente in self.lista_clientes:
            if cliente.ativo == True:
                clientes.append(cliente)
        return clientes
    
    def cliente_inativo(self):
        clientes=[]
        for cliente in self.lista_clientes:
            if cliente.ativo == False:
                clientes.append(cliente)
        return clientes
    
    def cadastrar_func_limpeza(self, func_limpeza):            
        self.lista_func_limpeza.append(func_limpeza)

    def alterar_func_limpeza(self,rg,novo_nome,novo_telefone,novo_endereco):
        func_limpeza=self.get_func_limpeza(rg)
        if func_limpeza!=None:
            func_limpeza.nome=novo_nome
            func_limpeza.telefone=novo_telefone
            func_limpeza.endereco=novo_endereco
            return True
        return False

    def remover_func_limpeza(self,rg):
        func_limpeza=self.get_func_limpeza(rg)
        if func_limpeza!=None:
            func_limpeza.ativo=False
            return True
        return False

    def func_limp_ativo(self):
        funcionarios_limp=[]
        for func_limp in self.lista_func_limpeza:
            if func_limp.ativo == True:
                funcionarios_limp.append(func_limp)
        return funcionarios_limp
    
    def func_limp_inativo(self):
        funcionarios_limp=[]
        for func_limp in self.lista_func_limpeza:
            if func_limp.ativo == False:
                funcionarios_limp.append(func_limp)
        return funcionarios_limp

    def cadastrar_func_atendimento(self, func_atendimento):           
        self.lista_func_atendimento.append(func_atendimento)

    def alterar_func_atendimento(self,rg,novo_nome,novo_telefone,nova_especialidade, novo_endereco):
        func_atendimento=self.get_func_atendimento(rg)
        if func_atendimento!=None:
            func_atendimento.nome=novo_nome
            func_atendimento.telefone=novo_telefone
            func_atendimento.especialidade=nova_especialidade
            func_atendimento.endereco=novo_endereco
            return True
        return False

    def remover_func_atendimento(self,rg):
        func_atendimento=self.get_func_atendimento(rg)
        if func_atendimento!=None:
            func_atendimento.ativo=False
            return True
        return False

    def func_atend_ativo(self):
        funcionarios_atend=[]
        for func_atend in self.lista_func_atendimento:
            if func_atend.ativo == True:
                funcionarios_atend.append(func_atend)
        return funcionarios_atend
    
    def func_atend_inativo(self):
        funcionarios_atend=[]
        for func_atend in self.lista_func_atendimento:
            if func_atend.ativo == False:
                funcionarios_atend.append(func_atend)
        return funcionarios_atend
    
    def cadastrar_convenio(self,convenio):
        self.lista_convenios.append(convenio)

    def alterar_convenio(self,sigla,nova_sigla,novo_nome,novo_telefone):
        for convenio in self.lista_convenios:
            if convenio.sigla == sigla:
                convenio.sigla=nova_sigla
                convenio.nome=novo_nome
                convenio.telefone=novo_telefone
                return True
        return False
    
    def remover_convenio(self,sigla):
        convenio=self.get_convenio(sigla)
        if convenio!=None:
            convenio.ativo=False
            return True
        return False

    def convenio_ativo(self):
        convenios=[]
        for convenio in self.lista_convenios:
            if convenio.ativo == True:
                convenios.append(convenio)
        return convenios
    
    def convenio_inativo(self):
        convenios=[]
        for convenio in self.lista_convenios:
            if convenio.ativo == False:
                convenios.append(convenio)
        return convenios

    def cadastrar_medico(self,medico):
        self.lista_medicos.append(medico)

    def alterar_medico(self,crm,novo_nome,novo_telefone,nova_especializacao):
        medico=self.get_medico_crm(crm)
        if medico!=None:
            medico.nome=novo_nome
            medico.telefone=novo_telefone
            medico.especialidade=nova_especializacao
            return True
        return False
    
    def remover_medico(self,crm):
        medico=self.get_medico_crm(crm)
        if medico!=None:
            medico.ativo=False
            return True
        return False
    
    def medico_ativo(self):
        medicos=[]
        for medico in self.lista_medicos:
            if medico.ativo == True:
                medicos.append(medico)
        return medicos
    
    def medico_inativo(self):
        medicos=[]
        for medico in self.lista_medicos:
            if medico.ativo == False:
                medicos.append(medico)
        return medicos
    
    def cadastrar_agendamento_convenio(self,agendamento):
        self.lista_agendamento_convenios.append(agendamento)

    
    def cadastrar_agendamento(self,agendamento):
        self.lista_agendamentos.append(agendamento)

    def alterar_agendamento_convenio(self,agendamento,nova_data,novo_horario):
            
        agendamento.data=nova_data
        agendamento.horario=novo_horario

    def alterar_agendamento_nao_conveniado(self,agendamento,nova_data,novo_horario):
            
        agendamento.data=nova_data
        agendamento.horario=novo_horario
       
    def remover_agendamento_convenio(self,data,horario):
        agendamento=self.get_agendamento_convenio(data,horario)
        if agendamento!=None:
            self.lista_agendamento_convenios.remove(agendamento)
            return True
        return False
    
    def remover_agendamento_nao_conveniado(self,data,horario):
        agendamento=self.get_agendamento_nao_conveniado(data,horario)
        if agendamento!=None:
            self.lista_agendamentos.remove(agendamento)
            return True
        return False

    def cadastrar_email(self,email):

        self.lista_emails.append(email)

class Func_limpeza:

    def __init__(self,rg,nome,telefone,end_func_limpeza):
        self.rg=rg
        self.nome = nome
        self.telefone = telefone
        self.end_func_limpeza=end_func_limpeza
        self.ativo=True


    def __str__(self):
        return f"RG: {self.rg}\n NOME: {self.nome}\n TELEFONE: {self.telefone}\n {self.end_func_limpeza}"
       
class Func_atendimento:

    def __init__(self,rg,nome,telefone,especialidade,end_func_atendimento):
        self.rg=rg
        self.nome = nome
        self.telefone = telefone
        self.especialidade=especialidade
        self.end_func_atendimento=end_func_atendimento
        self.ativo=True

    def __str__(self):
        return f"RG: {self.rg}\n NOME: {self.nome}\n FONE: {self.telefone}\n {self.especialidade}\n {self.end_func_atendimento}"
      
class End_func_limpeza:

    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"RUA: {self.rua}\nCIDADE: {self.cidade}\nESTADO: {self.estado}"
    
class End_func_atendimento:

        def __init__(self, rua, cidade, estado):
            self.rua = rua
            self.cidade = cidade
            self.estado = estado
        def __str__(self):
            return f"RUA: {self.rua}\nCIDADE: {self.cidade}\nESTADO: {self.estado}"

class Especialidade_func_atendimento:

    def __init__(self, nome_curso, ano_conclusao, faculdade, titulo):
        self.nome_curso = nome_curso
        self.ano_conclusao = ano_conclusao
        self.faculdade=faculdade
        self.titulo=titulo

    def __str__(self):
        return f"CURSO: {self.nome_curso}\nANO CONCLUSÃO: {self.ano_conclusao}\nFACUDADE: {self.faculdade}\nTITULO: {self.titulo}"

class Cliente:

    def __init__(self, rg,nome, telefone,endereco_cliente,email):
        self.rg=rg
        self.nome = nome
        self.telefone = telefone
        self.endereco_cliente=endereco_cliente
        self.email=email
        self.ativo=True

    def __str__(self):
        return f"RG: {self.rg}\nNOME: {self.nome}\nFONE: {self.telefone}\n{self.endereco_cliente}"
    
class Endereco_cliente:

    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"RUA: {self.rua}\nCIDADE: {self.cidade}\nESTADO: {self.estado}"
  
class Medico:

    def __init__(self, crm,nome, telefone,especialidade):
        self.crm=crm
        self.nome = nome
        self.telefone = telefone
        self.especialidade=especialidade
        self.ativo=True

    def __str__(self):
        return f"CRM: {self.crm}\nNOME MÉDICO: {self.nome}\nFONE: {self.telefone}\nESPECIALIDADE: {self.especialidade}"
    
class Especialidade_medica:

    def __init__(self, nome_curso, ano_conclusao):
        self.nome_curso = nome_curso
        self.ano_conclusao = ano_conclusao

    def __str__(self):
        return f'{self.nome_curso}'
          
class Convenio:
    def __init__(self,sigla,nome,telefone):
        self.sigla=sigla
        self.nome=nome
        self.telefone=telefone
        self.lista_hospitais=[]
        self.lista_medicos_convenio=[]
        self.ativo=True

    def __str__(self):
        return f"SIGLA: {self.sigla}\nNOME: {self.nome}\nTELEFONE: {self.telefone}" 
    
    def cadastrar_hospital(self,hospital):
        self.lista_hospitais.append(hospital)

    def cadastrar_medico_conveniado(self,medico):
        self.lista_medicos_convenio.append(medico)

class Hospital:
    def __init__(self,nome,cidade):
        self.nome=nome
        self.cidade=cidade
        self.lista_medicos_hospital=[]
    def __str__(self):
        return f"NOME HOSPITAL: {self.nome}\nLOCAL: {self.cidade}" 
                     
class Agendamento_convenio:
    def __init__(self,data,horario,cliente,convenio,medico):
        self.data=data
        self.horario=horario
        self.cliente=cliente
        self.convenio=convenio
        self.medico=medico
    
        

    def __str__(self):
        return f"DATA: {self.data}\nHORARIO: {self.horario}\n{self.cliente}\n{self.convenio}\n{self.medico}"
 
class Agendamento_nao_conveniado:
    def __init__(self,data,horario,cliente,medico):
        self.data=data
        self.horario=horario
        self.cliente=cliente
        self.medico=medico
        
        

    def __str__(self):
        return f"DATA: {self.data}\nHORARIO: {self.horario}\n{self.cliente}\n{self.medico}"

class Email:
    def __init__(self,email):
        self.email=email
    def __str__(self):
        return f"EMAIL: {self.email}"
    