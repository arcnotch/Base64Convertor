import base64
import argparse

parser = argparse.ArgumentParser(description='Base64 Convertor')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-d","--decode", action="store_true", default=False,help="Encode/Decode")
group.add_argument("-e","--encode", action="store_true", default=False,help="Encode/Decode")
parser.add_argument("-i","--input",help="Input a file to convert", required=True)
parser.add_argument("-o","--output", help="Output the converted data to a file", required=True)
args = parser.parse_args()

def opening():
    string = """ ____                   __ _  _    _____                          _             
|  _ \                 / /| || |  / ____|                        | |            
| |_) | __ _ ___  ___ / /_| || |_| |     ___  _ ____   _____ _ __| |_ ___  _ __ 
|  _ < / _` / __|/ _ \ '_ \__   _| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \| '__|
| |_) | (_| \__ \  __/ (_) | | | | |___| (_) | | | \ V /  __/ |  | || (_) | |   
|____/ \__,_|___/\___|\___/  |_|  \_____\___/|_| |_|\_/ \___|_|   \__\___/|_|   
"""
    print(string)

def Encode():
    try:
        print("Encoding",args.input)
        with open(args.input,"rb") as file:
            encoded = base64.b64encode(file.read())
        with open (args.output,"wb+") as io:
            io.write(encoded)
            print("Encoded successfully! The output file location is:",args.output)
    except Exception as e:
        print(e)
		
def Decode():
    try:
        print("Decoding",args.input)
        with open(args.input,"rb") as file:
            decoded = base64.b64decode(file.read())
        with open(args.output,"wb+") as io:
            io.write(decoded)
            print("Decoded successfully! The output file location is:",args.output)
    except Exception as e:
        print(e)
		
def main():
    opening()
    if (args.encode):
        Encode()
    if (args.decode):
        Decode()
       
if __name__ == '__main__':
    main()
        