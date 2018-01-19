count = 0
thing = input('Enter the file name: ')
if thing==('na na boo boo'):
	print('NA NA BOO BOO TO YOU - You have been punk\'d!')
else:
	thing = open(thing)
	for line in thing:
		count = count + 1
	print('There were ' + str(count) + ' subject lines in ' + str(thing))
