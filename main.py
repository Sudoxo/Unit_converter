import os

file = 'table.txt'
read_file = open(file, 'r')
lines = read_file.readlines()

numbers = ['1','2','3','4','5','6','7','8','9','0','.']
units = {}
available_units = []
for l in lines:
	if l == '\n':
		break
	i=0
	number1=""
	number2=""
	unit1=""
	unit2=""

	while(l[i] in numbers):
		number1+=l[i]
		i+=1
	if(l[i]==' '):
		i+=1
	while(l[i] != " " and l[i] != '='):
		unit1+=l[i]
		i+=1
	while(l[i] == ' ' or l[i] == '='):
		i+=1
	while(l[i] in numbers):
		number2+=l[i]
		i+=1
	if(l[i]==' '):
		i+=1
	while(i < len(l) and l[i] != '\n'):
		unit2+=l[i]
		i+=1

	number2 = float(number2) / float(number1)
	
	if unit1 not in units:
		units[unit1] = [[unit2, number2]]
	else:
		units[unit1].append([unit2, number2])

	if unit2 not in units:
		units[unit2] = [[unit1, 1/number2]]
	else:
		units[unit2].append([unit1, 1/number2])

	available_units.append(unit1)
	available_units.append(unit2)

def bfs_shortest_path(u1, u2):
	visited = [u1]
	queue = [(u1, [])]
	while queue:
		v, path = queue.pop(0)
		visited.append(v)
		for n in units[v]:
			if n[0] == u2:
				return path + [v,n[0]]
			if n[0] in visited:
				continue
			queue.append((n[0], path + [v]))
			visited.append(n[0])
	return None

def single():

	u1 = raw_input("Enter unit to convert from: ")
	am = int(raw_input("Enter amount of that unit: "))
	u2 = raw_input("Enter unit to convert to: ")

	if(u1 not in available_units or u2 not in available_units):
		print("Unit(s) not in table!")
		return 0
	#if u1 == u2:
	#	print(am)
	#	return 0

	path = bfs_shortest_path(u1,u2)

	if path == None:
		print("Conversion not possible")
		return 0

	x = am
	for i in range(len(path)-1):
		curr = path[i]
		for u in units[curr]:
			if(u[0] == path[i+1]):
				x = x * u[1]
				break
	print(x)

def multi():
	u1 = raw_input("Enter unit to convert from (use '/' to separate): ")
	am = int(raw_input("Enter amount of that unit: "))
	u2 = raw_input("Enter unit to convert to (use '/' to separate): ")

	u11 = u1.split('/')[0]
	u12 = u1.split('/')[1]

	u21 = u2.split('/')[0]
	u22 = u2.split('/')[1]

	if(u11 not in available_units or u12 not in available_units or u21 not in available_units or u22 not in available_units):
		print("Unit(s) not in table!")
		return 0

	path1 = bfs_shortest_path(u11,u21)
	path2 = bfs_shortest_path(u12,u22)
	if(path1 == None or path2 == None):
		print("Conversion not possible")
		return 0

	x1 = 1
	for i in range(len(path1)-1):
		curr = path1[i]
		for u in units[curr]:
			if(u[0] == path1[i+1]):
				x1 = x1 * u[1]
				break
	x2 = 1
	for i in range(len(path2)-1):
		curr = path2[i]
		for u in units[curr]:
			if(u[0] == path2[i+1]):
				x2 = x2 * u[1]
				break

	print(am * x1 / x2)


inp = raw_input("Single or complex conversion?(s/c): ")
if(inp == 's'):
	single()
elif(inp == 'c'):
	multi()
else:
	print("Type 's' or 'c'!")
