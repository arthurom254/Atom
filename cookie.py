from http import cookies
str="username=atom&email=atom@example.com&pwd=12345678"
details=str.split('&')
C=cookies.SimpleCookie()
mydict={}
for val in details:
    if '=' in val:
        token,value=val.split('=')
    else:
        value=val
    mydict[token]=value
print(mydict)
for val in mydict:
    C[val]=mydict[val]
print(C)
