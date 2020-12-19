
class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1 +=f" {i}a{index} +"          #concatinating index number and value
            index+=1                            #incrementing index value
        return str1[:-1]

    def __add__(self,vec2):
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])                        #appending
        return Vector(newlist)

    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
            sum+=self.vec[i] + vec2.vec[i]      # multiplying and then adding values of list
        return sum

v1=Vector([2,4,6])
v2=Vector([1,3,6])
print(v1+v2)
print(v1*v2)