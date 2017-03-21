def findAllShortestPaths(Matrix):
  N = len(Matrix)
  dist = Matrix[:] # copy distance matrix
  for k in range(N):
    for i in range(N):
      for j in range(N):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
  return dist

if __name__=='__main__':
  import PrintCosts
  m = [[0, 3, 10, float('inf')], [3, 0, 4, 10], [10, 4, 0, 14], [float('inf'), 10, 14, 0]]
  print("Original matrix:")
  PrintCosts.printCosts(m)
  d = findAllShortestPaths(m)
  print("Shortest distances:")
  printCosts(d)
