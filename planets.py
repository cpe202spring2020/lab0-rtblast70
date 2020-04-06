def weight_on_planets():
   x = input('What do you weigh on earth? ')
   y = int(x)
   print('')
   print('On Mars you would weigh ' + y*0.38 + ' pounds.')
   print('On Jupiter you would weigh ' + y*2.34 + ' pounds.')
   #test
   
   
if __name__ == '__main__':
   weight_on_planets()