# validador_fen.py
# Programa para validar notación FEN (Forsyth-Edwards Notation)

def validar_fen(cadena: str) -> bool:
    """
    Valida si una cadena corresponde a una notación FEN válida.
    Retorna True si es válida, False en caso contrario.
    """
    partes = cadena.strip().split()
    
    # Una FEN debe tener exactamente 6 partes separadas por espacio
    if len(partes) != 6:
        return False
    
    colocacion, turno, enroque, objetivo_peon, medio_movimiento, total_movimientos = partes
    
    # 1. Validar colocación de piezas (8 filas separadas por '/')
    filas = colocacion.split('/')
    if len(filas) != 8:
        return False
    
    for fila in filas:
        contador = 0
        for caracter in fila:
            if caracter.isdigit():
                contador += int(caracter)
            elif caracter in 'prnbqkPRNBQK':
                contador += 1
            else:
                return False  # Caracter inválido
        if contador != 8:
            return False  # Cada fila debe sumar 8 columnas
    
    # 2. Turno: debe ser 'w' (blancas) o 'b' (negras)
    if turno not in ('w', 'b'):
        return False
    
    # 3. Enroque: combinacion de KQkq o '-'
    if enroque == '-':
        pass
    else:
        if not all(c in 'KQkq' for c in enroque) or len(enroque) > 4 or len(set(enroque)) != len(enroque):
            return False
    
    # 4. Casilla de objetivo de peon al paso: formato letra+numero o '-'
    if objetivo_peon != '-':
        if len(objetivo_peon) != 2:
            return False
        letra, numero = objetivo_peon[0], objetivo_peon[1]
        if letra not in 'abcdefgh' or numero not in '12345678':
            return False
    
    # 5. Medio movimiento (contador de medias movidas desde último avance de peón o captura)
    if not medio_movimiento.isdigit():
        return False
    
    # 6. Número total de movimientos (debe ser entero positivo)
    if not total_movimientos.isdigit() or int(total_movimientos) < 1:
        return False
    
    return True


# ===== Ejemplo de uso interactivo =====
if __name__ == "__main__":
    print("=== Validador de notación FEN ===\n")
    cadena_prueba = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    print(f"Probando FEN inicial: {cadena_prueba}")
    print(f"Válida: {validar_fen(cadena_prueba)}\n")
    
    while True:
        entrada = input("Ingrese una cadena FEN (o 'salir' para terminar): ").strip()
        if entrada.lower() == 'salir':
            break
        if validar_fen(entrada):
            print("FEN valida.\n")
        else:
            print("FEN invalida.\n")
