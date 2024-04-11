def parse_expression(str1, index_number):

    #str1 is the given sting
    # index_number is the given index deafult 0

    len_str1 = len(str1)
    items = {
        "number": [],
        "operator": [],
        "variable": [],
        "parenthesis": []
    }

    while index_number < len_str1:
        char1 = str1[index_number]
        if char1.isdigit() or (char1=='-' and index_number+1 < len_str1 and str1[index_number + 1].isdigit()):
            # Number
            number = ""
            while index_number < len_str1 and (str1[index_number].isdigit() or str1[index_number] == '.' or (str1[index_number] == '-' and not number)):
                number += str1[index_number]
                index_number += 1
            items["number"].append(number)
        elif char1.isalpha() or char1 == '_':
            # Variable
            variable = ""
            while index_number < len_str1 and (str1[index_number].isalnum() or str1[index_number] == '_'):
                variable += str1[index_number]
                index_number += 1
            items["variable"].append(variable)
        elif char1 in ['*', '/', '+', '-', '**']:
            if char1 == '*' and index_number + 1 < len_str1 and str1[index_number + 1] == '*':
                # Power operator
                items["operator"].append('**')
                index_number += 2
            else:
                # Other operators
                items["operator"].append(char1)
                index_number += 1
        elif char1 == '(':
            # Start of Parenthesis
            parenthesis_count = 1
            index = index_number + 1
            while index < len_str1:
                if str1[index] == '(':
                    parenthesis_count += 1
                elif str1[index] == ')':
                    parenthesis_count -= 1
                    if parenthesis_count == 0:
                        break
                index += 1
            
            items["parenthesis"].append(str1[index_number:index+1])
            index_number = index + 1
        else:
            print(str1[index_number])
            index_number += 1
        # print("length",len_str1)

    return items, index_number

items,index_number = parse_expression("-59.8*4((a+c1)/2+(4.7))+--9**(e_10)-f-5", 0)

# print("1 number:", items["number"])
# print("2 operator:", items["operator"])
# print("3 variable:", items["variable"])
# print("4 parenthesis:", items["parenthesis"])
print(items)