fhand = open(input('Enter a filename (recommended mbox-short.txt): '))
count = 0
average = 0
for line in fhand:
	if line.startswith('X-DSPAM-Confidence:'):
		count = count + 1
		inp = line
		value = float(inp[20:])
		average = average + value
print(average/count)
