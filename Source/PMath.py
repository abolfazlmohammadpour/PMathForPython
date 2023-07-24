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


def Calculating_GCD(*Arguments) -> int:
    """This Function Calculates Greatest Common Devisor Of Input Arguments"""
    DivisorsOfArguments = dict()
    CommonDivisorsOfArgument = set()
    GCD = int()
    # Calculating Divisors Of Arguments
    for Argument in Arguments:
        DivisorsOfArguments[Argument] = set(Calculating_Divisors(Argument))
    # Calculating Common Divisors Of Arguments
    CommonDivisorsOfArgument = DivisorsOfArguments[Arguments[0]]
    for Argument in Arguments:
        CommonDivisorsOfArgument &= DivisorsOfArguments[Argument]
    # Calculating Greates Common Divisors Of Arguments
    GCD = max(CommonDivisorsOfArgument)
    return GCD
