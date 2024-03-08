def convert(number):
    """
    an inferior approach - very verbose

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
    """

    result = ""

    if number % 3 == 0: result += "Pling"
    if number % 5 == 0: result += "Plang"
    if number % 7 == 0: result += "Plong"

    return result if result else str(number)

    """
    "dig deeper" section suggests below. Benefit, need to play with dict to 
    change/add more conditions.

    def convert(number):

    sounds = {3: 'Pling',
              5: 'Plang', 
              7: 'Plong'}

    results = ''.join(sounds[divisor] for 
                      divisor in sounds.keys()
                      if number % divisor == 0)

    return results or str(number)
    """