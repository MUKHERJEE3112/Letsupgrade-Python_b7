'''DAY 3 LETSUPGRADE'''

'''WAP TO FIND ALL THE PRIME NUMBERS BETWEEN TWO NUMBERS'''
#THE NUMBERS GIVEN BY THE USER IS STORED IN start AND end 
start = int(input('ENTER THE STARTING VALUE :'))
end = int(input('ENTER THE ENDING VALUE :'))
for num in range(start,end):  
    for i in range(2,(num//2)+1):
        if num % i == 0 :
            break
    else:
        print(num)
else:
    print(':END OF LOOP:')

'''PILOT PROBLEM'''
# THE ALTITUDE GIVEN BY THE USER IS STORED IN alt
alt = float(input('ENTER THE CURRENT ALTITUDE'))
if alt <  1000:
    print('SAFE TO LAND')
elif alt >= 1000 and alt < 5000:
    print('BRING DOWN TO 1000ft')
else:
    print('TURN AROUND')


