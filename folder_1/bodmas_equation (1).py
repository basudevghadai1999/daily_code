# string = '-50.5*(a+(c1+b2)/2)/-4.7+9**e-))fe_10**b2+2+3+@$%))((a+b)'
# string = "-5.04*(4*7/2)*-2.45*(1+4)**2(a+b)+"
# string='5*(4*7/2)*(1+4)**2+((13+45)+2)'
# string = "item_price*0.05*@%$+item_price5(item_price2*(item_price3+item_price4))"
# string = "item_price*0.05+item_price5*(item_price2*(item_price3+item_price4))"
# string = "item_price*0.05*(item_price2*(item_price3+item_price4))"

string = "item_price2"


delimiters = "+-*/()"
expected_list = {
# "item_price":"10",
"item_price2":"20",
"item_price3":"30",
"item_price4":"40",
}
def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def split_string(string, values):
    tokens = []
    current_token = ''

    for char in string:
        if char in values:
            if current_token:
                tokens.append(current_token)
                current_token = ''
            #tokens.append(char)
        else:
            current_token += char

    if current_token:
        tokens.append(current_token)

    return tokens

def categorize(string, delimiters, expected_list):
    word = []
    result = []
    FLAG = False
    limiter = ""
    list_name=""
    paran_count = 0
    index_number = None
    value_list = []
    for num, char in enumerate(string):
        if FLAG==True and char not in limiter:
            if limiter in ")" and char == "(":
                paran_count+=1
            
            word.append(char)
            if num+1==len(string):
                print(f"word:{''.join(word)}")
                if "".join(word) in expected_list:
                    result.append(("".join(word), index_number))
                    value_list.append("".join(word))
                else:
                    result.append(("".join(word), index_number))
                    value_list.append("".join(word))
                print(f"word:{''.join(word)}")
            continue
        elif FLAG==True and char in limiter:
            if char in ")" and paran_count==1:
                word.append(char)
                print(f"word:{''.join(word)}")
                result.append(("".join(word), index_number))
                value_list.append("".join(word))
                word=[]
                limiter=""
                list_name=""
                FLAG=False
                paran_count=0
                continue
            elif char in ")" and paran_count>1:
                word.append(char)
                paran_count-=1
                if num+1==len(string):
                    print(f"word:{''.join(word)}")
                    result.append(("".join(word), index_number))
                    value_list.append("".join(word))
                continue

            print(f"word: {''.join(word)}")
            if "".join(word) in expected_list or list_name=="nums_list":
                result.append(("".join(word), index_number))
                value_list.append("".join(word))
                word=[]
                limiter=""
                listname=""
                FLAG=False
                paran_count=0
            else:
                result.append(("".join(word), index_number))
                value_list.append("".join(word))
                word=[]
                limiter=""
                listname=""
                FLAG=False
                paran_count=0

            if num+1==len(string):
                # print(f"word:{''.join(word)}")
                if "".join(word) in expected_list:
                    result.append(("".join(word), index_number))
                    value_list.append("".join(word))
                else:
                    result.append(("".join(word), index_number))
                    value_list.append("".join(word))
            word=[]
            limiter=""
            listname=""
            FLAG=False

        # start 
        if char in delimiters:
            # find negative numbers
            if char=="-" and string[num+1].isdigit():
                word.append(char)
                index_number=num
                limiter=delimiters
                list_name = "nums_list"
                FLAG=True
            # find paranthesis
            elif char in "(":
                word.append(char)
                index_number=num
                limiter=")"
                list_name = "parenthesis_list"
                FLAG=True
                paran_count+=1
            # find **
            elif char=="*" and string[num+1]=="*":
                word.append(char)
                index_number=num
                continue
            # find operators
            else:
                index_number=num
                word.append(char)
                if ''.join(word) not in ")":
                    result.append(("".join(word), index_number))
                    value_list.append("".join(word))
                else:
                    result.append(("".join(word), index_number))
                    value_list.append("".join(word))
                print(f"word: operator: {''.join(word)}, {result}")
                
                word=[]
                continue

        # find positive numbers
        elif char.isdigit():
            print("hi")
            index_number=num
            word.append(char)
            limiter=delimiters
            list_name = "nums_list"
            FLAG=True

        # find varibles
        else:
            index_number=num
            word.append(char)
            limiter=delimiters
            list_name = "variables_list"
            FLAG=True

        # push the word to tis category at the end of string length 
        if num+1==len(string):
            print(f"word:{''.join(word)}")
            if "".join(word) in expected_list or list_name=="nums_list":
                result.append(("".join(word), index_number))
                value_list.append("".join(word))
            else:
                result.append(("".join(word), index_number))
                value_list.append("".join(word))

            print(result)

    # print(f"result:{result}")
    return result, value_list

values, value_list = categorize(string, delimiters, expected_list)
print(f"The index output is: {values}")
# values = [('item_price', 0), ('*', 10), ('0.05', 11), ('*', 15), ('@%$', 16), ('+', 19), ('(item_price2*(item_price3+item_price4))', 20), ('+', 59), ('item_price5', 60), ('**', 72), ('item_price6', 73)]
def check_values(values, expected_list):
    operators = ["+","-","*","/","**","(",")"]
    validtity=None
    for value in values:
        if value in operators or is_numeric(value)==True or value in expected_list:
            continue
        elif value[0]=="(":
            sub_values = split_string(value,operators)
            for element in sub_values:
                if element in operators or is_numeric(element)==True or element in expected_list:
                    continue
                else:
                    print(f"value error: {element}")
                    validtity=element
                    break
            
        else:
            print(f"value error: {value}")
            validtity=value
            break


    if validtity==None:
        output_string = "".join(value_list)
        for key,value in expected_list.items():
            output_string= output_string.replace(key,value)

        print(f"replace string with number output: {output_string}")
        
        print(f"the result is: {eval(output_string)}")
        print(f"All Good")
    else:
        print(f"wrong input with value: {validtity}")

check_values(value_list, expected_list)