valor = int(input())

ctrl = 2

while ctrl <= valor:
    qdr = ctrl ** 2
    if valor % 2 == 1:
        print(f'{ctrl}^2 = {qdr}')
        ctrl += 1
    else:
        print(f'{ctrl}^2 = {qdr}')
        ctrl += 2
