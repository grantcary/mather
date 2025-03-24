# breaking down an equation to its simplest form, two values and an operator
# operators have an order of operation

def tokenizer(expression):
    new_expresssion = []
    prev_is_num = None
    buffer = ''
    for e, char in enumerate(expression):
        if not char.isspace():
            char_is_num = char.isnumeric()
            if prev_is_num == None:
                if char_is_num:
                    prev_is_num = True
                else:
                    prev_is_num = False
            else:
                if prev_is_num != char_is_num:
                    if buffer.isnumeric():
                        new_expresssion.append(buffer)
                        prev_is_num = False
                    else:
                        new_expresssion.extend(list(buffer))
                        prev_is_num = True
                    buffer = ''
            buffer += char
    if buffer.isnumeric():
        new_expresssion.append(buffer)
    else:
        new_expresssion.extend(list(buffer))
    return new_expresssion


def old_tokenizer(expression):
    expression = expression.split()

    new_expression = []
    for e, char in enumerate(expression):
        if '(' in char and len(char) > 1:
            char_group = char.split('(')
            value = char_group[-1]
            delimiter_count = len(char_group[:-1])
            new_delimiters = ['('] * delimiter_count
            new_expression.extend(new_delimiters + [value])
        elif ')' in char and len(char) > 1:
            char_group = char.split(')')
            value = char_group[0]
            delimiter_count = len(char_group[1:])
            new_delimiters = [')'] * delimiter_count
            new_expression.extend([value] + new_delimiters)
        else:
            new_expression.append(char)    

    return new_expression