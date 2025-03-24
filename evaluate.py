def get_inside(tok_expr):
    inside = False
    i = 0
    while i < len(tok_expr):
        if tok_expr[i] == '(':
            j = i + 1
            while j < len(tok_expr):
                if tok_expr[j] == '(':
                    break
                elif tok_expr[j] == ')':
                    inside = True
                    break
                j += 1
        if inside == True:
            break
        i += 1
    return (i, j)


def resolve(v1, v2, op):
    if op == '+':
        v3 = v1 + v2
    elif op == '-':
        v3 = v1 - v2
    elif op == '*':
        v3 = v1 * v2
    elif op == '/':
        v3 = v1 / v2
    elif op == '^':
        v3 = v1 ** v2
    return v3


def order_of_operations(expr):
    operator_order = ['^', '*', '/', '+', '-']
    for op in operator_order:
        i = 1
        while i < len(expr):
            if expr[i] == op:
                v1, v2 = int(expr[i - 1]), int(expr[i + 1])
                v3 = resolve(v1, v2, op)
                expr = expr[:i - 1] + [v3] + expr[i + 2:]
                i = 1
            else:
                i += 2
    return expr


def evaluate(tok_expr):
    while '(' in tok_expr:
        i, j = get_inside(tok_expr)
        tok_group = tok_expr[i + 1:j]

        print(tok_group)
        v3 = order_of_operations(tok_group)
        
        tok_expr = tok_expr[:i] + v3 + tok_expr[j + 1:]
        print(tok_expr)

    result = order_of_operations(tok_expr)[0]
    return result
