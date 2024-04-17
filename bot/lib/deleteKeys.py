from requests import post

class deleteKey:
    def __init__(self, accessKey: str, url: str, projectName: str, discordID: str) -> None:
        self.accessKey: str = accessKey
        self.url: str = f"{url}kill/{projectName}"
        self.projectName: str = projectName
        self.discordID: str = discordID
    
    def delete(self) -> None:
        

        headers = {
            "discordid": self.discordID,
            "accessKey": self.accessKey
        }

        delete = post(url=self.url, json=headers)
        #print(delete.text)

if __name__ == "__main__":
    print("please run main.py uwu")
    
