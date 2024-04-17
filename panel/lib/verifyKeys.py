from requests import post

class verifyKey:
    def __init__(self, accessKey: str, url: str, projectName: str) -> None:
        self.accessKey: str = accessKey
        self.url: str = f"{url}verify/{projectName}"
        self.projectName: str = projectName
    
    def verify(self):
        self.discordID: str = input("Discord ID:\t")
        self.authKey: str = input("AuthKey:\t")

        headers = {
            "discordid": self.discordID,
            "authKey": self.authKey
        }

        verify = post(url=self.url, json=headers)
        print(verify.text)
        input("Press any key to continue...")

if __name__ == "__main__":
    print("please run main.py uwu")
    
