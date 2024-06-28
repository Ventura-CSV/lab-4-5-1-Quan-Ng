import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    import random  
    
    list = []
    
    count = 0
    
    total = 0
    
    while  count <5:
        numbers = random.randint(1,100)
        
        list.append(numbers)
        
        print(f'The random values are {numbers}')
        
        total += numbers
        
        count += 1

    
    
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
