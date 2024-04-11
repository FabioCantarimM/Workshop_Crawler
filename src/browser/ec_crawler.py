##https://json-ld.org/learn.html
import time
import json
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from browser.crawlers.default_crawler import AbstractCrawler

class Ml_Crawler(AbstractCrawler):
    def __init__(self):
        super().__init__()

    def crawl(self, query):
        self.query = query
        self.browser.get(f"https://lista.mercadolivre.com.br/{query.replace(' ', '-')}")
        time.sleep(5)
        self.html = self.browser.page_source
        self.steps = self.get_steps("Ml")
        print(self.steps)
        self.content = self.extraction()
        self.browser.quit()
        df = self.transform_to_df_and_improve(self.content)
        self.mongo.save_dataframe(df)
        print("Wait")
        

    
    def extraction(self):
        soup = BeautifulSoup(self.html, "html.parser")
        json_steps = json.loads(self.steps)

        results = soup.find_all(json_steps["search"]["tag"], class_=json_steps["search"]["class"])

        data = []
        for result in results:
            product = {}
            for step in json_steps["product"]:
                value = json_steps["product"][step]
                content = eval(value)
                product[step] = content  # Adiciona o resultado ao dicionário do produto
        
            data.append(product)  # Adiciona o dicionário do produto aos dados

        return data
    

    def transform_to_df_and_improve(self, data):
        df = pd.DataFrame(data)
        df = df.assign(keyword=self.query)
        df = df.assign(dateTimeReference=datetime.now().isoformat())
        return df