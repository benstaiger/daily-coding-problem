
# This problem was asked by PayPal.
# 
# Given a string and a number of lines k, print the string in zigzag form. In
# zigzag, characters are printed out diagonally from top left to bottom right
# until reaching the kth line, then back up to top right, and so on.
# 
# For example, given the sentence "thisisazigzag" and k = 4, you should print:
# t     a     g
#  h   s z   a
#   i i   i z
#    s     g


def zigzag(word, lines):
    def next_line(current_line, direction, num_lines):
        current_line += direction
        if current_line >= num_lines:
            current_line = num_lines - 2
            direction = -1
        elif current_line < 0:
            current_line = 1
            direction = 1
        return current_line, direction
            
    line = [[] for _ in range(lines)]
    line_counter = 0
    line_dir = 1 if lines > 1 else 0
    for i, v in enumerate(word):
        line[line_counter].extend([" "]*(i - len(line[line_counter])))
        line[line_counter].append(v)
        line_counter, line_dir = next_line(line_counter, line_dir, lines)
    
    for i in range(lines):
        print("".join(line[i]))


zigzag("thisisazigzag", 4)
zigzag("thisisazigzag", 2)
