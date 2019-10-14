import requests
from bs4 import BeautifulSoup

URL =  "https://www.facebook.com/profile.php?id=100012534850545"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content,'html.parser')

# tags = soup.findAll(attrs={"class":"_50f3"})
tag = soup.find(id="u_0_x").get_text()
# price = soup.find(id='prcIsum').get_text();
# title =soup.find(id="itemTitle").get_text();

# print(title)
# print(price)

print(tag)
