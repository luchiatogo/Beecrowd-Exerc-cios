n1 = int(input())
n2 = int (input())

ctrl = n1
soma = 0

if ctrl % 2 == 1:
    ctrl -= 2

else:
    ctrl -= 1

while ctrl > n2:
    soma += ctrl
    ctrl -=2

    
print(soma)
