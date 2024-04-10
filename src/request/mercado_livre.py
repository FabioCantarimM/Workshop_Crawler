import requests
from bs4 import BeautifulSoup

def crawl_mercado_livre(query):
    # URL da página de pesquisa do Mercado Livre
    url = f"https://lista.mercadolivre.com.br/{query.replace(' ', '-')}"
    
    # Enviar uma solicitação GET para a página
    response = requests.get(url)
    
    # Verificar se a solicitação foi bem sucedida (código de status 200)
    if response.status_code == 200:
        # Parsear o HTML da página usando BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Encontrar todos os resultados da pesquisa
        results = soup.find_all("div", class_="ui-search-result")
        
        # Iterar sobre os resultados e extrair as informações desejadas
        for result in results:
            # Aqui você pode extrair informações específicas de cada resultado, como título, preço, etc.
            title = result.find("h2", class_="ui-search-item__title").text.strip()
            price = result.find("span", class_="price-tag-fraction").text.strip()
            print(f"Produto: {title}, Preço: {price}")
    else:
        print("Erro ao acessar a página:", response.status_code)

# Exemplo de utilização
crawl_mercado_livre("iphone 12")
