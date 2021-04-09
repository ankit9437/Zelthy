
def string(X, Y, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
  
    dex = L[m][n]
  
    
    lcs = [0] * (dex+1)            # Create a character array to store the lcs string

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
  
        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs[dex-1] = X[i-1]
            i-=1
            j-=1
            dex-=1
  
        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
    lcs.pop()
    print(lcs)
  

X = input()       #Input 1st word
Y = input()       #Input 2nd word
m = len(X)        #Length of 1st word
n = len(Y)        #Length of 2nd word
string(X, Y, m, n)   #Calling the function