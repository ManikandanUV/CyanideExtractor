from bs4 import BeautifulSoup
import requests

url = "http://explosm.net/comics/random"
save_path = '/home/blacky/comics/cyanide/random.png'

r = requests.get(url)
# print(r.status_code)


data = r.text
comic_page = BeautifulSoup(data, "html.parser")

image_url = comic_page.find(property="og:image")['content']
# print(image_url)

image = requests.get(image_url)
open(save_path, 'wb').write(image.content)
