def mergesort(input):
    li=len(input)
    output = []
    if li==1:
        #print(input)
        return input
    else:
        il = input[:li//2]
        ir = input[li//2:]
        #print (il,ir)
        a1 = mergesort(il)
        a2 = mergesort(ir)
        #print("hello",len(a1),len(a2),li)
        j = 0
        k = 0
        #print(a1,a2)
        l2=li//2
        for i in range(li):
            #print(i,j,k)
            if (j<l2 and k<l2):
                if a1[j] < a2[k]:
                    output.append(a1[j])
                    j+=1
                else:
                    output.append(a2[k])
                    k+=1
            elif(j<l2):
                output.append(a1[j])
                j+=1
            else:
                output.append(a2[k])
                k+=1
        #print(output)        
        return output
     
print(mergesort([3,7,8,10,22,42,6,8,5,9,11,23,77,89,101,211])) 
