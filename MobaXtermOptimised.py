######
#tundeakingbade11@gmail.com
######
#Supports MobaXterm 20.5 but the script can be modified to support any terminal program that can export its nodes as an editable file.
######
######
import pandas as pd
from datetime import datetime


#Creating csv file using time and date in other not to overwrite existing file
now = datetime.now()
f = now.strftime("Result/MobaXterm Sesions-%d-%m-%H%M.mxtsessions")
new_file = open(f, "w", newline="")

########################################
# Open file containing IP addresses
########################################

# Open file containing Nokia IP addresses
nokia_NE_list = input("Nokia list to work with: ")
df_NK = pd.read_csv(nokia_NE_list)


# Open file containing Huawei IP addresses
huawei_NE_list = input("Huawei list to work with: ")
df_HW = pd.read_csv(huawei_NE_list, skiprows=3)


new_file.write('[Bookmarks]\n')
new_file.write('SubRep=\n')
new_file.write('ImgNum=42\n')


###############################
# For Huawei List
###############################

new_file.write('ImgNum=41\n')
new_file.write('[Bookmarks_1]\n')
new_file.write('SubRep=Huawei_IPRAN\n')
new_file.write('ImgNum=41\n')

for d in range(0, df_HW.shape[0]):
    node = df_HW['NE Name'][d]
    IP = df_HW['NE IP Address'][d]
    new_file.write(f'{node}= #129#1%{IP}%23%%%2%%%%%0%0%%1080%#MobaFont%10%0%0%-1%15%236,236,236%30,30,30%180,180,192%0%-1%0%%xterm%-1%-1%_Std_Colors_0_%80%24%0%1%-1%<none>%%0#0# #-1\n')

# MPBN IP List
new_file.write('\n')
new_file.write('[Bookmarks_2]\n')
new_file.write('SubRep=MPBN\n')
new_file.write('ImgNum=41\n')

###############################
# For Nokia List
###############################
new_file.write('\n')
new_file.write('[Bookmarks_3]\n')
new_file.write('SubRep=Nokia_NE\n')
new_file.write('ImgNum=41\n')

for d in range(0, df_NK.shape[0]):
    node = df_NK['Site Name'][d]
    IP = df_NK['Site ID'][d]
    if "SASK" in node:
        new_file.write(f'{node}= #130#0%{IP}%22%%%0%-1%%%%%0%-1%0%%%-1%0%0%0%%1080%%0%0%1#MobaFont%10%0%0%-1%15%236,236,236%30,30,30%180,180,192%0%-1%0%%xterm%-1%-1%_Std_Colors_0_%80%24%0%1%-1%<none>%%0#0# #-1\n')
    elif "SARAX" in node:
        new_file.write(f'{node}= #130#0%{IP}%22%%%0%-1%%%%%0%-1%0%%%-1%0%0%0%%1080%%0%0%1#MobaFont%10%0%0%-1%15%236,236,236%30,30,30%180,180,192%0%-1%0%%xterm%-1%-1%_Std_Colors_0_%80%24%0%1%-1%<none>%%0#0# #-1\n')
    else:
        new_file.write(f'{node}=#129#1%{IP}%23%%%2%%%%%0%0%%1080%#MobaFont%10%0%0%-1%15%236,236,236%30,30,30%180,180,192%0%-1%0%%xterm%-1%-1%_Std_Colors_0_%80%24%0%1%-1%<none>%%0#0# #-1\n')

new_file.close()
print ("Script completed with success!!!")