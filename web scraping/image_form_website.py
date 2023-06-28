import requests
import bs4
import lxml

request = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

scope = bs4.BeautifulSoup(request.text,'lxml')

comp = scope.select('img')[3]
print(comp['src'])

image_link = requests.get('https://upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png')

print(image_link.content) # print the content of the image in the terminal

# downlaoded image in the computer using the web scrapping
f = open('my_computer_image.jpg','wb')
f.write(image_link.content)

f.close()



img = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

file = open('computer_chess.jpg','wb')
file.write(img.content)

f.close()