import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

def gerar_grafico_exemplo(df_plot, ordem_regioes, ordem_aplicativos, cores_plataformas, medias_por_aplicativo, caminho_saida):
    """
    Gera um gráfico de barras agrupadas comparando o uso de aplicativos por região,
    replicando um estilo comum de visualização.
    
    Args:
        df_plot (pd.DataFrame): DataFrame com os dados a serem plotados.
        ordem_regioes (list): Lista com a ordem das regiões para o gráfico.
        ordem_aplicativos (list): Lista com a ordem dos aplicativos para o gráfico.
        cores_plataformas (dict): Dicionário de mapeamento de cores para as plataformas.
        medias_por_aplicativo (dict): Dicionário com as médias por aplicativo.
        caminho_saida (str): Caminho para salvar o gráfico.
    """
    # --- Geração do Gráfico (Estilo Solicitado) ---
    print(f"Gerando gráfico e salvando em {caminho_saida}...")

    # Configurações de estilo
    plt.style.use('seaborn-v0_8-whitegrid') # Fundo branco e grade
    plt.rcParams['font.family'] = 'sans-serif' # Fonte sem serifa

    fig, ax = plt.subplots(figsize=(7.23, 6.57))

    # Gráfico de barras
    sns.barplot(data=df_plot, x='Regiao', y='Percentual', hue='Aplicativo',
                palette=cores_plataformas, ax=ax,
                order=ordem_regioes, hue_order=ordem_aplicativos,
                edgecolor='none') # Remove borda das barras para melhor visual

    # Título e Subtítulo
    ax.set_title("Trabalhadores plataformizados, segundo tipo de plataformas de serviços (%)\nPor grandes regiões",
                 fontsize=14, fontweight='bold', pad=20)

    # Rótulos dos eixos
    ax.set_xlabel("Região", fontsize=12, fontweight='bold')
    ax.set_ylabel("Percentual", fontsize=12, fontweight='bold')

    # Linhas finas e discretas nos eixos
    for spine in ax.spines.values():
        spine.set_edgecolor('#cccccc') # Cor cinza claro
        spine.set_linewidth(0.5)

    # Grade horizontal pontilhada em cinza claro
    ax.grid(axis='y', linestyle=':', color='#cccccc', linewidth=0.7)
    # Remove grade vertical (o estilo padrão já pode fazer isso ou não é necessário)

    # Rótulos percentuais acima das barras
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%', label_type='edge', padding=3, fontsize=8)

    # Re-obter os limites do eixo y e x para posicionamento preciso
    y_min, y_max = ax.get_ylim()
    x_min, x_max = ax.get_xlim()

    # Posição para os retângulos (ajustar conforme necessário)
    rect_width = (x_max - x_min) * 0.03 # Largura do retângulo (3% da largura do gráfico)
    rect_height = (y_max - y_min) * 0.02 # Altura do retângulo (2% da altura do gráfico)
    x_pos_rect = x_max + (x_max - x_min) * 0.02 # Posição à direita do gráfico

    for i, (app_name, media_val) in enumerate(medias_por_aplicativo.items()):
        color = cores_plataformas.get(app_name, 'black')
        
        # Desenha a linha média
        ax.axhline(y=media_val, color=color, linestyle='--', linewidth=1, alpha=0.7)
        
        # Adiciona o retângulo de destaque
        # Ajusta a posição vertical para evitar sobreposição
        # Usar um offset baseado na altura total do gráfico para espaçamento
        vertical_offset = (y_max - y_min) * 0.03 * i # Ajuste o 0.03 conforme necessário para espaçamento
        rect_y_pos = media_val + vertical_offset - (rect_height / 2) # Centraliza o retângulo na linha
        
        rect = Rectangle((x_pos_rect, rect_y_pos), rect_width, rect_height,
                         facecolor=color, edgecolor='none', alpha=0.7)
        ax.add_patch(rect)

        # Adiciona o texto da média (apenas o valor percentual) ao lado do retângulo
        ax.text(x_pos_rect + rect_width + (x_max - x_min) * 0.005, media_val + vertical_offset,
                f'{media_val:.1f}%',
                color='black', fontsize=8, ha='left', va='center')

    # Legenda principal do gráfico de barras
    handles, labels = ax.get_legend_handles_labels()
    # Criar handles com as cores corretas para a legenda
    colored_labels = []
    for label in labels:
        color = cores_plataformas.get(label, 'black') # Pega a cor do dicionário, ou preto se não encontrar
        colored_labels.append(plt.Text(0, 0, label, color=color, fontsize=8))

    legend = ax.legend(handles=handles, labels=[l.get_text() for l in colored_labels],
              loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=2,
              title_fontsize='10', fontsize='8', frameon=False)
    
    # Ajusta o layout para dar espaço à legenda
    fig.tight_layout()
    fig.subplots_adjust(bottom=legend.get_window_extent().height / fig.dpi / fig.get_size_inches()[1] + 0.05) # Ajusta o bottom para a altura da legenda + um pouco de margem

    plt.savefig(caminho_saida, bbox_inches='tight')
    plt.close()
    print("Gráfico gerado com sucesso!")