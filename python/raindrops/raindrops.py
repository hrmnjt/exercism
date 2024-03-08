def convert(number):
    mod_3 = number % 3
    mod_5 = number % 5
    mod_7 = number % 7
    if mod_3 != 0 and mod_5 != 0 and mod_7 !=0:
        return(str(number))
    else:
        result = ""
        if mod_3 == 0:
            result += "Pling"
        if mod_5 == 0:
            result +="Plang"
        if mod_7 == 0:
            result += "Plong"
        return(result)
