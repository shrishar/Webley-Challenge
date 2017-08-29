'''
Name: Shridivya Sharma
School: Indiana University Bloomington
Webley Challenge
Solution  Recursive way of finding combination
'''


import pandas as pd
import numpy as np
import itertools
import re
import sys
#result = []
#---------Created Regex Functions---------------------------------------------------------------------------------------
# Two regex functions to check Price of each items
regex_1 = re.compile(r"""         # beginning of string
                              (\$      # dollar sign
                              [0-9]    # first digit must be non-zero
                              \d * )   # followed by 0 or more digits
                              (\.       # optional cent portion
                              \d {2}  # only 2 digits allowed for cents
                                )?     # end of string""", re.X) # regex function for checking $ in file

regex_2 = re.compile(r"[+]?\d+(?:\.\d+)?", re.X) #Regex function for positive value
#-----------------------------------------------------------------------------------------------------------------------

#-------------- Creating a new dictionary with prices as keys and item as values----------------------------------------
def new_dict(dict):
    new_dict = {}
    for k, v in dict.items():
        new_dict.setdefault(float(v), []).append(k)
    return new_dict
#-----------------------------------------------------------------------------------------------------------------------

#------ Function to extract target price from the file------------------------------------------------------------------

def checktargetprice(targetprice):
    if re.match(regex_1,targetprice):
        final_price=targetprice.replace("$","")
    elif re.match(regex_2,targetprice):
        final_price=targetprice
    else:
        return 0
    return float(final_price)
#-----------------------------------------------------------------------------------------------------------------------

#----------Function to check the prices in the file---------------------------------------------------------------------
'''
checked following things:
1. If monetary value is less than 0, we won't go further. Prices can't be negative
2. Removes "$" from the prices, if the price is non negative.
3. Checks all other format like : $-2.34,-$2.70,rejects file processing if the prices are non negative.
'''

def CheckData(Dict):
    string_value=Dict.values()
    price_value=[]
    flag=True                # break the code if we encounter negative value
    for str in string_value:
        if(re.match(regex_1,str)):
            price_value.append(str.replace("$",""))
        elif (re.match(regex_2,str)):
            price_value.append(str)
        else:
            flag=False
            break
    return price_value,flag
#-----------------------------------------------------------------------------------------------------------------------

#------------Reading csv and converting data into dictionary -----------------------------------------------------------
def ReadCSV(CSV_Path):
    try:
        data = pd.read_csv(CSV_Path,header=None)
        data.columns = ['dishes', 'price']
        TargetPrice=data['price'][0]
        data['dishes'].fillna('Item Unknown',inplace=True) # for unknown items, replacing missing values with
                                                           # "Unknown Item"
        data['price'].fillna('0.50',inplace=True) # for missing price value, default value will be 0.50
        dict = {}
        for i in range(1, len(data)):             # Removing "$" from price
            if re.match(regex_1,data['price'][i]):
                tempval=data['price'][i]
                dict[data['dishes'][i]] = tempval.replace("$","")
            elif (re.match(regex_2,data['price'][i])):
                dict[data['dishes'][i]]= data['price'][i]
            else:
                dict[data['dishes'][i]] = data['price'][i]
        return dict, TargetPrice
    except IOError:
        print("Could not read file,check path again", CSV_Path) # if file not found/read, throw expression
        sys.exit()

#---find combination----------------------------------------------------------------------------------------------------

def find(arr, num,result,path=()):
    if not arr:
        return
    if arr[0] == num:
        result.append(path + (arr[0],))
    else:
        find(arr[1:], num - arr[0],result, path + (arr[0],))
        find(arr[1:], num, result,path)

def FindCombination(targetprice,dict,checked_price):
    arr=[float(i) for i in checked_price] #creating an array of price values
    arr.sort()
    result=[] #combination result
    find(arr, targetprice,result)# function which calculate combinations of prices
    result=list(set(result)) # removing duplicate combinations
    newdict = new_dict(dict) # creating a new dictionary with prices as key and items as values.
    dishes=[]
    '''
    Following logic is to create combinations of item using above combination result of prices
    '''
    for i in result:
        r=[]
        for j in i:
            r.append(newdict.get(j))
        k=list(itertools.product(*r))
        dishes.append(k)
    return dishes
#-----------------------------------------------------------------------------------------------------------------------

#------------Function to print final item combinations------------------------------------------------------------------
def CheckResult(result):
    if(len(result)==0):
        print("There is no combination of dishes that is equal to the target price")
    else:
        print('Combinations are as follows:')
        print(result)
#-----------------------------------------------------------------------------------------------------------------------
'''
main function calling all other functions.

'''

def main():
    print("Reading csv file....")
    CSV_Path=sys.argv[1]  # takes the file name/ file path from console
    dict,targetprice=ReadCSV(CSV_Path)
    print('Read csv file....')

    print("Validating target price value...")
    targetprice=checktargetprice(targetprice) # checks if the target value is correct or not
    if(targetprice==0):
        print("Target price is a negative value , check the final price again!")
    else:
        print("Target Value validates..validating price values")
        print("Validating price list")
        checked_price,flag=CheckData(dict)
        if (flag == False):  #Check the file for negative prices
            print("Check the file again, items have negative values,price cannot be negative")
        else:
            print("The prices are non negative,file check is complete..Good to go..!\n")
            result=FindCombination(targetprice,dict,checked_price) # List of prices sums to the target price
            print('Finding a combination of dishes which sums up to target price......')
            CheckResult(result) # printing final result of combination
main()

