class Post:
    def __init__(self, title, date, content, url):
        self.title = self.replace_symbols(title)
        self.date = self.type_valid(date)
        self.content = self.replace_symbols(content)
        self.url = self.type_valid(url)

    def type_valid(self, w):
        if type(w) is str:
            return w
        else:
            return ""

    def replace_symbols(self, w: str):
        w = self.type_valid(w)

        l = ["CDATA", "[", "]", "<!"]

        for i in l:
            w = w.replace(i, "")

        return w

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

