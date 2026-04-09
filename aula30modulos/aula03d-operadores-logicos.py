#lÓGICA e (and)

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no programa...")

#Lógica OU (ou)

logica_ou = False or False or True
print(logica_ou)

#Lógica NEGAÇÃO (not)

negacao = not False
print(negacao)

if not login:
    print("Digita certo ai...")