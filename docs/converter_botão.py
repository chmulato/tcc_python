from bs4 import BeautifulSoup

def replace_sumario_button_text(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    for a in soup.find_all("a", class_="back-to-sumario"):
        a.string = "AO SUMÁRIO"

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    replace_sumario_button_text(r"c:\dev\tcc_python\docs\tcc.html")
    print('Texto dos botões alterado para "AO SUMÁRIO"!')