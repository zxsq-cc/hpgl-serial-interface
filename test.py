#### def function(file to check, distance into file):
    # read(file) at (position, default:0) to (position+512)
    # save chars in a string
    # save last read position
    # if last char...
            # = "," or ";" then time.sleep(5)
            # = \0 then break
            # else
                #read next character in file
                #append to string
                # +1 to read position
        # return read position
import time

def fileCheck(checkFile="/Users/user/Desktop/hpglsender/test.txt", position=0):
    
    transport_string = []
    
    def charCheck(checkCharPos):
        CCC = transport_string[checkCharPos-1]
        if (CCC != "," and CCC != ";"):
            print("A"+transport_string[checkCharPos-1])
            return 1
        elif (CCC == "," or CCC == ";"):
            print("B"+transport_string[checkCharPos-1])
            return 0
        elif (CCC == '\0'):
            print("C"+transport_string[checkCharPos-1])
            return 2
    
    def chunkRead(readFile, readPos):
        readFile.seek(readPos)
        return readFile.read(5)
    
    def byteRead(readFile, readPos):
        readFile.seek(readPos)
        return readFile.read(1)
        
    
    distIntoFile = position
    checkFile = open(checkFile, "r")
    transport_string = chunkRead(checkFile, distIntoFile)
    distIntoFile == 5       #512
    charOK = 0
    
    while charOK == 0:
        CDC = charCheck(distIntoFile)
        if (CDC == 0):
            charOK = 1
            time.sleep(5)
            print("cc0")
        elif (CDC == 2):
            charOK = 1
            print("cc1")
              #break or whatev
        elif (CDC == 1):
            charOK = 0
            print("cc2")
            transport_string += byteRead(checkFile, distIntoFile)
            distIntoFile += 1
            
    
fileCheck()
          
          
          
          
####Output:
# Ae
# cc2
# Aa
# cc2
# Ab
# cc2
# Ac
# cc2
# Ad
# cc2
# Ae
# cc2
# Aa
# cc2
# Ab
# cc2
# Ac
# cc2
# Ad
# cc2
# Ae
# cc2
# B;
#           