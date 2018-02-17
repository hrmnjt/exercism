def is_leap_year(year):
    try:
        if (year % 100 == 0):
            if (year % 400 ==0):
                return True
            else:
                return False
        else:
            if (year % 4 == 0):
                return True
            else:
                return False

    except ValueError as err:
        raise Exception("Incorrect number inserted, please try again\n Error:", err)
