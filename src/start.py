from browser.ec_crawler import Ml_Crawler


ml = Ml_Crawler("Ml").crawl('Nintendo Switch')
az = Ml_Crawler("Amazon").crawl('playstation')


print(az)