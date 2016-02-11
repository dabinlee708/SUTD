def cipher(plaintext, keylength):
    totalLength=len(plaintext)
    outputString=""
    for a in range(keylength):
        i=a
        # print i,a
        while i<totalLength:
            # print i
            outputString=outputString+plaintext[i]
            i+=keylength
    pad=len(plaintext)%keylength
    i=1
    while i<=pad:
        if i%4==1:
            outputString+="a"
        if i%4==2:
            outputString+="b"
        if i%4==3:
            outputString+="c"
        if i%4==0:
            outputString+="d"
        i+=1

    print outputString.upper()




data=["DELHI",1,"thankyouforyourcooperation"]
print len(data[2])
keylength=len(data[0])
for a in data:
    if a==data[0] or a==data[1]:
        pass
    else:
        cipher(a,keylength)