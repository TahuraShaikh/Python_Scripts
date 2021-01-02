#Get unique values from dict
dict={'Red':[61,2,55,4],
      'Green':[5,23,7,6],
      'Blue':[7,61,5,3],
      'Yellow':[6,55,23,2]
      }
#original dict values
print (f'The original dict is: \n {dict}')

#to get unique values of dict
u = list(sorted({l for val in dict.values() for l in val}))

#print unique values
print (f'\n Unique values in dict are: {u}')