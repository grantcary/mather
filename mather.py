from parser import tokenizer
from evaluate import evaluate


if __name__ == "__main__":
    prompt = 'Math expression: '
    # expression = str(input(prompt))
    # expression = '5 + (((44 + 4 * 4) * (2 * 42 / 2)) + (4 * 5))'
    expression = '3 + 4 ^ 3 + 6 * 10'
    # expression = '3 + 4'
    tok_expr = tokenizer(expression)
    result = evaluate(tok_expr)
    print(result)