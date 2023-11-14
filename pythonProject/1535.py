class MyNumberDivisor():
    # def __init__(self, numbers):
    #     self.numbers = numbers
    @staticmethod
    def check_array_division(arr,divisor):
        newDivisor=divisor.copy()
        for delitel in (newDivisor):
            newDivisor[delitel]=arr.copy()
            newVal=list(filter(lambda x:x%int(delitel)==0,newDivisor[delitel]))
            newDivisor[delitel]=newVal
        return newDivisor

arraay=[j for j in range(100)]

my_divisor = MyNumberDivisor()

dd={"15":[],"3":[],"5":[]}

newD=(my_divisor.check_array_division(arraay,dd))
for j in newD.items():
    print(j)
