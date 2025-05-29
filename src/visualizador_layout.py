# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Módulo: visualizador_layout.py
# Descrição:
#   Este módulo é responsável por gerar visualizações gráficas
#   (em formato de imagem PNG) da ocupação do layout do restaurante
#   durante a simulação de eventos discretos (DES).
#
#   Ele transforma o layout ASCII do restaurante em um grid visual
#   usando cores para representar:
#     - Mesas livres
#     - Mesas ocupadas
#     - Buffet
#     - Caixas
#     - Paredes e áreas de circulação
#
#   A função principal desenhar_layout() recebe:
#     - uma matriz do layout base (caracteres ASCII),
#     - uma lista de coordenadas ou índices de mesas ocupadas,
#     - o tempo (minuto) da simulação.
#
#   O resultado é salvo como imagem PNG, com legenda, para uso
#   em relatórios ou geração de GIFs que animam a simulação.
#
# Autor: Christian Mulato
# Data: 28/05/2025
# ===============================================

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import glob
import os
import datetime
import imageio
import tempfile
from src.logger_config import get_logger

logger = get_logger()

INTERVALO_VISUAL = 10  # Gera um frame a cada 10 minutos

def gerar_mapa_mesas(layout_base):
    """
    Gera uma lista de coordenadas (i, j) das mesas no layout, na ordem dos índices.
    """
    mapa = []
    for i, linha in enumerate(layout_base):
        for j, cel in enumerate(linha):
            if cel == 'M':
                mapa.append((i, j))
    return mapa

