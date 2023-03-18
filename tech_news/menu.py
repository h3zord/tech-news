import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category
)


# Requisitos 11 e 12
def seed_database():
    option = int(input("Digite quantas notícias serão buscadas: "))
    return get_tech_news(option)


def get_title_news():
    option = (input("Digite o título: "))
    return print(search_by_title(option))


def get_date_news():
    option = input("Digite a data no formato aaaa-mm-dd: ")
    return print(search_by_date(option))


def get_category_news():
    option = input("Digite a categoria: ")
    return print(search_by_category(option))


def list_top_categories():
    return print(top_5_categories())


def finish():
    return print("Encerrando script")


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
        "4": list_top_categories,
        "5": finish
    }

    if option in msg_options:
        try:
            return msg_options[option]()
        except Exception as msgError:
            sys.stderr.write(msgError)
    else:
        sys.stderr.write("Opção inválida\n")
