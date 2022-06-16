A,B,C,D = input().split()
A = float (A)
B = float (B)
C = float (C)
D = float (D)
 
media = (A*2+B*3+C*4+D*1)/10

if media >= 7:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
    ex = 0
elif media <5:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
    ex = 0
else:
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    ex = 1

if ex == 1:
    rec = float(input())
    print(f'Nota do exame: {rec:.1f}')
    mex = (rec + media)/2
    if mex >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {mex:.1f}')
    else:
        print('Aluno reprovado')
        print(f'Media final: {mex:.1f}')
