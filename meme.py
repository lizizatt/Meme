import os.path
import sys

def run(toReplace, originalFile, substituteFile, outFile):

	if os.path.isfile(originalFile): 

		origFile = open(originalFile, "r")
		out = open(outFile, "w")

		subFileString = ""
		if (os.path.isfile(substituteFile)):
			subFile = open(substituteFile, "r")
			subFileString = subFile.read()
			subFileString = subFileString.replace("\n", "")
			subFileString = subFileString.decode('utf-8').encode("ascii", errors="ignore").decode() #this mess strips non-ascii characters
		else:
			subFileString = substituteFile

		substr = toReplace

		print "Opened files, parsing and writing output..."

		#the actual substitution happens here
		for origFileLine in origFile:
			origFileLine = origFileLine.replace("\n", "")
			if (len(origFileLine) > 0):
				toWrite = ""
				while (origFileLine.count(substr) > 0):	
					toWrite += origFileLine[:origFileLine.index(substr)];
					origFileLine = origFileLine[origFileLine.index(substr) + len(substr):]
					toWrite += subFileString
				out.write(toWrite + origFileLine + "\n")

		print "Done."
	else:
		print "Couldn't find file"

def runDefault():
	run("bee", "beemovie.txt", "myimmortal.txt", "meme.txt")

def printInstructions():
	print
	print "Meme Generator"
	print "----------------------------"
	print "Arg1: keyword string"
	print "Arg2: input text file"
	print "Arg3: replacement text file or string"
	print "Arg4: output text file"
	print "Example: 'python meme.py bee beemovie.txt myimmortal.txt meme.txt"
	print "Example: 'python meme.py bee beemovie.txt thiswordwillreplacebee meme.txt"
	print "----------------------------"
	print "If the arguments are incorrect, default arguments of 'beemovie.txt', 'myimmortal.txt', and 'meme.txt' will be used"
	print "----------------------------"
	print


def runInteractive():
	printInstructions()
	print sys.argv
	if (len (sys.argv) == 5):
		run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	else:
		runDefault()


runInteractive()

	


		