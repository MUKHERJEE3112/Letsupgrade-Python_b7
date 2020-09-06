'''LETSUPGRADE-DAY 2

# LIST AND IT'S METHODS
a =[5,10,15,20,25,30,35,40,45,50]
print(a)


#CHANGE THE ELEMENT OF 4TH POSITION BY ELEMENT 32
a[3]=32
print(a)
#DELETE 6TH ELEMENT USING 'POP'  
print('THE REMOVED ELEMENT IS :{} AND THE LIST AFTER THAT {}'.format(a.pop(5),a))
#INSERT A NEW ELEMENT 55 AT THE LAST POSITION OF THE LIST
a.append(55)
print('AFTER ADDING 55 IN THE END OF THE LIST :',a)
#DELETE THE ELEMENT 40 FROM THE LIST
a.remove(40)
print('THE REMOVED ELEMENT IS 40 THE LIST AFTER THAT {}'.format(a))
#EXTEND THE LIST BY ELEMENTS 60 ,65, 70 ,75
a.extend([60,65,70,75])
print('AFTER EXTENDING THE LIST :',a)
#INSERT A NEW ELEMENT 18 AT THE 4TH POSITION OF THE LIST
a.insert(3,18)
print('AFTER EDITNG THE LIST :',a)


# TUPLES AND IT'S METHODS
tup=(1,2,3,3,2,2,2)
print(tup)

# TO PRINT THE INDEX NUMBER OF AN ELEMENT
print('THE INDEX NUMBER OF 1 IS:' ,tup.index(1))
# TO PRINT THE OCCURANCE OF AN ELEMENT
print('THE OCCURANCE OF 2 IS:' ,tup.count(2))  

# SET AND IT'S METHODS
set1={'apple','banana','cherry'}
set2={'bat','ball','banana','apple'}
print(set1)

#to add one element
set1.add('mango')
print(set1)
#to  add multiple
set1.update(['grapes','lemon'])
print(set1)
#to sort these elemnts
print(sorted(set1))
#to remove we use discard() or remove()
set1.remove('lemon')
print(set1)
print('SET OPERATIONS')
# UNION OF set1 AND set2
print(set1|set2)
# INTERSECTION OF set1 AND set2
print(set1&set2)
# ELEMNTS IN set1 BUT NOT IN set2
print(set1-set2)
# ELEMENTS IN set1 OR set2 BUT NOT ON BOTH
print(set1^set2)

# STRING AND IT'S METHODS

#WAP to find the length of a string
st = input('ENTER YOUR STRING :')
print('LENGTH OF THE STRING IS : ',len(st))

#WAP to replace something in a string 
st = input('ENTER YOUR STRING :')
old = input('ENTER THE STRING YOU WANT TO CHANGE :')   
rep = input('ENTER YOUR REPLACED STRING :')
new = st.replace(old,rep)
print('REPLACED STRING :',new)

#WAP to check whether the given character is contained
# in a string or not and find its position.
st = input('ENTER YOUR STRING :')
srh = input('ENTER SEARCHING STRING :')
num = st.find(srh,0,len(st))
if num != -1:
    print('FOUND AT POSITION :',num+1)
else:
    print('NOT FOUND')

#WAP TO PRINT THE NUMBER OF WORDS IN A STRING
st = input('ENTER YOUR STRING :')
lst = st.split()
n = len(lst)
print('THE NO.OF WORDS IN :{} IS {}'.format(st,n))'''

#DICTIONARIES AND IT'S METHODS

dt={'name':'abcd','id':404,'salary':32000}
print(dt)

# to print the keys
print(dt.keys())
# to print the values
print(dt.values())
# to print the perticular value
print(dt.get('name'))
# to print the items
print(dt.items())
#to add a new key and value
dt.update(address='INDIA')
print(dt)




























