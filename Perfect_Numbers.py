def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    divisors = []
    for i in range(1, int(number/2)+1):
        if number%i==0:
            divisors.append(i)
    sum = 0
    for num in divisors:
        sum+=num
    print(sum)
    if number < sum:
        return "abundant"
    if number == sum:
        return "perfect"
    if number > sum:
        return "deficient"
    
classify(28)