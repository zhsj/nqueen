#filename nqueen-recurssion.py
#-*- coding:utf-8 -*-
def available(row,col):
	"""检查当前位置是否合法"""
	for k in range(row):
		if queen[k]==col or queen[k]-col == k - row or queen[k]-col == row - k:
			return False
	return True

def find(row):
	"""当row == n时表明已放置了n个皇后，递归结束，记录一个解"""
	global count,n,queen
	if row == n:
		count += 1
		print queen
	else:
		for col in range(n):
			if available(row,col):
				queen[row]=col
				find(row+1)

def main():
	global count,n,queen
	n = input()
	queen = [-1]*n
	count = 0
	find(0)
	print count

if __name__ == "__main__":
	main()
