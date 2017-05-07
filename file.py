
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
		
	def get_specific_author(self,data):
		sep = 72*'-'
		index = 0
		count = 0
		while index < len(data):
			try:
				index = data.index(sep, index + 1)
				details = data[index + 1].split('|')
				author = details[1].strip()
				if author == "Thomas":
					count += 1
			except IndexError:
				break
		return count
    
	def get_commit_comment(self):
		return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
			+ self.author + ' with the comment ' + ','.join(self.comment) \
			+ ' and the changes ' + ','.join(self.changes)
    
	def get_commits(self,data):
		commits = []
		current_commit = None
		index = 0
		sep = 72*'-'
		
		while True:
			try:
				# parse each of the commits and put them into a list of commits
				current_commit = Commit()
				details = data[index + 1].split('|')
				current_commit.revision = int(details[0].strip().strip('r'))
				current_commit.author = details[1].strip()
				current_commit.date = details[2].strip()
				current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
				current_commit.changes = data[index+2:data.index('',index+1)]
				#print(current_commit.changes)
				index = data.index(sep, index + 1)
				current_commit.comment = data[index-current_commit.comment_line_count:index]
				commits.append(current_commit)
			except IndexError:
				break
		return commits 
		
	
	


