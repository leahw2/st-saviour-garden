

if __name__ == '__main__':
    for i in range(11):
        for j in range(11):
             print('🌷', end='')
        print ('')

    print('horizontal')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0:
                print('🌷', end='') 
            else:
                print('🌼', end='')  
        print('')

    print('vertical')
    for i in range(11):
        for j in range(11):
            if j % 2 == 0: 
                 print('🌷', end='') 
            else:
                print('🌼', end='')  
        print('')

    print('diagnol')
    for i in range(11):
        for j in range(11):
            if (i+j) % 2 == 0:
                 print('🌷', end='') 
            else:
                print('🌼', end='')  
        print('')

    print('plaid')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0 and j % 2 == 0:
                 print('🌷', end='') 
            else:
                print('🌼', end='')  
        print('')

            
