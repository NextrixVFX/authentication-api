from requests import post

class deleteKey:
    def __init__(self, accessKey: str, url: str, projectName: str) -> None:
        self.accessKey: str = accessKey
        self.url: str = f"{url}kill/{projectName}"
        self.projectName: str = projectName
    
    def delete(self):
        self.discordID: str = input("Discord ID:\t")

        headers = {
            "discordid": self.discordID,
            "accessKey": self.accessKey
        }

        delete = post(url=self.url, json=headers)
        print(delete.text)
        input("Press any key to continue...")

if __name__ == "__main__":
    print("please run main.py uwu")
    
