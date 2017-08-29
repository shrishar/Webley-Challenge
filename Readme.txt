****************** Webley Challenge *******************************
Requirements: 

Write a program which will process the data listed below. The data must be placed into a csv file and read from it. The first variable is the target price and the following data values are menu items you could buy. The program should then find a combination of dishes that has a total of exactly the target price. If there is no solution if found, then the program should print that there is no combination of dishes that is equal to the target price. The program must run with different data files, so provide instructions on how to run the program from command line with the correct file. Use any programming language to solve this puzzle as long as it can be ran from linux command line. 
Here are some sample data values: 

Target price, $15.05
mixed fruit,$2.15
french fries,$2.75
side salad,$3.35
hot wings,$3.55
mozzarella sticks,$4.20
sampler plate,$5.80


Solution:
Programming language : Python 
Version : Can be run on Python 3.3 or higher

I came with a recursive way of finding all the subset of price which adds up to target price.





Assumptions made:
1)csv file is in the given format:
	Target price, $15.05
	mixed fruit,$2.15
	french fries,$2.75
	side salad,$3.35
	hot wings,$3.55
	mozzarella sticks,$4.20
	sampler plate,$5.80
	
First row always correspond to target price and it's values

2) If an item/dishes name is missing - default name given is "Unknown Item"
3) If an item price is missing - default value given is $0.50
4) If any of price values are negative, file can't be processed further.
5) File can't be processed if the values are in this format : -$3.4 ,$-3.5
6) Program can handle price values such as $4.5 or 4.5 or 4.0 or 1
7) All the combinations are returned in a list.

Steps to run file:



open terminal:
Go to Webley folder you cloned and run the following commands:

1) type python Solution_1.py file_path 
   python Solution_1.py pricedata.csv
2) hit ENTER
3) you can see the results on your console











