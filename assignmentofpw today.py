#1)ans:def is a keyword used to create a function
def test0():
    n=[]
    for i in range(1,26,2):
        if i<26:
            n.append(i)
    return n
print(test0())         
        
#2)ans:*args is used in fuction to add n number of arguments in a functions,**kwargs is used to add keys&values in a function.
#example of *args
def test1(*args):
    l=[]
    for i in args:
      if type(i)==list:
        l.append(i)
    return l
print(test1([1246554.4,2454,454,],"abhinav","pwslkills"))
#or simple one
def test2(*args):
 return args
print(test2((1232544,52,454,),"theking","pwskills"))
    #example of**kwargs
def test3(**kwargs):
   return kwargs
print(test3(a=124,b=5544435.9,c="abhinav the king"))

#4ans):
#genrator function genrates a sequence of values,one at a time ,without storing the data
#yield keyword is used to iterate the give value
#example
def genrate_odd_number():
   for i in range(1,50,2):
      yield i
gen=genrate_odd_number()
for j in gen:
   print(j)

#3ans):
#an iterator is used to iterate over a collection of data,one element at a time without having to know the underlying implementation of the data structure
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lst12=iter(numbers)
print(next(lst12))
print(next(lst12))
print(next(lst12))
print(next(lst12))
print(next(lst12))
#or
#5)ans 
def genrate_prime():
   number_=[num for num in range(2,201)]
   while True:
      prime=number_[0]
      yield prime
      for num in numbers:
         if num % prime ==0:
            number_.remove(num)
            if not number_:
               return
print(genrate_prime())

    
    

    
    
      

   









      
   

    