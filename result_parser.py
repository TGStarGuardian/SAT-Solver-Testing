from abc import ABC, abstractmethod

class Results_Parser(ABC):
	
	def __init__(self):
		super().__init__()
	
	@classmethod
	@abstractmethod
	def parse(cls, raw_data):
		pass
	
	@classmethod
	@abstractmethod
	def keys(cls):
		pass
		
class Basic_Kissat_Parser(Results_Parser):
	
	def __init__(self):
		super().__init__()
	
	@classmethod
	def parse(cls, raw_data):
		return not "UNSATISFIABLE" in raw_data
	
	@classmethod
	def keys(cls):
		return ['prob']
		
class Kissat_Parser(Results_Parser):
	
	def __init__(self):
		super().__init__()
		
	@classmethod
	def parse(cls, raw_data):
		results = {}
		results['sat'] = not "UNSATISFIABLE" in raw_data
		begin, end = raw_data.find("[ statistics ]"), raw_data.find("[ glue usage ]")
		data = raw_data[begin : end].split()
		for i in range(len(data)):
			if "conflicts" in data[i]:
				results['conflicts'] = int(data[i + 1])
			elif "decisions" in data[i]:
				results['decisions'] = int(data[i + 1])
			elif "propagations" in data[i]:
				results['propagations'] = int(data[i + 1])
			elif "switched" in data[i]:
				results['switched'] = int(data[i + 1])
		
		return results
		
	@classmethod
	def keys(cls):
		return ['sat', 'conflicts', 'decisions', 'propagations', 'switched']
		
		
		
