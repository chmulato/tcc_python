from bs4 import BeautifulSoup

def add_back_to_sumario(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Defina o id do sumário
    sumario_id = "sumario"

    # Texto do botão/link
    btn_html = (
        '<a href="#sumario" class="back-to-sumario" '
        'style="margin-left:1em;font-size:0.8em;text-decoration:none;">'
        '⬅ Voltar ao Sumário</a>'
    )

    # Adiciona o botão a todos os títulos, exceto o próprio sumário
    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        if tag.get("id") and tag["id"] != sumario_id:
            # Evita duplicar o botão se rodar o script mais de uma vez
            if not tag.find("a", class_="back-to-sumario"):
                tag.append(BeautifulSoup(btn_html, "html.parser"))

    # Adiciona um pequeno CSS para o botão (opcional)
    style = soup.new_tag("style")
    style.string = """
    .back-to-sumario:hover {
        text-decoration: underline;
        color: #0056b3;
    }
    """
    # Só adiciona se ainda não existir
    if not soup.find("style", string=lambda s: s and ".back-to-sumario" in s):
        soup.head.append(style)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    add_back_to_sumario(r"c:\dev\tcc_python\docs\tcc.html")
    print("Botões de retorno ao sumário inseridos!")