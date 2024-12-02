from solver import Kissat_Solver
from clause_generator import Mixed_3_4_Generator, CPM_Generator
from result_parser import Basic_Kissat_Parser

kissat = Kissat_Solver("./../kissat-master/build/kissat")
mixed_generator = Mixed_3_4_Generator()
basic_parser = Basic_Kissat_Parser

class Experiment:
	
	def __init__(self, num_tests, num_vars, num_clauses, solver = kissat, parser = basic_parser, generator = mixed_generator):
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
		total_sat = 0
		for i in range(self.__num_tests):
			total_sat += 1 if self.run_test(i) else 0
		return total_sat / self.__num_tests

num_tests = int(input("Enter the number of tests: "))

with open("./results/mixed_3_4_gent.csv", "w") as f:
	f.write("vars,clauses,probability\n")
	for num_vars in [25, 50, 75]:
		# p = 1.5 / num_vars
		# generator = CPM_Generator(p)
		generator = mixed_generator
		begin, end, step = num_vars // 5, 9 * num_vars, num_vars // 5
		for num_clauses in range(begin, end, step):
			experiment = Experiment(num_tests, num_vars, num_clauses, generator = generator, solver = kissat, parser = basic_parser)
			prob = experiment.run_experiment()
			f.write(str(num_vars) + "," + str(num_clauses) + "," + str(prob) + "\n")
			print(num_vars, num_clauses)




	


