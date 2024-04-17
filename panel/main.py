from json import loads, dump
from os import _exit, system
from time import sleep

try:
    from lib.createKeys import createKey
    from lib.deleteKeys import deleteKey
    from lib.verifyKeys import verifyKey
    from lib.getKeys import getKey
except Exception as e:
    print(f"Wrong file or Import Error!\nExitting!\n{e}")
    sleep(1)
    _exit(0)

class config:
    def __init__(self) -> None:
        try:
            self.__config__ = loads(open("config/config.json", "r+").read())
            if self.__config__ is None or self.__config__ == "":
                self.createConfig()
        except Exception as e:
            try:
                print(f"Unable to read config! Creating config!\n{e}")
                self.createConfig()
                self.__config__ = loads(open("config/config.json", "r+").read())
            except Exception as e:
                print(f"Config creation failed!\n{e}")
                _exit(0)

    def createConfig(self):
        with open("config/config.json", "w") as outfile:
                    dump(
                    {
                        "accessKey": "puturaccesskey",
                        "url": "http://127.0.0.1:85/",
                        "projectName": "k4rb1ne"
                    }, outfile)

class panel:
    def __init__(self) -> None:
        self.config = config()
        self.accessKey: str = self.config.__config__['accessKey']
        self.url: str = self.config.__config__['url']
        self.projectName: str = self.config.__config__['projectName']

        self.createKey = createKey(self.accessKey, self.url, self.projectName)
        self.deleteKey = deleteKey(self.accessKey, self.url, self.projectName)
        self.verifyKey = verifyKey(self.accessKey, self.url, self.projectName)
        self.getKey = getKey(self.accessKey, self.url, self.projectName)

    def clear(self) -> None:
        system("cls")
    
    def start(self) -> None:
        print("""\n
        \t1 = Create Key
        \t2 = Delete Key
        \t3 = Verify Key
        \t4 = Get Keys\n
        """)
        selection: int = int(input(">>\t"))
        if selection == 1:
            self.clear()
            self.createKey.create()
        elif selection == 2:
            self.clear()
            self.deleteKey.delete()
        elif selection == 3:
            self.clear()
            self.verifyKey.verify()
        elif selection == 4:
            self.clear()
            self.getKey.get()
        else:
            print("Invalid Option!")

if __name__ == "__main__":
    main = panel()
    try:
        while True:
            main.clear()
            main.start()
    except Exception as e:
        print(f"Error: {e}")