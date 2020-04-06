def weight_on_planets():
   WeightOnEarth = float(input('What do you weigh on earth? '))
   WeightOnMars = WeightOnEarth * 0.38
   WeightOnJupiter = WeightOnEarth * 2.34
   print(('\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds.' % (WeightOnMars, WeightOnJupiter)))
   
   
if __name__ == '__main__':
   weight_on_planets()