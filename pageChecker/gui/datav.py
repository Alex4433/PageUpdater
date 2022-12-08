from faker import Faker


mock_data_list = []


class Post:
    def __init__(self, title, date, content, url):
        self.title = f.text()[:40]
        self.date = f"{f.date()} {f.time()}"
        self.content = "content_content_content_content_content_content"
        self.url = f.url()

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


class DB:
    def __init__(self, name):
        self.name = name
        self.data = []
        self.data.append(Post("1","2","3","4"))
        self.data.append(Post("1","2","3","4"))
        self.data.append(Post("1","2","3","4"))
        self.data.append(Post("1","2","3","4"))
        self.data.append(Post("1","2","3","4"))
        self.data.append(Post("1","2","3","4"))
        self.data.append(Post("1","2","3","4"))


class Mock:
    def __init__(self, name):
        self.name = name
        self.db: DB = DB(name)
        self.data: list = self.db.data


f = Faker()


# print(f"{f.url()}"
#       f"{f.text()[:50]}"
#       f""
#       f""
#       f"")


mock_data_list.append(Mock(f.url().split("/")[-2].replace("www.", "")))
mock_data_list.append(Mock(f.url().split("/")[-2].replace("www.", "")))
mock_data_list.append(Mock(f.url().split("/")[-2].replace("www.", "")))
mock_data_list.append(Mock(f.url().split("/")[-2].replace("www.", "")))
mock_data_list.append(Mock(f.url().split("/")[-2].replace("www.", "")))
