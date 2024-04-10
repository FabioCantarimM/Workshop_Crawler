from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def crawl_mercado_livre(query):
    # Configurando as opções do Chrome para rodar headless
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Rodar o Chrome em modo headless
    chrome_options.add_argument("--no-sandbox")  # Evitar problemas de sandbox

    # Inicializando o driver do Chrome
    driver = webdriver.Chrome(options=chrome_options)

    # Navegando para a página de pesquisa do Mercado Livre
    driver.get(f"https://lista.mercadolivre.com.br/{query.replace(' ', '-')}")
    
    # Aguardando um momento para a página carregar completamente
    time.sleep(5)

    # Obtendo o HTML da página
    html = driver.page_source

    # Fechando o navegador
    driver.quit()

    # Analisando o HTML com BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Extraindo os dados que você deseja
    results = soup.find_all("div", class_="ui-search-result")

    for result in results:
        # Aqui você pode extrair informações específicas de cada resultado, como título, preço, etc.
        title = result.find("h2", class_="ui-search-item__title").text.strip()
        price = result.find("span", class_="price-tag-fraction").text.strip()
        print(f"Produto: {title}, Preço: {price}")

# Exemplo de utilização
crawl_mercado_livre("iphone 12")
