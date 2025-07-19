README for Hello World Multi Línguas
This hello.py script is a simple Python program that displays "Hello, World!" in different languages based on the user's environment settings. It's designed to be straightforward and demonstrate basic internationalization.

How it Works
The script checks the LANG environment variable to determine the user's preferred language. If LANG is set to a supported language (Portuguese, Italian, Spanish, or French), it prints the corresponding "Hello, World!" message. Otherwise, it defaults to English.

Supported Languages
English (default): "Hello, World!"

Portuguese (pt_BR): "Olá, Mundo!"

Italian (it_IT): "Ciao, Mondo"

Spanish (es_SP): "Holla, Mundo!"

French (fr_FR): "Bonjour Monde"

Usage
Set the LANG environment variable:
Before running the script, ensure your LANG environment variable is correctly configured. For example, to set it to Brazilian Portuguese:

Bash

export LANG=pt_BR
You can verify your current LANG setting by typing echo $LANG in your terminal.

Run the script:

Using python3:

Bash

python3 hello.py
As an executable (if permissions are set):

Bash

./hello.py
To make it executable, you might need to run chmod +x hello.py first.

Example
If your LANG is set to pt_BR, running the script will output:

Olá, Mundo!
If LANG is not set or set to an unsupported language (e.g., en_US), it will output:

Hello, World!
Author: Gleice Avelino
Version: 0.0.1
License: Unlicense

EM Portuguese

README para Hello World Multi Línguas
Este script hello.py é um programa Python simples que exibe "Olá, Mundo!" em diferentes idiomas, com base nas configurações de ambiente do usuário. Ele foi projetado para ser direto e demonstrar a internacionalização básica.

Como Funciona
O script verifica a variável de ambiente LANG para determinar o idioma preferido do usuário. Se LANG estiver configurada para um idioma suportado (português, italiano, espanhol ou francês), ele imprimirá a mensagem "Olá, Mundo!" correspondente. Caso contrário, o padrão será o inglês.

Idiomas Suportados
Inglês (padrão): "Hello, World!"

Português (pt_BR): "Olá, Mundo!"

Italiano (it_IT): "Ciao, Mondo"

Espanhol (es_SP): "Holla, Mundo!"

Francês (fr_FR): "Bonjour Monde"

Como Usar
Defina a variável de ambiente LANG:
Antes de executar o script, certifique-se de que sua variável de ambiente LANG esteja configurada corretamente. Por exemplo, para configurá-la para português do Brasil:

Bash

export LANG=pt_BR
Você pode verificar sua configuração atual de LANG digitando echo $LANG no seu terminal.

Execute o script:

Usando python3:

Bash

python3 hello.py
Como um executável (se as permissões estiverem definidas):

Bash

./hello.py
Para torná-lo executável, talvez você precise executar chmod +x hello.py primeiro.

Exemplo
Se sua variável LANG estiver definida como pt_BR, a execução do script resultará em:

Olá, Mundo!
Se LANG não estiver definida ou estiver definida para um idioma não suportado (por exemplo, en_US), o resultado será:

Hello, World!
Autor: Gleice Avelino
Versão: 0.0.1
Licença: Unlicense
