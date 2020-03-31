from bs4 import BeautifulSoup
from locators.all_book_page import AllBooksPageLocators
from parsers.book_parser import BookParser
import re


class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]\

    @property
    def page_count(self):
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        page_count = int(matcher.group(1))
        return page_count
