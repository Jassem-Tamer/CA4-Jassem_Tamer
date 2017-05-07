from file import Commit

d = Commit()
data = d.read_file("file.txt")
excel = d.transfer_to_excel(data)
authors = d.get_authors(data)
count = d.get_number_of_updated_commits(data)
count1 = d.get_specific_author(data)
commits = d.get_commits(data)
commits.reverse()
for index, commit in enumerate(commits):
	print "Authors and their contributions in file: \n", (commit.get_commit_comment())
	



print "There are {} lines in the file starting with word 'Updated' \n".format(count)
print "The file contains {} lines \n".format(len(data))
print "The file has {} commits by different authors \n".format(len(commits))
print "Authors who commit the file are: \n{} ".format(authors)
print "Total number of committers is: \n{} ".format(len(authors))
print "The first author who commits is {} at time {} \n".format((commits[0].author),(commits[0].date))
print "The last author who commits is {} at time {} \n".format((commits[421].author),(commits[421].date))
print "Author 'Thomas' has the highest {} commits in the file \n".format(count1)















