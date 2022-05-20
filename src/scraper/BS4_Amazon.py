import requests
import bs4
import pandas as pd
import datetime


def parse_webpage_bs(search_url):
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    site_request = requests.get(search_url, headers=HEADERS)
    if site_request.status_code == 200:
        site_soup = bs4.BeautifulSoup(site_request.content, "html.parser")
        return site_soup
    else:
        return None

def save_data(data_list, filename):
    final_data = pd.DataFrame(data_list)
    final_data.to_csv(f"./BS4_DATA{filename}, header=["product_name", "product_price"], sep="|", encoding='utf-8')


def extract_item_info(keyword):
    data_list = []
    current_time = datetime.datetime.now().strftime('%m-%d-%Y')
    filename = f"{keyword}_{current_time}.csv"
    search_url = f"https://www.amazon.in/s?k={keyword}"
    site_soup = parse_webpage_bs(search_url)
    for element in site_soup.find_all('div', attrs={'data-component-type': 's-search-result'}):
        try:
            product_name = element.find("span", attrs={'class': "a-size-medium a-color-base a-text-normal"}).get_text()
            product_price = element.find("span", attrs={'class': "a-price-whole"}).get_text()
            product_price = "Rs." + product_price
            print(product_price)
            print(product_name)
            data_list.append([product_name, product_price])

        except:
            continue
        if len(data_list) == 10:
            save_data(data_list, filename)
            print("done!")
            break


keyword = "smartphones"
extract_item_info(keyword)
