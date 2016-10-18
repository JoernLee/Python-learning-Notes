import re
document = "txtgoal.txt"
group = list()
handle = open(document)
for line in handle:
	line = line.rstrip()
	if not re.search('[0-9]+',line):continue
	number = re.findall('([0-9]+)',line)
	print number
	a = 0
	for m in number:
		num = int(number[a])
		group.append(num)
		a = a+1
	a = 0
final = sum(group)
print final