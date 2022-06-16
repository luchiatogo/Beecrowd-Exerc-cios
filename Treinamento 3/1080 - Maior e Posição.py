leitura = 0
pos = 0
maiorn = 0
maiorpos = 0
prevnum = 0
while leitura <=99:
        num = int(input())
        leitura +=1
        pos +=1
        if num > maiorn:
                maiorn = num
                maiorpos = pos
        prevnum = num

print(maiorn)
print(maiorpos)
