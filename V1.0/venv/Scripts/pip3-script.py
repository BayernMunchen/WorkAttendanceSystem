#!C:\Users\lenovo\Desktop\2018\实践是检验真理的唯一标准\python课程设计\venv\Scripts\python.exe -x
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==9.0.1','console_scripts','pip3'
__requires__ = 'pip==9.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==9.0.1', 'console_scripts', 'pip3')()
    )
