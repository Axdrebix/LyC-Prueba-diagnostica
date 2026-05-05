import time

def generar_coeficientes(n):
    # En Python, las listas son estructuras de memoria dinámica nativas
    coefs = [0] * (n + 1)
    coefs[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            coefs[j] = coefs[j] + coefs[j - 1]
    return coefs

def mostrar_polinomio(coefs, n):
    terminos = []
    for i in range(n + 1):
        potencia = n - i
        if coefs[i] != 0:
            termino = f"{coefs[i]}"
            if potencia > 0:
                termino += f"x^{potencia}"
            terminos.append(termino)
    
    print(f"Polinomio f(x) = {' + '.join(terminos)}")

def calcular_por_pasos(coefs, n, x):
    print(f"\nCalculando f({x}) paso a paso:")
    resultado_total = 0
    
    for i in range(n + 1):
        potencia = n - i
        valor_x = x ** potencia
        termino = coefs[i] * valor_x
        resultado_total += termino
        
        print(f"Paso {i + 1} -> Coeficiente: {coefs[i]} | x^{potencia} = {valor_x} | Valor del término = {termino}")
        
    print(f"\nResultado final f({x}) = {resultado_total}")

if __name__ == "__main__":
    print("--- EVALUACION INTERACTIVA ---")
    n = int(input("Ingrese el grado del polinomio (n): "))
    x = float(input("Ingrese el valor de x: "))
    
    coefs_usuario = generar_coeficientes(n)
    mostrar_polinomio(coefs_usuario, n)
    calcular_por_pasos(coefs_usuario, n, x)
    
    print("\n--- PRUEBA DE RENDIMIENTO PARA n=100 ---")
    
    inicio = time.perf_counter()
    coefs_100 = generar_coeficientes(100)
    fin = time.perf_counter()
    
    tiempo_ejecucion_ms = (fin - inicio) * 1000
    
    # Escribir en archivo txt (haciendo append)
    with open("tiempos_ejecucion.txt", "a") as archivo:
        archivo.write(f"Python | Tiempo para n=100: {tiempo_ejecucion_ms:.6f} milisegundos.\n")
        
    print(f"Tiempo registrado en 'tiempos_ejecucion.txt': {tiempo_ejecucion_ms:.6f} ms.")