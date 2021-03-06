from threading import Thread
import requests


class Butler(Thread):
    def __init__(self, whomst, spacshaps):
        super().__init__()
        self.ships = spacshaps
        self.host = whomst

    def run(self):
        while True:
            try:
                r = requests.get(self.host)
                if r.status_code == 200:
                    remote_ships = r.json()
                    for i in range(0, 4):
                        try:
                            self.ships[i].power["engines"] = float(remote_ships[i]["engine"]["power"]) / 200
                        except:
                            print("oof")
                        try:
                            self.ships[i].power["shields"] = float(remote_ships[i]["shields"]["power"])
                        except:
                            print("oof")
                        try:
                            self.ships[i].power["weapons"] = float(remote_ships[i]["weapons"]["power"])
                        except:
                            print("oof")

                        try:
                            self.ships[i].bearing["engines"] = float(
                                remote_ships[i]["engine"]["angle"]
                            )-90
                        except:
                            print("oof")
                        try:
                            self.ships[i].bearing["shields"] = float(
                                remote_ships[i]["shields"]["angle"]
                            )-90
                        except:
                            print("oof")
                        try:
                            self.ships[i].bearing["weapons"] = float(
                                remote_ships[i]["weapons"]["angle"]
                            )-90
                        except:
                            print("oof")

                        try:
                            self.ships[i].active["engines"] = bool(int(
                                remote_ships[i]["engine"]["active"]
                            ))
                        except:
                            print("oof")
                        try:
                            self.ships[i].active["shields"] = bool(int(
                                remote_ships[i]["shields"]["active"]
                            ))
                        except:
                            print("oof")
                        try:
                            self.ships[i].active["weapons"] = bool(int(
                                remote_ships[i]["weapons"]["active"]
                            ))
                        except:
                            print("oof")
                else:
                    print("[WARNING] Server returned not 200; ungood!")
            except:
                print("[WARNING] Server borked aggressively; ungood!")
