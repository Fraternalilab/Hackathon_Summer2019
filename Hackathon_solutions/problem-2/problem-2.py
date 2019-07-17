def table(filename):
	table = {}
	with open(filename) as f:
		for line in f:
			aa = line.split()
			table[aa[0]] = float(aa[1])
	f.closed
	return table

aa_table = table("table")

def count_mass(s, table):
	aas = list(s)
	mass = 0.0
	for aa in aas:
		mass += table[aa]

	return round(mass, 3)

print(count_mass("SKADEYK", aa_table))
	

