## Brute force (Time Limited Exceeded)

class Solution1(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def is_subseq(i, s):
            c1 = 0
            for char in s:
                if char == i[c1]:
                    c1 = c1 +1  # Move to the next character in the word
                if c1 == len(i):
                    return True    
   
        c = 0
        for i in words:
            if is_subseq(i, s):
                c = c + 1
        return c
    
    

## Hashmap + sliding (Accepted) 

import collections

class Solution2(object):
    def numMatchingSubseq(self, S, words):
        # Initialize a defaultdict to store lists of words grouped by their first character
        buckets = collections.defaultdict(list)
        
        # Group words by their first character
        for word in words:
            # Example: if words = ["a", "bb", "acd", "ace"]
            # After this step, buckets will be:
            # {'a': ['a', 'acd', 'ace'], 'b': ['bb']}
            buckets[word[0]].append(word)

        # Now, iterate through each character in S
        for c in S:
            # For example, S = "abcde", so we start with c = 'a', then 'b', 'c', etc.
            # Get the list of words that start with character 'c'
            bucket = buckets[c]
            # Delete the entry for 'c' as we are processing it now
            del buckets[c]
            
            # Process each word in the current bucket
            for word in bucket:
                # If the word is longer than 1 character, move the remaining part to the next bucket
                if len(word) > 1:
                    # For example, word = "acd", after processing 'a', we have "cd", so we place "cd" in the 'c' bucket
                    buckets[word[1]].append(word[1:])
                    # For word = "ace", after processing 'a', we place "ce" in the 'c' bucket
                    # The bucket now looks like {'c': ['cd', 'ce']}
        
        # After processing all characters in S, we'll have some words left in the buckets
        # These are words that have not been completely matched, meaning they are not subsequences of S
        mismatch_count = 0
        for c in buckets:
            # Add the number of words remaining in each bucket to mismatch_count
            mismatch_count += len(buckets[c])
            # Example: if buckets = {'c': ['cd', 'ce'], 'b': ['b']}
            # mismatch_count will be 3 (2 from 'c' and 1 from 'b')

        # Return the number of subsequences by subtracting the mismatch count from total words
        return len(words) - mismatch_count


# Input S = "abcde" words = ["a", "bb", "acd", "ace"] # Output: 3
# Explanation: "a", "acd", and "ace" are subsequences of "abcde"

# Input S = "dsahjpjauf" words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]  # Output: 2
# Explanation: "ahjpjau" and "ja" are subsequences of "dsahjpjauf"