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


def Calculating_Multiples(Number: int, From: int, To: int) -> tuple:
    """This Function Calculates Multiples Of <Number> Argument From <From> Argument To <To Argument>"""
    Multiples = list()
    if (Number == 0):
        raise "The Input Argument Does Not Have To Be Zero"
    elif (Number > 0):
        if (From > To):
            raise "The <From> Argument Does Not Have To Be Greater Than <To> Argument"
        else:
            for Counter in range(From, (To + 1)):
                Multiples.append((Number * Counter))
    elif (Number < 0):
        if (From > To):
            raise "The <From> Argument Does Not Have To Be Greater Than <To> Argument"
        else:
            for Counter in range(From, (To + 1)):
                Multiples.append((Number * Counter))

    return tuple(Multiples)
