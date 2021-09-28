from tqdm import tqdm
import time

# forma mais simples
#for i in tqdm(range(10)):
#    time.sleep(1)

""" lista = [1,2,3,10,15]

for item in tqdm(lista):
    time.sleep(1) """

""" with tqdm(total=100) as barra_progresso:
    for i in range(10):
        time.sleep(1)
        barra_progresso.update(10) """

# Quero entregar pra cidade do Rio de Janeiro
import requests

# Passo 1 = Pegar a lista de ceps
with open('ceps.txt', 'r') as arquivo:
    ceps = arquivo.read()
ceps = ceps.split('\n')

# Passo 2 = pegar as informações de cada cep
enderecos_entrega = [] # Para não printar a barra de progresso em cada linha
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
    # Passo 3 = Verificar se a cidade é Rio de Janeiro
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']

    # Passo 4 = Printar o cep e o bairro  
    if cidade == 'Rio de Janeiro':
        enderecos_entrega.append((cep,bairro))
        #print(cep, bairro) Iria printar a barra de progresso em cada linha
print(enderecos_entrega)