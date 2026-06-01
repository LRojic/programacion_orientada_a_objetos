def transfer(S, T):

    while len(S) > 0:
        T.append(S.pop())


S = [1, 2, 3, 4]
T = []

transfer(S, T)

print("S:", S)
print("T:", T)