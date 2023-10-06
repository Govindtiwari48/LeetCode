class Solution:
    def integerBreak(self, n: int) -> int:
        # Base cases: for n < 4, return n-1
        if n < 4:
            return n - 1

        # Calculate the number of times 3 can be multiplied
        num_of_threes = n // 3

        # Initialize the answer with the product of 3 raised to num_of_threes
        product_of_threes = 3 ** num_of_threes

        # Adjust the product based on the remainder when divided by 3
        if n % 3 == 1:
            # If remainder is 1, you can multiply by 4 instead of 3
            product_of_threes //= 3
            product_of_threes *= 4
        elif n % 3 == 2:
            # If remainder is 2, multiply by 2
            product_of_threes *= 2

        # Return the maximum product
        return product_of_threes