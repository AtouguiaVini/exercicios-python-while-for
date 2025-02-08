# José está desenvolvendo uma funcionalidade no sistema do Buscante para interromper a busca assim que um livro específico é encontrado. A lista de livros já cadastrados no sistema é a seguinte:

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

# Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrado. Após encontrar o livro, o programa deve parar imediatamente a busca, sem verificar os livros restantes.

for livro in livros:
    if livro == "O Hobbit":
        print(f'--> Livro encontrado! {livro}')
        break # não permite avançar para o prox print

    print(f'- Livro {livro} não é o livro correspondente')