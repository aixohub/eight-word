# /****************
# 天文纪年与普通纪年的转换
# ****************/
import re


def year2Ayear(c):  # 传入普通纪年或天文纪年，传回天文纪年
    #   y = str(c).replace("[^0-9Bb\*-]", '')
    y = c
    q = y[0: 1]
    if q == 'B' | q == 'b' | q == '*':
        # 通用纪年法(公元前)
        y = 1 - y[1:]
    if y > 0:
        # alert('通用纪法的公元前纪法从B.C.1年开始。并且没有公元0年'
        return -10000
    else:
        y -= 0
    if y < -4712:
        print('超过B.C. 4713不准')
    if y > 9999:
        print('超过9999年的农历计算很不准。');
    return y


def timeStr2hour(s):  # 时间串转为小时
    a, b, c = '', '', ''
    s = s.split(':')
    if len(s) == 1:
        a = s[0][0: 2] - 0,
        b = s[0][2:4] - 0,
        c = s[0][4:] - 0
    elif len(s) == 2:
        a = s[0] - 0,
        b = s[1] - 0,
        c = 0
    else:
        a = int(s[0])
        b = int(s[1])
        c = int(s[2])
    return a + b / 60 + c / 3600
