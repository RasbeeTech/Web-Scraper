from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv
import threading

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome("./chromedriver", options=chrome_options)


def get_content(webpage="https://webscraper.io/test-sites/e-commerce/allinone"):
    driver.get(webpage)

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    title = soup.title.text
    body = soup.body.text
    head = soup.head.text

    # print(head, title, body)
    # print(head.strip())
    return soup


def get_all_tags(content, tag='h1'):
    all_tags = []

    for element in content.select(tag):
        all_tags.append(element.text.strip())

    # print(all_tags)
    return all_tags


def get_items(content, product_container='div.thumbnail'):
    top_items = []

    products = content.select(product_container)
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


def get_all_products(content, content_container='div.thumbnail'):
    all_products = []

    products = content.select(content_container)
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


def save_product_csv(all_products):
    keys = all_products[0].keys()

    with open('products.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_products)


if __name__ == "__main__":
    print("WebScraper.py\n")

    url_home = 'https://webscraper.io/test-sites/e-commerce/allinone'
    url_computers_top_items = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
    url_laptops = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    url_tablets = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
    url_phones = "https://webscraper.io/test-sites/e-commerce/allinone/phones"
    url_phones_touch = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

    urls = [url_home,
            url_computers_top_items,
            url_laptops,
            url_tablets,
            url_phones,
            url_phones_touch]

    start_time = time.time()
    for url in urls:
        html = get_content(url)
        element_tags = get_all_tags(html, "h1.page-header")
        # print(tags)
        for element_tag in element_tags:
            print(element_tag)

        products = get_all_products(html)
        for product in products:
            print(product)

    end_time = time.time()
    print("total time: %s" % (end_time - start_time))


    driver.quit()
