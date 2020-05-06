#!D:\alexandros\programming\python\pyProjects\texnLogismikou\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'django-herokuapp==0.9.20','console_scripts','herokuapp_startproject.py'
__requires__ = 'django-herokuapp==0.9.20'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('django-herokuapp==0.9.20', 'console_scripts', 'herokuapp_startproject.py')()
    )
