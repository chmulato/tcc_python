from bs4 import BeautifulSoup
import re

def slugify(text):
    # Gera um slug semelhante ao id dos títulos
    text = text.lower()
    text = re.sub(r'[áàãâä]', 'a', text)
    text = re.sub(r'[éèêë]', 'e', text)
    text = re.sub(r'[íìîï]', 'i', text)
    text = re.sub(r'[óòõôö]', 'o', text)
    text = re.sub(r'[úùûü]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

def link_list_items(soup, section_id, heading_tags):
    # Encontra a seção pelo id
    section = soup.find(id=section_id)
    if not section:
        return
    # Procura a lista (ol ou ul) logo após o título
    lista = section.find_next(['ol', 'ul'])
    if not lista:
        return

    # Mapeia todos os títulos de figuras/tabelas e seus ids
    headings = {}
    for tag in soup.find_all(heading_tags):
        if tag.get('id'):
            headings[tag.get_text(strip=True)] = tag['id']

    # Para cada item da lista, tenta criar o link
    for li in lista.find_all('li'):
        texto = li.get_text(strip=True)
        # Procura id exato, senão tenta slugify
        id_destino = None
        for titulo, id_ in headings.items():
            if texto in titulo or titulo in texto:
                id_destino = id_
                break
        if not id_destino:
            id_destino = slugify(texto)
            # Confirma se existe esse id
            if not soup.find(id=id_destino):
                id_destino = None
        if id_destino:
            # Substitui o conteúdo do <li> por um link
            li.clear()
            a = soup.new_tag('a', href=f'#{id_destino}')
            a.string = texto
            li.append(a)

def main():
    html_path = r"c:\dev\tcc_python\docs\tcc.html"
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Lista de Figuras
    link_list_items(soup, "lista-de-figuras", ["h3", "h4", "h5"])
    # Lista de Tabelas
    link_list_items(soup, "lista-de-tabelas", ["h4", "h5"])

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Listas de figuras e tabelas transformadas em links!")

if __name__ == "__main__":
    main()