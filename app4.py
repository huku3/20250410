import requests
from io import BytesIO
from PIL import Image

url = "https://api.thecatapi.com/v1/images/search"

response = requests.get(url)

dic = response.json()

print(dic)

cat_url = dic[0]['url']

# print(cat_url)

cat_response = requests.get(cat_url)
# print(cat_response)

cat_data = BytesIO(cat_response.content)


cat_image = Image.open(cat_data)

cat_image.show()
