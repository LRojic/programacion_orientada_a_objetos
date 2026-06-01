def esta_anidado(texto):

    stack = []

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for caracter in texto:

        # Si es apertura
        if caracter in "([{":
            stack.append(caracter)

        # Si es cierre
        else:

            # Si el stack está vacío -> error
            if len(stack) == 0:
                return 0

            tope = stack.pop()

            # Verifica si coincide
            if tope != pares[caracter]:
                return 0

    # Si quedó algo sin cerrar -> error
    if len(stack) != 0:
        return 0

    return 1


# =========================
# PRUEBAS
# =========================

print(esta_anidado("{[()]}"))   # 1
print(esta_anidado("([)]"))     # 0
print(esta_anidado("((()))"))   # 1
print(esta_anidado("{[(])}"))   # 0
print(esta_anidado(""))         # 1 