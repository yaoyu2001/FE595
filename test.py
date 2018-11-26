import urllib.request

def get_stock(stock_no):
    # 使用腾讯股票查询接口进行查询
    f = urllib.request.urlopen('http://qt.gtimg.cn/q=s_us' + str(stock_no))
    # f = urllib.request.urlopen('http://qt.gtimg.cn/q=s_usAAPL')
    res = f.read().decode('gbk')
    f.close()
    return res

print(get_stock("AAPL"))

result_spl = get_stock("AAPL")[14:-3].split('~')
result_spl1 = get_stock("APL")[14:-3].split('~')
print(result_spl)
print(result_spl1)
print(len(result_spl))
print(len(result_spl1))
# for abc in get_stock("AAPL"):
#   print(abc)
#
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)