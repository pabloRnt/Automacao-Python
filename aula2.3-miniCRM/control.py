from pathlib import Path # Necessário para acessar caminhos de diretórios
import json, csv # Necessário para manipular JSON e CSV

DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "leads.json"

# === CRUD ===

# READ
def read_leads()->list:

    if not DB_PATH.exists(): # Se o caminho não existir
        return []

    try: 
        return json.loads(DB_PATH.read_text(encoding="utf_8")) # Carrega o arquivo json usando o path do "banco de dados" usando o encode usual do Brasil (utf-8)

    except json.JSONDecodeError:
        return []


# CREATE
def create_lead(lead_dict):

    leads = read_leads() # Retorna TODA lista de dicionários de leads (inviável em produção)
    leads.append(lead_dict)

    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8") # Envia ao banco de dados em formato JSON (json.dumps) a lead_criado

def update_lead(query):
    
    leads = read_leads()
    
    results = read_leads_search(query)
    
    if not results:
        print("Nenhum lead encontrado!")
        return
    
    houve_alteracao = False
    
    for result in results:
        index_lead = result[0]
        lead = result[1] 
            
        campo = input("Qual informação você quer alterar? ").lower()
        alteracao = input(f"{campo.capitalize()}: ")
        
        if input("Tem certeza da alteração? ").lower() == "sim":
            
            # Atualiza o lead modificado dentro da lista completa de leads
            lead[campo] = alteracao
            leads[index_lead] = lead
            houve_alteracao=True
    
    if houve_alteracao:   
        with open(DB_PATH, 'w', encoding='utf-8') as file:
            json.dump(leads, file, ensure_ascii=False, indent=4)

# === EXPORTAR CSV ===

def export_csv():
    '''Exporta os leads consultados para CSV e RETORNA caminho de arquivo criado'''

    path_csv = DATA_DIR / "leads.csv"

    leads = read_leads()

    try:
        with path_csv.open(mode="w", newline="", encoding="utf8") as file_csv:
            writer = csv.DictWriter(file_csv, leads[0].keys())
            writer.writeheader()

            for row in leads:
                writer.writerow(row) # Como declaramos o leitor como DictWriter, ele deduz que cada registro a ser escrito está em formato de dicionário

    except PermissionError:
        return None;

# === READ LEADS FROM QUERY/SEARCH ===

def read_leads_search(query):

    leads = read_leads()
    results = []

    for i, lead in enumerate(leads):

        txt_lead = f"{lead["name"]} {lead["email"]} {lead["company"]}".lower()

        if query.lower() in txt_lead:
            results.append((i, lead)) # (0, {"name": "Alexandre"...})

    return results
