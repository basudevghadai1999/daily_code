"""
    Parses the given expression using the specified delimiters and returns a dictionary containing the numbers, operators, variables, and parentheses in the expression.
    :param expression: The expression to be parsed
    :param delimiters: The delimiters used to parse the expression
    :return: A dictionary containing the parsed components of the expression
    """

def parse_expression(expression, delimiters):
    result = {
        "number": [],
        "operator": [],
        "variable": [],
        "parenthesis": [],
    }
    i = 0
    open_parentheses = []
    inside_parentheses = set()
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
                result["number"].append(num)
            elif expression[i] in delimiters:
                if expression[i] == '(':
                    open_parentheses.append(i)
                    i += 1
                elif expression[i] == ')':
                    if not open_parentheses:
                        raise ValueError(f"Unmatched closing parenthesis at index {i}")
                    start = open_parentheses.pop()
                    inside_parentheses.update(range(start + 1, i))
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
                result["variable"].append(var)
            else:
                i += 1

        if open_parentheses:
            raise ValueError(f"Unclosed parenthesis at index {open_parentheses.pop()}")
    except ValueError as e:
        print(e)
        return None

    return result

# Example usage
data = "-59.8*4(a+c1)/2+(4.7)-9**(e_10)-f-5()"
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
#                 result["number"].append(num)
#             elif expression[i] in delimiters:
#                 if expression[i] == '(':
#                     open_parentheses.append(i)
#                     i += 1
#                 elif expression[i] == ')':
#                     if not open_parentheses:
#                         raise ValueError(f"Unmatched closing parenthesis at index {i}")
#                     start = open_parentheses.pop()
#                     result["parenthesis"].append(expression[start:i+1])
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
#                 result["variable"].append(var)
#             else:
#                 i += 1

#         if open_parentheses:
#             raise ValueError(f"Unclosed parenthesis at index {open_parentheses.pop()}")
#     except ValueError as e:
#         print(e)
#         return None

#     return result

# # Example usage
# data = "-59.8*4(a+c1)/2+(4.7)-9**(e_10)-f-5"
# delimiters = ['+', '-', '*', '/', '(', ')']
# tokens = parse_expression(data, delimiters)

# if tokens is not None:
#     print(tokens)


















# def parse_expression(expression, delimiters):
#     result = {
#         "number": [],
#         "operator": [],
#         "variable": [],
#         "parenthesis": [],
#     }
#     i = 0
#     open_parentheses = []
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
#                 result["number"].append(num)
#             elif expression[i] in delimiters:
#                 if expression[i] == '(':
#                     start = i
#                     count = 1
#                     i += 1
#                     while i < len(expression) and count > 0:
#                         if expression[i] == '(':
#                             count += 1
#                         elif expression[i] == ')':
#                             count -= 1
#                         i += 1
#                     if count > 0:
#                         raise ValueError(f"Unclosed parenthesis at index {start}")
#                     result["parenthesis"].append(expression[start:i])
#                 elif expression[i:i+2] == '**':	
#                     result["operator"].append('**')
#                     i +=2
#                 else:
#                     result["operator"].append(expression[i])
#                     i += 1
#             elif expression[i].isalpha() or expression[i] == '_':
#                 var = ""
#                 while i < len(expression) and (expression[i].isalnum() or expression[i] == '_'):
#                     var += expression[i]
#                     i += 1
#                 result["variable"].append(var)
#             else:
#                 i += 1

#         if open_parentheses:
#             raise ValueError(f"Unclosed parenthesis at index {open_parentheses[0]}")
#     except ValueError as e:
#         print(e)
#         return None

#     return result

# # Example usage
# data = "-59.8*4(a+c1)/2+(4.7))-9**(e_10)-f-5"
# delimiters = ['+', '-', '*', '/', '(', ')']
# tokens = parse_expression(data, delimiters)

# if tokens is not None:
#     print(tokens)









# def parse_expression(expression, delimiters):
#     result = {
#         "number": [],
#         "operator": [],
#         "variable": [],
#         "parenthesis": [],
#     }
#     i = 0
#     open_parentheses = []
#     try:
#         while i < len(expression):
#             if expression[i] in delimiters:
#                 if expression[i] == '(':
#                     start = i
#                     count = 1
#                     i += 1
#                     while i < len(expression) and count > 0:
#                         if expression[i] == '(':
#                             count += 1
#                         elif expression[i] == ')':
#                             count -= 1
#                         i += 1
#                     if count > 0:
#                         raise ValueError(f"Unclosed parenthesis at index {start}")
#                     result["parenthesis"].append(expression[start:i])
#                 else:
#                     result["operator"].append(expression[i])
#                     i += 1
#             elif expression[i].isdigit() or (expression[i] == '-' and (i == 0 or expression[i - 1] in delimiters)):
#                 # Check if it's a negative number
#                 num = ""
#                 num += expression[i]  # Include the '-'
#                 i += 1
#                 while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
#                     num += expression[i]
#                     i += 1
#                 result["number"].append(num)
#             elif expression[i].isalpha() or expression[i] == '_':
#                 var = ""
#                 while i < len(expression) and (expression[i].isalnum() or expression[i] == '_'):
#                     var += expression[i]
#                     i += 1
#                 result["variable"].append(var)
#             else:
#                 i += 1

