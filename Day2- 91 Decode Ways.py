class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize the decoding count for the base case (empty prefix).
        num_decode = [1]  

        # Convert the input string into a list of integers for easier processing.
        l = [int(x) for x in list(s)]  
        n = len(l)  # Get the length of the list.

        # If the first digit is '0', return 0 as decoding is impossible.
        if l[0] == 0:  
            return 0
        else:
            # Loop through the string from the second character onwards.
            for i in range(1, n):
                # Case 1: Current digit can form a valid two-digit number with the previous digit.
                if l[i] > 0 and (l[i-1] == 1 or (l[i-1] == 2 and l[i] < 7)):
                    if i > 1:
                        # Add the decoding count of the last two positions.
                        num_decode.append(num_decode[i-1] + num_decode[i-2])
                    else:
                        # For the first two digits, there are exactly 2 ways to decode.
                        num_decode.append(2)
                # Case 2: Current digit is '0' but forms a valid two-digit number (10 or 20).
                elif l[i] == 0 and (l[i-1] == 1 or l[i-1] == 2):
                    if i > 1:
                        # Use the decoding count from two positions back.
                        num_decode.append(num_decode[i-2])
                    else:
                        # Decode as a single valid two-digit number.
                        num_decode.append(1)
                # Case 3: Current digit is '0' but cannot form a valid two-digit number.
                elif l[i] == 0 and not (l[i-1] == 1 or l[i-1] == 2):
                    return 0
                # Default case: Only single-digit decoding is possible.
                else:
                    num_decode.append(num_decode[i-1])

            # Debugging output to show the decoding counts at each step.
            print(num_decode)

            # Return the total number of decoding ways for the full string.
            return num_decode[-1]


solution = Solution()
print("Output for '12':", solution.numDecodings("12"))  # Example 1: "12" -> "AB" or "L" # Expected output: 2
print("Output for '226':", solution.numDecodings("226"))  # Example 2: "226" -> "BBF", "BZ", "VF" # Expected output: 3
print("Output for '06':", solution.numDecodings("06"))  # Example 3: "06" -> No valid decoding # Expected output: 0
