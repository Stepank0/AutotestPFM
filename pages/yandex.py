import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class YandexPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://yandex.ru'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(xpath="//input[@class='arrow__input mini-suggest__input']")

    # Search button
    search_run_button = WebElement(xpath="//button[@class='search2-iframe__button']")

    search_result = ManyWebElements(xpath="//ul[@class='serp-list serp-list_left_yes']")
