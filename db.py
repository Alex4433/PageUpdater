import os
import pickle
import string
import json
from dataclass import Post

class DB:
    """
    :: save - saving a data
    :: load - loading a data
    """

    _path_db = f"{os.getcwd()}/db/"

    def __init__(self, name):
        self.file_name = self.__format_url_to_name(name)
        self.path_file = self._path_db + self.file_name

        self.data: list = []
        self.load()

    def __check_exist_file(self):
        if self.file_name in os.listdir(self._path_db):
            return True
        else:
            return False

    def __format_url_to_name(self, name):
        return ''.join(filter(lambda l: l in string.ascii_letters, name)).replace('www', '').replace('https', '').replace('http', '')


    def save(self):
        pass

    def load(self):
        pass


class PickleDB(DB):

    def save(self):
        with open(self.path_file, 'wb') as file:
            pickle.dump(self.data, file)

    def load(self):
        if self.__check_exist_file():
            with open(self.path_file, 'rb') as file:
                try:
                    self.data = pickle.load(file)
                except EOFError:
                    self.data = []
                except Exception as ex:
                    raise Exception(f"Unknown error from DB load : {ex}")
        else:
            open(self.path_file, 'x')


class JsonDB(DB):
    def __init__(self, name):
        super().__init__(name)
        self.path_file += ".json"

    def save(self):
        with open(self.path_file, "w") as file:
            json.dump(self.format_to_json(), file, indent=4, ensure_ascii=False)

    def load(self):
        with open(self.path_file, "r") as file:
            a = json.load(file)
            self.format_from_json(a)

    def format_to_json(self):
        dec = []
        for i in self.data:
            tmp = [i.title, i.date, i.content, i.url]
            dec.append(tmp)

        return dec

    def format_from_json(self, ls):
        self.data = []
        for i in ls:
            for j in i:
                self.data.append(Post(*j))



def factory_db(*args, **kwargs):
    # return PickleDB(*args, **kwargs)
    return JsonDB(*args, **kwargs)