done3 = True
print()
print('  >>>>>>>>>>>>>>>>>>>>>  MATHS PERFECT ROOT CALCULATOR  <<<<<<<<<<<<<<<<<<<<<')
print()
print()
while done3 :
    done = True
    done2 = True
    answer = 1
    done4 = True
    radicand = int(input('>> Please enter Radicand : '))
    index = int(input('>> Please enter Index : '))
    print()
    while done and answer < radicand and radicand > 0 and index > 0 :
        if index == 1 :
            print('* Answer ------> 1st root of',radicand,'=',radicand)
            done = False
            done2 = False
        elif answer**index == radicand :
            print('* Answer ------> ',index,end='')
            if index == 2 :
                print('nd',end='')
            if index == 3 :
                print('rd',end='')
            if index > 3 :
                print('th',end='')
            print(' root of',radicand,'=',answer,end='')
            if index % 2 == 0 :
                print(',',answer * -1,sep='')
            else :
                print()
            done = False
            done2 = False
        else :
            answer = answer + 1
    if done2 and radicand > 0 and index > 0 :
        print('                         >>>>>> PERFECT ROOT NOT FOUND ! <<<<<<')
        print()
        print('                     ',index,end='')
        if index == 2 :
            print('nd',end='')
        if index == 3 :
            print('rd',end='')
        if index > 3:
            print('th',end='')
        print(' root of',radicand,'is not a counting number.')
    if radicand <= 0 or index <= 0 :
        print('                            >>>>>> Wrong Input ! <<<<<<')
    while done4 :
        print()
        userinput = input('>> Press C to Continue or Press E to Exit : ')
        if userinput == 'c' or userinput == 'C' :
            done4 = False
            print('-----------------------------------------------------------------------------')
            print()
        elif userinput == 'e' or userinput == 'E' :
            done4 = False
            done3 = False
        else :
            print()
            print('                            >>>>>> Wrong Input ! <<<<<<')
