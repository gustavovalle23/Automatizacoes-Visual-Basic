def contagemRegressiva(n):
    if n == 0:
        print('Decolar!')
    else:
        print(n)
        contagemRegressiva(n-1)
