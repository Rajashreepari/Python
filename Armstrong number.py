class Armstrong:
    def __init__(self,number):
        self.number=number
    def check(self):
        num=str(self.number)
        digit=len(num)
        n=int(num)
        sum_of_digit=0
        while n!=0:
            remainder=n%10
            sum_of_digit+=(remainder**digit)
            n=n//10
        if self.number==sum_of_digit:
            print(self.number," is Armstrong number")
        else:
            print(self.number," is not an Armstrong number")

number=int(input("enter number:"))
Num=Armstrong(number)
Num.check()
