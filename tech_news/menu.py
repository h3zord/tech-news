import sys


# Requisitos 11 e 12
def seed_database():
    option = input("Digite quantas notícias serão buscadas: ")


def get_title_news():
    option = input("Digite o título: ")


def get_date_news():
    option = input("Digite a data no formato aaaa-mm-dd: ")


def get_category_news():
    option = input("Digite a categoria: ")


def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.\n"
    )

    msg_options = {
        "0": seed_database,
        "1": get_title_news,
        "2": get_date_news,
        "3": get_category_news,
    }

    if option in msg_options:
        return msg_options[option]()
    else:
        sys.stderr.write("Opção inválida")


analyzer_menu()
