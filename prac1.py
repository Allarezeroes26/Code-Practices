import time

class CleanerBot:
  def __init__(self, name, roomsCleaned, isCleaning):
    self.name = name
    self.roomsCleaned = roomsCleaned
    self.isCleaning = isCleaning
  
  def clean(self):
    rooms = 5
    
    
    while self.roomsCleaned < 5:
      print(f"Cleaning Room: {rooms}")
      time.sleep(1)
      rooms -= 1
      
      if rooms <= 0:
        print(f"No rooms left")
      self.roomsCleaned += 1
      print(f"Room Cleaned: {self.roomsCleaned}")
    
    print("Rooms all cleaned")
    self.isCleaning = False
    print(f"Cleaning mode set to : {self.isCleaning}")
    
cleanerbot = CleanerBot("Ekko", 6, True)

cleanerbot.clean()
