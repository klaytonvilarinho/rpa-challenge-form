from pathlib import Path

from src.browser import iniciar_navegador
from src.excel_reader import ler_planilha
from src.form_filler import clicar_iniciar, preencher_formulario, submeter_formulario

URL      = "https://www.rpachallenge.com/"
PLANILHA = Path("challenge.xlsx")


def main():
    """
    Ponto de entrada da automação RPA Challenge.

    Carrega os dados da planilha, abre o navegador, inicia o cronômetro
    e preenche o formulário para cada registro encontrado.
    """
    # Carrega os dados da planilha antes de abrir o navegador
    dados = ler_planilha(PLANILHA)
    print(f"{len(dados)} registros carregados da planilha.")

    driver = iniciar_navegador()
    driver.get(URL)

    # Inicia o desafio — a partir daqui o cronômetro começa
    clicar_iniciar(driver)

    for i, linha in enumerate(dados, start=1):
        print(f"Rodada {i}/{len(dados)}: {linha}")
        preencher_formulario(driver, linha)
        submeter_formulario(driver)

    print("Desafio concluído!")


if __name__ == "__main__":
    main()