# -*- coding:utf-8 -*-
import urllib.request


def get_stock(stock_no):
    # 使用腾讯股票查询接口进行查询
    f = urllib.request.urlopen('http://qt.gtimg.cn/q=s_us' + str(stock_no))
    # f = urllib.request.urlopen('http://qt.gtimg.cn/q=s_usAAPL')
    res = f.read().decode('gbk')
    f.close()
    return res


def result_parse(result):
    res_dict = {}
    result_spl = result[14:-3].split('~')
    res_dict['stock_name'] = result_spl[1]
    res_dict['stock_no'] = result_spl[2]
    res_dict['current_price'] = result_spl[3]
    res_dict['fluctuation'] = result_spl[4]
    res_dict['fluctuation_by_percent'] = result_spl[5]
    res_dict['volume'] = result_spl[6]
    res_dict['turnover'] = result_spl[8]
    return res_dict


def stock_check(stock_no):
    if len(stock_no) != 6:
        return 0
    no_first = stock_no[0]
    if int(no_first) == 6:
        code = 'sh' + stock_no
        return code
    elif (int(no_first) == 0) | (int(no_first) == 3):
        code = 'sz' + stock_no
        return code
    else:
        return 0


def stock_query():
    # 此方法用于不进行web交互查询
    stock_no = input("请输入股票代码:")
    code = stock_check(stock_no)
    if code != 0:
        result = result_parse(get_stock(code))
        print('**************查询结果*****************')
        print('股票名称:', result['stock_name'])
        print('股票代码:', result['stock_no'])
        print('当前价格:', result['current_price'])
        print('涨    跌:', result['fluctuation'])
        print('涨   跌(%):', result['fluctuation_by_percent'], '%')
        print('成交量(手):', result['volume'])
        print('成交额(万):', result['turnover'])
        print('**************查询结果*****************')
    else:
        print('请输入正确的股票代码')
