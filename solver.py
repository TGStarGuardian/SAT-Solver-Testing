from abc import ABC, abstractmethod
from os import fork, pipe, close, write, wait, dup2, execv, fdopen
from sys import exit
from cnf_generator import DIMACS

class Solver(ABC):
	@abstractmethod
	def initialise_input(self, params):
		pass
	
	@abstractmethod
	def solve(self, params):
		pass
	
	def run(self, **kwargs):
		input_params = self.initialise_input(**kwargs)
		output = self.solve(input_params)
		return output

class Kissat_Solver(Solver):
	
	def __init__(self, path):
		self.__path = path
	
	def initialise_input(self, **kwargs):
		return DIMACS.create_file(clauses = kwargs['clauses'], path = "./formulae/" + str(kwargs['test_id']) + ".cnf", num_vars = kwargs['num_vars'])
	
	def solve(self, cnf_path):
		# start a process
		try:
			r, w = pipe()
			
			pid = fork()
			
			if pid == 0:
				# child process
				close(r)
				# redirect stdout to w
				dup2(w, 1)
				args = [self.__path, cnf_path]
				# the process now becomes:
				# kissat params
				execv(self.__path, args)
				# close pipe
				close(w)
				
				exit("Child Finished")
			else:
				# parent process
				close(w)
				# wait for the child to finish
				status = wait()
				# open r in the reading mode
				r = fdopen(r)
				# read the results
				result = r.read()
				r.close()
				
				return result
				
		except OSError as e:
			print(e)
			exit("Could not fork!")

# kissat = Kissat_Solver("./../kissat-master/build/kissat")
# result = kissat.solve("./test/proba.cnf")
# print(result)

