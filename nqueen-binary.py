#filename nqueen-binary.py
#-*- coding:utf-8 -*-

def find(row, ld, rd):
	global n, upperlim,count
	if row == upperlim: #当row == upperlim时，所有列已有棋子，即产生一个解
		count += 1
	else:
		pos = upperlim & (~(row | ld | rd)) # pos二进制表示时，1代表该位可放棋子
		while pos: #有位置可放
			p = pos & (~pos + 1) #取出pos中最后一位1
			pos = pos - p #将取出的1（合法的位置）从pos中去除
			find(row | p, (ld | p) << 1, (rd | p) >> 1) #递归查找


def main():
	global n,upperlim,count
	n = input()
	upperlim = (1 << n) - 1 #表示N个1
	count = 0
	find(0, 0 ,0)
	print count

if __name__ == "__main__":
	main()
