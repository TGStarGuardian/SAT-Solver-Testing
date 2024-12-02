from secrets import choice, randbelow
from abc import ABC, abstractmethod
from struct import pack

def float_to_binary(num):
    integer_part, fractional_part = int(num), num - int(num)
    binary_integer_part = bin(integer_part).lstrip('0b') + '.'
    binary_fractional_part = ''
    
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        if bit == 1:
            fractional_part -= bit
            binary_fractional_part += '1'
        else:
            binary_fractional_part += '0'
    
    return binary_integer_part + binary_fractional_part

# Algorithm from "Computational Complexity: A Modern Approach" by Barak & Arora
def unfair_coin(p):
	s = float_to_binary(p)
	for i in range(1, len(s)):
		p_i, b_i = int(s[i]), randbelow(2)
		if b_i < p_i:
			return 1
		elif b_i > p_i:
			return 0
				
	while randbelow(2) == 0:
		continue
		
	return 1

class Clause_Generator(ABC):
	
	@abstractmethod
	def generate_clause(self, num_vars):
		pass
		
class Mixed_3_4_Generator(Clause_Generator):

	def __init__(self):
		pass
	
	def generate_clause(self, num_vars):
		# choose a number between 3 and 4 at random
		clause_length, clause = choice([3, 4]), []
		
		signs = [-1, 1]
		for i in range(clause_length):
			# choose a random number between [-N, N], excluding 0
			# i.e. choose a number from [0, N - 1], then add 1
			# and then choose a sign
			# Z = X(Y + 1)
			# Y is uniform on [0, N - 1]
			# Y + 1 is then uniform on [1, N]
			# X is uniform on {-1, 1}
			# Prob{Z = i} = Prob{X(Y + 1) = i}
			# if i > 0, then Prob{Z = i} = Prob{Y + 1 = i | X = 1} Prob{X = 1}
			# Prob{X = 1} = 0.5, Prob{Y + 1 = i | X = 1} = 1/N
			# Prob{Z = i} = 0.5/N = 1/(2N)
			# if i < 0, then Prob{Z = i} = 1/(2N)
			# if i = 0, then Prob{Z = i} = 0
			# Z is uniform on [-N, N] without 0
			sign, var = choice(signs), 1 + randbelow(num_vars)
			clause.append(sign * var)
		return clause

class CPM_Generator(Clause_Generator):
	
	def __init__(self, p):
		self.__p = p
	
	def generate_clause(self, num_vars):
		clauses = []
		
		for i in range(1, num_vars + 1):
			if unfair_coin(self.__p) == 1:
				clauses.append(i)
			if unfair_coin(self.__p) == 1:
				clauses.append(-i)
		
		if len(clauses) < 2:
			return self.generate_clause(num_vars)
		else:
			return clauses

#generator = Mixed_3_4_Generator()
#clause = generator.generate_clause(10)
#print(clause)

