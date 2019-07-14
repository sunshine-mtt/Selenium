
def exchange_value(input, rate):
    out_value = input * rate
    return out_value

def main():
    # 请输入金额
    input_value = input("请输入您要查询的带单位的金额(退出请按Q)：")
    # 汇率
    currency_exchange_rate = 6.77

    while input_value != 'Q':
        # 获取单位
        unit = input_value[-3:]
        #判断是人民币还是美元
        if unit == 'CNY':
            rmb_value = eval(input_value[:-3])
            exchange_rate = 1 / currency_exchange_rate
            print(exchange_value(rmb_value, exchange_rate))

        elif unit == 'USD':
            usd_value = eval(input_value[:-3])
            exchange_rate = 1 * currency_exchange_rate
            print(exchange_value(usd_value, exchange_rate))
        else:
            print("程序暂不支持该单位的查询！")

        #重新输入查询金额
        input_value = input("请输入您要查询的带单位的金额(退出请按Q)：")

    print("程序已退出！")

if __name__ == '__main__':
    main()

