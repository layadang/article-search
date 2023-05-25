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

for i in range( len(df.index) ):
        if pd.isna(df.Link[i]):
            new_link = scholarsearch(i)
            df.at[i, 'Link'] = new_link if new_link else ''

df.to_csv("articlestest_updated.csv", index=None, header=True)
