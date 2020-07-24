lst = [1,2,3,4,5]

lst.append(20)

lst

lst.pop()

lst






# here new example of pyt

# def functions with examples :-




def name ():
    print("My name is Tom , and I'm a BCA Students of Mumbai college")

name()

# other examples 


def greeting(name):
    print(f'hello {name}, {"where you been"}')
    
    

greeting("tom")

def computer(name):
    print(f'virus {name}')

computer("this is a malware of comouter its bad for our computer")



def add_num(num1,num2):
    return num1+num2

add_num(10,20)

def my_name_here(num1,num2,num3,num4):
    return num1+num2-num3*num4


my_name_here(1,1,2,0)

def my_list(num1,num2,num3):
    return num1+num2*25

result = my_list(2,5,2)

result

def tom(a,b):
    print(a*b)

tom(20,30)

def return_name(num1,num2):
    print(num1+num2)
    

return_name(2,3)

def even_check(number):
    return number % 2==0

even_check(21)

def check_odd (number):
    return number % 2 == 0

check_odd(21)

def check_even_list(mylist):
    for number in mylist:
        if number % 3 == 0:
            return True
    else:
        return False

check_even_list([20,10,50])

def check_odd_number(mylist):
    for number in mylist:
        if number % 3 == 0:
            return True 
    else:
        print("all the numebrs is get passed")

check_odd_number([2,9,8])



#  tuples examples for mix all thing :------

stock_price = [('Apple',30),('Berry',60),('Banana',50)]

for item in stock_price:
    print(item)

for price in stock_price:
    print(price)

#  lets see anothe examples :--



work_hours = [('Bobby',100),('Tom',50),('Rok',300)]


def employee_check(work_hours):
    
    current_max = 0
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
        
    return (employee_of_month,current_max)

employee_check(work_hours)

#   check code spelly clearly and write ....

computer_work_time = [('10 hours a day')]

def computer_work_time(work_hours):
    
    current_max =  0
    computer_working_hours = ''
    
    for computer,hours in work_hours:
        if hours > current_max:
            current_max = hours
            computer_work_time = computer
        else:
            pass
    
    return (computer_work_time,current_max)

computer_work_time







#   EXERCISE FOR FUNCTION:----



#1. Define a function called myfunc that takes in a name, and print 'Hello Name'

#  ans :-----


def myfunc(name):
    print('Hello {}'.format(name))

#2. Define a function called myfunc that takes in a Boolean value 
#  (True or False) if True return 'Hello' if Flase return 'Goodbye'

# ans :-----


def myfunc(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'

#3. Define a function called myfunc that takes three argumetns x,y,z.
#  if z is True, return x. if z is False, ruruen y.
 
#  ans:----


def myfunc(x,y,z):
    if z == True :
        return x
    else:
        return y

#4. Define a function called myfunc that takes in two argumetns and returns their sum

#  ans:-------


def myfunc (o,p):
    return(o+p)

myfunc(20,2)

#  5. define a function called is_even that tales in one argument, and returns
#  True if the pass values is even, False it is not .


# ans:--


def is_even(a):
    if a%2 == 0:
        return True
    else:
        return False

#6. Define a function called is_greater that takes in two arguments, and returns
#   True if the if the values is greater than second , False if it is less than 
#  or equal to the second .

def is_greater(a,b):
    if a>b:
        return True
    else:
        return False

def is_greater(a,b):
    if a>b:
        return True
    elif a<b:
        return False

