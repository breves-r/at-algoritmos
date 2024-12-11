import os

def list_files(location):
    itens = os.listdir(location)
    for item in itens:
        full_location = os.path.join(location, item)

        if os.path.isdir(full_location):
            list_files(full_location)
        elif os.path.isfile(full_location):
            print(f"- {item}")


location = "/Users/rafa/Desktop/Facul/Bloco de Entrada"
list_files(location)
