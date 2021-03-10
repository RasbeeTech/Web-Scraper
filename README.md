# Web-Scraper
 Web scraper via Python and Selenium.
 
 Python version: 3.8.7  
 Selenium version: 3.141.0  
 Tested using: www.webscraper.io/test-sites  
 ### Description
 This webscraper is used to test scraping functionality.  The goal was to scrape all products found in the test urls.  
 ## Modules
 ### main.py
 Use this module to run/test the program.
 ### threader.py
 **Thread**(*self, thread_id, func, args*): initializes thread.  Declare a thread id(thread_id) for identification.  This custom class also passes a function(func) to and and argument(args).  
 **run**(): When Thread().start is called the initiated function(func) will be called with arguement(arg).  
 ### scraper.py
 **Scraper**(*url*): Initializes scraper with url to be scraped.  When Scraper() is declared, a Selenium Chrome webdriver is created, and the content of the url is scraped.  
 **set_chrome_options**(): Defines the chrome options.  They are already set to headless and to disable gpu.  
 **get_content**(): Scrapes all html content from url address.  
 **get_all_tags**(*tag="h1"*): retrieves all elements with a chosen html tag.  Note: Default is "h1" tag.  
 **get_items**(*product_container="div.thumbnail"*): Retrives all specified containers.  Note: Default is "div.thumbnail".  
 **get_all_products**(*content_container="div.thumbnail"*): gets all products found in url.  Takes the arguement content_container which specifies the container holding each product.  Note: Default is "div.thumbnail".  
 **quit**(): terminate the webdriver. Note: Webdrivers should be terminated at the end of each session or they will stay active and occupy device memory.  
 **save_product_csv**(*all_products*): Takes arguement all_products as dictionary object.  Saves all_product into .csv file in the same directory.  
