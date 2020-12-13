# 创建测试数据
# 将测试数据用于测试，先前构建的指纹库的精度

import os
import numpy as np


def averageNum(num):
    total = 0
    for i in range(len(num)):
        total += float(num[i])
    return total / len(num)

#测试数据的文件
file_obj = open('/Users/my_private_folder/Desktop/measureData20201124.txt', 'r')
# file_obj = open('bluetoothData4.txt', 'r')
all_lines = file_obj.readlines()  # 读取文件，所有行

collection = np.zeros((49, 3), dtype=np.float)  # 一共有48个观测点，每个点有三个ap的测量值
list_288 = []
list_542 = []
list_741 = []
counter = 0  # 计数器，用来记录点的个数和位置
for line in all_lines:
    if ('location' in line):
        line = line.replace('\n', '')  # 每一行有存在一个换行符，取出换行符，直接使用空字符去替换换行符
        print(line)
        if (counter == 0):
            counter = counter + 1
            continue  # 要注意break 和continue的区别，在使用上要注意
        else:
            if (counter == 49):
                break;
            collection[counter - 1][0] = averageNum(list_288)
            print(averageNum(list_288))
            collection[counter - 1][1] = averageNum(list_542)
            print(averageNum(list_542))
            collection[counter - 1][2] = averageNum(list_741)
            print(averageNum(list_741))
            list_288 = []
            list_542 = []
            list_741 = []
            counter = counter + 1
    else:
        line = line.replace('\n', '')
        data_arr = line.split('-')

        if ('devices :741' in line):
            list_741.append(data_arr[1])
        if ('devices :288' in line):
            list_288.append(data_arr[1])
        if ('devices :542' in line):
            list_542.append(data_arr[1])

collection[counter - 1][0] = averageNum(list_288)
print(averageNum(list_288))
collection[counter - 1][1] = averageNum(list_542)
print(averageNum(list_542))
collection[counter - 1][2] = averageNum(list_741)
print(averageNum(list_741))

print("---------------------------------------------")
# 创建三个数组，用于放置得到的数据
collection_288 = np.zeros((12, 4), dtype=np.float)
collection_542 = np.zeros((12, 4), dtype=np.float)
collection_741 = np.zeros((12, 4), dtype=np.float)

# 放置数据的过程
for i in range(0, 12):
    for j in range(0, 4):
        collection_288[i][j] = collection[i * 4 + j][0]

print()

for i in range(0, 12):
    for j in range(0, 4):
        collection_542[i][j] = collection[i * 4 + j][1]

print()

for i in range(0, 12):
    for j in range(0, 4):
        collection_741[i][j] = collection[i * 4 + j][2]

print()

testdatabase = []
for i in range(0, 12):
    for j in range(0, 4):
        fingerPrintArr = np.zeros(5)
        fingerPrintArr[0] = i + 1
        fingerPrintArr[1] = j + 1
        fingerPrintArr[2] = collection_288[i][j]
        fingerPrintArr[3] = collection_542[i][j]
        fingerPrintArr[4] = collection_741[i][j]
        testdatabase.append(fingerPrintArr)
print("++++++++++++++++++++++++++++++++++++++++++++")

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def averageNum(num):
    total = 0
    for i in range(len(num)):
        total += float(num[i])
    return total / len(num)


