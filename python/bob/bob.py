def response(hey_bob):
    """
    truth table
    is_shout    is_question     response
    0           0               "Whatever"
    0           1               "Sure"
    1           0               "Whoa"
    1           1               "Calm"
    """
    hey_bob = hey_bob.rstrip()
    
    if not hey_bob:
        return("Fine. Be that way!")
    
    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith("?")
    
    if is_shout:
        if is_question:
            return("Calm down, I know what I'm doing!")
        else:
            return("Whoa, chill out!")
    elif is_question:
        return("Sure.")
    else:
        return("Whatever.")
