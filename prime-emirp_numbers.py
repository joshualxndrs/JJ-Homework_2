def PrimeNum(num):
	
    if num < 10 or num == 11: 
        return False

    
    check = 0 
    for x in range(1,num + 1):
        if num % x == 0:
            check += 1

    
    if check == 2:
        return True
    else: return False


def EmirpNum(num):
	
	num = int(num)
	if PrimeNum(num) == False:
		return False
		
	reverse = 0
	while num != 0:
		d = num % 10
		reverse = reverse * 10 + d
		num = int(num / 10)
		
	return PrimeNum(reverse)


def switched(num):
 
    rev = 0
    while (num > 0):
        rev = (rev * 10) + num % 10
        num = int(num / 10)
 
    return rev


num = int(input("Enter number to be evalutated: ")) 
if EmirpNum(num):
	print("TRUE. This is an Emirp Number.","Number", num,"and", "Number",switched(num))
else:
	print("FALSE. This is NOT an Emirp Number.")