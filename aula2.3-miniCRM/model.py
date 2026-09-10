from datetime import date
from json import dumps, loads

def model_lead(name, email, companay, step="novo")->dict:
    '''Estrutura um lead como um dicionário'''

    return {
        "name": name,
        "email": email,
        "company": companay,
        "step": step,
        "created_at": date.today().isoformat()
    }