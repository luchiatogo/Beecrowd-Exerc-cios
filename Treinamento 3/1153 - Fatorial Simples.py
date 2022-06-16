num = int(input())
fat = 1
ctrl = num
while ctrl > 0:
        ctrl -= 1
        fat += fat*(ctrl)
print(fat)
