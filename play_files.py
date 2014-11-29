fname = raw_input('Enter the file name: ')
if fname=='na na boo boo':
    print "NA NA BOO BOO TO YOU - You have been punk'd!"
try:
    fhand = open(fname)
except: 
    print "File doesn't exist"
    exit()
#print and count lines starting with "Subject"
#count = 0
#for line in fhand:
#    if line.startswith('Subject:') :
#        print line.rstrip()
#        count = count + 1
#print 'There were', count, 'subject lines in', fname

#----------------------------------------------------------
#Exercise 1   
#Write a program to read through a file and 
#print the contents of the file (line by line) all in upper case.
#for line in fhand:
#    print line.rstrip().upper()
#----------------------------------------------------------

#Exercise 2   
#Write a program to prompt for a file name, 
#and then read through the file and look for lines of the form:
#X-DSPAM-Confidence:  0.8475
#When you encounter a line that starts with 'X-DSPAM-Confidence:' 
#pull apart the line to extract the floating point number on the line.
#Count these lines and the compute the total of the spam confidence values 
#from these lines. 
#When you reach the end of the file, print out the average spam confidence.

count_spam=0
total=0.
for line in fhand:
    line=line.rstrip().lower()
    if line.startswith('x-dspam-confidence:') :
        count_spam=count_spam+1
        a=line.find(':')
        conf_str=line[a+1:len(line)]
        conf=float(conf_str.strip())
        total=total+conf
print "Average spam confidence: ", total/float(count_spam)
