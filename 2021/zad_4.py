def main():
	arr = open('/home/mike/Desktop/pyton/maturki/2021/DANE_2105/przyklad.txt', 'r')
	content = [x.split(' ') for x in arr.read().strip().split('\n')]
	arr.close()
	print(zad_1(content))


def zad_1(arr: list):
	word = ''
	for el in arr:
		if el[0] == 'DOPISZ':
			word += el[1]
		elif el[0] == 'USUN':
			word = word[:-1]
		else:
			index = word.find(el[1])
			

	return word


if __name__ == '__main__':
	main()
