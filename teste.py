from model import *
from povoar import *

nome= "CLINIC CONTROL"
cnpj="55.238.976/0001-33"
endereco="Rua José Cavalcante Nº 177 Parelhas RN"
empresa=Empresa(nome,cnpj,endereco)
povoar(empresa)

verif=empresa.remover_agendamento_convenio(10,10.0)

print(verif)