from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def iniciar_navegador():
    """
    Inicializa e retorna o driver do Chrome com a janela maximizada.

    Usa a opção 'detach' para manter o navegador aberto após o término
    do script, facilitando a visualização do resultado final.

    Returns:
        webdriver.Chrome: Instância do WebDriver pronta para uso.
    """
    # Mantém o navegador aberto após o script encerrar
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver