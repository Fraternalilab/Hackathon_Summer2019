def count_nt(s):
	nts = (set(s))
	nt_count = {}
	for nt in nts:
		nt_count[nt] = s.count(nt)
	return nt_count

def count_nt2(s):
	nts = ['A', 'C', 'G', 'T']
	nt_count = [s.count(nt) for nt in nts]
	return nt_count

print(count_nt2("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))

