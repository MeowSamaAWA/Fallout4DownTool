import os
import fnmatch
import sys
import zipfile


# Files
deleteFiles = [
    "ccBGSFO4044-HellfirePowerArmor.esl",
    "ccBGSFO4046-TesCan - Textures.ba2",
    "ccBGSFO4046-TesCan - Main.ba2",
    "ccBGSFO4046-TesCan.esl",
    "ccBGSFO4096-AS_Enclave - Main.ba2",
    "ccBGSFO4096-AS_Enclave - Textures.ba2",
    "ccBGSFO4096-AS_Enclave.esl",
    "ccBGSFO4110-WS_Enclave - Main.ba2",
    "ccBGSFO4110-WS_Enclave - Textures.ba2",
    "ccBGSFO4110-WS_Enclave.esl",
    "ccBGSFO4115-X02 - Main.ba2",
    "ccBGSFO4115-X02 - Textures.ba2",
    "ccBGSFO4115-X02.esl",
    "ccBGSFO4116-HeavyFlamer - Main.ba2",
    "ccBGSFO4116-HeavyFlamer - Textures.ba2",
    "ccBGSFO4116-HeavyFlamer.esl",
    "ccFSVFO4007-Halloween - Main.ba2",
    "ccFSVFO4007-Halloween - Textures.ba2",
    "ccFSVFO4007-Halloween.esl",
    "ccOTMFO4001-Remnants - Main.ba2",
    "ccOTMFO4001-Remnants - Textures.ba2",
    "ccOTMFO4001-Remnants.esl",
    "ccSBJFO4003-Grenade - Main.ba2",
    "ccSBJFO4003-Grenade - Textures.ba2",
    "ccSBJFO4003-Grenade.esl"
]

# functions
def isRoot():
    isRoot = os.path.exists(rootPath + "\\" + "Fallout4.exe")
    if isRoot:
        return True
    elif isRoot == False:
        return False
def isZipExists():
    isZipExists = os.path.exists(unZipFilePath)
    if isZipExists:
        return True
    elif isZipExists == False:
        return False
def userConfirmation():
    a = input("你确定要继续吗（y/n）")
    if a == 'y':
        return True
    elif a == "n":
        return False
    else:
        print("无效选择，请重新输入")
        return  userConfirmation()
def _deleteFiles():
    print("开始删除次世代更新内容")
    #print("ok")
    dataPath = rootPath + "\\Data"
    try:
        if rootPath != "":
            for delete in deleteFiles:
                deleteFilesPath = dataPath+'\\'+delete
                isExists = os.path.exists(deleteFilesPath)
                #print(isExists)
                if isExists:
                    try:
                        trueDeleteFiles = []
                        trueDeleteFiles.append(delete)
                        for a in trueDeleteFiles:
                            os.remove(dataPath+'\\'+a)
                            print(f"已删除 {dataPath+'\\'+a}")
                    except ValueError:
                        print("不存在")
            print("已删除次世代更新内容")
    except IOError:
        print("删除次世代内容失败")
def unZipFile():
    print("开始解压")
    with zipfile.ZipFile(unZipFilePath, 'r') as unzip:
        fileList = unzip.namelist()
        try:
            for index, file in enumerate(fileList):
                unzip.extract(file, rootPath)
                progress = (index + 1) / len(fileList) * 100
                sys.stdout.write('\r' + '解压进度：{:.2f}%'.format(progress))
                sys.stdout.flush()
            print("\n解压成功")
        except IOError:
            print("\n解压失败")

# Main

# 用户拖入的文件
try:
    # 存在,rootPath = falloutexePath 的上一级
    falloutexePath =sys.argv[1]
    rootPath = os.path.dirname(os.path.abspath(falloutexePath))
except:
    # 不存在,用户自行填入
    rootPath = str(input("请输入游戏根目录\n"))

unZipFilePath = str(input("请输入 Fallout4.7z 文件路径\n"))

print(f"你的游戏路径： {rootPath}")
print(f"你的 Fallout4.7z 文件路径： {unZipFilePath}")

print("注意：此操作会删除你的游戏文件")
if userConfirmation():
    if isZipExists() and isRoot():
        unZipFile()
        _deleteFiles()
    else:
        print("错误的 Fallout4游戏路径 或 错误的 Fallout4.7z 文件路径\n")
else:
    sys.exit(0)

input("按下 enter 键退出\n")