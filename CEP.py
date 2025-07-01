import requests
from time import sleep

#Digita o CEP
while True:
    cep = input('Digite o CEP (somente númemros): ')
    #Verifica se o CEP tem 8 digítos
    if len(cep) != 8 or not cep.isdigit():
        print('CEP inválido!')
    else:
        print('PESQUISANDO...')
        sleep(0.3)
    #Monta a URL da API
        url = f'https://viacep.com.br/ws/{cep}/json/'

    #Faz a requisição
        response = requests.get(url)
        
    #200 OK, Requisição recebida    
        if response.status_code == 200:
            data = response.json()

    #Verifica se tem erro no CEP
            if 'erro' in data:
                print('CEP não encontrado.')
            else:
                print('\n Informações do CEP:')
                print(f'CEP: {data.get('cep')}')
                print(f'Logradouro: {data.get('logradouro')}')
                print(f'Bairro: {data.get('bairro')}')
                print(f'Cidade: {data.get('localidade')}')
                print(f'Estado: {data.get('uf')}')
        else:
            print('Erro na requisição. Verifique sua conexão com a internet.')
    
    resp = input('Deseja consultar outro CEP? [S/N]: ').strip().upper()
    if resp == 'N':
        print('Encerrando o programa. Até!')
        sleep(1)
        break
