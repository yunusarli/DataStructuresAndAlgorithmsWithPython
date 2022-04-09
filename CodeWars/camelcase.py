#convert the given string to camel case
#input => the_lower_case_input
#output => theLowerCaseInput



def to_camel_case(text):
    result = ""
    length = len(text)

    counter = 0

    if not text:
        return text

    while True:
        pointer = text[counter]
        if pointer in "_-":
            pointer = text[counter+1]
            result += pointer.upper()
            counter = counter + 2
        else:
            result += pointer
            counter += 1
        
        if length <= counter:
            break
    return result


print(to_camel_case("A-b-c"))