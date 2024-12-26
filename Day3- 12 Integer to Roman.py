class Solution:
    def intToRoman(self, num) :
        # Roman numeral symbols and their values
        roman_symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I") ]
        
        result = ""
        
        # Process each symbol-value pair
        for value, symbol in roman_symbols:
            while num >= value:
                result = result + symbol
                num = num - value
        
        return result
    
sol = Solution()
print(sol.intToRoman(1987))  # Expected output: "MCMLXXXVII"
print(sol.intToRoman(2444))  # Expected output: "MMCDXLIV"