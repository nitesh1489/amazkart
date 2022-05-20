from dotenv import load_dotenv
load_dotenv('.env')

from src.scraper.Sel_Flipkart import flipkart_scrap

fs=flipkart_scrap('Smartphones',2)
fs.scrape()