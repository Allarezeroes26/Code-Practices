import random
import string
import csv
import os

class Password:
  def __init__ (self, length, name):
    self.length = length
    self.name = name
  
  def generate(self):
    if self.length < 8:
      print("It is generally recommended to have a password length of up to 8 to 32 characters!")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(self.length))
    return password
      
  def writeCsv(self, passwordName, password):  
    with open('pwrd.csv', 'w', newline="", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerow(['Name', 'Password'])
      writer.writerow([passwordName, password])
    print('File successfully created')
    
  def appendCsv(self, passwordName, password):
    with open('pwrd.csv', 'a', newline='', encoding='utf-8') as f:
      writer = csv.writer(f)
      writer.writerow([passwordName, password])
    print('Successfully added Password!')
      
  def conditional(self, passwordName, password):
    if os.path.isfile('pwrd.csv'):
      with open('pwrd.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        
        if [passwordName, password] in rows[1:]:
          print('Password name and password already exists!')
        else:
          self.appendCsv(passwordName, password)
          print(f'Password Name: {passwordName} \nPassword: {password}')
    else:
      self.writeCsv(passwordName, password)
      print(f'Password Name: {passwordName} \n Password: {password}')

passwordName = input('Enter your password name: ')
print(f'Remember that the recommended password length is 8 to 32 characters')
passwordLength = int(input('Enter desired password Length!: '))

passwordMe = Password(passwordLength, passwordName)
passwordResult = passwordMe.generate()
passwordMe.conditional(passwordName, passwordResult)
