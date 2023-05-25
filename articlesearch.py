import pandas as pd
import requests
from bs4 import BeautifulSoup

excelfile = pd.read_excel("articlestest.xlsx")
excelfile.to_csv("articlestest.csv", index=None,header=True)
df = pd.DataFrame(pd.read_csv("articlestest.csv"))

url = "https://scholar.google.com/scholar?q="
def scholarsearch():
    article=df.Name[0].replace(" ", "-")
    req = requests.get(url+ "/scholar?q=" + article)
    soup = BeautifulSoup(req.text, 'html.parser')
    headerres = soup.find('h3', {'class': 'gs_rt'})

    if headerres:
        linkres = headerres.find('a')['href']
        return linkres
    
    return None

scholarsearch()
