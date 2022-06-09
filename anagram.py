a=input("enter string")
b=input("enter check string")
c=a.lower()
d=b.lower()
if(sorted(c)==sorted(d)):
	print("anagram")
else:
	print("not anagram")
