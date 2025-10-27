import time
class SecurityGuard:
  def __init__(self, name, areas, rounds):
    self.name = name
    self.areas = areas
    self.rounds = rounds
  
  def patrol(self):
    for round in range(1, self.rounds + 1):
      print(f"Starting round {round} of patrollling")
      for area in self.areas:
        print(f"{self.name} is checking {area}")
        time.sleep(1)
      print(f"Round {round} is complete")
    print("All rounds are complete!")
    
security1 = SecurityGuard("Jamie", ['Hall', 'Vault', 'Rooms'], 9)
security2 = SecurityGuard("James", ['Vault', 'Hall', 'Rooms'], 3)

security1.patrol()
security2.patrol()
