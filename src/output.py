# encoding: utf-8
import sys
import os
if __name__ == "__main__":
    file_name = sys.argv[1]
    try:
        os.system(".\excel_and_json.exe singlebook -o ..\Config\ -i %s" % file_name);
    except:
        import traceback
        print traceback.format_exc();
        print "发生错误，生成失败！".decode("utf-8").encode("gbk")
    else:
        input("已完成！输入回车键关闭程序".decode("utf-8").encode("gbk"))