file_obj = open('/Users/my_private_folder/Desktop/measureData20201118-23.txt', 'r')
# file_obj = open('bluetoothData4.txt', 'r')
all_lines = file_obj.readlines()  # 读取文件，所有行
print(all_lines.__len__())  # 输出文件的行数大小
#创建指纹库的数据
collection = np.zeros((49, 3), dtype=np.float)  # 一共有48个观测点，每个点有三个ap的测量值
list_288 = []
list_542 = []
list_741 = []
counter = 0  # 计数器，用来记录点的个数和位置
for line in all_lines:
    if ('location' in line):
        line = line.replace('\n', '')  # 每一行有存在一个换行符，取出换行符，直接使用空字符去替换换行符
        print(line)
        if (counter == 0):
            counter = counter + 1
            continue  # 要注意break 和continue的区别，在使用上要注意
        else:
            if (counter == 49):
                break;
            collection[counter - 1][0] = averageNum(list_288)
            print(averageNum(list_288))
            collection[counter - 1][1] = averageNum(list_542)
            print(averageNum(list_542))
            collection[counter - 1][2] = averageNum(list_741)
            print(averageNum(list_741))
            list_288 = []
            list_542 = []
            list_741 = []
            counter = counter + 1
    else:
        line = line.replace('\n', '')
        data_arr = line.split('-')

        if ('devices :741' in line):
            list_741.append(data_arr[1])
        if ('devices :288' in line):
            list_288.append(data_arr[1])
        if ('devices :542' in line):
            list_542.append(data_arr[1])

collection[counter - 1][0] = averageNum(list_288)
print(averageNum(list_288))
collection[counter - 1][1] = averageNum(list_542)
print(averageNum(list_542))
collection[counter - 1][2] = averageNum(list_741)
print(averageNum(list_741))

print("+++++++++++++++++++++++++++++++++++")

'''
完成每一个接收器的在每个测试点的数据平均值的计算
'''

print("---------------------------------------------")
collection_288 = np.zeros((12, 4), dtype=np.float)
collection_542 = np.zeros((12, 4), dtype=np.float)
collection_741 = np.zeros((12, 4), dtype=np.float)

for i in range(0, 12):
    for j in range(0, 4):
        collection_288[i][j] = collection[i * 4 + j][0]

print()
print(collection_288[0][0])
print(collection_288[11][3])

for i in range(0, 12):
    for j in range(0, 4):
        collection_542[i][j] = collection[i * 4 + j][1]

print()
print(collection_542[0][0])
print(collection_542[11][3])

for i in range(0, 12):
    for j in range(0, 4):
        collection_741[i][j] = collection[i * 4 + j][2]

print("------------------------------------------------")
database = []
for i in range(0, 12):
    for j in range(0, 4):
        fingerPrintArr = np.zeros(5)
        fingerPrintArr[0] = i + 1
        fingerPrintArr[1] = j + 1
        fingerPrintArr[2] = collection_288[i][j]
        fingerPrintArr[3] = collection_542[i][j]
        fingerPrintArr[4] = collection_741[i][j]
        database.append(fingerPrintArr)

# database是指纹库，testdatabase是测试数据
judgedData = database

euclidDis = np.zeros(48)


def countKNearest(measuredData):
    for index in range(0, 48):
        # 计算欧式距离
        euclidDis[index] = np.sqrt(pow(judgedData[index][2] - measuredData[0], 2)
                                   + pow(judgedData[index][3] - measuredData[1], 2)
                                   + pow(judgedData[index][4] - measuredData[2], 2))
    return


prediction_result = []
K = 4


def getLocation(data):
    countKNearest(data)
    dis_value = []
    # 得到距离最近的信号强度的下标
    dis_value = np.argpartition(euclidDis, K)[:K]
    horizon_loc = 0
    vertical_loc = 0
    for i in range(0, K):
        horizon_loc += judgedData[dis_value[i]][0]
        vertical_loc += judgedData[dis_value[i]][1]
    prediction_result.append([horizon_loc / K, vertical_loc / K])
    return horizon_loc / K, vertical_loc / K


total_dis = 0.00

for i in range(0, 48):
    xl, yl = getLocation([testdatabase[i][2], testdatabase[i][3], testdatabase[i][4]])
    total_dis = total_dis + np.sqrt((xl - testdatabase[i][0]) ** 2 + (yl - testdatabase[i][1]) ** 2)
    plt.plot([xl, testdatabase[i][0]], [yl, testdatabase[i][1]], c='r')
    plt.scatter(xl, yl, c='k', marker='*')
    plt.scatter(testdatabase[i][0], testdatabase[i][1], c='y', marker='<')

plt.show()
print(str(total_dis / 48) + 'm')
