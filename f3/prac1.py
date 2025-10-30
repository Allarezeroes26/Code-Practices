class Convert:
  def __init__ (self, celsius):
    self.celsius = celsius
    
  def convertMe(self):
   farrenheit = (self.celsius * 9 / 5) + 32
   kelvin = self.celsius + 273.15
   print(f"{self.celsius} is {farrenheit}°")
   print(f"{self.celsius} is {kelvin}")

Number = int(input('Convert your number to Farrenheit and Kelvin! '))  
conversion = Convert(Number)

conversion.convertMe()
    