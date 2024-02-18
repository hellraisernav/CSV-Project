# Import libraries
import csv,re,os,sys,shutil
from pathlib import Path
from re import search
q=True
while(q==True):
    #  Get the address from input
    addressInput=input("Enter the address: ")
    print(addressInput)

    aISplit=addressInput.split(os.path.sep)
    print(aISplit)
    addressInput=Path(addressInput)
    os.chdir(addressInput)
    print(os.getcwd())

    # Start Walking down the file list
    def walkPath(aInput):
        
        z=[]
        for root,dirs,files in os.walk(aInput):
            for file in files:
                a=[]
                b=removeEnum(file)
                x=titleName(b)
                os.rename(file,x+Path(file).suffix)
                fullString=x
                subString="By"
                if search(subString,fullString):
                    fullString=fullString.split(subString)
                    a.append(fullString)
                else:
                    a.append(x)
                z.append(a)
                print(z)

        return z

            
            

    def titleName(fileName):
        newName=(Path(fileName).stem)
        newName=newName.title() 
        return newName   

    def removeEnum(fileName):
        newName=re.sub('^\d{1,}[-\.\s]','',fileName)
        return newName
    z=walkPath(addressInput)


    #  Use the folder Names csv file name
    csvN=aISplit[-1]
    csvNExtenstion=csvN+'.csv'
    outputFile= open(csvNExtenstion,'w',newline='')
    outputWriter=csv.writer(outputFile,dialect="excel")
    outputWriter.writerows(z)
    outputFile.close()

    confirmVar=input("do you want to do another one? y/n:")
    if confirmVar=="y":
        q=True
    else:
        q==False
        break

    # TODO: Write each file name based or regex as a csv row
    # yearInName

    # remove By
    # TODO: Do before state until all files were handled

    # TODO: Populate the csv file

    # TODO: save the csv file

