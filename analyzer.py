import re

# Token types
TOKEN_INTEGER = 'INTEGER'
TOKEN_BOOLEAN = 'BOOLEAN'
TOKEN_OPERATOR = 'OPERATOR'
TOKEN_ASSIGNMENT = 'ASSIGNMENT'
TOKEN_KEYWORD_IF = 'IF'
TOKEN_KEYWORD_ELSE = 'ELSE'
TOKEN_KEYWORD_PRINT = 'PRINT'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_LITERAL_TRUE = 'TRUE'
TOKEN_LITERAL_FALSE = 'FALSE'
TOKEN_COMMENT = 'COMMENT'
TOKEN_UNKNOWN = 'UNKNOWN'

# Regular expressions for token patterns
INTEGER_PATTERN = r'\d+'
BOOLEAN_PATTERN = r'true|false'
OPERATOR_PATTERN = r'\+|\-|\*|\/|==|!='
ASSIGNMENT_PATTERN = r'='
KEYWORD_IF_PATTERN = r'if'
KEYWORD_ELSE_PATTERN = r'else'
KEYWORD_PRINT_PATTERN = r'print'
IDENTIFIER_PATTERN = r'[a-zA-Z][a-zA-Z0-9]*'
COMMENT_PATTERN = r'//.*'

# Token pattern mapping
TOKEN_PATTERNS = [
    (TOKEN_INTEGER, INTEGER_PATTERN),
    (TOKEN_BOOLEAN, BOOLEAN_PATTERN),
    (TOKEN_OPERATOR, OPERATOR_PATTERN),
    (TOKEN_ASSIGNMENT, ASSIGNMENT_PATTERN),
    (TOKEN_KEYWORD_IF, KEYWORD_IF_PATTERN),
    (TOKEN_KEYWORD_ELSE, KEYWORD_ELSE_PATTERN),
    (TOKEN_KEYWORD_PRINT, KEYWORD_PRINT_PATTERN),
    (TOKEN_IDENTIFIER, IDENTIFIER_PATTERN),
    (TOKEN_COMMENT, COMMENT_PATTERN)
]

class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

def tokenize(code):
    tokens = []
    code_lines = code.split('\n')
    for line_number, line in enumerate(code_lines):
        line = line.strip()
        while line:
            match = None
            for token_type, pattern in TOKEN_PATTERNS:
                regex = re.compile('^' + pattern)
                match = regex.match(line)
                if match:
                    lexeme = match.group(0)
                    line = line[len(lexeme):].strip()
                    if token_type != TOKEN_COMMENT:
                        tokens.append(Token(token_type, lexeme))
                    break
            if not match:
                tokens.append(Token(TOKEN_UNKNOWN, line))
                break
        # Add newline token
        tokens.append(Token(TOKEN_UNKNOWN, '\n'))
    return tokens

def main():
    filename = input("name of the text file that you want to test it on: ")
    try:
        with open(filename, 'r') as file:
            code = file.read()
            tokens = tokenize(code)
            for token in tokens:
                print(f'Type: {token.token_type}, Lexeme: {token.lexeme}')
    except FileNotFoundError:
        print("error")

if __name__ == "__main__":
    main()
