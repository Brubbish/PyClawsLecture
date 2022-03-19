# -*- coding: utf-8 -*-  
import os
import requests
import os
import config
import threading
#import Crawling

lock = threading.Lock()
# lock.acquire()
# lock.release()

event = threading.Event()
# event.set() event.clear()
# if event.is_set()
# else event.wait()


#字典存放院校名称和地址，用空格分开

def rurl():
    file = os.path.join(os.getcwd(),'url.txt')
    dic1 = {}
    dic2 = {}
    dic3 = {}
    ty = 0
    with open(file, "r") as f:
        cnt = 0
        one = f.readline().split()
        while ( one ):
            if ( '#' in one[0] ):
                ty = int(one[0][1:])
                # print(ty,config.FP,(ty==config.FP),type(ty),type(config.FP))
                one = f.readline().split()
                continue
            cnt += 1
            try: 
                if (one[2]):
                    config.redprint("uurl.txt文件里的格式可能不太对，跳过第%s行了哦" % cnt)
                    continue
                    #这个输出不知道为啥会去掉第一个非空字符
            except:
                pass
            # 先不检查每行"院校 url"是否冲突
            # if (one[0] in dic): 
            #     if (config.urlCx = 0):
            #print(one[1])
            # type(ty)==str   type(config.FP)==int
            if (ty == config.FP ): 
                dic1[one[0]] = one[1]
            elif (ty == config.SPA ): dic2[one[0]] = one[1]
            else : dic3[one[0]] = one[1]
            one = f.readline().split()
    print("已读入所有url信息")
    return dic1,dic2,dic3
                   


def main():
    url1,url2,url3 = rurl()
    print(url1.items(),url2.items,url3.items())

    # for func in ("1","2","3"):
    #     Task"{}".format(func) = 
    
    #优雅但好像慢一点
    # Task = []
    # for func in ("1","2","3"):
    #     Task[func-1] = "threading.Thread(target = Crawling.TaskType{},args=(url{},lock)).setDaemon(True)".format(func,func)
    #     eval(Task[func-1])
    
    Task1 = threading.Thread(target = Crawling.TaskType1,args=(url1,lock)).setDaemon(True)
    Task2 = threading.Thread(target = Crawling.TaskType2,args=(url2,lock)).setDaemon(True)
    Task3 = threading.Thread(target = Crawling.TaskType3,args=(url3,lock)).setDaemon(True)
    
    Task1.start()
    Task2.start()
    Task3.start()

    
    
    
if __name__ == "__main__":

    main()
#else: