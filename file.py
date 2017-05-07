
class Commit(object):
	def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
		self.revision = revision
		self.author = author
		self.date = date
		self.comment_line_count = comment_line_count
		self.changes = changes
		self.comment = comment
		
		
	def read_file(self,data):
		while True:
			str_input = raw_input("Please enter your file name")
			try:
				data = [line.strip() for line in open(str_input)]
				return data
			except:
				print "File is not existed!!!!"
				continue
		
			
	