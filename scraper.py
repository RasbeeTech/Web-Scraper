from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv


class Scraper:
    def __init__(self, url):
        self.driver = webdriver.Chrome("./chromedriver", options=self.set_chrome_options())
        self.url = url
        self.open_url()
        self.content = self.get_content()

    def set_chrome_options(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        return chrome_options

    def open_url(self):
        self.driver.get(self.url)

    def get_content(self):
        content = self.driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        return soup

    # retrieves all elements with a chosen html tag
    def get_all_tags(self, tag="h1"):
        all_tags = []
        for element in self.content.select(tag):
            all_tags.append(element.text.strip())

        return all_tags
    
    def get_items(self, product_container='div.thumbnail'):
        top_items = []

        products = self.content.select(product_container)
        for elem in products:
            title = elem.select('h4 > a.title')[0].text
            review_label = elem.select('div.ratings')[0].text
            info = {
                "title": title.strip(),
                "review": review_label.strip()
            }
            top_items.append(info)

        print(top_items)
        # return(top_items)

    def get_all_products(self, content_container='div.thumbnail'):
        all_products = []

        products = self.content.select(content_container)
        for product in products:
            name = product.select('h4 > a')[0].text.strip()
            description = product.select('p.description')[0].text.strip()
            price = product.select('h4.price')[0].text.strip()
            reviews = product.select('div.ratings')[0].text.strip()
            image = product.select('img')[0].get('src')

            all_products.append({
                "name": name,
                "description": description,
                "price": price,
                "reviews": reviews,
                "image": image
            })

        # print(all_products)
        return all_products

    def quit(self):
        self.driver.quit()

    def save_product_csv(self, all_products):
        keys = all_products[0].keys()

        with open('products.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(all_products)


if __name__ == "__main__":
    urls = [
        "https://webscraper.io/test-sites/e-commerce/allinone",
        "https://webscraper.io/test-sites/e-commerce/allinone/computers",
        "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops",
        "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets",
        "https://webscraper.io/test-sites/e-commerce/allinone/phones",
        "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
    ]

    start_time = time.time()

    for url in urls:
        scraper = Scraper(url)
        print("products:", scraper.get_all_products())
        scraper.quit()

    total_time = time.time() - start_time

    print("time:", total_time)