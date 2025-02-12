import json
import pandas as pd
import sys

def toReceiveCategory(numr):
    categories = {
        '1': "Logistics",
        '2': "Carrier",
        '3': "Food",
        '4': "Cleaning"
    }
    return categories.get(numr, "Not defined")

def OpenAndCloseen(x,y=None):
    # Abrir e carregar os dados do arquivo
    if x == 'A':
        try:
            # Caminho para o arquivo
            with open('./company.data.json','r') as arquivo_json:
                return json.load(arquivo_json)
            
        except FileNotFoundError:
            # Cria um dicionário vazio se o arquivo não existir    
            return {}
    elif x == 'F':
        # Salvar os dados de volta no arquivo
        if y is not None:
            with open('./company.data.json', 'w') as arquivo_json:
                json.dump(y, arquivo_json, indent=4)
            return "File updated successfully!"
        return "No data to save."
    else:
        return "Invalid option."
    
# Abrindo ou criando arquivo JSON
object_json = OpenAndCloseen(x='A')

print("File opened successfully" if object_json != {} else "File not found. Creating a new one")

adc = input('To add?\n1-Yes\n2-No\3-Data Base\n>')
if adc == "1":

    # Editar os dados
    NameCompany = input("Enter company name: ").strip()
    while True:
        CnpjCompany = input("Enter the CNPJ: (14 digits): ").strip()
        caracter_repedito = CnpjCompany != CnpjCompany[0]*len(CnpjCompany)
        if caracter_repedito and CnpjCompany.isdigit() and len(CnpjCompany) == 14:
            break
        
        else:
            print("Invalid CNPJ! Please enter exactly 14 digits.") 
            print("Enter numbers only!!!")
            continue
        
        

     # Escolha da categoria
    Add = input("Enter the number corresponding to the category:\n"
                "1 -> Logistics\n2 -> Carrier\n3 -> Food\n4 -> Cleaning\n> ").strip()
    Category = toReceiveCategory(Add[0])
    
    # Cria o codigo de 5 digitos
    import random
    code5digts = ''
    for i in range(5):
        code5digts += str(random.randint(0, 5))
        
    # Adiciona as informações ao dicionário
    object_json.update(
        {   
            f"RegistrationCode-{code5digts}":
            {
                'NAME' : NameCompany,
                'CNPJ' : CnpjCompany,
                'CATEGORY': Category
            }
        }
    )

elif adc == '2':
    print("See you later, Thank you")

elif adc == '3':
    # Mostra empresas cadastradas:
    json_index = json.dumps(object_json)
    print(pd.read_json(json_index, orient = 'index'))

else:
    print("Numero invalido\nPrograma encerrado")
    SystemExit()

print(OpenAndCloseen(x="F", y=object_json))

"""TESTA POSSIVEIS ERROS DE USUARIOS - REQUISITOS FUNCIONAIS E NÃO FUNCIONAIS"""
"""Organizar gits por etapas alteradas"""