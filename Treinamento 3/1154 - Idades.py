div=0
soma = 0 

while True:
        idade = int(input())
        div +=1
        soma += idade

        if idade < 0:
                soma -= idade
                div -=1 
                break

tot = soma/div
print(f'{tot:.2f}')
