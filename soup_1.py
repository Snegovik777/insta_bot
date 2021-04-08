from urllib.request import urlopen
import bs4


config_data = dict()
html = urlopen('https://promo22.site/data.txt')
code = list(str(bs4.BeautifulSoup(html.read(), 'html.parser')).split('\n'))
for f in code:
    (key, val) = f.strip().split(' = ')
    val = val.strip('\'')
    config_data[key] = val
print(config_data)

#  exec(code)