import time

class PowerCleaner:
    def __init__(self, battery, total_rooms):
        self.battery = battery
        self.total_rooms = total_rooms
        self.rooms_left = total_rooms

    def clean(self):
        print("Robot Cleaning started")

        if self.battery > 100:
            print("Battery is overcharged, robot died")
            return

        current_room = 1
        while self.rooms_left > 0:
            if self.battery <= 0:
                print("Power died. Charging robot...")
                while self.battery < 100:
                    self.battery += 20
                    if self.battery > 100:
                        self.battery = 100
                    print(f"Charging: {self.battery}%")
                    time.sleep(1)
                print("Battery full! Resuming cleaning.")

            print(f"Power: {self.battery}%, Rooms Left to Clean: {self.rooms_left}")
            print(f"Cleaning Room: {current_room}")
            self.battery -= 20
            self.rooms_left -= 1
            current_room += 1
            print(f"Battery Power left: {self.battery}%\n")
            time.sleep(1)

        print(f"All rooms cleaned! Battery power left: {self.battery}%")

powercleaner1 = PowerCleaner(100, 8)
powercleaner1.clean()
