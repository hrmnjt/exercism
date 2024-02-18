def steps(number:int) -> int:
    steps:int = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    else:
        while number != 1:
            number = 3*number+1 if number % 2 else number // 2
            steps += 1
    return steps
