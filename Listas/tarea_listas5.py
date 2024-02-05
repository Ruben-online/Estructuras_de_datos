# Reducir una cadena de letras o numeros en funcion de sus repeticiones

def compress_string(string):
    result = ""

    if not string:
        return result


    current_char = string[0]
    current_count = 1


    for char in string[1:]:
        if char == current_char:

            current_count += 1
        else:

            result += current_char + str(current_count)


            current_char = char
            current_count = 1


    result += current_char + str(current_count)

    return result



original_string = "aaabbccccdd"
compressed_string = compress_string(original_string)
print(compressed_string)