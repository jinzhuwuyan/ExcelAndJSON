import sys
import json
import SheetManager
import os

if __name__ == "__main__":
	jsonPath =  sys.argv[1]
	if(os.path.exists(jsonPath)):
		for root, dirs, files in os.walk(jsonPath, topdown=False):
			for name in files:
				if name[-5:] == ".json":
					
					jsonPath = os.path.abspath(name)
					SheetManager.addJson(jsonPath)
					excelPath = jsonPath.replace("json", "xls")
					SheetManager.saveWorkBook(excelPath)
				



