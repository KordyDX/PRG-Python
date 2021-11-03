from bs4 import BeautifulSoup
import requests as rq

url = "https://www.alza.cz"
page = rq.get(url)

soup = BeautifulSoup(page.content, "html.parser")
lists = soup.find("div", class_ = "item1")


title = lists.find("a", class_ = "title").text
description = lists.find("a", class_ = "anot").text
description = lists.find("p", class_=False, id=False).text
all = title + "\n\n" + description

with open("Alza_Novinka.txt", "w", encoding = "utf-8") as f_output:
    f_output.write(all)
