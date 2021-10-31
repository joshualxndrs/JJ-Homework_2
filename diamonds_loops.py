length = eval(input("Enter the length of diamond: "))

for i in list(range(length)) + list(reversed(range(length-1))):
    print("{: <{width1}}{:*<{width2}}".format("", "", width1=length-i-1, width2=i*2+1))