#You are given an integer N followed by N email addresses. 
#Your task is to print a list containing valid email addresses, in lexicographic order.
#A valid email address is of the format username@websitename.extension
#Username can only contain letters, digits, dash and underscore.
#Website name can have letters and digits. Maximum length of the extension is 3. 

def check(x):
	if ("@" in x):
		a = x.index("@")
	else: return 0
	if ("." in x):
		dot = x.index(".")
	else: return 0
	if(len(x[dot+1:]) > 3):
		return 0
	if(len(x[:a]) == 0):
		return 0
	for i in x[0:a]:
		if not ((i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9')
			or (i == '-') or (i == '_') or (i == ' ')):
			return 0
	for i in x[a+1:dot]:
		if not ((i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9')):
			return 0
	return 1

l = []
num = input()
for i in range(0,num):
	string = raw_input()
	l.append(string)
l.sort()

l = list(filter(lambda x:check(x) == 1,l))
print l
