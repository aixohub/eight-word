import math

from base import JD
from base.Eph0 import J2000, int2, radd, rad2str2
from base.JW import JW
from base.Lunar import Obb, Ob
from base.Tool import year2Ayear, timeStr2hour
import datetime






if __name__ == '__main__':
    curTZ = -8
    t = timeStr2hour("12:2:41");
    jd = JD(2022, 12, 18 + t/24)
    obb = Obb()
    ob = Ob()
    print("jd")
    print(jd.jd)
    a = JW()
    a.get_i(3)
    c = a.get_lat(3, '兰州市')
    a.jw_decode(c)
    r = a.J / math.pi * 180
    obb.mingLiBaZi(jd.jd + curTZ / 24 - J2000, r / radd, ob) # 八字计算

    print('[八字]：' + ob.bz_jn + '年 ' + ob.bz_jy + '月 ' + ob.bz_jr + '日 ' + ob.bz_js + '时 真太阳 <font color=red>' + ob.bz_zty + '</font><br>'
        + '<font color=green><b>[纪时]：</b></font><i>' + ob.bz_JS + '</i><br>')

