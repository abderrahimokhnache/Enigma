from subprocess import call as shell

def File(**kwargs):
	"""This Fucntion is Shortcut for File operations
			Example : File(Path = test.txt , Mode = 'wb' , Content = 'test', stat = [True , "+h +r +s"]) """
	Data = kwargs 
	
	with open(Data['Path'] , Data['Mode']) as file :
		
		if file.mode == 'r' or file.mode == "rb" == file.mode == "r+":
		
			return file.read()
		
		if file.mode == 'w' or file.mode  == "a" or file.mode  == "wb":
			
			file.write(Data['Content'])

		if file.mode  == "rl":
			return file.readlines()
			
			# shell('attrib {} {}'.format(Data['stat'][1] ,Data['Path']))





def header(Path , header):
	"""This Fucntion write headers for file like csv...ext
		Example : header(test.txt , 'Data, Date')
		"""
	
	try:
		
		with open(Path , 'r') as file :
			
			try:
				
				f_line = next(file)
			
				if header != f_line :
				
					open(Path , "a").write(header)
					
			
			except StopIteration :

				open(Path , "a").write(header)					

	except IOError as e :

		with open(Path , 'wb') as file:

			file.write(header)

def more(**kwargs):

	Data = kwargs 

	shell('more {}'.format(Data['Path']), shell = 1)
	
	shell('del {}'.format(Data['Path']), shell = 1)
