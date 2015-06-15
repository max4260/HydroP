import os

#start either one or all scripts in the ../monitor folder
class Start(object):

	def All():
		for filename in os.listdir('../monitor'):
			#do stuff for each file found
		
	def One(module):
		#do stuff for single file

#stop either one or all scripts in the ../monitor folder
class Stop(object):

	def All():
		#set database so all files stop
		
	def One(module):
		#et database so specific file stops files stop