#some features is added

def parse_expression(expression, delimiters):
    result = {
        "number": [],
        "operator": [],
        "variable": [],
        "parenthesis": [],
    }
    i = 0
    open_parentheses = []
    errors = []
    try:
        while i < len(expression):
            if expression[i].isdigit() or (expression[i] == '-' and i + 1 < len(expression) and expression[i + 1].isdigit()):
                # Number logic including negative numbers
                num = ""
                if expression[i] == '-':
                    num += expression[i]
                    i += 1
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                if not open_parentheses or open_parentheses[-1] not in range(i):
                    result["number"].append(num)
            elif expression[i] in delimiters:
                if expression[i] == '(':
                    open_parentheses.append(i)
                    i += 1
                elif expression[i] == ')':
                    if not open_parentheses:
                        errors.append(f"Unmatched closing parenthesis at index {i}")
                    else:
                        start = open_parentheses.pop()
                        if not open_parentheses:  # If no open parenthesis inside
                            result["parenthesis"].append(expression[start:i+1])
                    i += 1
                elif expression[i:i+2] == '**':
                    result["operator"].append('**')
                    i += 2
                else:
                    result["operator"].append(expression[i])
                    i += 1
            elif expression[i].isalpha() or expression[i] == '_':
                var = ""
                while i < len(expression) and (expression[i].isalnum() or expression[i] == '_'):
                    var += expression[i]
                    i += 1
                if not open_parentheses or open_parentheses[-1] not in range(i):
                    result["variable"].append(var)
            elif expression[i] not in delimiters and not expression[i].isspace():
                errors.append(f"Invalid character '{expression[i]}' at index {i}")
                i += 1
            else:
                i += 1

        if open_parentheses:
            for index in open_parentheses:
                errors.append(f"Unclosed parenthesis at index {index}")
    except ValueError as e:
        errors.append(str(e))

    if errors:
        for error in errors:
            print(error)
        return None

    return result

# Example usage
data = "item*10.5-(5-3(34-5)+(item2-2)**10-55+10)"
delimiters = ['+', '-', '*', '/', '(', ')']
tokens = parse_expression(data, delimiters)

if tokens is not None:
    print(tokens)




# def parse_expression(expression, delimiters):
#     result = {
#         "number": [],
#         "operator": [],
#         "variable": [],
#         "parenthesis": [],
#     }
#     i = 0
#     open_parentheses = []
#     close_parentheses = []
#     errors = []
#     try:
#         while i < len(expression):
#             if expression[i].isdigit() or (expression[i] == '-' and i + 1 < len(expression) and expression[i + 1].isdigit()):
#                 # Number logic including negative numbers
#                 num = ""
#                 if expression[i] == '-':
#                     num += expression[i]
#                     i += 1
#                 while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
#                     num += expression[i]
#                     i += 1
#                 if not open_parentheses or i - 1 not in range(open_parentheses[-1] + 1, len(expression)):
#                     result["number"].append(num)
#             elif expression[i] in delimiters:
#                 if expression[i] == '(':
#                     open_parentheses.append(i)
#                     i += 1
#                 elif expression[i] == ')':
#                     if not open_parentheses:
#                         errors.append(f"Unmatched closing parenthesis at index {i}")
#                     else:
#                         start = open_parentheses.pop()
#                         result["parenthesis"].append(expression[start:i+1])
#                     i += 1
#                 elif expression[i:i+2] == '**':
#                     result["operator"].append('**')
#                     i += 2
#                 else:
#                     result["operator"].append(expression[i])
#                     i += 1
#             elif expression[i].isalpha() or expression[i] == '_':
#                 var = ""
#                 while i < len(expression) and (expression[i].isalnum() or expression[i] == '_'):
#                     var += expression[i]
#                     i += 1
#                 if not open_parentheses or i - 1 not in range(open_parentheses[-1] + 1, len(expression)):
#                     result["variable"].append(var)
#             elif expression[i] not in delimiters and not expression[i].isspace():
#                 errors.append(f"Invalid character '{expression[i]}' at index {i}")
#                 i += 1
#             else:
#                 i += 1

#         if open_parentheses:
#             for index in open_parentheses:
#                 errors.append(f"Unclosed parenthesis at index {index}")
#         if close_parentheses:
#             for index in close_parentheses:
#                 errors.append(f"Unmatched closing parenthesis at index {index}")
#     except ValueError as e:
#         errors.append(str(e))

#     if errors:
#         for error in errors:
#             print(error)
#         return None

#     return result

# # Example usage
# data = "item*10.5-(5-3(34-5)+(item2-2))**10-55+10+"
# delimiters = ['+', '-', '*', '/', '(', ')']
# tokens = parse_expression(data, delimiters)

# if tokens is not None:
#     print(tokens)
