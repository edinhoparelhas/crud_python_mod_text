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

data=21
horario=10.00


verif=empresa.remover_agendamento_convenio(data,horario)

print(f"\n{verif}\n")

lista=empresa.lista_agendamento_convenios
for agend in lista:
    print(agend)
    print("............")