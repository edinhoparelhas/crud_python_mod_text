from model import *
from povoar import *

nome= "CLINIC CONTROL"
cnpj="55.238.976/0001-33"
endereco="Rua José Cavalcante Nº 177 Parelhas RN"
empresa=Empresa(nome,cnpj,endereco)
povoar(empresa)

lista=empresa.lista_agendamento_convenios
for agend in lista:
    print(agend)
    print("............")

verif=empresa.remover_agendamento_convenio(20,10.00)

print(verif)

lista=empresa.lista_agendamento_convenios
for agend in lista:
    print(agend)
    print("............")