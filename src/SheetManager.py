# encoding: utf-8
__author__ = 'goldlion'
__qq__ = 233424570
__email__ = 'gdgoldlion@gmail.com'

import xlrd
import json
import Sheet
import xlwt

sheetDict = {}
sheetNameList = []
sheetJsonDict = {}

def saveWorkBook(filepath):
    wb = xlwt.Workbook(encoding="utf-8");
    for sheetName in sheetNameList:
        sheet = wb.add_sheet(sheetName)
        sheetObj = Sheet.Sheet(sheet, sheetJsonDict[sheetName]);
        sheetObj.SaveToExcel()
    wb.save(filepath)
        
        
def clearJson():
    global sheetNameList
    global sheetJsonDict
    sheetNameList = []
    sheetJsonDict = {}

def addWorkBook(filepath):
    wb = xlrd.open_workbook(filepath)
    for sheet_index in range(wb.nsheets):
        try:
            sh = wb.sheet_by_index(sheet_index)
            sheet = Sheet.openSheet(sh)
            addSheet(sheet)
        except:
            import traceback
            print traceback.format_exc()
            continue
        

def addSheet(sheet):
    sheetDict[sheet.name] = sheet
    sheetNameList.append(sheet.name)

def addJson(jsonPath):
    import os
    jsonName = os.path.basename(jsonPath)
    with open(jsonPath, "r") as fd:
        if(fd):
            jsonStr = fd.read()
            sheetJsonDict[jsonName] = jsonStr;
            sheetNameList.append(jsonName)


def getSheet(name):
    return sheetDict[name]

def getSheetNameList():
    return sheetNameList

def exportJSON(name,sheet_output_field = []):
    return sheetDict[name].toJSON(sheet_output_field)

def isReferencedSheet(name):
    for sheetName in sheetDict:
        if name in sheetDict[sheetName].referenceSheets:
            return  True

    return False