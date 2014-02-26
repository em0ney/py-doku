#!/usr/bin/python

# Define puzzle here

row0=[0,0,0,0,0,0,4,0,0]
row1=[5,6,0,4,3,0,0,0,1]
row2=[0,0,0,0,0,5,0,0,6]

row3=[1,0,3,0,0,9,0,6,0]
row4=[8,0,6,0,0,0,7,0,3]
row5=[0,4,0,8,0,0,1,0,2]

row6=[9,0,0,6,0,0,0,0,0]
row7=[6,0,0,0,1,8,0,7,4]
row8=[0,0,8,0,0,0,0,0,0]

rows=[row0, row1, row2, row3, row4, row5, row6, row7, row8]

#returns 1 for legal, 0 otherwise
def isLegal():
	#check whether the current sudoku is valid
	#first check rows
	for i in range(0,9):
		group = []
		for j in range(0,9):
			if rows[i][j] != 0:
				group.append(rows[i][j])
		if checkGroup(group) != 1:
			return 0
	#now check columns
	for i in range(0,9):
		group = []
		for j in range(0,9):
			if rows[j][i] != 0:
				group.append(rows[j][i])
		if checkGroup(group) != 1:
			return 0	
	#now check boxes
	group = []
	x=0
	while x != 9:	
		for i in range(0,9):
			if (i%3 == 0 and i != 0):
				if checkGroup(group) != 1:
					return 0
				else:
					group = []
			for j in range(x,x+3):
				if rows[i][j] != 0:
					group.append(rows[i][j])
		if checkGroup(group) != 1:
			return 0
		else:
			group = []
		x+=3	
	return 1
	
def checkGroup(groupList):
	for i in range(1,10):
		if groupList.count(i) > 1:
			return 0
	return 1
	

#returns 1 if solved, 0 otherwise
def solved():
	for i in range(0,9):
		for j in range(0,9):
			if rows[j][i] == 0:
				return 0
	return 1

def solve():
	if isLegal() != 1:
		return
	if solved():
		print("Sudoku solved")
		showGrid()
		quit()
	for i in range(0,9):
		for j in range (0,9):
			if (rows[j][i] == 0):
				for tryNum in range(1,10):
					rows[j][i] = tryNum
					solve()
				rows[j][i] = 0
				return

def showGrid():
	for counter in range(0,9):
		line = ''
		if counter%3==0 and counter!=0:
			print('---------------------------------')
		for i in range(0,9):
			line+=' '
			if (i%3==0 and i!=0):
				line+='|  '
			line+=str(rows[counter][i])
			line+=' '
		print(line)
	return
				

	
# Main function
showGrid()
solve()
quit()
	
