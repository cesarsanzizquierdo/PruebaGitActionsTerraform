from src.suma_resta import operaciones


def main():
    resultado_suma = operaciones.sum_two_numbers(10, 5)
    resultado_resta = operaciones.subtract_two_numbers(10, 5)
    resultado_multiplicacion=operaciones.multiply_two_numbers(5,10)

    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
    print(f"Multiplicacion: {resultado_multiplicacion}")


if __name__ == "__main__":
    main()