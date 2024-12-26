class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Count character frequencies manually
        dict1 = {}  # Initializing an empty dictionary to store frequencies
        for c in s:  # Iterating over each character in the string "tree"
            if c in dict1:
                dict1[c] += 1  # If the character is already in dict1, increment its count
            else:
                dict1[c] = 1  # If the character is not in dict1, add it with a count of 1

        # Process for the string "tree":
        # - 't' is not in dict1, so dict1 = {'t': 1}
        # - 'r' is not in dict1, so dict1 = {'t': 1, 'r': 1}
        # - 'e' is not in dict1, so dict1 = {'t': 1, 'r': 1, 'e': 1}
        # - 'e' is already in dict1, so dict1 = {'t': 1, 'r': 1, 'e': 2}

        # Step 2: Convert frequency dictionary to a list of tuples
        freq_list = []  # Initialize an empty list to store (char, frequency) tuples
        for key in dict1:  # Iterate through the dictionary keys (characters)
            freq_list.append((key, dict1[key]))  # Append (character, frequency) to the list

        # After this step:
        # freq_list = [('t', 1), ('r', 1), ('e', 2)]

        # Step 3: Sort the list manually by frequency in descending order
        for i in range(len(freq_list)):  # Outer loop to iterate over each element in freq_list
            for j in range(i + 1, len(freq_list)):  # Inner loop to compare elements after index i
                if freq_list[i][1] < freq_list[j][1]:  # Compare frequencies (second element of tuple)
                    freq_list[i], freq_list[j] = freq_list[j], freq_list[i]  # Swap if needed

        # Sorting step explanation:
        # Initial freq_list = [('t', 1), ('r', 1), ('e', 2)]
        # Compare 't' and 'r' (both have frequency 1), no swap needed.
        # Compare 't' and 'e' (frequency 1 vs 2), swap them: freq_list = [('e', 2), ('r', 1), ('t', 1)]
        # No more swaps needed since 'r' and 't' have equal frequency.
        
        # Step 4: Build the result string
        result = ""  # Initialize an empty string to build the final result
        for char, count in freq_list:  # Iterate over the sorted list of (char, frequency) tuples
            result += char * count  # Repeat the character `count` times and append to the result

        # Final result after constructing the string:
        # - 'e' * 2 = "ee"
        # - 't' * 1 = "t"
        # - 'r' * 1 = "r"
        # So the final result is "eetr".

        return result  # Return the sorted string


sol = Solution()
print(sol.frequencySort("tree"))  # Output: "eert" or "eetr" (depending on sort stability)
print(sol.frequencySort("cccaaa"))  # Output: "aaaccc" or "cccaaa"
print(sol.frequencySort("Aabb"))  # Output: "bbaA" or "bbAa"