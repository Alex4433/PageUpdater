UPDATE_TIME = 200
TITLE_MAX_CMD_WIGHT = 40

proxies = {
    'http': 'socks5://127.0.0.1:8371',
    'https': 'socks5://127.0.0.1:8371'
}

list_of_sites = {
    # '1': {        'name'     : 'habr',
    #               'url'      : 'https://habr.com/ru/rss/all/all/?fl=ru',
    #               'find_word': []},

    '2': {        'name'     : 'pikabu',
                  'url'      : 'https://pikabu.ru/xmlfeeds.php?cmd=popular',
                  'find_word': []},
}


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

parsing_flags = {
    "item": ["item", "entry"],
    "title": ["title"],
    "date": ["pubDate", "pubdate", "published"],
    "content": ["description"],
    "url": ["link", "guid", "url", "uri"],
}

