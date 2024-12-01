from abc import ABC, abstractmethod

class Results_Parser(ABC):
	
	def __init__(self):
		super().__init__()
	
	@classmethod
	@abstractmethod
	def parse(cls, raw_data):
		pass
		
class Kissat_Parser(Results_Parser):
	
	def __init__(self):
		super().__init__()
	
	@classmethod
	def parse(cls, raw_data):
		return raw_data

