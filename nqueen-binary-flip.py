#filename nqueen-binary-flip.py
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

def find_flip():
	global n,count
	pos = (1<< (n >> 1)) -1#只探索第一行后半列的情况
	while pos:
		p = pos & ( ~pos + 1)
		pos = pos - p
		find(p, p<< 1, p >> 1)
	count <<= 1 #将结果×2
	if n & 1 : #对于棋盘为奇数的情况，再探索一次第一行中间位置放子的情况
		p = 1 << (n >> 1)
		find(p, p<< 1, p >> 1)

def main():
	global n,upperlim,count
	n = input()
	upperlim = (1 << n) - 1 #表示N个1
	count = 0
	find_flip()
	print count

if __name__ == "__main__":
	main()
