from my_parser import parse
from graph import graph_info

url = input('Введите адрес страницы:')
text = parse(url)
print(graph_info(text))
