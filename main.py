from scraper import Scraper
from threader import Thread
import time


def print_all_products(url):
    scraper = Scraper(url)
    print("products:", scraper.get_all_products())
    scraper.quit()


if __name__ == "__main__":
    # Create list of urls for testing
    urls = [
        "https://webscraper.io/test-sites/e-commerce/allinone",
        "https://webscraper.io/test-sites/e-commerce/allinone/computers",
        "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops",
        "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets",
        "https://webscraper.io/test-sites/e-commerce/allinone/phones",
        "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
    ]

    # Used to measure performance speed
    start_time = time.time()

    # Create threads and place them in threads list
    threads = []
    for url in urls:
        thread = Thread(urls.index(url), print_all_products, url)
        threads.append(thread)
    # Start all threads
    for thread in threads:
        thread.start()
    # Join all threads (waits till all threads are completed)
    for thread in threads:
        thread.join()

    total_time = time.time() - start_time

    print("time:", total_time)
