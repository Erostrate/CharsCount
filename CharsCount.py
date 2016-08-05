'''
版本v1.0:
对txtfiles中的.txt文件进行字符统计(不含换行符\n)，
并且按照UNICODE正序写入chars.txt。输入文本编码必须为utf-16，带BOM头。
支持子目录下的文件
版本v1.1:
增加字频统计，按照出现次数由少到多写入文件charscount.txt
'''
import os,fnmatch,sys,operator

#递归遍历一个目录下所有文件（含子目录），返回包含目录中所有文件的文件名的列表，对于空目录及空子目录不返回任何值。
#增加按模式匹配功能，默认返回所有文件(*)，也可以只返回匹配的文件列表
#参数1:目录名称
#参数2:匹配模式，默认*
def walk(dirname,pattern='*'):
    filelist=[]
    for root,dirs,files in os.walk(dirname):
        for filename in files:
            fullname=os.path.join(root,filename)
            filelist.append(fullname)
    return fnmatch.filter(filelist,pattern)


#主程序
filelist=walk('txt_files','*.txt')
charsdict={}
for file in filelist:
    with open(file,'r',encoding='utf-16') as txtfile:
        #读取全部字符并去掉字符中的换行符\n
        chars=txtfile.read().replace('\n','')
        #依次遍历字符，建立字典
        for char in chars:
            charsdict[char]=charsdict.get(char,0)+1
#将字典中的字符按照UNICODE正序排列，并写入文件
with open('chars.txt','w',encoding='utf-16') as charfile:
    for char in sorted(charsdict):
        charfile.write(char)
print('共有%i个字符写入文件chars.txt.'%(len(charsdict)))
#将字典转换为元组对列表，按照出现次数进行排序，并按照从少到多的顺序写入文件
with open('charscount.txt','w',encoding='utf-16') as charfile:
    for (char,counts) in sorted(list(charsdict.items()),key=operator.itemgetter(1)):
        charfile.write('%s %s\n'%(char,counts))
print('每个字符出现的次数已按照由少到多的顺序写入文件charscount.txt.')
os.system('pause')
