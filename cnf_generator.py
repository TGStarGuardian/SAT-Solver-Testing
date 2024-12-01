from abc import ABC, abstractmethod

class CNF_File_Generator(ABC):
	
	def __init__(self):
		super().__init__()
	
	@classmethod
	@abstractmethod
	def create_file(cls, path, num_vars, clauses):
		pass

class DIMACS(CNF_File_Generator):

	def __init__(self):
		super().__init__()
	
	@classmethod
	def create_file(cls, path, num_vars, clauses):
		with open(path, 'w') as cnf:
			cnf.write("p cnf " + str(num_vars) + " " + str(len(clauses)) + "\n")
			for clause in clauses:
				cnf.write(" ".join(list(map(str, clause))))
				cnf.write(" 0 \n")
		return path

#num_vars = 5
#clauses = [[1, 2, 3], [-1, -4, 2], [3, -2]]

#path = DIMACS.create_file("./test/proba.cnf", num_vars, clauses)
