import math

from base import JD
from base.BaseDict import jia_zi, ArrayDunRi, ArrayDunNian
from base.Eph0 import J2000, int2, radd, rad2str2
from base.JW import JW
from base.JieQi import JieQi
from base.Lunar import Obb, DaySelected
from base.Tool import year2Ayear, timeStr2hour
import datetime


class Paipan:
    def __init__(self):
        self.ob = DaySelected()
        self.obb = Obb()
        self.jw = JW()
        self.jd = None
        self.curTZ = -8
        self.birth_place_lat = None
        self.jie_qi = JieQi()
        self.eight_char = None

    def get_eight_char(self, province, city, date, time):
        t = timeStr2hour(time)
        day_date = date.split("-")
        year = int(day_date[0])
        month = int(day_date[1])
        day = int(day_date[2])
        jd_object = JD()
        self.jd = jd_object.get_jd(year, month, day + t / 24)
        self.birth_place_lat = self.jw.get_r(province, city)
        self.ob.yyyy_MM_dd = date + " " + time
        self.ob.pro = province
        self.ob.city = city
        self.obb.mingLiBaZi(self.jd + self.curTZ / 24 - J2000, self.birth_place_lat / radd, self.ob)
        self.eight_char = self.ob.bz_jn + ' ' + self.ob.bz_jy + ' ' + self.ob.bz_jr + ' ' + self.ob.bz_js
        return self.eight_char

    def get_birth_place_lat(self, province, city):
        self.birth_place_lat = self.jw.get_r(province, city)
        return self.birth_place_lat

    def getFanTuiJD(self, ftStartYear, year, month, day, hour):
        self.eight_char = year + ' ' + month + ' ' + day + ' ' + hour
        # 计算当前年份
        jzYear = jia_zi.index(year)
        jzStartMM = ArrayDunNian[jzYear % 5]
        month_dict = {}
        i = 0
        while i < 12:
            month_dict.setdefault(jia_zi[(jzStartMM + i) % 60], i)
            i = i + 1
        ixMonth = month_dict[month]
        jzDay = jia_zi.index(day)
        jzStartHH = ArrayDunRi[jzDay % 5]
        # 清空旧列表
        hour_dict = {}
        i = 0
        while i < 12:
            hour_dict.setdefault(jia_zi[(jzStartHH + i) % 60], i)
            i = i + 1
        ixHour = hour_dict[hour]
        curYear = ftStartYear + jzYear
        # 获取该年节气列表，当年立春到下年立春，25个节气
        arrayJQ = self.jie_qi.get_jie_qi(curYear)
        # 月份就是 ixMonth，节气范围是 ixMonth*2 到 ixMonth*2 + 2
        nStartDay = math.floor(arrayJQ[ixMonth * 2] + 0.5)  # 转到整数儒略日，节气日的中午12点
        nEndDay = math.floor(arrayJQ[ixMonth * 2 + 2] + 0.5)  # 整数儒略日
        # 计算起始节气的日子甲子序号
        jzStartDay = (nStartDay - J2000 - 6 + 9000000) % 60
        # 查找该月有无 jzDay 这天
        theIndex = -1
        dCount = nEndDay - nStartDay
        i = 0
        while i <= dCount:
            curJiaZi = (jzStartDay + i) % 60
            if curJiaZi == jzDay:
                theIndex = i
                break  # 找到了
            i = i + 1
        # 判断
        if (theIndex < 0):
            return -1  # 没找到
        # 假定找到了
        # 如果该八字在节气当天，月份可能对，也可能错，不管对错，都当找到了
        jdRet = (nStartDay - 0.5) + theIndex + (ixHour + (1.0 / 3600)) * 2 / 24  # 返回偶数小时的当天，补了2秒，避免浮点数少了一丁点
        return jdRet


if __name__ == '__main__':
    a = Paipan()
    c = a.get_eight_char('甘肃省', '兰州市', "2022-12-18", "12:2:41")
    print(c)
    b = a.get_eight_char('安徽省', '太和县', "1991-3-16", "3:01:41")
    print(b)
    ob = a.ob

    print(
        '[八字]：' + ob.bz_jn + '年 ' + ob.bz_jy + '月 ' + ob.bz_jr + '日 ' + ob.bz_js + '时 真太阳 <font color=red>' + ob.bz_zty + '</font><br>'
        + '<font color=green><b>[纪时]：</b></font><i>' + ob.bz_JS + '</i><br>')
