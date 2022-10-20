import threading
import settings


class Thread_CMD:

    def __init__(self, objects):
        self.objects = objects

    def start_thread(self):
        threading.Thread(target=self.cmd).start()

    def cmd(self):
        while True:
            try:

                inp = input()

                if inp in "1234567890":
                    inp = int(inp)


                if inp == 'show':
                    i = 0
                    print("id , name")
                    for it in self.objects:
                        print(i, it.name)
                        i += 1

                elif type(inp) == int:
                    for it in self.objects[inp].data[:10:-1]:
                        print(it.title[:settings.TITLE_MAX_CMD_WIGHT], it.date, it.url, it.content[:30])


            except Exception as ex:
                print(ex)