
# python3 -m pip install pip setuptools wheel --upgrade
# Ou py,  estamos instalando e   (Fazendo o upgrade também)

#### Criando um ambiente virtual ###
# Primeir criamos a pasta em qustão, depois entramos no interpretador e apontamos a pasta
# Vamos em view e terminal, e digitamos py -m venv venv para dar o nome de venv para a venv
# Depois temos que ativar a venv, venv\scripts\activate , no windows pode dar aquele erro
# de polici, então temos que colocar no power shell aquela instrução.

### Configurando Github via SSH ###

# git config --global user.name "A7Gabriel"
# OBS: Temos que estar dentro da pasta do projeto, aqui estamos via terminal do windows
# Estamos acessando o usuário em questão!

# git config --global user.email "suportegabriel@gmail.com"
# Definindo o email

# git config --global init.defaultBrach main
# Definindo nome para o Branch, como main

# git init
#Reinicializa o projeto

#######  Criando uma chave de SSH #######

# No terminal: ssh-keygen, vai criar o endereço no pc onde será salvo e pedir senha

# Ele vai criar a pasta SSH no diretório raiz do usuário em questão, vamos até a pasta
#ssh e abrimos o arquivo id_rsa.pub , pode ser com bloco de notas
# Logo depois vamos copiar o conteúdo "chave pública" 
# Vamos até o site do git e selecionamos Perfil em cima a direita, depois settings
# Logo depois, SSH e GPG KEYS, colamos na guia SSH e confirmamos.
# logo depois escolhemos SSH e copiamos o link
# Vamos no terminal e inserimos: git remote origin link copiado
# no git remote git remote -v, vai mostra a origem de fetch e push
# Depois git init para initializar o git na pasta em questão

###########  GIT INGNORE ##############
# Serve para ingnorar arquivos para que não vá para o repositório no github



