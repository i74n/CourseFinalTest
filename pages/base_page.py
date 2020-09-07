from selenium import webdriver


class BasePage():
    def __init__(self, browser : webdriver, url):
        self.browser = browser
        self.url = url

    def open(self, browser, url):
        self.browser.get(self.url)