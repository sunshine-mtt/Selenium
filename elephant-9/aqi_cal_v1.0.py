"""
    作者: sunshine
    功能: AQI计算
    版本: 1.0
    日期: 2019/4/28
"""
def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, C):
    """
        线性计算
    """
    iaqi = (iaqi_hi - iaqi_lo) * (C - bp_lo) / (bp_hi - bp_lo) + iaqi_lo

    return iaqi

def iaqi_pm_cal(pm_value):
    """
        计算pm2.5的iaqi
    """
    if 0 <= pm_value < 36:
        iaqi_pm = cal_linear(0, 50, 0, 35, pm_value)
    elif 36 <= pm_value < 76:
        iaqi_pm = cal_linear(50, 100, 35, 75, pm_value)
    elif 76 <= pm_value < 116:
        iaqi_pm = cal_linear(100, 150, 75, 115, pm_value)
    elif 116 <= pm_value < 151:
        iaqi_pm = cal_linear(150, 200, 116, 150, pm_value)
    else:
        pass

    return iaqi_pm

def iaqi_co_cal(co_value):
    """
        计算co的iaqi
    """
    if 0 <= co_value < 3:
        iaqi_co = cal_linear(0, 50, 0, 2, co_value)
    elif 3 <= co_value < 5:
        iaqi_co = cal_linear(50, 100, 2, 4, co_value)
    elif 5 <= co_value < 15:
        iaqi_co = cal_linear(100, 150, 4, 14, co_value)
    elif 15 <= co_value < 25:
        iaqi_co = cal_linear(150, 200, 14, 24, co_value)
    else:
        pass

    return iaqi_co

def aqi_cal(param_list):
    """
        iaqi计算程序
    """
    pm_value = param_list[0]
    co_value = param_list[1]
    iaqi_pm = iaqi_pm_cal(pm_value)
    iaqi_co = iaqi_co_cal(co_value)

    iaqi_list = []
    iaqi_list.append(iaqi_pm)
    iaqi_list.append(iaqi_co)

    AQI = max(iaqi_list)
    return AQI

def main():
    """
        主函数
    """
    input_str = input('请输入(1)pm2.5 (2)co,以空格分割: ')
    input_list = input_str.split(' ')
    pm_value = float(input_list[0])
    co_value = float(input_list[1])
    param_list = []
    param_list.append(pm_value)
    param_list.append(co_value)
    #调用aqi_cal函数获取aqi值
    aqi_val = aqi_cal(param_list)

    print('AQI空气质量指数为{}'.format(aqi_val))


if __name__ == '__main__':
    main()