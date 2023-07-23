def Calculating_Divisors(Number: int) -> tuple:
    """This Function Calculates Divisors Of <Number> Argument """
    Divisors = list()
    if (Number == 0):
        raise "The Input Argument Does Not Have To Be Zero"
    elif (Number > 0):
        for Counter in range(1, (Number + 1)):
            if ((Number % Counter) == 0):
                Divisors.append(Counter)
    elif (Number < 0):
        for Counter in range(1, ((-Number) + 1)):
            if ((Number % Counter) == 0):
                Divisors.append(Counter)

    return tuple(Divisors)
