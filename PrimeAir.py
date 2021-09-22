'''
def find(F, B, T):
    ans = [0, 0, 0]
    F = sorted([x, i] for i,x in F)
    for idy,y in B:
        f = 0
        end = len(F)
        z = T - y
        
        while f != end:
            m = (f + end)//2
            if F[m][0] <= z:
                f = m+1
            else:
                end = m

        if f != 0 and y+F[f-1][0] > ans[0]:
            ans = [y+F[f-1][0], F[f-1][1], idy]
    
    return ans[1:]
        
if __name__ == '__main__':
    #print (find([(1,3000),(2,5000),(3,4000),(4,10000)], [(1,2000),(2,3000),(3,4000)], 11000))
    print (find([(1,3000),(2,5000), (5,5000), (5,5000) ,(3,4000),(4,10000)], [(1,2000),(2,3000),(3,4000), (4,4000)], 11000))
'''

def primeAir(a,b,target):
    maxSum=float("-inf")
    # sort the array using values
    arr1=sorted(a,key=lambda x: x[1])
    arr2=sorted(b,key=lambda x: x[1])
    i,j,n1,n2,res=0,len(arr2)-1,len(arr1),len(arr2),list()
    # for each element in 1st array iterate and compare with elements in 2nd array
    while(i<n1 and j>=0):
        #take the sum 
        val=arr1[i][1]+arr2[j][1]
        # if sum exceeds the target and move left 
        if val>target:
            j-=1 
        else: 
            # else if it's less than target and then we compare with the maximum sum we obtained till now .
            if val>=maxSum:
                # if its exceeds then forget the pairs calculated till now. 
                if val>maxSum:
                    maxSum,res=val,list()
                # now append the current pair in res array.
                res.append([arr1[i][0],arr2[j][0]])
                temp=j
               # now since the all the elements before j in arr2 will be lesser(since the array is sorted) so, find the equal ones and add them to res. 
                while( j>=0 and arr2[j][1]==arr2[temp-1][1]):
                    res.append([arr1[i][0],arr2[temp-1][1]])
                    temp-=1 
            i+=1 
    if not res:
        res=[[]]
    return res
target=10000
a=[[1,3000],[2,5000], [2,5000],[3,7000],[4,10000]]
b=[[1,2000],[2,3000],[3,4000],[4,5000]]
'''
Output: [[2, 4], [3, 2]]
'''

print(primeAir(a,b,target))