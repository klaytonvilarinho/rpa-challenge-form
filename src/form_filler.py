from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clicar_iniciar(driver):
    """
    Aguarda e clica no botão START para iniciar o cronômetro do desafio.

    Args:
        driver: Instância do WebDriver do Selenium.
    """
    wait = WebDriverWait(driver, 10)
    btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.uiColorButton")
    ))
    btn.click()


def preencher_formulario(driver, linha):
    """
    Preenche todos os campos do formulário com os dados de uma linha da planilha.

    Localiza cada campo pelo texto do <label> correspondente e navega para o
    elemento pai para encontrar o <input> associado. Converte os valores para
    string para garantir compatibilidade com o campo de texto.

    Args:
        driver: Instância do WebDriver do Selenium.
        linha (dict): Dicionário com os dados da linha atual da planilha.
    """
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))

    labels = driver.find_elements(By.TAG_NAME, "label")

    for label in labels:
        nome_campo = label.text.strip()
        if nome_campo in linha:
            parent = label.find_element(By.XPATH, "..")
            inp = parent.find_element(By.TAG_NAME, "input")
            inp.clear()
            inp.send_keys(str(linha[nome_campo]))


def submeter_formulario(driver):
    """
    Clica no botão Submit para enviar o formulário e avançar para a próxima rodada.

    Args:
        driver: Instância do WebDriver do Selenium.
    """
    btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    btn.click()