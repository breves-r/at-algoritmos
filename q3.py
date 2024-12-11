def get_contato(nome, array):
    for contato in array:
        if contato['nome'] == nome:
            return contato['telefone']
    return None

contatos = [
    {'nome': 'Mariana', 'telefone': '11999999999'},
    {'nome': 'Bruno', 'telefone': '11999999990'},
    {'nome': 'Rafaela', 'telefone': '21988888800'}
]

print(get_contato("Rafaela", contatos))
