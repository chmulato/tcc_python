import markdown
from pathlib import Path

# Caminhos dos arquivos
md_path = Path(r"c:\dev\tcc_python\docs\tcc.md")
html_path = Path(r"c:\dev\tcc_python\docs\tcc.html")

# CSS responsivo para tablets
CSS = """
<style>
body {
    font-family: 'Segoe UI', Arial, sans-serif;
    margin: 0;
    padding: 0 1em;
    background: #fafbfc;
    color: #222;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}
h1, h2, h3, h4 {
    color: #2d3a4a;
}
pre, code {
    background: #f4f4f4;
    border-radius: 4px;
    font-size: 0.95em;
    overflow-x: auto;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 1em;
}
th, td {
    border: 1px solid #bbb;
    padding: 0.5em;
    text-align: left;
}
@media (max-width: 900px) {
    body { max-width: 100vw; }
    table, thead, tbody, th, td, tr {
        display: block;
    }
    th, td {
        box-sizing: border-box;
        width: 100%;
        border: none;
        border-bottom: 1px solid #eee;
    }
    tr { margin-bottom: 1em; }
}
img, svg {
    max-width: 100%;
    height: auto;
}
</style>
"""

def main():
    # Lê o markdown
    md_text = md_path.read_text(encoding="utf-8")
    # Converte para HTML
    html_body = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'toc'])
    # Monta o HTML final
    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Simulador de Tempo de Permanência em Restaurantes por Quilo</title>
{CSS}
</head>
<body>
{html_body}
</body>
</html>
"""
    # Salva o HTML
    html_path.write_text(html, encoding="utf-8")
    print(f"Arquivo HTML gerado em: {html_path.resolve()}")

if __name__ == "__main__":
    main()