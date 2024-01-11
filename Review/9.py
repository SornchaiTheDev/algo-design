def max_dot_product(A, B):
  n = len(A)
  B.sort(reverse=True) 
  dp = [float('-inf')] * n

  for i in range(n):
    for j in range(n):
      dp[i] = max(dp[i], A[i] * B[j])

  return max(dp)
