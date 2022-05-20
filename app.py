from dotenv import load_dotenv
load_dotenv('.env')
import configparser

from src.scraper.Sel_Flipkart import flipkart_scrap
config=configparser.ConfigParser()
config.read('config.ini')
arguments=config['ARGUMENTS']
keyword=str(arguments['KEYWORD'])
pages=int(arguments['PAGES'])
driver_config=config['DRIVER']
headless=driver_config.getboolean('HEADLESS')

fs=flipkart_scrap(keyword=keyword,no_of_pages=pages,headless=headless)
fs.scrape()