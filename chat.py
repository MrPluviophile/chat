import os

# read file
def read_file(filename):
	c_sen = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			sentence = ''
			line = line.strip()
			if 'Allen' == line:
				talker = 'Allen'
				continue
			if 'Tom' == line:
				talker = 'Tom'
				continue
			sentence = talker + ': ' + line
			c_sen.append(sentence)		
	return c_sen

# write into file
def write_file(filename, c_sen):
	with open(filename, 'w', encoding='utf-8') as f:
		for s in c_sen:
			f.write(s + '\n')

def main():
	filename = 'input.txt'
	if os.path.isfile(filename):# check if file exist
		print('File exist')
		c_sen = read_file(filename)
	else:
		print('File not found')

	write_file('ouput.txt', c_sen)

main()