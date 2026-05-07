class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open_website(self, url):
        self.driver.get(url)
        print("hi")

    def get_page_title(self):
        return self.driver.title
