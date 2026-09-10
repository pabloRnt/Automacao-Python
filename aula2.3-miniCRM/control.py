from pathlib import Path # Necessário para acessar caminhos de diretórios
import json # Necessário para manipular JSON

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

print(read_leads())

# CREATE

def create_lead(lead_dict):

    leads = read_leads() # Retorna TODA lista de dicionários de leads (inviável em produção)
    leads.append(lead_dict)

    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8") # Envia ao banco de dados em formato JSON (json.dumps) a lead_criado