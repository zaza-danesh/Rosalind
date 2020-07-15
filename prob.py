

def func(k, m, n):
	dom_mk = 1.
	dom_nk = 1.
	dom_mn = 1./2.
	dom_mm = 3./4.
	dom_nn = 0
	dom_kk = 1.
	p_mk = 2*(m/(m+n+k))*(k/(m+n+k-1))
	p_nk = 2*(n/(m+n+k))*(k/(m+n+k-1))
	p_mn = 2*(m/(m+n+k))*(n/(m+n+k-1))
	p_mm = (m/(m+n+k))*((m-1)/(m+n+k-1))
	p_nn = (n/(m+n+k))*((n-1)/(m+n+k-1))
	p_kk = (k/(m+n+k))*((k-1)/(m+n+k-1))

	return (dom_mk*p_mk + dom_nk*p_nk + dom_mn*p_mn + dom_mm*p_mm + dom_nn*p_nn + dom_kk*p_kk)


f = file('rosalind_iprb.txt')
array = [float(x) for x in f.readline().split()]

print(func(array[0],array[1],array[2]))