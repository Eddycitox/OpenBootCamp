'''Este programa pide al usuario su peso y estatura,
y luego calcula el índice de masa corporal (IMC) dividiendo el peso
 por la estatura al cuadrado. 
Finalmente, imprime el resultado redondeado a dos decimales.'''


peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

imc = peso / (estatura ** 2)

print(f"Tu índice de masa corporal es {imc:.2f}")
