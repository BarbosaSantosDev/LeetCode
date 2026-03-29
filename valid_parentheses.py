

def valid_strings(input_str: str) -> bool:
    str_is_true = ["()", "[]", "{}"] 
    
    while any(x in input_str for x in str_is_true):
        for x in str_is_true:
            input_str = input_str.replace(x, "")
    return not input_str


if __name__ == "__main__":
    print(valid_strings("()"))
        
