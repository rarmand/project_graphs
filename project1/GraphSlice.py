def GraphSlice(A, vers):
  return [[ A[i][j]  for j,x in enumerate(row)  if (j in vers)]
                     for i,row in enumerate(A)  if (i in vers)]