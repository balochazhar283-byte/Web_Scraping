#Using the python library of request module
import requests

respone=requests.get("https://www.ibm.com/think/topics/vector-database")

#creating the variable to store data in the memory

ibmfile=open("ibmfile.bin","wb")
#writing data in the ibmfile in the text fromat

for data in respone.iter_content():
    #writing in the ibmfile
    ibmfile.write(data)

#closing the file
ibmfile.close() 

