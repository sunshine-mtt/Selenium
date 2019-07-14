# balance = 10000.0
# year_rate = 5.0
# result_list = []
#
# for year in range(1,21):
#     interest = balance * year_rate/100
#     balance = balance + interest
#     print(year,balance)
#     result_list.append(balance)
#
# print(result_list)
#
#
#
#
#
#
# score = 11
# right = 'adbdcacbdac'
#
# while True:
#     input_str = input('请输入答案：')
#
#     if len(right) != len(input_str):
#         print('长度不对')
#     for i in range(11):
#         if right[i] != input_str[i]:
#             score -= 1
#     print(score)
#     input_str = input('请输入答案：')
#     if input_str == 'n':
#         break


pi_estimate = 0
flag = 0
for i in range(1,10000):
    if i % 2:
        if flag == 0:
            pi_estimate += 1/i
            flag = 1
        else:
            pi_estimate -= 1/i
            flag = 0

print(pi_estimate * 4)


a = lambda x:x *x
print(a(2))

a = '1233333333'
print(a[0:5])

fin = open('hero.py','r')
while True:
    line = fin.readline()
    if not line:
        break
    print(line,end=" ")

fin.close()