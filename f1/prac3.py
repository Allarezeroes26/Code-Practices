import time

class Animal:
  def __init__(self, name, actions):
    self.name = name
    self.actions = actions
  
  def daily_routine(self, days):
    for day in range(days):
      day += 1
      print(f"Day {day} routine for {self.name}")
      for action in self.actions:
        print(f"{self.name} is {action}ing")
        time.sleep(1)
    print(f"End of Day {day} Routine for {self.name}")
    
animal1 = Animal("Zebra", ['Run', 'Eat', 'Sleep'])
animal2 = Animal("Tiger", ["Hunt", "Sleep", "Eat"])

animal1.daily_routine(2)
animal2.daily_routine(3)