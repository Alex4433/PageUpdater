import requests

from bs4 import BeautifulSoup

from db import DB
from settings import proxies, headers
from dataclass import Post


class Parser:

    """
    :: save
    :: load
    :: request
    :: get_posts


    """

    def __init__(self, name: str, url: str, find_word: list):
        self.name = name
        self.url = url
        self.find_word = find_word

        self.db: DB = DB(url)
        self.data: list = self.db.data

        self.new_posts = []
        self.status = True

    def save(self):
        self.db.save()

    def request(self):

        if self.status:
            try:
                self.req = requests.get(url=self.url, proxies=proxies, headers=headers)
            except Exception as ex:
                print(ex)
                print(f"[log] connection failed site: {self.name}")
                self.req = ''
                self.status = False

    def get_posts(self):
        pass

    def valid_post(self, post:Post):
        return True

    def check_duplicate(self, post:Post):
        # self.title_posts = list(map(str, self.data))  # mb change __str__ return f"title + date"

        # if post.title in self.title_posts:
        #     return False
        # else:
        #     return True

        for p in self.data:
            if p.title == post.title:
                if p.date:
                    if p.date == post.date:
                        return False
                return False

        return True

    def find_post(self, post):
        if self.find_word:
            for wr in self.find_word:
                if wr in post.title:
                    return True
        else:
            return True

    def _add_post_to_inner_list(self, title, date, content, url):

        post = Post(title, date, content, url)
        if self.check_duplicate(post) and self.valid_post(post):

            self.data.append(post)
            if self.find_post:
                self.new_posts.append(post)

    def get_new_posts(self):
        s = self.new_posts[:]
        self.new_posts = []
        return s

    def __str__(self):
        return self.__class__.__name__


class ParserVk(Parser):
    pass


class ParserYt(Parser):
    def get_posts(self):
        soup = BeautifulSoup(self.req.text, "lxml")
        list_of_items = soup.find_all('entry')

        for item in list_of_items[::-1]:
            try:
                title = item.find('title').text
            except:
                continue
            try:
                date = item.find('published').text
            except:
                date = None
            try:
                content = item.find('media:description').text
            except:
                content = None
            try:
                url = item.find('link').attrs['href']
            except:
                url = None

            self._add_post_to_inner_list(title, date, content, url)


class ParserRSS(Parser):
    def get_posts(self):

        soup = BeautifulSoup(self.req.text, "lxml")
        list_of_items = soup.find_all('item')

        for item in list_of_items[::-1]:
            try:
                title = item.find('title').text
            except:
                continue
            try:
                date = item.find('pubdate').text
            except:
                date = None
            try:
                content = item.find('description').text
            except:
                content = None
            try:
                url = item.find('guid').text
            except:
                url = None

            self._add_post_to_inner_list(title, date, content, url)


def factory_parser(name, url, find_word):
    if 'youtube.com' in url:
        return ParserYt(name, url, find_word)

    elif 'rss' or 'RSS' in url:
        return ParserRSS(name, url, find_word)

    elif 'vk.com' in url:
        return ParserVk(name, url, find_word)
