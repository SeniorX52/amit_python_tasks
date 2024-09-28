def decode_message(message):
    core_message=''.join(char for char in message if char.isalpha() or char == ' ')
    first_word,second_word=core_message.split()[0],core_message.split()[1]
    first_word=first_word[::-1]
    vowels = "AEIOUaeiou"
    second_word=''.join(char for char in second_word if vowels.count(char)!=1)
    return f"{first_word} {second_word}"

print(decode_message("###!!@mocleW EPGTQ!!!6789"))
