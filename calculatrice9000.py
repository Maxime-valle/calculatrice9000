def calculate():
    try:
        num1 = float(input("Entrez le premier nombre: "))
        operator = input("Entrez l'opérateur (+, -, *, /): ")
        num2 = float(input("Entrez le deuxième nombre: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                raise ValueError("Erreur: Division par zéro")
        else:
            raise ValueError(f"Opérateur non supporté: {operator}")

        print(f"Résultat: {result}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Erreur inattendue:", e)

calculate()