def desenhar_layout(layout_base, mesas_ocupadas=None, tempo=0, pasta_saida="monitoramento", prefixo="", mapa_mesas=None):
    """
    Gera uma imagem PNG do layout ASCII do restaurante, destacando mesas ocupadas.
    Só gera o frame se o tempo for múltiplo de INTERVALO_VISUAL.
    Aceita mesas_ocupadas como lista de coordenadas (i, j) ou índices (int) se mapa_mesas for fornecido.
    """
    if tempo % INTERVALO_VISUAL != 0:
        return  # Não gera frame neste minuto

    if mesas_ocupadas is None:
        mesas_ocupadas = []

    # Se mesas_ocupadas for lista de índices, converte para coordenadas usando mapa_mesas
    if mapa_mesas and mesas_ocupadas and isinstance(mesas_ocupadas[0], int):
        mesas_ocupadas = [mapa_mesas[idx] for idx in mesas_ocupadas if idx < len(mapa_mesas)]

    logger.info(f"[Frame {tempo}] Mesas ocupadas: {len(mesas_ocupadas)} - {mesas_ocupadas[:10]}{' ...' if len(mesas_ocupadas) > 10 else ''}")

    # Mapeamento de caracteres para cores
    cor_mapa = {
        'M': '#cccccc',   # Mesa livre - cinza claro
        'O': '#4caf50',   # Mesa ocupada - verde
        'B': '#ffe066',   # Buffet - amarelo
        'C': '#2196f3',   # Caixa - azul
        '#': '#222222',   # Parede - preto
        ' ': '#ffffff',   # Espaço - branco
    }

    n_linhas = len(layout_base)
    n_colunas = max(len(linha) for linha in layout_base)
    matriz_cores = []

    for i, linha in enumerate(layout_base):
        linha_cores = []
        for j, cel in enumerate(linha):
            if cel == 'M' and (i, j) in mesas_ocupadas:
                linha_cores.append(cor_mapa['O'])  # Mesa ocupada
            else:
                cor = cor_mapa.get(cel)
                if cor is None:
                    logger.warning(f"Caractere desconhecido no layout: '{cel}' em ({i},{j})")
                    cor = '#ffffff'
                linha_cores.append(cor)
        while len(linha_cores) < n_colunas:
            linha_cores.append('#ffffff')
        matriz_cores.append(linha_cores)

    # CORREÇÃO: converte hex para RGB float
    rgb_matriz = np.array([
        [mcolors.to_rgb(cor) for cor in linha]
        for linha in matriz_cores
    ], dtype=np.float32)

    # Loga um resumo das cores do frame (quantas mesas livres/ocupadas)
    total_livres = sum(
        1 for i, linha in enumerate(layout_base)
        for j, cel in enumerate(linha)
        if cel == 'M' and (i, j) not in mesas_ocupadas
    )
    total_ocupadas = len(mesas_ocupadas)
    logger.info(f"[Frame {tempo}] Mesas livres: {total_livres} | Mesas ocupadas: {total_ocupadas}")

    fig, ax = plt.subplots(figsize=(n_colunas * 0.5, n_linhas * 0.5))
    ax.imshow(rgb_matriz, aspect='equal')

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    legendas = [
        mpatches.Patch(color=cor_mapa['M'], label='Mesa livre'),
        mpatches.Patch(color=cor_mapa['O'], label='Mesa ocupada'),
        mpatches.Patch(color=cor_mapa['B'], label='Buffet'),
        mpatches.Patch(color=cor_mapa['C'], label='Caixa'),
        mpatches.Patch(color=cor_mapa['#'], label='Parede'),
        mpatches.Patch(color=cor_mapa[' '], label='Espaço'),
    ]
    ax.legend(handles=legendas, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    ax.set_title(f"Layout do Restaurante - Minuto {tempo}")

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
        logger.info(f"Pasta de saída criada: {pasta_saida}")

    nome_arquivo = os.path.join(pasta_saida, f"{prefixo}frame_{tempo:05d}.png")
    plt.tight_layout()
    plt.savefig(nome_arquivo, dpi=120)
    plt.close(fig)
    logger.info(f"Imagem do layout salva: {nome_arquivo}")
    return nome_arquivo

def gerar_animacao(layout_base, lista_mesas_ocupadas_por_tempo, pasta_saida="monitoramento", nome_gif="layout_animacao.gif"):
    logger.info(f"Iniciando geração dos frames PNG com {len(lista_mesas_ocupadas_por_tempo)} quadros.")
    logger.info(f"Simulação cobre {len(lista_mesas_ocupadas_por_tempo)} minutos.")

    # Gera o mapa de mesas para converter índices em coordenadas
    mapa_mesas = gerar_mapa_mesas(layout_base)

    # Cria pasta temporária para os frames
    datahora_str = datetime.datetime.now().strftime("%Y_%d_%m_%H_%M_%S")
    temp_dir = os.path.join(pasta_saida, "temp_frames")
    try:
        os.makedirs(temp_dir, exist_ok=True)
        # Remove todos os frames antigos antes de gerar novos
        for f in glob.glob(os.path.join(temp_dir, "*.png")):
            try:
                os.remove(f)
            except Exception as e:
                logger.warning(f"Não foi possível remover o frame antigo: {f} ({e})")
        # Testa permissão de escrita criando um arquivo temporário
        with tempfile.TemporaryFile(dir=temp_dir):
            pass
        logger.debug(f"Pasta temporária '{temp_dir}' criada e limpa, com permissão de escrita.")
    except Exception as e:
        logger.error(f"Não foi possível criar ou escrever na pasta temporária '{temp_dir}': {e}")
        return None

    prefixo = f"{datahora_str}_"
    caminhos_imagens = []
    erro_similar = "Image data of dtype <U7 cannot be converted to float"
    contador_erros = 0
    limite_erros = 10

    for tempo, mesas_ocupadas in enumerate(lista_mesas_ocupadas_por_tempo):
        logger.debug(f"Gerando frame {tempo} para mesas ocupadas: {mesas_ocupadas}")
        try:
            nome_frame = desenhar_layout(layout_base, mesas_ocupadas, tempo, pasta_saida=temp_dir, prefixo=prefixo, mapa_mesas=mapa_mesas)
            if nome_frame and os.path.exists(nome_frame):
                caminhos_imagens.append(nome_frame)
            elif nome_frame is not None:
                logger.error(f"Quadro não gerado corretamente: {nome_frame}")
        except Exception as e:
            logger.error(f"Erro ao gerar frame {tempo}: {e}")
            if erro_similar in str(e):
                contador_erros += 1
                if contador_erros >= limite_erros:
                    logger.error(f"Limite de {limite_erros} erros '{erro_similar}' atingido. Interrompendo geração dos frames.")
                    break

    logger.info(f"Total de frames salvos em {temp_dir}: {len(caminhos_imagens)}")
    logger.info("Os frames PNG estão prontos para montagem do GIF em etapa separada.")

    # Chama automaticamente a montagem do GIF ao final
    if caminhos_imagens:
        caminho_gif = montar_gif_a_partir_de_frames(
            temp_dir=temp_dir,
            nome_gif=nome_gif,
            pasta_saida="resultados/relatorios"
        )
        if caminho_gif:
            logger.info(f"GIF animado salvo com sucesso em: {caminho_gif}")
        else:
            logger.error("Falha ao criar o GIF animado após geração dos frames.")
        return caminho_gif
    else:
        logger.warning("Nenhum frame foi gerado, GIF não será criado.")
        return None

def montar_gif_a_partir_de_frames(temp_dir="monitoramento/temp_frames", nome_gif="layout_animacao.gif", pasta_saida="resultados/relatorios"):
    """
    Lê todos os PNGs da pasta temp_dir em ordem e gera um GIF animado.
    """
    import glob
    arquivos = sorted(glob.glob(os.path.join(temp_dir, "*.png")))
    logger.info(f"Ordem dos frames para o GIF: {arquivos[:10]}{' ...' if len(arquivos) > 10 else ''}")
    if not arquivos:
        logger.warning(f"Nenhum frame PNG encontrado em {temp_dir}. GIF não será gerado.")
        return None

    imagens = []
    for img in arquivos:
        try:
            imagens.append(imageio.v2.imread(img))
        except Exception as e:
            logger.error(f"Erro ao ler imagem {img}: {e}")

    if not imagens:
        logger.error("Nenhuma imagem válida encontrada para gerar o GIF.")
        return None

    # Ajuste: inclui data e hora completa no nome do arquivo
    datahora_str = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    nome_gif_data = f"{datahora_str}_{nome_gif}"
    caminho_gif = os.path.join(pasta_saida, nome_gif_data)

    # Garante que a pasta de destino existe
    os.makedirs(pasta_saida, exist_ok=True)

    try:
        logger.info(f"Tentando salvar GIF animado em: {caminho_gif}")
        imageio.mimsave(caminho_gif, imagens, duration=0.25)
        if os.path.exists(caminho_gif):
            logger.info(f"GIF animado salvo com sucesso em: {caminho_gif}")
        else:
            logger.error(f"Falha ao salvar o GIF animado em: {caminho_gif}")
            return None
    except Exception as e:
        logger.error(f"Erro ao salvar GIF animado: {e}")
        return None
    return caminho_gif