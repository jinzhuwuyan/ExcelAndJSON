 # encoding: utf-8
__author__ = 'goldlion'
__qq__ = 233424570
__email__ = 'gdgoldlion@gmail.com'

import xlrd
import sys
import getopt

import SheetManager

#单表模式
def singlebook():
    opts, args = getopt.getopt(sys.argv[2:], "hi:o:")

    for op, value in opts:
        if op == "-i":
            file_path = value
        elif op == "-o":
            output_path = value
        elif op == "-h":
            #TODO 写说明文�?
            # usage()
            sys.exit()

    if not "file_path" in locals().keys():
        # usage()
        sys.exit()
    elif not "output_path" in locals().keys():
        # usage()
        sys.exit()
    print file_path
    SheetManager.addWorkBook(file_path)
    sheetNameList = SheetManager.getSheetNameList()
    print sheetNameList
    for sheet_name in sheetNameList:
        #单表模式下，被引用的表不会输�?
        if SheetManager.isReferencedSheet(sheet_name):
            continue

        sheetJSON = SheetManager.exportJSON(sheet_name)
        sheet_name = sheet_name.replace(".json", "")
        f = file(output_path+sheet_name+'.json', 'w')
        f.write(sheetJSON.encode('UTF-8'))
        f.close()

#主表模式
def mainbook():
    opts, args = getopt.getopt(sys.argv[2:], "hi:o:")

    for op, value in opts:
        if op == "-i":
            file_path = value
        elif op == "-o":
            output_path = value
        elif op == "-h":
            #TODO 写说明文�?
            # usage()
            sys.exit()

    if not "file_path" in locals().keys():
        # usage()
        sys.exit()
    elif not "output_path" in locals().keys():
        # usage()
        sys.exit()

    #获取主表各种参数#
    wb = xlrd.open_workbook(file_path)
    sh = wb.sheet_by_index(0)

    workbookPathList = []
    sheetList = []
    for row in range(sh.nrows):
        type = sh.cell(row,0).value

        if type == '__workbook__':
            pass
        else:
            sheetList.append([])
            sheet = sheetList[-1]
            sheet.append(type)

        for col in range(1,sh.ncols):
            value = sh.cell(row,col).value

            if type == '__workbook__' and value != '':
                workbookPathList.append(value)
            elif value != '':
                sheet.append(value)

    #加载所有xlsx文件#
    for workbookPath in workbookPathList:
        #读取所有sheet
        SheetManager.addWorkBook(workbookPath+".xlsx")

    #输出所有表#
    for sheet in sheetList:

        #表改名处�?
        if '->' in sheet[0]:
            sheet_name = sheet[0].split('->')[0]
            sheet_output_name = sheet[0].split('->')[1]
        else:
            sheet_output_name = sheet_name = sheet[0]

        sheet_output_field = sheet[1:]

        sheetJSON = SheetManager.exportJSON(sheet_name,sheet_output_field)

        f = file(output_path+sheet_output_name+'.json', 'w')
        f.write(sheetJSON.encode('UTF-8'))
        f.close()

if __name__ == '__main__':
    modelType =  sys.argv[1]

    if modelType == "singlebook":
        singlebook()
    elif modelType == "mainbook":
        mainbook()
    else:
        # usage()
        sys.exit()