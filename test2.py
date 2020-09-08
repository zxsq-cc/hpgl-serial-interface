#file=open(path, "r")
#
#file_transport = []
#
#file_transport = file.read(512)
##if (file_transport[511] != "," or file_transport[511] != ";"):
#    
#def charCheck(pos):
#    if (file_transport[pos-1] != "," or file_transport[pos-1] != ";"):
#        return 1
#    elif (file_transport[pos-1] = "," or file_transport[pos-1] = ";"):
#        return 0
#    elif (file_transport[pos-1] = \0):
#        return 2
#    
#if (charCheck(pos) = 0):
#    #wait a bit
#elif (charCheck(pos) = 2):
#    #do nothing, maybe break?
#elif (charCheck(pos) = 1):
#    #nextChar = file.seek(pos+1, 0)
#    #file_transport.append(nextChar)
def main():
    checkFile=open("/Users/user/Desktop/hpglsender/test.txt", "r")
    position=0
    def chunkRead(readFile, readPos):
        readFile.seek(readPos)
        return readFile.read(5)
    
    print(chunkRead(checkFile, position))
main()