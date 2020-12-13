# computeGC() function returns GC base pair proportion as a decimal

def computeGC(seq):

	# Initialize count to 0
	n = 0

	# Iterate through the sequence
	for char in seq:
		if char.upper() == 'G':
			n += 1
		elif char.upper() == 'C':
			n += 1
		else:
			pass

	# Convert numbers to floats, carry out division, multiply by 100 and return result with 2 decimal places
	return str(round((float(n) / float(len(seq))*100), 2))
