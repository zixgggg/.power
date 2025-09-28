#!/usr/bin/python3
import os
f=os.path.expanduser("~/.power/power_mode.conf")#我power_mode.conf的內容是0或1或2
with open(f,"r+")as i:#以r+讀寫模式打開(檔案指標在內容結尾)
    m=i.read()#讀
    m=int(m)#把內容變整數 例如0
    mode=["performance","balanced","power-saver"]#所有模式的陣列
    if m>=2:
        m=0
        i.seek(0)#把檔案指標移到開頭
        i.truncate()#清空檔案(因爲truncate()預設是截斷檔案指標的後面)
        i.write(str(m))#寫入0
        ans="powerprofilesctl set "+mode[m]#指令
        os.system(ans)#執行指令
    else:
        i.seek(0)#把檔案指標移到開頭
        i.truncate()#清空檔案(因爲truncate()預設是截斷檔案指標的後面)
        m=m+1#要執行下一個模式
        ans="powerprofilesctl set "+mode[m]#指令
        os.system(ans)#執行指令
        i.write(str(m))#寫入0
        #i.close()#關閉用r+打開的檔案
        #w.close()#關閉用w+打開的檔案
