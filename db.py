import os
import pickle
import string


class DB:
    """
    :: save - saving a data
    :: load - loading a data
    """

    __path_db = f"{os.getcwd()}/db/"

    def __init__(self, name):
        self.file_name = self.__format_url_to_name(name)
        self.path_file = self.__path_db + self.file_name

        self.data: list = []
        self.load()

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

    def __check_exist_file(self):
        if self.file_name in os.listdir(self.__path_db):
            return True
        else:
            return False

    def __format_url_to_name(self, name):
        return ''.join(filter(lambda l: l in string.ascii_letters, name)).replace('www', '').replace('https', '').replace('http', '')
