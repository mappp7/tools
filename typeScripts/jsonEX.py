import json

testJson ={ 'TEST' : { 'aaa':[], 'ccc':['ddd'], 'eee':'fff' } }


filePath = '/home/taehoon.kim/Desktop/TESTJSON.json'



# write
F = open( filePath, 'w' )

F.write(json.dumps( testJson, indent = 4 ))

F.close()

# load
F = open( filePath )
loadedData = json.load( F )
F.close()


##############same##############################################
# write
with open( filePath, 'w' ) as outFile:
    outFile.write(json.dumps( testJson, indent = 4 ))
# load
with open( filePath ) as dataFile:
    loadedData = json.load(dataFile)

