import threading
import time

from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import Qt

import sys
from db import DB
from parser import factory_parser
from gui.gui import create_ui
import settings
from thread_func import *

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

list_of_sites = []


def create_list_of_sites() -> list:
    """ create from settings.list_of_sites to list """

    for site in settings.list_of_sites.values():
        list_of_sites.append(factory_parser(site['name'], site['url'], site['find_word']))

    return list_of_sites


def check_list_of_sites(list_of_sites):
    for site in list_of_sites:
        site.request()
        site.get_posts()
        new = site.get_new_posts()
        site.save()
        display_controller(site.name, new)


def loop_update(list_of_sites):
    while True:

        check_list_of_sites(list_of_sites)

        time.sleep(settings.UPDATE_TIME)


def display_updates(site, page, title):
    print(site, page, title)


def display_controller(site_name, posts: list):
    if len(posts) > 5:
        display_updates(site_name, "",  len(posts))

    elif 5 > len(posts) > 1:
        for post in posts[::-1]:
            display_updates(site_name, post.url, post.title)

    elif len(posts) == 1:
        display_updates(site_name, posts[0].url, posts[0].title)


def start_ui(db):
    threading.Thread(target=create_ui, args=(db, )).start()


def main():
    global list_of_sites

    Thread_CMD(list_of_sites).start_thread()

    list_of_sites = create_list_of_sites()
    start_ui(list_of_sites)

    loop_update(list_of_sites)


if __name__ == '__main__':
    main()
