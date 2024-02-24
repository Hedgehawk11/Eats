import easywebhooks
import sys as sus

# Dictionary for graphing user input
foods = ["steak","cake","burger","golden carrot"]
prices = {
  "64 steak": 1,
  "2 cakes": 1,
  "64 burgers": 3,
  "32 golden carrot": 1
}
running = True
while running:
  user = input('Enter your username: ')
  user = user.lower()
  if user == 'psych82':
      user = 'mike nelson'
  if user == 'hedgehawk11' or user == 'captainbanna19' or user == 'mike nelson' or user == 'fullwizard' or user == 'ashnelo' or user == 'nj256':
      print('Welcome, ' + user + '!')
      print('What would you like to buy?')
      print('We sell:')
      for i in list(prices.keys()):
          print(i)
      food = input()
      food = food.lower()
      if food in foods:
          print('How many sets/racks of ' + food + 's would you like to buy?')

          if food in foods:
              amount = input()
          else:
              print('Sorry, we do not sell that.')
              continue
          amount = int(amount)
          easywebhooks.send(user + ' bought ' + str(amount) + ' sets of ' + food + 's!')
          print('Would you like to buy anything else?')
          exit = input()
          exit.lower()

          if exit == "no" or exit == "n":
              running = False
          if exit == "yes" or exit == "y" or exit == "hungry" or exit == "plz":
              running = True
            
          answer = input()
          answer = answer.lower()
