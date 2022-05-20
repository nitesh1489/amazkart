from typing import final
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time,sys,os
from ..helpers.utils.export import export_csv

class flipkart_scrap():
    def __init__(self,keyword:str,no_of_pages:int,headless=False):
        self.keyword = keyword
        self.no_of_pages = int(no_of_pages)
        self._initialize_driver(headless)
        
    def _initialize_driver(self,headless):    
        firefox_options=FirefoxOptions()
        firefox_options.headless=headless
        self.driver=webdriver.Firefox(options=firefox_options,executable_path=os.environ.get('GECKODRIVER_PATH'))
        self.driver.maximize_window()
        return self.driver
    
    def pagination(self,page):
        self.keyword=self.keyword
        search_url=f"https://www.flipkart.com/search?q={self.keyword}&page={page}"
        return search_url
    
    def get_data(self):
        final_data={
            "p_name_list":[],
            "price_list":[],
            "specifications_list":[],
            "rating_list":[],
            "product_url_list":[],
            "thumbnail_list":[],
        }
        
        for i in range(1,self.no_of_pages+1):
            url_built=self.pagination(i)
            self.driver.get(url_built)
            p_names=self.driver.find_elements(By.CLASS_NAME,'_4rR01T')
            try:
                p_names=[i.text for i in p_names]
            except:
                p_names=None
            if not p_names:
                print('DATA LIMIT')
                break
            
            price=self.driver.find_elements(By.XPATH,"//div[@class='_3I9_wc _27UcVY']")
            price=[i.get_attribute('textContent') for i in price]
            
            specifications=self.driver.find_elements(By.CLASS_NAME,'_1xgFaf')
            specifications=[i.text.strip() for i in specifications]
            
            thumbnail=self.driver.find_elements(By.XPATH,"//div[@class='_2kHMtA']//img[@class='_396cs4 _3exPp9']")
            thumbnail=[i.get_attribute('src') for i in thumbnail]
            
            discounted_price=self.driver.find_elements(By.CLASS_NAME,'_3I9_wc _27UcVY')
            discounted_price=[i.get_attribute('textContent') for i in discounted_price]
            
            rating=self.driver.find_elements(By.XPATH,"//div[@class='_2kHMtA']//div[@class='_3LWZlK']")
            rating=[i.text for i in rating]
            
            product_url=self.driver.find_elements(By.XPATH,"//div[@class='_2kHMtA']//a")
            product_url=[i.get_attribute('href') for i in product_url]
            
            final_data["p_name_list"].extend(p_names)
            final_data["specifications_list"].extend(specifications)
            final_data["thumbnail_list"].extend(thumbnail)
            # final_data["discounted_price_list"].extend(discounted_price)
            final_data["rating_list"].extend(rating)
            final_data["product_url_list"].extend(product_url)
            final_data["price_list"].extend(price)
            
        # print(len(final_data['p_name_list']))
        # print(len(final_data['specifications_list']))
        # print(len(final_data['thumbnail_list']))
        # # print(len(final_data["discounted_price_list"]))
        # print(len(final_data['rating_list']))
        # print(len(final_data['product_url_list']))
        # print(len(final_data['price_list']))
        
    
        # print(p_name_list)
        # zipped_list=zip(p_name_list,specifications_list,thumbnail_list,discounted_price_list,rating_list,product_url_list,price_list)
        # print(zipped_list)
        # for i,j,k,l,m,n,o in zipped_list:
        #     article_data=Product(
        #         product=i,
        #         specifications=j,
        #         thumbnail=k,
        #         discounted_price=l,
        #         rating=m,
        #         product_url=n,
        #         price=o
        #         )
        #     product_list.append(article_data)
        
        return final_data
    
    def scrape(self):
        data=self.get_data()
        export_csv(data)
        
if __name__ == '__main__':      
    fp=flipkart_scrap('Smartphones',3)
    fp.scrape()