#def trait(all1, all2):

#	pass
import numpy as np

class Trait(object):
	def __init__(self, a1, a2):
		self.allel1 = a1
		self.allel2 = a2

	def __str__(self):
		return "%s,%s" % (self.allel1, self.allel2)

	@staticmethod
	def hetero_dom(a):
		return Trait(a.upper(),a.lower())
	
	@staticmethod
	def homo_dom(a):
		return Trait(a.upper(),a.upper())

	@staticmethod
	def homo_rec(a):
		return Trait(a.lower(),a.lower())

def mate(trait1, trait2):
	trait = Trait(trait2.allel1, trait2.allel2)
	if np.random.rand() < 0.5:
		trait.allel1 = trait1.allel1
	if np.random.rand() < 0.5:
		trait.allel2 = trait1.allel2
	return trait




trait1 = Trait("A","A")
trait2 = Trait("A","a")

trait3 = mate(trait1,trait2)

trait4 = Trait.homo_rec("b")

