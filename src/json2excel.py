import sys
import json
import SheetManager
import os

reload(sys)
sys.setdefaultencoding("utf-8")

def saveJson(jsonPath, exportPath = ""):
	SheetManager.clearJson()
	SheetManager.addJson(jsonPath)
	excelPath = jsonPath.replace("json", "xls")
	if(exportPath.__len__() != 0):
		if(exportPath[-4:] == ".xls"):
			print "receive fileName, ", exportPath
			exportPath = os.path.abspath(exportPath)
		elif os.path.exists(exportPath):
			exportPath = "".join([os.path.abspath(exportPath), "\\", os.path.basename(jsonPath).replace(".json", ".xls")]) 
		excelPath = exportPath
	SheetManager.saveWorkBook(excelPath)
	return

if __name__ == "__main__":
	
	jsonPath, exportPath =  sys.argv[1], sys.argv[2] 
	if(jsonPath[-5:] == ".json"):
		saveJson(os.path.abspath(jsonPath), exportPath)
	elif(os.path.exists(jsonPath)):
		for root, dirs, files in os.walk(jsonPath):
			for name in files:
				if root == jsonPath and name[-5:] == ".json":
					jsonDir = "".join([os.path.abspath(jsonPath), "\\", name])
					saveJson(jsonDir, exportPath)
			break
			
				



