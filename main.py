from src.suma_resta import operaciones


def main():
    resultado_suma = operaciones.sum_two_numbers(10, 5)
    resultado_resta = operaciones.subtract_two_numbers(10, 5)

    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")


if __name__ == "__main__":
    main()