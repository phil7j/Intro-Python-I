"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open(r"C:\Users\phil7\Documents\Projects\Lambda\CS\python\Intro-Python-I\src\foo.txt", "r")
foo = f.read()
print(foo)
f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
bar = open(
    r"C:\Users\phil7\Documents\Projects\Lambda\CS\python\Intro-Python-I\src\bar.txt", "w")
bar.write("This is the first line")
bar.write("\n This is the second line")
bar.write("\n This is the third line")
bar.close()
# YOUR CODE HERE
