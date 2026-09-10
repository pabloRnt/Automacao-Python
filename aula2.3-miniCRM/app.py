from model import model_lead
import control

def add_lead():

    name = input("Nome: ")
    email = input("E-mail: ")
    company = input("Empresa: ")
    step = input("Etapa de vendas: ")

    # Validar as entradas do usuário
    # Depois de validados, vamos modelar os dados

    print(model_lead(name, company, email, step))

    # Depois de modelado, vamos enviar o dict (leads) para o leads.json
    # Para salvar, vamos usar o módulo control

    control.create_lead(model_lead(name, company, email, step))
    print("Lead adicionado(func)")

def list_leads():

    leads = control.read_leads()

    if not leads:
        print("Nenhum lead ainda")
        return

    print(leads) # A FAZER: Formatar lista em uma tabela

def main():
    print("\nMini CRM de Leads")
    print("[1] - Adicionar Lead")
    print("[2] - Listar Leads")
    print("[0] - Sair do programa")

    opt = input("Escolha sua opção: ")

    while True:
        
        if opt =="1":
            add_lead()
        elif opt =="2":
            list_leads()
        elif opt =="0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()