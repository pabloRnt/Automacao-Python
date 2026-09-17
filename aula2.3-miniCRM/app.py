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

    print(f"\n## | {"Nome":<10} | {"Email" :10} | {"Empresa":<10}")
    print("-"*50)

    for i, lead, in enumerate(leads):
        print(f"{i:02d} | {lead["name"] :10} | {lead["email"] :10} | {lead["company"]:<10}")
        
def search_leads():

    query = input("Buscar por: ").strip().lower()

    if not query:
        print("Consulta vazia")
        return

    # Envia a query para oo control realizar a busca no leads.json
    leads_finded = control.read_leads_search(query)
    print(f"\n## | {"Nome":<10} | {"Email" :10} | {"Empresa":<10}")
    print("-"*50)

    for i, lead in leads_finded:
        print(f"{i:02d} | {lead["name"] :10} | {lead["email"] :10} | {lead["company"]:<10}")

def export_leads():
   
    path_csv = control.export_csv()

    if path_csv is None:
       print("Não foi possível exportar os leads")
    else:
       print(f"Exportando para {path_csv}")

def main():

    while True:

        print("\nMini CRM de Leads")
        print("[1] - Adicionar Lead")
        print("[2] - Listar Leads")
        print("[3] - Buscar(nome/email/empresa)")
        print("[4] - Exportar CSV")
        print("[0] - Sair do programa")

        opt = input("Escolha sua opção: ")
        
        if opt =="1":
            add_lead()
        elif opt =="2":
            list_leads()
        elif opt =="3":
            search_leads()
        elif opt =="4":
            export_leads()
        elif opt =="0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()