#filename nqueen-backtrack.py
#-*- coding:utf-8 -*-
def available(row,col):
	"""检查当前位置是否合法"""
	for k in range(row):
		if queen[k]==col or queen[k]-col == k - row or queen[k]-col == row - k:
			return False
	return True

def find(n):
	"""回溯法求解"""
	count = 0
	row = 0
	global queen
	queen[row] = 0
	while row >=0 : #当前行为 -1 时结束
		if row < n and queen[row] < n: #当前行、当前列均为到达最后
			if available(row,queen[row]): #当前位置合法，则探索下一行
				row += 1
				queen[row] = 0
			else: #当前位置不合法，探测当前行的下一个位置
				queen[row] += 1 
		else:
			if row >= n: #当前行、当前列均到了最后，记录一个解
				count += 1 
			row -= 1 # 返回上一行，继续探索
			queen[row] += 1
	return count

def main():
	global queen
	n = input()
	queen = [-1]*(n+1)
	print find(n)

if __name__ == "__main__":
	main()
