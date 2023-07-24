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


def Calculating_GCD(Arguments: list) -> int:
    """This Function Calculates Greatest Common Devisor Of Input Arguments"""
    DivisorsOfArguments = dict()
    CommonDivisorsOfArguments = set()
    GCD = int()
    # Calculating Divisors Of Arguments
    for Argument in Arguments:
        DivisorsOfArguments[Argument] = set(Calculating_Divisors(Argument))
    # Calculating Common Divisors Of Arguments
    CommonDivisorsOfArguments = DivisorsOfArguments[Arguments[0]]
    for Argument in Arguments:
        CommonDivisorsOfArguments &= DivisorsOfArguments[Argument]
    # Calculating Greates Common Divisors Of Arguments
    CommonDivisorsOfArguments = list(CommonDivisorsOfArguments)
    if (len(CommonDivisorsOfArguments) > 0):
        GCD = CommonDivisorsOfArguments[0]
    for CommonDivisorOfArgument in CommonDivisorsOfArguments:
        if (CommonDivisorOfArgument > GCD):
            GCD = CommonDivisorOfArgument

    return GCD


def Calculating_LCM(From: int, To: int, Arguments: list) -> int:
    """This Function Calculates Least Common Multiple Of Input Arguments From <From> Argument To <To> Argument"""
    MultiplesOfArguments = dict()
    CommonMultiplesOfArguments = set()
    LCM = int()
    # Calculating Multiples Of Arguments
    for Argument in Arguments:
        MultiplesOfArguments[Argument] = set(
            Calculating_Multiples(Argument, From, To))
    # Calculating Common Multiples Of Arguments
    CommonMultiplesOfArguments = MultiplesOfArguments[Arguments[0]]
    for Argument in Arguments:
        CommonMultiplesOfArguments &= MultiplesOfArguments[Argument]
    # Calculating Least Common Multiples Of Arguments
    LCM = min(CommonMultiplesOfArguments)
    return LCM
