#!/usr/bin/python
import sys, getopt
def main(argv):
    inputfile = ''
    outputfile = '' 
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
    ifile = open(inputfile, 'r')    
    ofile = open(outputfile, 'w')
    lines = ifile.readlines()
    for l in lines:
        spL = l.split(" , ")
        if len(spL)>=3:
            ofile.write("<tr>\n")
            ofile.write("<td class = \"time\">"+spL[0]+"</td>\n")
            ofile.write("<td class=\"marker marker-"+spL[1].lower()+"\">"+spL[1]+"</td>\n")
            ofile.write("<td>"+spL[2]+"</td>\n")
            ofile.write("<td>"+"</td>\n")
            ofile.write("</tr>\n")
    ofile.close()
if __name__ == "__main__":
   main(sys.argv[1:])
