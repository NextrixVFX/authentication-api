from requests import post

class getKey:
    def __init__(self, accessKey: str, url: str, projectName: str) -> None:
        self.accessKey: str = accessKey
        self.url: str = f"{url}keys/{projectName}"
        self.projectName: str = projectName
    
    def get(self):
        headers = {
            "accessKey": self.accessKey
        }

        get = post(url=self.url, json=headers)
        print(get.text)
        input("Press any key to continue...")

if __name__ == "__main__":
    print("please run main.py uwu")
    
