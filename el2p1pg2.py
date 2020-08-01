#A String is said to be palindrome...
for _ in range(int(input())):
    s = input()
    if s==s[::-1]:
        print("0")
    else:
        lr,rr=0,0
        ds = s
        fl,fr = False,False
        #lr
        for i in range(len(s)):
            ds = ds[1:]+ds[0:1]
            lr = lr + 1
            if ds == ds[::-1]:
                fl == True
                break
        #rr
        for i in range(len(s)):
            ds = ds[len(ds)-1:]+ds[0:len(ds)-1]
            rr = rr + 1
            if ds == ds[::-1]:
                fr = True
                break
       if fl==True and fr==True:
           print(min(lr,rr))
       elif fl==False and fr==True:
           print(rr)
       elif fl==True and fr==False:
           print(lr)
       else:
           print("-1")
               