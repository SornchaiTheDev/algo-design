def sort_string(order, str1):

    order_map = {char: i for i, char in enumerate(order)}

    def key_func(char):
        position = order_map.get(char, len(order))
        if position == len(order):
            return (1, char)
        return (0, position)

    sorted_chars = sorted(str1, key=key_func)

    return "".join(sorted_chars)


order = "cbafg"
str1 = "abced"
sorted_str = sort_string(order, str1)
print(sorted_str)  # Output: cbad
