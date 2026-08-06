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

for requisicoes in status:
    
    numero_requisicoes = 0
    requisicoes_ok = 0
    porcentagem_requisicoes_ok = []

    for requisicao in requisicoes:

        numero_requisicoes += 1

        status_requisicao = lambda req: req >= 200 and req <= 299
        if status_requisicao:
            requisicoes_ok += 1

    porcentagem_requisicoes_ok.append(requisicoes_ok/len(requisicoes))

endpoint_menos_ok = status(status.index(min(porcentagem_requisicoes_ok)))