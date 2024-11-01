"""
This is my custom math package
"""


class BasicMath:
    """
    Basic Math Operations
    """

    def add(self, num1: int, num2: int) -> int:
        """This function calculates the sum of two numbers


        Args:
            :num1 (int): first number
            :num2 (int): secound number

        Returns:
            int: the sum of two numbers
        """
        return num1 + num2


bm = BasicMath()

print(bm.add.__doc__)
