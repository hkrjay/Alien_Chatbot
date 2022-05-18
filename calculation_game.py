
import random

def calgame():
    print("\tCALCULATION GAME \t".center(50,'*'))
    count=0
    l=['*','+','-','%']
    while True:
        a=random.randint(1,20)
        b=random.randint(1,20)
        random_cal=random.choice(l)
        print(a , random_cal , b , '=' ,end=' ')
        usr=int(input())
        if random_cal=='+':
            if a+b==usr:
                print("Right")
                count+=1
            else:
                print('\t:( Wrong :(')
                break
        elif random_cal=='-':
            if a-b==usr:
                print("Right")
                count+=1
            else:
                print('\t:( Wrong :(')
                break
        elif random_cal=='*':
            if a*b==usr:
                print("Right")
                count+=1
            else:
                print('\t:( Wrong :(')
                break
        elif random_cal=='%':
            if a%b==usr:
                print("Right")
                count+=1
            else:
                print('\t:( Wrong :(')
                break
    
    print('Total Score = ', count)
