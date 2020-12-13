# from typed_ast._ast3 import List


class Solution:
    def lemonadeChange(self,bills) ->bool:
        a=[0,0,0,0,0]
        for i in bills:
            a[int(i/5)]+=1
            a[int(i/10)]-=1
            a[int(i/20)]-=1
            if a[1]<0 or a[1]+2*a[2]<0:
                return False
        return True

a=[5,5,5,10,20]
b=Solution()
c=b.lemonadeChange(a)
print(c)