import re
import unicodedata
from bs4 import BeautifulSoup

def slugify(text):
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s_]+', '-', text)
    return text

def main():
    html_path = r"c:\dev\tcc_python\docs\tcc.html"
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    headings = {}
    for tag in soup.find_all(re.compile('^h[1-6]$')):
        if tag.get('id'):
            headings[tag.get_text(strip=True)] = tag['id']

    sumario = soup.find('h1', string=re.compile("sum[aá]rio", re.I))
    if sumario:
        ul = sumario.find_next('ul')
        if ul:
            for a in ul.find_all('a'):
                texto = a.get_text(strip=True)
                id_destino = headings.get(texto)
                if not id_destino:
                    id_destino = slugify(texto)
                a['href'] = f"#{id_destino}"

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Links do sumário corrigidos!")

if __name__ == "__main__":
    main()