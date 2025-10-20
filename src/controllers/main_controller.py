import pandas as pd
import os
from src.models.data_loader import ler_dados_pnad
from src.views.plot_generator import gerar_grafico_exemplo

def run_analysis_and_plot():
    """
    Orchestrates the data loading, processing, analysis, and plotting.
    """
    # --- Configuração e Mapeamento ---
    caminho_base = r"c:\Users\john-\OneDrive - Universidade Federal da Paraíba\Área de Trabalho\pnad_continua_analise"
    caminho_dados = os.path.join(caminho_base, "dados", "brutos", "PNADC_032024.txt")
    caminho_saida = os.path.join(caminho_base, "relatorios", "grafico_exemplo_replicado.png")

    mapa_regioes = {
        '11': 'Norte', '12': 'Norte', '13': 'Norte', '14': 'Norte', '15': 'Norte', '16': 'Norte', '17': 'Norte',
        '21': 'Nordeste', '22': 'Nordeste', '23': 'Nordeste', '24': 'Nordeste', '25': 'Nordeste', '26': 'Nordeste', '27': 'Nordeste', '28': 'Nordeste', '29': 'Nordeste',
        '31': 'Sudeste', '32': 'Sudeste', '33': 'Sudeste', '35': 'Sudeste',
        '41': 'Sul', '42': 'Sul', '43': 'Sul',
        '50': 'Centro-Oeste', '51': 'Centro-Oeste', '52': 'Centro-Oeste', '53': 'Centro-Oeste'
    }

    # --- Leitura e Preparação dos Dados ---
    print("Lendo e preparando os dados para análise regional...")
    df = ler_dados_pnad(caminho_dados)
    df['Regiao'] = df['UF'].astype(str).map(mapa_regioes)

    colunas_apps = [col for col in df.columns if col.startswith('app_')]
    for col in colunas_apps:
        df[col] = df[col].map({1.0: 'Sim', 2.0: 'Não'}).fillna("Não aplicável")

    # --- Cálculo dos Percentuais por Região (percentual de cada app dentro da região, em relação ao total de 'Sim' na região) ---
    print("Calculando percentuais ponderados por região (percentual de cada app dentro da região, em relação ao total de 'Sim' na região)...")
    
    resultados = []
    
    # Primeiro, vamos criar um DataFrame longo com todas as respostas 'Sim' e seus pesos
    df_long_sim = pd.DataFrame()
    for app_col in colunas_apps:
        temp_df = df[df[app_col] == 'Sim'][['Regiao', 'peso']].copy()
        temp_df['Aplicativo'] = app_col
        df_long_sim = pd.concat([df_long_sim, temp_df])

    # Calcular o total de peso de 'Sim' para todos os aplicativos por região
    # Isso representa a soma dos pesos de todas as ocorrências de 'Sim' em cada região
    total_sim_por_regiao = df_long_sim.groupby('Regiao')['peso'].sum()

    for app in colunas_apps:
        # População que disse 'Sim' para este app, por região
        pop_sim_regiao = df[df[app] == 'Sim'].groupby('Regiao')['peso'].sum()
        
        # Calcula o percentual de cada app em relação ao total de 'Sim' de TODOS os apps naquela região
        # Usamos .reindex para garantir que todas as regiões sejam consideradas e para evitar erros de divisão por zero
        percentual_regiao = (pop_sim_regiao / total_sim_por_regiao.reindex(pop_sim_regiao.index, fill_value=0) * 100).reset_index(name='Percentual')
        percentual_regiao['Aplicativo'] = app
        resultados.append(percentual_regiao)

    df_plot = pd.concat(resultados)
    df_plot['Aplicativo'] = df_plot['Aplicativo'].replace({
        'app_taxi': 'Aplicativo de táxi',
        'app_transporte_passageiros': 'Aplicativo de transporte particular de passageiros (exclusive táxi)',
        'app_entrega_produtos': 'Aplicativo de entrega de comida, produtos, etc.',
        'app_servicos_gerais': 'Aplicativo de prestação de serviços gerais ou profissionais'
    })

    # --- Ordenar Regiões e Aplicativos ---
    # Ordenar regiões pelo percentual total (soma de todos os aplicativos na região)
    ordem_regioes = df_plot.groupby('Regiao')['Percentual'].sum().sort_values(ascending=True).index.tolist()

    # Ordenar aplicativos pelo percentual médio geral (do maior para o menor)
    ordem_aplicativos = df_plot.groupby('Aplicativo')['Percentual'].mean().sort_values(ascending=False).index.tolist()

    # Mapeamento de cores
    cores_plataformas = {
        'Aplicativo de transporte particular de passageiros (exclusive táxi)': '#4b2c80',
        'Aplicativo de táxi': '#6f8cc2',
        'Aplicativo de entrega de comida, produtos, etc.': '#9fb9e0',
        'Aplicativo de prestação de serviços gerais ou profissionais': '#d0ccd0'
    }

    # Calcular a média geral de cada aplicativo para as linhas de referência
    medias_por_aplicativo = df_plot.groupby('Aplicativo')['Percentual'].mean().to_dict()

    # --- Chamar a função de plotagem ---
    gerar_grafico_exemplo(df_plot, ordem_regioes, ordem_aplicativos, cores_plataformas, medias_por_aplicativo, caminho_saida)