from threading import Thread
import requests


class Butler(Thread):
    def __init__(self, whomst, spacshaps):
        super().__init__()
        self.ships = spacshaps
        self.host = whomst

    def run(self):
        while True:
            r = requests.get(self.host)
            if r.status_code == 200:
                remote_ships = r.json()
                for i in range(0, 4):

                    self.ships[i].power["engines"] = float(remote_ships[i]["engine"]["power"]) / 200
                    self.ships[i].power["shields"] = float(remote_ships[i]["shields"]["power"])
                    self.ships[i].power["weapons"] = float(remote_ships[i]["weapons"]["power"])

                    self.ships[i].bearing["engines"] = float(
                        remote_ships[i]["engine"]["angle"]
                    )
                    self.ships[i].bearing["shields"] = float(
                        remote_ships[i]["shields"]["angle"]
                    )
                    self.ships[i].bearing["weapons"] = float(
                        remote_ships[i]["weapons"]["angle"]
                    )

                    self.ships[i].active["engines"] = bool(int(
                        remote_ships[i]["engine"]["active"]
                    ))
                    self.ships[i].active["shields"] = bool(int(
                        remote_ships[i]["shields"]["active"]
                    ))
                    self.ships[i].active["weapons"] = bool(int(
                        remote_ships[i]["weapons"]["active"]
                    ))
            else:
                print("[WARNING] Server returned not 200; ungood!")
