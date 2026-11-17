import os
import platform

print(f'Sistema Operacional         : {platform.system()}')
print(f'Usuário Logado              : {os.getlogin()}')
print(f'Diretório Atual             : {os.getcwd()}')
input(f'Informe o Status da Máquina : ')