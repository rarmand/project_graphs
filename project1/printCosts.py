
def printCosts(Matrix): # zakladamy, ze brak polaczenia to po prostu wartosc 'inf'
  N = len(Matrix)
  for col in Matrix:
    for elem in col:
      if elem == float('inf'):
        print ' -',
      else:
	print "{:2d}".format(elem),
    print
