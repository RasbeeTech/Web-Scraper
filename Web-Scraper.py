from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from BeautifulSoup import BeautifulSoup
# from BeautifulSoup import BeautifulSoup4
# import BeautifulSoup
from bs4 import BeautifulSoup
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome('./chromedriver', options=chrome_options)

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

driver.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

title = soup.title.text
body = soup.body.text
head = soup.head.text

#print(head, title, body)

all_h1_tags = []

for element in soup.select('h1'):
    all_h1_tags.append(element.text)

#print(all_h1_tags)
top_items = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.thumbnail')
for elem in products:
    title = elem.select('h4 > a.title')[0].text
    review_label = elem.select('div.ratings')[0].text
    info = {
        "title": title.strip(),
        "review": review_label.strip()
    }
    top_items.append(info)

# print(top_items)

all_links = []

# Extract and store in top_items according to instructions on the left
links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    all_links.append({"href": href, "text": text})

# print(all_links)
all_products = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.thumbnail')
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


keys = all_products[2].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)


driver.quit()

if __name__ == "__main__":
    # TODO: make program able to access different ecommerce sites: https://webscraper.io/test-sites
    print("WebScraper.py")

