#Check if the first and last number of a list is the same
#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.


# 3 types of arrays 

# 1 tuple - seznam
ovoce=("banan", "meloun")
ovoce[1]="Jablko"   #error
#nemuzu zmenit ale muzu vytvorit novy


# 2 list 

ovoce = ["Banan", "Meloun"]
ovoce[1]="Jablko"  #++ 

print (ovoce)


#3 dictionary 
# Key and value
znamky_studentu={"Pupkin":5, "Sidorov":3, "Vaneckin":1}
znamky_studentu ["Vaneckin"]
znamky_studentu ["Pupkin"]=1
znamky_studentu["Pupkin"]




lst_1=[10,2,23,234,12,53,23,10]
lst_2=[123,120,212,342,423,1214,576]

print (lst_1 [0])
print (lst_1[-1])

lst_1[0] == lst_1[-1]


#ukol 

def chek_first_last(lst):
    print (f"Your list: {lst}")
    print (f"Result is: {lst[0]==lst[-1]} ")
 


chek_first_last(lst_1)
