#a = [["root", ""], [2, "root"], [3, "root"], [4, 3], [1, 2]]

#d = {}

#for i in a:
#	if not i[1]:
#		continue
#	if not i[1] in d:
#		d[i[1]] = []
#		d[i[1]].append(i[0])
#	elif i[1] in d:
#		d[i[1]].append(i[0])
#print d

from BeautifulSoup import BeautifulStoneSoup

file_name = "hypo.xml"
file = open(file_name)
soup = BeautifulStoneSoup(file.read())

n = soup.findAll("node")
nodes = []
try:
	for i in n:
		temp = []
		temp.append(str(i.attrs[0][1]))
		if i.relation == None:
			temp.append("")
			nodes.append(temp)
			continue
		else:
			temp.append(str(i.relation.attrs[0][1]))
			nodes.append(temp)
except:
	print i
	
d = {}

for i in nodes:
#	if not i[1]:
#		continue
	if not i[1] in d:
		d[i[1]] = []
		d[i[1]].append(i[0])
	elif i[1] in d:
		d[i[1]].append(i[0])
print d
	
