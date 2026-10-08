class operaciones:

    def sum_two_numbers(a: float, b: float) -> float:
        """Suma dos números y devuelve el resultado."""
        return a + b

    def subtract_two_numbers(a: float, b: float) -> float:
        """Resta el segundo número del primero y devuelve el resultado."""
        return a - b
    
    def multiply_two_numbers(a: float, b: float) -> float:
        """Multiplica dos números y devuelve el resultado."""
        return a * b

    def divide_two_numbers(a: float, b: float) -> float:
        """Divide el primer número entre el segundo."""
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b





