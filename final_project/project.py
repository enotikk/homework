#скачать страницу
#превратить в список слов кириллицой в нач. форме (mystem)
#для кажд. слова в окне 3: добавляем вершины, если их еще нет; добавляем ребро, если нет, иначе увелич. вес ребра
#строим граф
#оформить flask
import urllib.request
from urllib.parse import quote

url = 'https://ru.wikipedia.org/wiki/'+quote('Русский_мат')
print(url)
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')
print(html)
