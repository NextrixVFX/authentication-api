from requests import post

class createKey:
    def __init__(self, accessKey: str, url: str, projectName: str) -> None:
        self.accessKey: str = accessKey
        self.url: str = f"{url}create/{projectName}"
        self.projectName: str = projectName
    
    def create(self) -> None:
        self.discordID: str = input("Discord ID:\t")
        self.authKey: str = input("AuthKey:\t")

        print("""
            1 = 1 Day    [Free]
            2 = 7 Days   [$5]
            3 = 30 Days  [$12]
            4 = 3 Months [$25]
            5 = Lifetime [$35]
        """)

        try:
            dOption: int = int(input("Duration:\t"))
        except:
            print("Invalid Option!") # cant convert int

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
        print(create.text)
        input("Press any key to continue...")
        

if __name__ == "__main__":
    print("please run main.py uwu")
    
