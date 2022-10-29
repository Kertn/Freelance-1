import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

fn = "Data.xlsx"
wb = load_workbook(fn)
ws = wb["Sheet"]

for i in range(673):
    urls = []
    req = requests.get(f"https://www.inmyroom.ru/profi/professionals/dizayner-interiera/page/{i+1}")

    soup = BeautifulSoup(req.text, "lxml")

    n_urls = soup.find_all("a", class_="user-preview_name")
    for i in range(20):
        urls.append(n_urls[i].get("href"))


    for i in range(20):
        r = requests.get(urls[i])
        soup_page = BeautifulSoup(r.text, "lxml")

        name = soup_page.find("h1", class_="s-UserProfile_b-Header_title").text
        city = soup_page.find("p", class_="s-UserProfile_b-Header_subtitle").text
        try:
            number = soup_page.find("a", class_="__withIcon __phone").get("data-active-text")
        except:
            continue

        ws.append([name, city, number])
        wb.save(fn)
        wb.close()



