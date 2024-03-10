import math

while True:
    print("\nChoose the math operation : \n\n 0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root \n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")
    
    oper = int(input("Your option from the menu: "))
    
    if oper == 0:#addition
        addition_val1 = float(input("\n First Value : "))
        addition_val2 = float(input(" Second Value : "))
        
        print("\n The result is : " + str(addition_val1 + addition_val2) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back.lower() == 'y':
            continue
        else:
            break
    elif oper == 1: #subtraction
        sub_val1 = float(input("\n First Value: "))
        sub_val2 = float(input("\n Second Value: "))
        
        print("\n The result is : " + str(sub_val1 - sub_val2) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back.lower() == 'y':
            continue
        else:
            break
        
    elif oper == 2: #multiplication
        mul_val1 = float(input("\n First Value: "))
        mul_val2 = float(input("\n Second Value: "))
        
        print("\n The result is : " + str(mul_val1 * mul_val2) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        
        if back.lower() == 'y':
            continue
        else:
            break
    
    elif oper == 3:#Division
        div_val1 = float(input("\n First Value: "))
        div_val2 = float(input("\n Second Value: "))
        
        print("\n The result is : " + str(div_val1 / div_val2) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back.lower() == 'y':
            continue
        else:
            break
        
    elif oper == 4:#Modulo
        mod_val1 = float(input("\n First Value: "))
        mod_val2 = float(input("\n Second Value: "))
        
        print("\n The result is : " + str(mod_val1 % mod_val2) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back.lower() == 'y':
            continue
        else:
            break
        
    elif oper == 5:#Raising to the Power
        pow_val1 = float(input("\n First Value: "))
        pow_val2 = float(input("\n Second Value: "))
        
        print("\n The result is : " + str(math.pow(pow_val1,pow_val2)) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back.lower() == 'y':
            continue
        else:
            break
        
    elif oper == 6:#Square root
        sqrt_val1 = float(input("\n Value: "))
       
        print("\n The result is : " + str(math.sqrt(sqrt_val1)) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back.lower() == 'y':
            continue
        else:
            break
        
    elif oper == 7:#Logarithm
        log_val1 = float(input("\nEnter the value for calculating the logarithm to base 2: "))
        
        print("\n The result is : " + str(math.log(log_val1, 2)) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back.lower() == 'y':
            continue
        else:
            break
    
    elif oper == 8:#Sine
        sin_val1 = float(input("\nEnter the value for (in degrees) for calculating the sine: "))
        
        print("\n The result is : " + str(math.sin(math.radians(sin_val1))) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back.lower() == 'y':
            continue
        else:
            break
        
    elif oper == 9:#Cosine
        cos_val1 = float(input("\nEnter the value for (in degrees) for calculating the cos: "))
        
        print("\n The result is : " + str(math.cos(math.radians(cos_val1))) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back.lower() == 'y':
            continue
        else:
            break
        
    elif oper == 10:#Tan
        tan_val1 = float(input("\nEnter the value for (in degrees) for calculating the tan: "))
        
        print("\n The result is : " + str(math.tan(math.radians(tan_val1))) + "\n")
        
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back.lower() == 'y':
            continue
        else:
            break
    
    else:
        print('Invalid option')
        continue 
 