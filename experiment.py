from solver import Kissat_Solver
from clause_generator import Mixed_3_4_Generator, CPM_Generator
from result_parser import Basic_Kissat_Parser, Kissat_Parser

kissat = Kissat_Solver("./../kissat-master/build/kissat")
mixed_generator = Mixed_3_4_Generator()
basic_parser = Basic_Kissat_Parser
kissat_parser = Kissat_Parser

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
		results = {}
		for key in self.__parser.keys():
			results[key] = 0
		for i in range(self.__num_tests):
			test_result = self.run_test(i)
			for (key, value) in test_result.items():
				results[key] += value
		for key in results:
			results[key] /= self.__num_tests
		return results
		
def mixed_limits(num_vars):
	return (num_vars // 5, num_vars * 10, num_vars // 5)

def cpm_limits(num_vars):
	return (num_vars // 5, 7*num_vars + 1 , num_vars // 5)

def test_phase_transition(variables, clauses_limits, generators, parser, solver, path, num_tests):
	with open(path, "w") as f:
		f.write("vars, clauses,")
		f.write(",".join(parser.keys()))
		f.write('\n')
		
		for i in range(len(variables)):
			num_vars, generator = variables[i], generators[i]
			begin, end, step = clauses_limits(num_vars)
			for num_clauses in range(begin, end, step):
				experiment = Experiment(num_tests, num_vars, num_clauses, generator = generator, solver = solver, parser = parser)
				results = experiment.run_experiment()
				f.write(str(num_vars) + ", " + str(num_clauses) + ",")
				results = list(map(str, results.values()))
				f.write(",".join(results))
				f.write('\n')
				print(num_vars, num_clauses)


num_tests = int(input("Enter the number of tests: "))

generators = [CPM_Generator(1.5/25), CPM_Generator(1.5/50), CPM_Generator(1.5/75), CPM_Generator(1.5/100)]
test_phase_transition([25, 50, 75, 100], cpm_limits, generators, kissat_parser, kissat, "./results/cp_proba.csv", num_tests)
				
				
				
				
				
