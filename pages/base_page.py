class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        self.page.goto(url)

    def get_page_title(self):
        return self.page.title()