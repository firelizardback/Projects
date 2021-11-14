counts = [ "900,google.com", 
 "60,mail.yahoo.com", 
 "10,mobile.sports.yahoo.com", 
 "40,sports.yahoo.com", 
 "300,yahoo.com", 
 "10,stackoverflow.com", 
 "20,overflow.com", 
 "5,com.com", 
 "2,en.wikipedia.org", 
 "1,m.wikipedia.org", 
 "1,mobile.sports", 
 "1,google.co.uk"]

def domain_count(counts):
    dic = {}
    for i in counts:
        s = i.split(',')
        d = s[-1].split('.')
        
        for j in range(len(d)-1,-1,-1):
            if j == len(d)-1:
                st =d[j]
            else:
                st = d[j] + '.' + st 
            dic[st] = dic.get(st, 0) + int(s[0]) 
  
    return(dic)

new_dic =  domain_count(counts)       
print(type(list(new_dic.items())))
print(domain_count([]))