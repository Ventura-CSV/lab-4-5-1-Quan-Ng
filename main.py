import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    import random  
    
    list = []
   
    numbers_random = 5
    
    count = 0
    
    count += 1
    
    while  count < numbers_random:
        numbers = random.randint(1,100)
        
        list.append(numbers)
        print(f'The random values are {numbers}')

total = sum(list)
    
print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
