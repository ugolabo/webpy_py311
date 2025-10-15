helloFile = open('new2.txt', 'r')
helloContent = helloFile.read()

line = helloContent.strip()
print(line)
print("=" * 25)

start = 0
w = 50

# get the length of long line
line_length = len(line)

# loop through the long line using the desired line
# width
while line_length - start >= w:
      print(line[start:start+w])
      start += w
# The rest of the line that does not completely
# use a line of length w
print(line[start:])

helloFile.close()

'''
linux script

# do one file
fold -sw 40 text1.txt > text2.txt

# loop throught many files
for i in *.txt
do
  fold -sw 40 $i > $i.output
done

# links
nicCraft
http://www.cyberciti.biz/


# Advanced Bash-Scripting Guide
http://www.tldp.org/LDP/abs/html/index.html

# fold and fmt command
http://www.tldp.org/LDP/abs/html/textproc.html

# Unix & Linux Stack Exchange is a question and answer site for users of Linux
http://unix.stackexchange.com/

# Command line reference – Web, Database and OS scripting
http://ss64.com/

# Linux Guide/Linux commands wikibooks
https://en.wikibooks.org/wiki/Linux_Guide/Linux_commands

# blog/website that offers command line tips for Linux/Mac OS X newbies
# Linux and Python Tips
http://cmdlinetips.com/
'''