#         if open_parentheses:
#             raise ValueError(f"Unclosed parenthesis at index {open_parentheses[0]}")
#     except ValueError as e:
#         print(e)
#         return None

#     return result

# # Example usage
# data = "-59.8+*4((a+c1)/-+2+(4.7))+--9**e_10-f--5"
# delimiters = ['+', '-', '*', '/', '(', ')']
# tokens = parse_expression(data, delimiters)

# if tokens is not None:
#     print(tokens)









# def parse_expression(expression, delimiters):
#     result = {
#         "number": [],
#         "operator": [],
#         "variable": [],
#         "parenthesis": [],
#     }
#     i = 0
#     open_parentheses = []
#     while i < len(expression):
#         if expression[i] in delimiters:
#             if expression[i] == '(':
#                 start = i
#                 count = 1
#                 i += 1
#                 while i < len(expression) and count > 0:
#                     if expression[i] == '(':
#                         count += 1
#                     elif expression[i] == ')':
#                         count -= 1
#                     i += 1
#                 if count > 0:
#                     raise ValueError(f"Unclosed parenthesis at index {start}")
#                 result["parenthesis"].append(expression[start:i])
#             else:
#                 result["operator"].append(expression[i])
#                 i += 1
#         elif expression[i].isdigit() or (expression[i] == '-' and i + 1 < len(expression) and expression[i + 1].isdigit()):
#             # Negative number logic
#             num = ""
#             while i < len(expression) and (expression[i].isdigit() or expression[i] == '.' or (expression[i] == '-' and not num)):
#                 num += expression[i]
#                 i += 1
#             result["number"].append(num)
#         elif expression[i].isalpha() or expression[i] == '_':
#             var = ""
#             while i < len(expression) and (expression[i].isalnum() or expression[i] == '_'):
#                 var += expression[i]
#                 i += 1
#             result["variable"].append(var)
#         else:
#             i += 1

#     if open_parentheses:
#         raise ValueError(f"Unclosed parenthesis at index {open_parentheses[0]}")

#     return result

# # Example usage
# data = "-59.8+*4((a+c1)/+2+(4.7))-9**e_10-f--5"
# delimiters = ['+', '-', '*', '/', '(', ')']
# tokens = parse_expression(data, delimiters)

# if tokens is not None:
#     print(tokens)







# def parse_expression(expression, delimiters):
#     result = {
#         "number": [],
#         "operator": [],
#         "variable": [],
#         "parenthesis": [],
#     }
#     i = 0
#     while i < len(expression):
#         if expression[i] in delimiters:
#             if expression[i] == '(':
#                 start = i
#                 count = 1
#                 i += 1
#                 while i < len(expression) and count > 0:
#                     if expression[i] == '(':
#                         count += 1
#                     elif expression[i] == ')':
#                         count -= 1
#                     i += 1
#                 result["parenthesis"].append(expression[start:i])
#             else:
#                 if expression[i] == '-' and (i == 0 or (i > 0 and expression[i - 1] in delimiters)):
#                     num = "-"
#                     i += 1
#                     while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
#                         num += expression[i]
#                         i += 1
#                     result["number"].append(num)
#                 else:
#                     result["operator"].append(expression[i])
#                     i += 1
#         elif expression[i].isdigit():
#             num = ""
#             while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
#                 num += expression[i]
#                 i += 1
#             result["number"].append(num)
#         elif expression[i].isalpha() or expression[i] == '_':
#             var = ""
#             while i < len(expression) and (expression[i].isalnum() or expression[i] == '_'):
#                 var += expression[i]
#                 i += 1
#             result["variable"].append(var)
#         else:
#             i += 1

#     return result

# # Example usage
# data = "-59.8+*4((a+c1)/-+2+(4.7))+-9**e_10-f--5"
# delimiters = ['+', '-', '*', '/', '(', ')']
# tokens = parse_expression(data, delimiters)

# print(tokens)



