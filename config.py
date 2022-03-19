import os
from colorama import Fore,Back,Style 


#字体颜色
redprint = lambda cont: print("\033[0;31 %s \033[0m" % cont) #print(Fore.RED) 

#网站类型（Warning：Dont modify）
FP = 1
SPA = 2
SPP = 3



time_limit = 30
urlCx = 0   #