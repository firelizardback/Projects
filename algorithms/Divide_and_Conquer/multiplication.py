def find2n(input):
    a = input - 1
    a |= a >> 1
    a |= a >> 2
    a |= a >> 4
    a |= a >> 8
    a |= a >> 16
    return(a+1)

# Python3 program to find sum of
# two large numbers.

# Function for finding sum of
# larger numbers
def findSum(str1, str2):
	
	# Before proceeding further,
	# make sure length of str2 is larger.
	if (len(str1) > len(str2)):
		t = str1;
		str1 = str2;
		str2 = t;

	# Take an empty string for
	# storing result
	str = "";

	# Calculate length of both string
	n1 = len(str1);
	n2 = len(str2);

	# Reverse both of strings
	str1 = str1[::-1];
	str2 = str2[::-1];

	carry = 0;
	for i in range(n1):
		
		# Do school mathematics, compute
		# sum of current digits and carry
		sum = ((ord(str1[i]) - 48) +
			((ord(str2[i]) - 48) + carry));
		str += chr(sum % 10 + 48);

		# Calculate carry for next step
		carry = int(sum / 10);

	# Add remaining digits of larger number
	for i in range(n1, n2):
		sum = ((ord(str2[i]) - 48) + carry);
		str += chr(sum % 10 + 48);
		carry = (int)(sum / 10);

	# Add remaining carry
	if (carry):
		str += chr(carry + 48);

	# reverse resultant string
	str = str[::-1];

	return str;

def multiplication(input1,input2):
    l1 = len(input1)
    l2 = len(input2)
    l = find2n(max(l1,l2))
    zerol1 = l - l1
    zerol2 = l - l2
    a = "0" * zerol1 + input1
    b = "0" * zerol2 + input2
    print (a,b,l)
    return (mult(a,b,l))
    
def mult(a,b,l):
    if l==1:
        return (str(int(a) * int(b)))
    else:
        l2 = l//2
        ac = mult(a[:l2],b[:l2],l2)
        bd = mult(a[l2:],b[l2:],l2)
        ad = mult(a[:l2],b[l2:],l2)
        bc = mult(a[l2:],b[:l2],l2)
        return(findSum(bd, findSum(ac + "0" * l, findSum(ad,bc) + "0" * l2)))

    


# Driver code
#str1 = "12";
#str2 = "198111";
#print(findSum(str1, str2));

# This code is contributed by mits

a = "3141592653589793238462643383279502884197169399375105820974944592"
b = "2718281828459045235360287471352662497757247093699959574966967627"
print(multiplication(a,b))
#print (a * b)