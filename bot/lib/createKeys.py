from requests import post
from random import randint
from hashlib import sha256

class createKey:
    def __init__(self, accessKey: str, url: str, projectName: str, discordID: str, duration: str) -> None:
        self.accessKey: str = accessKey
        self.url: str = f"{url}create/{projectName}"
        self.projectName: str = projectName

        self.randomKey = f"{str(randint(24328185281, 9215981208402))}{randint(16264, 513224)}"

        self.discordID: str = discordID
        self.authKey: str = str(sha256(self.randomKey.encode('utf-8')).hexdigest())
        self.duration: str = duration
    
    def create(self) -> str:
        dOption: int = int(self.duration)

        if dOption == 1: # free trial
            self.duration: str = "1"
        elif dOption == 2: # 1 week
            self.duration: str = "7"
        elif dOption == 3: # 1 month
            self.duration: str = "30"
        elif dOption == 4: # 3 months
            self.duration: str = "90"
        elif dOption == 5: # life
            self.duration: str = "-1"
        else:
            print("Invalid Option!") # option not listed

        headers = {
            "discordid": self.discordID,
            "authKey": self.authKey,
            "duration": self.duration,
            "accessKey": self.accessKey
        }

        create = post(url=self.url, json=headers)
        
        return self.authKey


if __name__ == "__main__":
    print("please run main.py uwu")
    
