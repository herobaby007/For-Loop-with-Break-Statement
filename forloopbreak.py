l = eval(input())


keyword = input()

for value in l:

	if value == keyword:
	   print("Keyword Found")
	   break
	else:
	   continue

else:
	   print("Keyword not found")   

