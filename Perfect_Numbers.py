from datetime import datetime

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

def classify_another(number):
    """Classify a positive integer as perfect, abundant, or deficient.

    A perfect number equals the sum of its positive divisors (excluding itself).
    
    :param number: int - a positive integer
    :return: str - the classification of the input integer
    :raises ValueError: if the input is not a positive integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    # Find sum of proper divisors
    divisor_sum = 1  # Start with 1 as it is always a divisor
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisor_sum += i
            # If i is not the square root, add the pair divisor (number // i)
            if i != number // i:
                print(i)
                print(number // i)
                divisor_sum += number // i
    
    # Classify based on the sum of divisors
    if divisor_sum == number:
        return "perfect"
    elif divisor_sum > number:
        return "abundant"
    else:
        return "deficient"

time_n = datetime.now()
print(classify(33550336))
print(datetime.now()-time_n)
time_n = datetime.now()
print(classify_another(33550336))
print(datetime.now()-time_n)