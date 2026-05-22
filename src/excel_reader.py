import pandas as pd


def ler_planilha(caminho):
    """
    Lê uma planilha Excel e retorna os dados como lista de dicionários.

    Remove espaços extras dos cabeçalhos para garantir correspondência
    correta com os campos do formulário.

    Args:
        caminho (Path | str): Caminho para o arquivo .xlsx.

    Returns:
        list[dict]: Lista de registros, um dicionário por linha.
    """
    df = pd.read_excel(caminho)
    df.columns = df.columns.str.strip()
    return df.to_dict(orient="records")