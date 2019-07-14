def main():
    # 请输入金额
    currency_input_value = input("请输入您要查询的带单位的金额(退出请按Q)：")
    # 汇率
    currency_exchange_rate = 6.77


    while currency_input_value != 'Q':
        # 获取单位
        unit = currency_input_value[-3:]

        #判断是人民币还是美元
        if unit == 'CNY':
            exchange_rate = 1 / currency_exchange_rate
        elif unit == 'USD':
            exchange_rate = 1 * currency_exchange_rate
        else:
            exchange_rate = -1

        if exchange_rate != -1:
            # 获取金额
            input_value = eval(currency_input_value[:-3])

            #函数名为converse_currency,有一个参数x
            converse_currency = lambda x : x * exchange_rate

            #输出结果
            out_value = converse_currency(input_value)
            print(out_value)
        else:
            print("程序暂不支持该种单位查询！")

        # 请输入金额
        currency_input_value = input("请输入您要查询的带单位的金额(退出请按Q)：")

    print("退出程序！")


if __name__ == '__main__':
    main()
