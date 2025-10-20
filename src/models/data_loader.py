import pandas as pd

def ler_dados_pnad(caminho_dados):
    """
    Lê o arquivo de dados da PNAD de largura fixa, extraindo as variáveis de interesse.
    
    Args:
        caminho_dados (str): O caminho para o arquivo de dados da PNAD.

    Returns:
        pandas.DataFrame: Um DataFrame contendo os dados das variáveis selecionadas.
    """
    # As posições são baseadas no dicionário (iniciando em 1). 
    # O pandas usa 0-based, então subtraímos 1 do início.
    # A especificação é (início, fim) da coluna.
    col_specs = [
        (5, 7),      # UF
        (49, 64),    # V1028: Peso com calibração
        (681, 682),  # S140091: App de táxi
        (682, 683),  # S140092: App de transporte de passageiros
        (683, 684),  # S140093: App de entrega de produtos
        (684, 685),  # S140094: App de serviços gerais
    ]
    
    # Nomes correspondentes para as colunas
    col_names = [
        "UF",
        "peso",
        "app_taxi",
        "app_transporte_passageiros",
        "app_entrega_produtos",
        "app_servicos_gerais",
    ]

    # Lê o arquivo de largura fixa
    df = pd.read_fwf(caminho_dados, colspecs=col_specs, names=col_names, encoding='utf-8')
    
    return df
