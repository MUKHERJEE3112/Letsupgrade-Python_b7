'''WAP TO FIND THE ARMSTRONG NUMBER FROM 1042000 TO 702648265
AND EXIT THE LOOP AS SOON AS YOU ENCOUNTER THE FIRST ARMSTRONG NUMBER'''

#THE NUMBERS GIVEN BY THE USER IS STORED IN start AND end
start = int(input('ENTER THE STARTING VALUE :'))
end = int(input('ENTER THE ENDING VALUE :'))
for num in range(start,end):
    sum,n = 0,num 
    while n!=0:
        sum += ((n%10)**3)    
        n//=10
    if num==sum :
        print('THE NUMBER IS ARMSTRONG NUMBER',num)
        break
else:
    print('NO ARMSTRONG NUMBER')
    
