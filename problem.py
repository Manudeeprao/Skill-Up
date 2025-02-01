n=int(input())
def cal(n):
    if(n>0):
        for i in range(1,n//2+1):
            sum=0
            res=[]
            while(sum!=n):
                res.append(i)
                sum+=i
                i+=1
                if(sum==n):
                    print(res)
                if(sum>n):
                    break
cal(n)          