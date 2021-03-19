from pefile import PE

from pefile import *
import sys
def getPE(file):
    if(PE(file)==True):
        PEFileInstance = PE(file, data='module.dll')
        yeet = PEFileInstance.dump_info().strip().split('\n')
        pedata = []
        keys = ['SizeOfOptionalHeader','Characteristics','MajorLinkerVersion','MinorLinkerVersion','SizeOfCode','SizeOfInitializedData','SizeOfUninitializedData','AddressOfEntryPoint','BaseOfCode','BaseOfData','ImageBase','SectionAlignment','FileAlignment','MajorOperatingSystemVersion','MinorOperatingSystemVersion','MajorImageVersion','MinorImageVersion','MajorSubsystemVersion','MinorSubsystemVersion','SizeOfImage','SizeOfHeaders','CheckSum','Subsystem','DllCharacteristics','SizeOfStackReserve','SizeOfStackCommit','SizeOfHeapReserve','SizeOfHeapCommit','LoaderFlags','NumberOfRvaAndSizes','SectionsMeanVirtualsize','SectionsMinVirtualsize','SectionMaxVirtualsize']
        for key in keys:
            for x in range(len(yeet)):
                if(yeet[x].find(key)!=-1):
                    pedata.append(int(str(yeet[x][48:].strip()),16))
                    break
        print(pedata)
if __name__ == '__main__':
    getPE(sys.argv[1])
