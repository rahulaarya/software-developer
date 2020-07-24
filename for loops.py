****** FOR LOOPS  IN PYTHON:-----

#  A for loop acts as an iterator in Python. 
general format for a loop

for item in object:
	statements to do stuff

# This is formula for a loop while we need to run here with code 
iterator through a list 

EXAPMLES:--

list1 = [1,2,3,4,5,6]
for number in list1:
	print(number)

		1
		2
		3
		4
		5
		6
		7
		8
		9
		10

* MODULO
The modulo allows us to get the remaninder in a division and uses the % symbol
EXAPMLES:-

17 % 5 
2 # this makes sense 17 divided by 5 is 3 remainder 2 .

10 % 3 
1

20 % 5
0  # 0 because of it's divide all nothing to balance .

* lets print only even number from the list1
EXAPMLES:-

for number in list1:
	if number % 2 == 0:
		print(number)

	2
	4
	6
	8
	10

for number in list1:
	if number % 2 == 0:
		print(number)
	else:
		print('Odd number')

			Odd number
			2
			Odd number
			4
			Odd number
			6
			Odd number
			8
			Odd number
			10

# during a for loop is keeping some sort of running some tally during multiple loops .
# let's create a for loop that sums up the list:

list_sum = 0 
for numberin list1:
	list_sum = list_sum + number

print(list_sum)

55 # all the numbers is add......

EXA:-

list_sum = 0
 
for numberin list1:
	list_sum += number
print(list_sum)

55   # same thig here also we changed only += sing .

*Remember strings are a sequence so when we iterate through them we will be accessing each item in that string.

for letter in "computer":
	print(letter)

	c 
	o 
	m 
	p 
	u 
	t 
	e 
	r 

	* loop in tuple:

	tup = (1,2,3,4)
	for number in tup:
		print(number)

		1
		2
		3
		4

list2 = [(2,4),(5,10),(15,20)]
for tup in list2:
	print(tup)

		(2, 4)
		(5, 10)
		(15, 20)

EXA:-
for (t1,t2) in list2:
	print(t1)
	2
	5
	15


EXAPMLES of dictionary 

d = {'k1':1,'k2':2,'k3':3}
for item in d:
	print(item)

	k1
	k2
	k3
 # there are three types of keywords in dictionary here .
 .keys()
 .values()
 .item()

 EXA
d.keys()  #  k1,k2,k3
d.values() # 1,2,3
d.item() # ([('k1', 1), ('k2', 2), ('k3', 3)])


two more tyes here 
 list(d.keys())  # ................
 sorted(d.values())   # .................
 