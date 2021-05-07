# Importações...
import os
import time
import sys
import json
try:
    from colorama import Fore
    import requests
    from requests.api import request
except:
    print("Baixando requirementos")
    os.system('pip install requests colorama')

# Variaveis!

consulta_local = "Menu"
vercao = "1.8 BETA"
titulo = "GrabberTool Verção 1.8! "

# Banner's

BannerMenu = (f'''
    {Fore.LIGHTBLUE_EX}
     _______            __    __               _______             __
    |   _   .----.---.-|  |--|  |--.-----.----|       .-----.-----|  |
    |.  |___|   _|  _  |  _  |  _  |  -__|   _|.|   | |  _  |  _  |  |_____.
    |.  |   |__| |___._|_____|_____|_____|__| `-|.  |-|_____|_____|________|
    |:  1   |                                   |:  |                 
    |::.. . |                                   |::.|                 
    `-------'                                   `---'{Fore.LIGHTWHITE_EX}
    ''')

# Menu inicial...

def menu():
    """
    Menu inicial para consultas
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    consulta_local = "Menu"
    os.system('title ' + titulo + '- ' + consulta_local)
    print(BannerMenu)
    print(f'''
        1 - Consulta CEP
        2 - Consulta CPF
        3 - Consulta CNPJ
        4 - Consulta Placa
        5 - Consulta Bin
        6 - Consulta Numero {Fore.LIGHTGREEN_EX}[Simples]{Fore.LIGHTWHITE_EX} {Fore.LIGHTRED_EX}[OFF]{Fore.LIGHTWHITE_EX}
        7 - Checker CC {Fore.LIGHTRED_EX}[OFF]{Fore.LIGHTWHITE_EX}
        8 - Consulta Nome
        {Fore.LIGHTRED_EX}0 - Fechar{Fore.LIGHTWHITE_EX}
        ''')
    inputt = input('[Escolha um]:')
    if inputt == '1' or inputt == '01':
        print('')
        cleaner()
        consulta_local = "CEP"
        os.system('title ' + titulo + '- ' + consulta_local)
        consultacep()
    if inputt == '2' or inputt == '02':
        print('')
        cleaner()
        consulta_local = "CPF"
        os.system('title ' + titulo + '- ' + consulta_local)
        consultacpf()
    if inputt == '3' or inputt == '03':
        print('')
        cleaner()
        consulta_local = "CNPJ"
        os.system('title ' + titulo + '- ' + consulta_local)
        consultacnpj()
    if inputt == '4' or inputt == '04':
        print('')
        cleaner()
        consulta_local = "PLACA"
        os.system('title ' + titulo + '- ' + consulta_local)
        consultaplaca()
    if inputt == '5' or inputt == '05':
        print('')
        cleaner()
        consulta_local = "BIN"
        os.system('title ' + titulo + '- ' + consulta_local)
        consultabin()
    if inputt == '6' or inputt == '06':
        print('')
        cleaner()
        consulta_local = "NUMERO"
        os.system('title '+ titulo + '- ' + consulta_local)
        consultanum()
    if inputt == '7' or inputt == '07':
        print('')
        cleaner()
        consulta_local = "CHECKER GG"
        os.system('title ' + titulo + '- ' + consulta_local)
        checkercc()
    if inputt == '8' or inputt == '08':
        print('')
        cleaner()
        consulta_local = "NOME"
        os.system('title ' + titulo + '- ' + consulta_local)
        consultanome()
    if inputt == '0' or inputt == '00':
        cleaner()
        exit()
    else:
        print('')
        cleaner()
        error404()

# Ferramentas e Gerenciamento geral!

def consultacep():
    cleaner()
    print(BannerMenu)
    cep = input('Digite o CEP:\n')
    url = f"https://ws.apicep.com/cep/{cep}.json"
    try:
        json: object = requests.get(url).json()
        cep = json["code"]
        bairro = json["district"]
        estado = json["state"]
        cidade = json["city"]
        rua = json["address"]
        Spinner()
        print('')
        print('Busca Completa')
        print('Dados coletados...')
        print('-============///////=============-')
        print('CEP :', json["code"])
        print('Bairro :', json["district"])
        print('Endereco :', json["address"] )
        print('Cidade :', json["city"])
        print('Estado :', json["state"])
        print('-============///////=============-')
        print('')
    except:
        print('A busca não pode ser completada')
    print('Em 10 Segundos voce voltara ao menu!')
    time.sleep(10.0)
    cleaner()
    menu()
def consultacpf():
    cleaner()
    print(BannerMenu)
    cpf_consultar = input('-=>>')
    data = requests.get('http://api.trackear.com.br/basepv/cpf/{}/noip'.format(cpf_consultar)).json()
    print("CPF: {}".format(data['cpf']))
    print("Nome: {}".format(data['nome']))
    print("Sexo: {}".format(data['sexo']))
    print("Data de Nascimento: {}".format(data['dtNascimento']))
    print("Idade: {}".format(data['idade']))
    print('Em 5 Segundos voce voltara ao menu!')
    time.sleep(5.0)
    cleaner()
    menu()
def consultanome():
    cleaner()
    print(BannerMenu)
    individuo = input(">>")
    r = requests.get("http://45.178.183.3/nome.php?nome={}".format(individuo))
    r = r.json()
    results = r["quantidadeResultados"]
    results = int(results)
    print("Quantidade de resultados: ", r["quantidadeResultados"])
    if results < 1:
        print('Não encontrado nada')
    else:
        i = 0
        try:
            print('-============///////=============-')
            while i < 10 :
                print("CPF:", r["resultados"][i]["cpf"])
                print("Nome Completo:", r["resultados"][i]["nome"])
                print("Nascimento:", r["resultados"][i]["nascimento"])
                print("Sexo:", r["resultados"][i]["sexo"])
                i += 1
            print('-============///////=============-')
        except:
            print('-============///////=============-')
            print("Não foi possivel printar mais!")
    time.sleep(10)
def consultacnpj():
    cleaner()
    print(BannerMenu)
    cnpj = input('Digite o CNPJ :\n')
    try: 
        url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
        cpj = requests.get(url).json()
        print('Encontrado!')
        print('Dados coletados...')
        print('-============///////=============-')
        print('Nome:', cpj["nome"])
        print('Nome Fantasia:', cpj["fantasia"])
        print('Estado:', cpj["uf"])
        print('Telefone:', cpj["telefone"])
        print('Email:', cpj["email"])
        print('Data de abertura:', cpj["abertura"])
        print('Capital:', cpj["capital_social"])
        print('Situacao:', cpj["situacao"])
        print('Municipio:', cpj["municipio"])
        print('CEP:', cpj["cep"])
        print('Bairro:', cpj["bairro"])
        print('Porte:', cpj["porte"])
        print('-============///////=============-')
        print('')
    except:
        print('Algo não ocorreu bem...')
    print('Em 10 Segundos voce voltara ao menu!')
    time.sleep(10.0)
    cleaner()
    menu()
def consultaplaca():
    cleaner()
    print(BannerMenu)
    print('''
    [I] Para buscar, utilize o exemplo:
    ABC-1224
    ''')
    placa = input('[<>]:')
    time.sleep(0.4)
    try:
        h = {
            
        }

        url = " "
        r=requests.post(url=url, headers=h)
        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Encontramos dados sobre a placa {placa}")
        print()
        time.sleep(10)
    except:
        print(f"{Fore.LIGHTRED_EX}[-]{Fore.LIGHTWHITE_EX} Não encontramos dados da placa {placa}")
        time.sleep(2)
def consultabin():
    cleaner()
    print(BannerMenu)
    Bin = input('Insira a Bin:')
    try:
        req = requests.get(f'https://lookup.binlist.net/{Bin}')
        BIN = json.loads(req.text)
        Spinner()
        print('')
        print('Bin:', Bin)
        print('Bandeira:', BIN["scheme"])
        print('Nivel:', BIN["type"])
        print('Tipo:', BIN["brand"])
    except:
        print('Algo não ocorreu bem...')
    print('Em 10 Segundos voce voltara ao menu!')
    time.sleep(10.0)
    cleaner()
    menu()
def consultanum():
    cleaner()
    print(BannerMenu)
    num = input('Digite o numero: ')
    try:
        numss = requests.get('{}'.format(num))
        result = (numss.text)
        Spinner()
        print('Encontrado!')
        print('Dados coletados...')
        print('-==//GrabberTool-Consulta//==-')
        print( result )
        print('-==//GrabberTool-Consulta//==-')
    except:
        print('Algo não ocorreu bem...')
    time.sleep(10.0)
    cleaner()
    menu()
def checkercc():
    cleaner()
    print(BannerMenu)
    print('Formato checker ( NumeroCC|Mes|Ano|CCV )')
    cc = input('Digite sua CC: ')
    try:
        resultado = requests.get(f'https://grabbertool.000webhostapp.com/Checker-api/?cartaum={cc}').text
        print('-==//GrabberTool-Consulta//==- \n',
              resultado, 
              '\n -==//GrabberTool-Consulta//==-')
    except:
        print('Algo não ocorreu bem...')
    print('Em 10 Segundos voce voltara ao menu!')
    time.sleep(10.0)
    cleaner()
    menu()
# 3RR0r 404
def error404():
    os.system('title Gr4bb3rT00l - BAD SYSTEM -=- ERRO 404')
    cleaner()
    print('ERROR 404 | Número Incorreto')
    print('')
    print('Em 2 Segundos voce voltara ao menu!')
    time.sleep(2.0)
    cleaner()
    menu()

# Faxineiro
def cleaner():
    try:
        os.system('cls')
    except:
        os.systtem('clear')
# Spinner's 

def Spinnerinicio():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r''[*] Iniciando...'+i)
		sys.stdout.flush()
		time.sleep(0.3)
def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r''[*] Consultando..'+i)
		sys.stdout.flush()
		time.sleep(0.3)

# Inicialização padrão

cleaner()
Spinnerinicio()
try:
    os.system('git pull')
    menu()
except KeyboardInterrupt:
    print("Quer sair? \nS - Sim\nN - Não")
    sair = input('[S/N]\n>>')
    if sair == 'S' or sair == 's':
        print('Ok, Adeus...')
        exit()
    else:
        print('Ok. Aguarde estamos redirecionando para o Menu!')
        time.sleep(5)
        menu()

