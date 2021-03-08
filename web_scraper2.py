from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url = url

    def run(self):
        print("Starting " + self.name)
        # do_all(self.url)
        print("Exiting " + self.name)
