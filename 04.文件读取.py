# #打开文件
# f = open("望庐山瀑布", "r", encoding="utf-8")
#
# #读取文件
# # content = f.read()
# # print(content)
# # content_list = f.readlines()
# # for line in content_list:
# #     print(line.strip())
#
# #关闭文件
# f.close()

#写文件

with open("静夜思.txt", "w", encoding="utf-8") as f:
    f.write("窗前明月光，\n")
    f.write("疑似地上霜, \n")
    f.write("举头望明月, \n")
    f.write("低头思故乡.")



