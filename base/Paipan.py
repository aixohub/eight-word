from base import JD
from base.Eph0 import J2000, int2
from base.Lunar import Obb, Ob
from base.Tool import year2Ayear, timeStr2hour
import datetime






if __name__ == '__main__':
    curTZ = -8
    jd = JD(1991, 3, 16)
    obb = Obb()
    ob = Ob()
    obb.mingLiBaZi(jd.jd + curTZ / 24 - J2000, 2.0173097212790148, ob) # 八字计算

    print('<font color=red  ><b>[八字]：</b></font>' + ob.bz_jn + '年 ' + ob.bz_jy + '月 ' + ob.bz_jr + '日 ' + ob.bz_js + '时 真太阳 <font color=red>' + ob.bz_zty + '</font><br>'
        + '<font color=green><b>[纪时]：</b></font><i>' + ob.bz_JS + '</i><br>')

