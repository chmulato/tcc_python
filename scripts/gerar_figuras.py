"""
Geração de figuras (paper-like) para o estudo de caso.

Saída padrão: docs/figuras/

Este script gera:
- Fig 01: esquema/analogia (cópia do img/esquema.png)
- Fig 03: layout base (render do layout ASCII)
- Fig 04: throughput (saídas por minuto + cumulativo)
- Fig 05: ocupação de mesas e filas (séries)
- Fig 06: distribuição do tempo de residência (histograma)
- Fig 07: comparação antes/depois (baseline vs intervenção)
"""

from __future__ import annotations

import os
import shutil
import sys
from typing import Dict, Any

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Garante imports do pacote local (src/*) quando executado via "python scripts/..."
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import yaml

from src.layout_parser import ler_layout_ascii
from src.simulador import rodar_simulacao
from src.visualizador_layout import desenhar_layout, gerar_mapa_mesas


OUT_DIR = os.path.join(ROOT, "docs", "figuras")

def _fig_style(ax) -> None:
    ax.set_facecolor("white")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def _draw_flow(ax, title: str, nodes, arrows, subtitle: str | None = None) -> None:
    """
    Desenha um diagrama simples (paper-like) com caixas e setas.

    nodes: list[dict] com chaves: x,y,w,h,label,sub(optional),color(optional)
    arrows: list[tuple] (x1,y1,x2,y2,label(optional))
    """
    _fig_style(ax)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 40)

    # Fundo leve (grade sutil)
    ax.add_patch(
        patches.Rectangle((0, 0), 100, 40, facecolor="#f6fbf8", edgecolor="#d7e6df", linewidth=1.0)
    )

    # Título
    ax.text(3, 36.5, title, fontsize=12.5, fontweight="bold", color="#0c1b17")
    if subtitle:
        ax.text(3, 34.2, subtitle, fontsize=9.5, color="#3c5a53")

    # Nós
    for n in nodes:
        x, y, w, h = n["x"], n["y"], n["w"], n["h"]
        label = n["label"]
        sub = n.get("sub")
        color = n.get("color", "#ffffff")
        edge = n.get("edge", "#1d3b33")

        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0.35,rounding_size=3.2",
                linewidth=1.2,
                edgecolor=edge,
                facecolor=color,
            )
        )
        ax.text(x + w / 2, y + h / 2 + (2.0 if sub else 0), label, ha="center", va="center",
                fontsize=10.5, fontweight="bold", color="#0c1b17")
        if sub:
            ax.text(x + w / 2, y + h / 2 - 5.2, sub, ha="center", va="center",
                    fontsize=9.0, color="#3c5a53")

    # Setas
    for a in arrows:
        x1, y1, x2, y2 = a[0], a[1], a[2], a[3]
        label = a[4] if len(a) > 4 else None
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(arrowstyle="-|>", lw=1.6, color="#244a42", shrinkA=0, shrinkB=0),
        )
        if label:
            ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 2.0, label, ha="center", va="bottom",
                    fontsize=9.0, color="#3c5a53")


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def _load_yaml(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _save_fig(path: str, title: str | None = None) -> None:
    if title:
        plt.title(title)
    plt.tight_layout()
    plt.savefig(path, dpi=170)
    plt.close()


def _run_case(parametros: Dict[str, Any], layout) -> Dict[str, Any]:
    p = dict(parametros)
    p["coletar_series"] = True

    # Torna chegada coerente com clientes/min, se estiver fora de escala.
    try:
        cpm = float(p.get("clientes_por_minuto", 10))
        dt = float(p.get("tempo_entre_clientes", 0))
        dt_ideal = 1.0 / max(cpm, 0.0001)
        # Se dt for muito grande, ajusta para não "desligar" o feed.
        if dt <= 0 or dt > 5 * dt_ideal:
            p["tempo_entre_clientes"] = dt_ideal
    except Exception:
        pass

    return rodar_simulacao(p, layout, exportar_pdf_automatico=False, usar_des=True)


def main() -> None:
    _ensure_dir(OUT_DIR)

    # Inputs padrão do repositório
    yaml_path = os.path.join(ROOT, "config", "parametros.yaml")
    layout_path = os.path.join(ROOT, "layouts", "layout_padrao.txt")
    esquema_path = os.path.join(ROOT, "img", "esquema.png")

    parametros = _load_yaml(yaml_path)
    layout = ler_layout_ascii(layout_path)

    # Fig 01 — esquema/analogia (imagem fornecida)
    if os.path.exists(esquema_path):
        shutil.copyfile(esquema_path, os.path.join(OUT_DIR, "fig_01_esquema_analogia.png"))

    # Fig 02A/02B — diagramas (PNG) no mesmo estilo das demais
    try:
        # 02A — serviços (restaurante)
        fig, ax = plt.subplots(figsize=(10.2, 3.4))
        nodes = [
            dict(x=5, y=14, w=18, h=12, label="Entrada", sub="Feed (λ)", color="#ffffff", edge="#0f5ea8"),
            dict(x=29, y=14, w=18, h=12, label="Buffer", sub="Filas", color="#ffffff", edge="#0a7a72"),
            dict(x=53, y=14, w=18, h=12, label="Serviço", sub="Buffet/Caixa", color="#ffffff", edge="#0b6b4d"),
            dict(x=77, y=14, w=18, h=12, label="Mesa", sub="Residência (τ)", color="#ffffff", edge="#0b6b4d"),
        ]
        arrows = [
            (23, 20, 29, 20, "transferência"),
            (47, 20, 53, 20, "capacidade μ"),
            (71, 20, 77, 20, "saída"),
        ]
        _draw_flow(
            ax,
            "Figura 2A — Fluxo em sistema de serviços (DES)",
            nodes,
            arrows,
            subtitle="Entrada → buffers (filas) → operações (serviço) → residência → saída",
        )
        _save_fig(os.path.join(OUT_DIR, "fig_02a_fluxo_servico.png"))

        # 02B — processo (operação unitária)
        fig, ax = plt.subplots(figsize=(10.2, 3.4))
        nodes = [
            dict(x=5, y=14, w=20, h=12, label="Reagentes", sub="F, composição", color="#ffffff", edge="#0f5ea8"),
            dict(x=31, y=14, w=20, h=12, label="Reator", sub="τ, cinética", color="#ffffff", edge="#0b6b4d"),
            dict(x=57, y=14, w=20, h=12, label="Separador", sub="α, split", color="#ffffff", edge="#0a7a72"),
            dict(x=83, y=14, w=12, h=12, label="Produto", sub="P", color="#ffffff", edge="#0f5ea8"),
        ]
        arrows = [
            (25, 20, 31, 20, "F"),
            (51, 20, 57, 20, "corrente"),
            (77, 20, 83, 20, "P"),
        ]
        _draw_flow(
            ax,
            "Figura 2B — Fluxo em sistema de processo (engenharia química)",
            nodes,
            arrows,
            subtitle="Entrada → reator → separação → produtos (balanços governam acúmulos)",
        )
        _save_fig(os.path.join(OUT_DIR, "fig_02b_fluxo_processo.png"))
    except Exception:
        # best effort
        pass

    # Fig 03 — layout base (render)
    try:
        mapa = gerar_mapa_mesas(layout)
        # frame 0 sempre gera (INTERVALO_VISUAL=10)
        img_path = desenhar_layout(layout, mesas_ocupadas=[], tempo=0, pasta_saida=OUT_DIR, prefixo="fig_03_", mapa_mesas=mapa)
        if img_path:
            # renomeia para um nome estável
            stable = os.path.join(OUT_DIR, "fig_03_layout_base.png")
            if os.path.exists(img_path) and img_path != stable:
                os.replace(img_path, stable)
    except Exception:
        # layout renderer é "best effort"
        pass

    # Caso baseline
    base = _run_case(parametros, layout)
    series = base.get("series") or {}
    minutos = series.get("minutos") or []
    saidas = series.get("saidas_por_minuto") or []
    mesas = series.get("mesas_ocupadas") or []
    fila_mesa = series.get("fila_mesa") or []
    fila_caixa = series.get("fila_caixa") or []

    # Fig 04 — throughput
    if minutos and saidas:
        cumul = []
        acc = 0
        for v in saidas:
            acc += int(v)
            cumul.append(acc)

        plt.figure(figsize=(8.2, 4.4))
        plt.plot(minutos, cumul, color="#0b6b4d", linewidth=2.2, label="Saída acumulada (throughput)")
        plt.bar(minutos, saidas, color="#0f5ea8", alpha=0.25, label="Saídas por minuto")
        plt.xlabel("Tempo (min)")
        plt.ylabel("Clientes (unid.)")
        plt.grid(True, alpha=0.22)
        plt.legend(frameon=False)
        _save_fig(os.path.join(OUT_DIR, "fig_04_throughput.png"), "Throughput (saída) ao longo do tempo")

    # Fig 05 — ocupação e filas
    if minutos and mesas:
        plt.figure(figsize=(8.2, 4.6))
        plt.plot(minutos, mesas, color="#0b6b4d", linewidth=2.2, label="Mesas ocupadas (holdup)")
        if fila_mesa:
            plt.plot(minutos, fila_mesa, color="#0f5ea8", linewidth=2.0, label="Fila para mesa (buffer)")
        if fila_caixa:
            plt.plot(minutos, fila_caixa, color="#0a7a72", linewidth=2.0, label="Fila no caixa (buffer)")
        plt.xlabel("Tempo (min)")
        plt.ylabel("Quantidade (unid.)")
        plt.grid(True, alpha=0.22)
        plt.legend(frameon=False)
        _save_fig(os.path.join(OUT_DIR, "fig_05_ocupacao_e_filas.png"), "Holdup e buffers (filas) por minuto")

    # Fig 06 — distribuição do tempo de residência
    residence = base.get("residence_times") or []
    if residence:
        plt.figure(figsize=(8.2, 4.4))
        plt.hist(residence, bins=30, color="#0f5ea8", alpha=0.85, edgecolor="white")
        plt.xlabel("Tempo de residência (min)")
        plt.ylabel("Frequência")
        plt.grid(True, axis="y", alpha=0.22)
        _save_fig(os.path.join(OUT_DIR, "fig_06_distribuicao_residencia.png"), "Distribuição do tempo de residência")

    # Fig 07 — antes vs depois (intervenção de capacidade)
    otim = dict(parametros)
    # Intervenção simples e interpretável: aumenta mesas (capacidade de holdup) e reduz espera.
    try:
        otim["numero_de_mesas"] = int(otim.get("numero_de_mesas", 25)) + 5
    except Exception:
        otim["numero_de_mesas"] = 30

    after = _run_case(otim, layout)

    # Comparação em métricas
    labels = ["Tempo médio de espera (mesa)", "Uso médio de mesas (%)", "Clientes processados"]
    before_vals = [
        float(base.get("tempo_medio_espera_fila_mesa", 0) or 0),
        float(base.get("uso_medio_mesas", 0) or 0),
        float(base.get("clientes_processados", 0) or 0),
    ]
    after_vals = [
        float(after.get("tempo_medio_espera_fila_mesa", 0) or 0),
        float(after.get("uso_medio_mesas", 0) or 0),
        float(after.get("clientes_processados", 0) or 0),
    ]

    x = range(len(labels))
    plt.figure(figsize=(9.0, 4.5))
    plt.bar([i - 0.18 for i in x], before_vals, width=0.36, color="#0f5ea8", alpha=0.80, label="Antes (baseline)")
    plt.bar([i + 0.18 for i in x], after_vals, width=0.36, color="#0b6b4d", alpha=0.80, label="Depois (intervenção)")
    plt.xticks(list(x), labels, rotation=0)
    plt.grid(True, axis="y", alpha=0.22)
    plt.legend(frameon=False)
    _save_fig(os.path.join(OUT_DIR, "fig_07_antes_depois.png"), "Antes vs Depois (intervenção de capacidade)")

    print(f"Figuras geradas em: {OUT_DIR}")


if __name__ == "__main__":
    main()

