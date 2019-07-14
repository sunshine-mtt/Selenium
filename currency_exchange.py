#美元汇率
USD_EXCHANGE_RATE = 6.77
#输入货币金额
currency_str_value = input("请输入带有单位的货币金额(如果退出请按Q): ")
#统计循环次数
i = 0

while currency_str_value != 'Q':

    i = i + 1
    # 获取货币单位
    unit = currency_str_value[-3:]
    if unit == 'CNY':
        # 获取货币金额
        rmb_str_value = currency_str_value[:-3]
        rmb_value = eval(rmb_str_value)
        usd_value = rmb_value / USD_EXCHANGE_RATE
        print("美元汇兑金额是：", usd_value)
    elif unit == 'USD':
        # 获取货币金额-字符串
        usd_str_value = currency_str_value[:-3]
        # 获取货币金额
        usd_value = eval(usd_str_value)
        rmb_value = usd_value * USD_EXCHANGE_RATE
        print("人民币汇兑金额是：", rmb_value)
    else:
        print("您输入的货币单位不在查询范围")

    print("************************************")
    # 输入货币金额
    currency_str_value = input("请输入带有单位的货币金额（如果退出请按Q）: ")

print("您已退出程序！")