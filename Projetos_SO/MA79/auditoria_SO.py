import os
import platform
from datetime import datetime

print("=" * 50)
print("RELATÓRIO DE AUDITORIA DO SISTEMA OPERACIONAL")
print("=" * 50)
print(f'Sistema Operacional  : {platform.system()} {platform.release()}')
print(f'Versão Detalhada     : {platform.version()}')
print(f'Arquitetura da CPU   : {platform.machine()}')
print(f'Processador          : {platform.processor()}')
print(f'Núcleos Lógicos      : {os.cpu_count()}')
print(f'Usuário Logado       : {os.getlogin()}')
print(f'Diretório Atual      : {os.getcwd()}')
print(f'Data/Hora Execução   : {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print("=" * 50)
