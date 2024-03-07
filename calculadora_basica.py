num1 = float(input("Primer numero:"))
num2 = float(input("Segundo numero: "))
sig = input("Signo: ")
solution = 0

if (sig == '+'):
    solution = num1 + num2
elif (sig == '-'):
    solution = num1 - num2
elif (sig == '*'):
    solution = num1 * num2
elif (sig == '**'):
    solution = num1 ** num2
elif (sig == '/'):
    solution = num1 / num2
elif (sig == '//'):
    solution = num1 // num2
elif (sig == '%'):
    solution = num1 % num2

print("Aqui tienes la solucion:", solution)
