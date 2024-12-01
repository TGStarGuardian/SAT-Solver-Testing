from solver import Kissat_Solver
from clause_generator import Mixed_3_4_Generator, CPM_Generator
from result_parser import Kissat_Parser

kissat = Kissat_Solver("./../kissat-master/build/kissat")
mixed_generator = Mixed_3_4_Generator()
cpm_generator = CPM_Generator(0.11111)

class Experiment:
	
	def __init__(self, num_tests, num_vars, num_clauses, solver = kissat, parser = Kissat_Parser(), generator = mixed_generator):
		self.__num_tests = num_tests
		self.__num_vars = num_vars
		self.__num_clauses = num_clauses
		self.__generator = generator
		self.__parser = parser
		self.__solver = solver
		
	def run_test(self, test_id):
		# generate clauses
		clauses = []
		for i in range(self.__num_clauses):
			clause = self.__generator.generate_clause(self.__num_vars)
			clauses.append(clause)
		# call solver
		raw_data = self.__solver.run(test_id = test_id, num_vars = self.__num_vars, clauses = clauses)
		# parse the results
		return self.__parser.parse(raw_data)
		
	def run_experiment(self):
		for i in range(self.__num_tests):
			print(self.run_test(i))


number_of_tests = int(input("Enter the number of tests: "))
number_of_variables = int(input("Enter the number of variables: "))
number_of_clauses = int(input("Enter the number of clauses: "))

experiment = Experiment(number_of_tests, number_of_variables, number_of_clauses)
experiment.run_experiment()
