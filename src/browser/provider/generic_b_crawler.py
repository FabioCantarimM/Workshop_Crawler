import os
from selenium import webdriver

class GenericBrowserCrawler:

    browser: None
    options = webdriver.ChromeOptions()

    def __init__(self):
        pass

    def get_browser(self, args: list[str]):
        self.set_options(args)
        self.browser = self.driver = webdriver.Chrome(options=self.options)
    
    def is_headless(self):
        headless = os.getenv('HEADLESS', True)
        if headless:
            self.options.add_argument("--headless")

    
    def set_options(self, args: list[str]):
        self.is_headless()
        self.set_proxy()
        if args:
            for arg in args:
                self.options.add_argument(arg)

    def set_proxy(self):
        if os.getenv("USE_PROXY"):
            #Proxy url possibilities: IP or Protocol://User:Password@IP:Port
            user  = os.getenv("PROXY_USER")
            password = os.getenv("PROXY_PASSWORD")
            url = os.getenv("PROXY_URL")
            port = os.getenv("PROXY_PORT")
            proxy_provider = f'http://{user}:{password}@{url}:{port}'
            self.options.add_argument(f'--proxy-server={proxy_provider}')

    def close_chromium(self):
        if self.driver:
            self.driver.quit()
