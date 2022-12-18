import math

from base import JD
from base.Eph0 import J2000, int2, radd, rad2str2
from base.JW import JW
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
        return self.ob.bz_jn + ' ' + self.ob.bz_jy + ' ' + self.ob.bz_jr + ' ' + self.ob.bz_js


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
