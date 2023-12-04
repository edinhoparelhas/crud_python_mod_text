ACESSAR_FUNCIONARIO="1"
ACESSAR_CLIENTE="2"
ACESSAR_CONVENIO="3"
AGENDAR_ATENDIMENTO="4"

CADASTRAR_CLIENTE="1"
ALTERAR_DADOS_CLIENTE="2"
REMOVER_CLIENTE="3"
LISTA_CLIENTES_ATIVOS="4"
LISTA_CLIENTES_INATIVOS="5"
DADOS_CLIENTE="6"

CADASTRAR_FUNCIONARIO="1"
ALTERAR_DADOS_FUNCIONARIO="2"
REMOVER_FUNCIONARIO="3"
LISTA_FUNCIONARIOS_ATIVOS="4"
LISTA_FUNCIONARIOS_INATIVOS="5"
DADOS_FUNCIONARIO="6"

MEDICO="1"
FUNCIONARIO_LIMPEZA="2"
FUNCIONARIO_ATEND="3"

CADASTRAR_MEDICO="1"
ALTERAR_DADOS_MEDICO="2"
REMOVER_MEDICO="3"
LISTA_MEDICOS_ATIVOS="4"
LISTA_MEDICOS_INATIVOS="5"
DADOS_MEDICO="6"
SAIR="0"

CADASTRAR_CONVENIO="1"
ALTERAR_CONVENIO="2"
REMOVER_CONVENIO="3"
LISTA_CONVENIO="4"
LISTA_CONVENIO_INATIVOS="5"
DADOS_CONVENIO="6"
SAIR="0"

AGENDAR="1"
ALTERAR_AGENDAMENTO_CONVENIO="2"
ALTERAR_AGENDAMENTO_NAO_CONVENIADO="3"
REMOVER_AGENDAMENTO_CONVENIO="4"
REMOVER_AGENDAMENTO_NAO_CONVENIADO="5"
LISTA_AGENDAMENTOS_CONVENIO_ATIVOS="6"
LISTA_AGENDAMENTOS_ATIVOS_NAO_CONVENIADOS="7"
DADOS_AGENDAMENTO_CONVENIO="8"
DADOS_AGENDAMENTO_NAO_CONVENIADO="9"
SAIR="0"

MENU_PRINCIPAL= f'''
                

{ACESSAR_FUNCIONARIO} .................ACESSAR FUNCIONÁRIO
{ACESSAR_CLIENTE} ................ ACESSAR CLIENTE
{ACESSAR_CONVENIO}................. ACESSAR CONVÊNIO
{AGENDAR_ATENDIMENTO} ................ACESSAR AGENDAMENTO
{SAIR} ............... Sair
'''
MENU_CLIENTE= f'''
                

{CADASTRAR_CLIENTE} .................Cadastrar Cliente
{ALTERAR_DADOS_CLIENTE} ................ Alterar dados do Cliente
{REMOVER_CLIENTE}................. Remover Cliente
{LISTA_CLIENTES_ATIVOS}...................solicitar lista de clientes
{LISTA_CLIENTES_INATIVOS}...................solicitar lista de clientes inativos
{DADOS_CLIENTE}.................verificar cliente
{SAIR} ............... Sair
'''
MENU_FUNCIONARIO= f'''
                

{CADASTRAR_FUNCIONARIO} .................Cadastrar funcionario
{ALTERAR_DADOS_FUNCIONARIO} ................ Alterar dados do funcionario
{REMOVER_FUNCIONARIO}................. Remover funcionario
{LISTA_FUNCIONARIOS_ATIVOS}...................solicitar lista de funcionarios
{LISTA_FUNCIONARIOS_INATIVOS}...................solicitar lista de funcionarios inativos
{DADOS_FUNCIONARIO}.................verificar funcionario
{SAIR} ............... Sair

'''
MENU_CONVENIO= f'''

{CADASTRAR_CONVENIO} .................Cadastrar Convênio
{ALTERAR_CONVENIO} ................ Alterar dados do Convênio
{REMOVER_CONVENIO}................. Remover Convênio
{LISTA_CONVENIO}...................solicitar lista de Convênios
{LISTA_CONVENIO_INATIVOS}...................solicitar lista de Convênios inativos
{DADOS_CONVENIO}.................verificar Convênio
{SAIR} ............... Sair
'''
MENU_CADAST_FUNC= f'''
{MEDICO}..... MEDICO
{FUNCIONARIO_LIMPEZA}..... FUNCIONARIO DA LIMPEZA
{FUNCIONARIO_ATEND}..... FUNCIONARIO DO ATENDIMENTO
{SAIR} ............... Sair
'''
MENU_AGENDAMENTO= f'''
                
{AGENDAR} .................agendar Paciente
{ALTERAR_AGENDAMENTO_CONVENIO} ................ Alterar agendamento convenio
{ALTERAR_AGENDAMENTO_NAO_CONVENIADO} ................ Alterar agendamento não conveniado
{REMOVER_AGENDAMENTO_CONVENIO}................. Remover agendamento convênio
{REMOVER_AGENDAMENTO_NAO_CONVENIADO}................. Remover agendamento não convêniado
{LISTA_AGENDAMENTOS_CONVENIO_ATIVOS}...................solicitar lista de agendamentos de convenio
{LISTA_AGENDAMENTOS_ATIVOS_NAO_CONVENIADOS}...................solicitar lista de agendamentos não conveniados
{DADOS_AGENDAMENTO_CONVENIO}.................dados do agendamento para coveniado
{DADOS_AGENDAMENTO_NAO_CONVENIADO}.................dados do agendamento não conveniado
{SAIR} ............... Sair
'''

