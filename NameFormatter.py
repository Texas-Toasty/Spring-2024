def full_name(spaceless_name):
    result = spaceless_name[0]
    for i in range(1, len(spaceless_name)):
        char = spaceless_name[i]
        if char.isupper():
            result += " " + char
        else:
            result += char
    return result


def initials_obtain(spaceless_name):
    initials = ''
    i = 0
    while i < len(spaceless_name):
        if spaceless_name[i].isupper():
            initials += spaceless_name[i].upper()
            i += 1
            while i < len(spaceless_name) and spaceless_name[i].islower():
                i += 1
            if i < len(spaceless_name):
                initials += '.'
        else:
            i += 1
    return initials


spaceless_name = input("Enter your full name without spaces: ")
name_output = full_name(spaceless_name)
initials_output = initials_obtain(spaceless_name)
print("Welcome", name_output.strip() + "!", "Your trademark is", "'" + initials_output.strip() + "'.")
