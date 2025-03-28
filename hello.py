#!/usr/bin/env python3 - linux
"""Hello World Multi Línguas.

Dependendo da lingua configurada no ambienteo programa exibe a mensagem correspondente.
Como usar:
Tenha a variável LANG devidamente configurada ex:
    
     export LANG=pt BR
Execução:
    
    python3 hello.py
    ou
    .//hello.py
     
"""
""" 
__version__"0.0.1" # type:
__author__ "Gleice Avelino" 
__license__ "Unlincense"

"""

import os 

current_language = os.getenv("LANG", "us_US")[:5]

msg = "Hello, Word!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo"
print(msg)
