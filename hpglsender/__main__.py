from argparse import ArgumentParser
from serial import Serial
import time
import os

def show_progress(pos, total, length=100):
    fill = length * pos // total
    print('\rProgress: [' + fill * '\u2592' + (length-fill) * '\u2591' + '] ' + str(pos) + ' of ' + str(total), end='\r')
    if pos == total:
        print()
    return 0

def fileCheck(checkFile="/Users/user/Desktop/hpglsender/test.txt", position=0):
    
    transport_string = []
    
    def charCheck():
        CCC = transport_string[(len(transport_string)-1)]
        if (CCC != "," and CCC != ";"):
            print("A"+transport_string[(len(transport_string)-1)])
            return 1
        elif (CCC == "," or CCC == ";"):
            print("B"+transport_string[(len(transport_string)-1)])
            return 0
        elif (CCC == '\0'):
            print("C"+transport_string[(len(transport_string)-1)])
            return 2
        else:
            print("F"+transport_string[(len(transport_string)-1)])
            return None
    
    def byteRead(readFile, readPos):
        readFile.seek(readPos)
        return readFile.read(1)
        
    
    distIntoFile = position
    checkFile = open(checkFile, "r")
    transport_string = byteRead(checkFile, distIntoFile)
    print("yo", transport_string)
    distIntoFile += 1       #idk why but this makes it work
    charOK = 0
    
    while charOK == 0:
        CDC = charCheck()
        print("hecc ", transport_string)
        if (CDC == 0):
            charOK = 1
            #time.sleep(sleepTime)
            pauseBit = 1
            print("cc0")
            print("dist ", distIntoFile)
        elif (CDC == 2):
            charOK = 1
            pauseBit = 0
            print("cc1")
              #break or whatev
        elif (CDC == 1):
            charOK = 0
            pauseBit = 0
            print("cc2")
            transport_string += byteRead(checkFile, distIntoFile)
            distIntoFile += 1
            print("dist ", distIntoFile)
    
    checkFile.close()
    returnDataStruct = namedtuple('returnDataStruct', 'int_Dist, str_Data, bool_Pause')
    returnData = returnDataStruct(distIntoFile, transport_string, pauseBit)
            
    return returnData;
        
        

def main():
    parser = ArgumentParser()
    parser.add_argument('port', default='/dev/tty.usbserial',
                        help='serial port location, def: /dev/tty.usbserial')
    parser.add_argument('file', help='/path/to/file.hpgl')
    parser.add_argument('--sleeptime', default=5,
                        help='seconds to wait for plotter to clear buffer, def:5')
    args = parser.parse_args()
    
    serial = Serial(port=args.port, timeout=0) #open port
    
    fileSize = os.path.getsize(args.file)
    distanceIntoFile = 0
    pos = 0
    while distanceIntoFile < fileSize:
        dataTuple = fileCheck(args.file, pos)
        distanceIntoFile = dataTuple.int_Dist
        dataPacket = dataTuple.str_Data
        doPause = dataTuple.bool_Pause
        if doPause == 1:
            #actually send serial line the dataPacket
            serial.write(dataPacket)
            time.sleep(args.sleeptime)
    
