from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv


def get_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    return driver


def get_content():
    driver.get("https://webscraper.io/test-sites/e-commerce/allinone")

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    title = soup.title.text
    body = soup.body.text
    head = soup.head.text

    print(head, title, body)
    return soup


def get_all_tags(content, tag='h1'):
    all_tags = []

    for element in content.select(str(tag)):
        all_tags.append(element.text)

    print(all_tags)
    # return all_tags


def get_items(content):
    top_items = []
    # Extract and store in top_items according to instructions on the left
    products = content.select('div.thumbnail')
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


def get_links(content):
    # Finds all links ('a' elements) on selected page
    all_links = []
    links = content.select('a')
    for ahref in links:
        text = ahref.text
        text = text.strip() if text is not None else ''

        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        all_links.append({"href": href, "text": text})

    print(all_links)
    # return(all_links)


def get_all_products(content):
    all_products = []

    # Extract and store in top_items according to instructions on the left

    products = content.select('div.thumbnail')
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


def save_product_csv(all_products):
    keys = all_products[0].keys()

    with open('products.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_products)


if __name__ == "__main__":
    # TODO: make program able to access different ecommerce sites: https://webscraper.io/test-sites
    print("WebScraper.py")

    driver = get_driver()
    driver.get('https://webscraper.io/test-sites/e-commerce/allinone')
    time.sleep(2)
    driver.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
    time.sleep(2)
    driver.quit()
