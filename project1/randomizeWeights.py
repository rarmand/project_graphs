import random

def getNextWeight(mini,maxi):
  return int(random.uniform(mini,maxi))

def randomizeWeights(A,mini=1,maxi=10):
  N = len(A)
  for i in range(N):
    for j in range(i+1,N):
      if A[i][j] != float('inf'):
        A[i][j] = getNextWeight(mini,maxi)
      A[j][i] = A[i][j] # symmetrical A
  return A