from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import threading
import time


class Thread(threading.Thread):
    def __init__(self, thread_id, name, url):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.url = url

    def run(self):
        start_time = time.time()
        print("Starting " + self.name)

        scraper = Scraper(url=self.url)
        scraper.test()
        scraper.quit()

        print(self.name + " completed in: %s" % (time.time()-start_time))


class Scraper:
    def __init__(self, url):
        self.driver = webdriver.Chrome("./chromedriver", options=self.set_chrome_options())
        self.url = url

        self.open_url()
        self.content = self.get_content()

        # self.all_tags = self.get_all_tags(tag="h1")
        # self.get_items()

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

    def test(self):
        element_tags = self.get_all_tags()
        for element_tag in element_tags:
            print(element_tag)

        products = self.get_all_products()
        for product in products:
            print(product)


thread1 = Thread(1, "thread1", "https://webscraper.io/test-sites/e-commerce/allinone")
thread2 = Thread(2, "thread2", "https://webscraper.io/test-sites/e-commerce/allinone/computers")
thread3 = Thread(3, "thread3", "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
thread4 = Thread(4, "thread4", "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets")
thread5 = Thread(5, "thread5", "https://webscraper.io/test-sites/e-commerce/allinone/phones")
thread6 = Thread(6, "thread6", "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch")

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()