
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
		
			
	def get_number_of_updated_commits(self,data):
		count = 0
		for line in data:
			if line.startswith("Updated"):
				word = line.split()
				print word[0:2]
				count = count + 1
		return count
		
	def get_authors(self,data):
		sep = 72*'-'
		authors = []
		index = 0
		
		while index < len(data):
			try:
				index = data.index(sep, index + 1)
				details = data[index + 1].split('|')
				author = details[1].strip()
				if author not in authors:
					authors.append(author)
			except IndexError:
				break
		return authors 
		
	