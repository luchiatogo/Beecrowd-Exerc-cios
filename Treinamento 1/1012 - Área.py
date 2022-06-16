a, b, c = input().split()
a=float(a)
b=float(b)
c=float(c)
tria=a*c/2
circ=3.14159*c**2
quad=b**2
ret=a*b
trap=(a+b)*c/2
print(f'TRIANGULO: {tria:.3f}')
print(f'CIRCULO: {circ:.3f}')
print(f'TRAPEZIO: {trap:.3f}')
print(f'QUADRADO: {quad:.3f}')
print(f'RETANGULO: {ret:.3f}')
