import requests
import bs4
import lxml

# result = requests.get("http://www.example.com")
# print(type(result))
#
# print(result.text)
#
# soup = bs4.BeautifulSoup(result.text,'lxml')
#
# print(soup.select('title')[0].getText())




# The below script is used to store the text from the class tag in the website html document in the Python
req = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

# print(req.text)
soups = bs4.BeautifulSoup(req.text,'lxml')

store = soups.select('.infobox-data')[0]
print(store.text)

for item in soups.select('.infobox-data'):
    print(item.text)