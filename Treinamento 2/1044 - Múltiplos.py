A, B = input().split()
A = int(A)
B = int(B)

if B > A:
    BA = B % A
    if BA == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
if B < A:
    AB = A % B
    if AB == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
