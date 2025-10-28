import time

class CarRace:
  def __init__ (self, fuel, speed):
    self.fuel = fuel
    self.speed = speed
    
  def race(self):
    print('Race Started!')
    distanceCovered = 0
    refuels = 0
    
    for laps in range(1, 11):
      distanceCovered += distanceCovered
      
      if self.fuel <= 0:
        refuels += 1
        print(f"Car rans out of fuel")
        while self.fuel < 300:
          self.fuel += 50
          print(f"PitCrew refueling car: {self.fuel}")
          time.sleep(1)
      
      print(f"Lap: {laps} starting")
      distanceCovered += self.speed * 2
      self.fuel -= 100
      print(f'Distance: {distanceCovered} | fuel left: {self.fuel}')
      time.sleep(2)
    
    print(f"Race ended! Distance: {distanceCovered}, Number of Refuels: {refuels}")
      
car = CarRace(200, 60)

car.race()