class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        line = []
        line_length = 0

        i = 0
        while i < len(words):
            word = words[i]
            # Check if adding the next word exceeds maxWidth (including spaces)
            if line_length + len(word) + len(line) > maxWidth:
                # Distribute spaces
                spaces_needed = maxWidth - line_length
                if len(line) == 1:
                    # If only one word in the line, left justify
                    result.append(line[0] + " " * spaces_needed)
                else:
                    # Distribute spaces evenly
                    space_slots = len(line) - 1
                    space_width, extra_spaces = divmod(spaces_needed, space_slots)
                    justified_line = ""
                    for j in range(space_slots):
                        justified_line += line[j] + " " * (space_width + (1 if j < extra_spaces else 0))
                    justified_line += line[-1]  # Add the last word
                    result.append(justified_line)
                
                # Reset line
                line = []
                line_length = 0
            
            # Add the current word to the line
            line.append(word)
            line_length += len(word)
            i += 1

        # Process the last line (left justified)
        last_line = " ".join(line)
        last_line += " " * (maxWidth - len(last_line))
        result.append(last_line)

        return result
