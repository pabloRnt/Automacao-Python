'''Crie um programa que:
1. calcule a porcentagem de requisições bem-sucedidas de
cada endpoint;
2. identifique o endpoint com mais erros;
3. verifique se algum endpoint teve dois erros seguidos;
4. classifique cada endpoint como:
▪ ESTÁVEL: pelo menos 80% de sucesso

Considere sucesso qualquer código entre 200 e 299.
O programa deve utilizar pelo menos uma função e
funcionar caso novos endpoints ou requisições sejam
adicionados'''

endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500] 
]

endpoint_mais_erros = None
porcentagem_requisicoes_ok = []
endpoint_2_erros_seguidos = []

for i, requisicoes in enumerate(status):
    
    numero_requisicoes = len(requisicoes)
    requisicoes_ok = 0
    
    lista_status_requisicao = []

    for requisicao in requisicoes:
        
        status_requisicao = lambda req: req >= 200 and req <= 299
        if status_requisicao(requisicao):
            requisicoes_ok += 1
            lista_status_requisicao.append(True)
        else:
            lista_status_requisicao.append(False)

    for j in range(len(lista_status_requisicao)-1):
        
        if lista_status_requisicao[j] == False and lista_status_requisicao[j+1] == False:
            endpoint_2_erros_seguidos.append(endpoints[i])
            break
    
    porcentagem_requisicoes_ok.append(requisicoes_ok/len(status[i])*100)
endpoint_mais_erros = endpoints[porcentagem_requisicoes_ok.index(min(porcentagem_requisicoes_ok))]

string_porcentagem_requisicoes_ok = list(map(lambda x: str(x), porcentagem_requisicoes_ok))
string_endpoint_2_erros_seguidos = list(map(lambda x: str(x), endpoint_2_erros_seguidos))
string_endpoint_mais_erros = list(map(lambda x: str(x), endpoint_mais_erros))

print(f"A porcentagem de requisições bem sucedidas em cada endpoint foram, respectivamente: {'. '.join(string_porcentagem_requisicoes_ok[:-1] )} e {string_porcentagem_requisicoes_ok[-1]} %")
print(f"O endpoint com mais erros foi o {endpoint_mais_erros}")

match len(string_endpoint_2_erros_seguidos):
    case 1:
        print(f"O endpoint com pelo menos 2 erros seguidos foi {string_endpoint_2_erros_seguidos[0]}")        
    case 2:
        print(f"Os endpoints com pelo menos 2 erros seguidos foram {string_endpoint_2_erros_seguidos[0]} e {string_endpoint_2_erros_seguidos[1]}")
    case _:
        print(f"Os endpoints com pelo menos 2 erros seguidos foram {', '.join(string_endpoint_2_erros_seguidos[:-1])} e {string_endpoint_2_erros_seguidos[-1]}")
            