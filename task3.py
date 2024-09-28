def decode_msg(msg):
    core_msg = "".join([char for char in msg if char.isalpha() or char == " "])
    first_word, second_word = core_msg.split()
    first_word = first_word[::-1]
    second_word = second_word.replace('I', 'E').replace('O', 'U')
    return f"{first_word} {second_word}"

print(decode_msg("&&&**$gnirtS PLIO!!@1234 "))
