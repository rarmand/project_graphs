def chooseMiniMax(Matrix):
  N = len(Matrix)
  vertex = 0
  minimax = float('inf')
  for i in range(N):
    v_minimax = 0
    for j in range(N):
      if Matrix[i][j] > v_minimax:
        v_minimax = Matrix[i][j]
    if v_minimax < minimax:
      minimax = v_minimax
      vertex = i
  return (vertex, minimax)

def chooseCenter(Matrix):
  N = len(Matrix)
  vertex = 0
  suma = float('inf')
  for i in range(N):
    v_suma = 0
    for j in range(N):
      v_suma += Matrix[i][j]
    if v_suma < suma:
      suma = v_suma
      vertex = i
  return (vertex, suma)
