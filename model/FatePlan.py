import math

from base import int2, J2000, radd, dt_T, pi2, XL, pty_zty2, JD
from base.Lunar import SSQ, Obb
from model.EightChar import EightChar
from model.Nayin import JieQiMing, ArrayDunNian, NaYin, jia_zi
from model.TenGodTable import FiveElementTable
import pandas as pd


class JieQi:
    def __init__(self):
        self.arrayJQ = None
        self.ssq = SSQ()
        self.obb = Obb()
        print()

    def get_jie_qi(self, y):
        """
        //根据公历年份返回24节气，节气从每年立春开始，这是八字月柱的排法
        //共25个节气，今年立春到明年立春，北京时间
        """
        self.arrayJQ = []
        self.ssq.calcY(int2((y - 2000) * 365.2422 + 180))
        i = 3
        while i < 24:  # 立春到大雪，21个
            index = i - 3
            zq = self.ssq.ZQ[i]
            self.arrayJQ.append(self.obb.qi_accurate2(zq) + J2000)
            i = i + 1
        # 计算下一年的节气表，提取冬至到立春4个
        self.ssq.calcY(int2((y + 1 - 2000) * 365.2422 + 180))
        i = 0
        while i < 4:  # 立春到大雪，21个
            self.arrayJQ.append(self.obb.qi_accurate2(self.ssq.ZQ[i]) + J2000)
            i = i + 1

    # 快捷函数，根据年数字获取甲子数
    def GetNianJiaZiShu(self, yy):
        iJZ = (yy - 1984 + 6000000) % 60
        return iJZ


class BaZiObject:
    def __init__(self):
        self.IsUseZTY = None
        self.JDBirth = None
        self.JDBirthZTY = None
        self.JQMing0 = None  # 前一个节气名称
        self.JQJD0 = None  # 前一个节气儒略日
        self.JQMing1 = None  # 后一个节气名称
        self.JQJD1 = None  # 后一个节气儒略日
        self.DaYunJD = None  # 大运起运的儒略日
        self.isNiDaYun = None  # 是否大运逆序排列
        self.iYueJZ = None


class FatePlan:

    def __init__(self):
        table_header = ['sex', '阳', '阴']
        # 定义表数据
        table_data = [['男', '顺', '逆'],
                      ['女', '逆', '顺']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("sex", inplace=True)
        self.table = table
        self.trunk = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        self.branch = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        self.eightChar = None
        self.sex = None
        self.fiveElementTable = FiveElementTable()
        self.bzpp = BaZiObject()
        self.XL = XL()
        self.curDD = None  # 排盘的公历时间
        self.curJD = None  # 排盘的儒略日时间
        self.JD = JD()
        self.jie_qi = JieQi()
        self.arrayJieQi = None
        self.birthDD = None
        self.tips = None
        self.qiyunDD = None
        self.strRet = ''
        self.strDaYunJiaZi = "大运 "
        self.strDaYunNaYin = "纳音 "
        self.strDaYunZhouSui = "周岁 "
        self.strDaYunQiNian = "起年 "
        self.big_yun = []
        self.syblArray = []

    def get_big_fate(self):
        """
        运若顺行,从生日生时，数至最近未来节之日时，
        运若逆行,从生日生时，数至最近已往节之日时，
        每三日为一岁，每一日为百二十天，每一时为十天，
        如离节三日，则一岁行运，如离节一日，则落地百二十天行运，离节一时，则落地十天行运，每足三日，方算一岁，
        且须扣算清楚，某年某月某日时交运,不得混称几岁,列例如下。

        男命甲子年正月十五日子时生。
        甲子（年）
        丙寅（月）
        戊辰（日）
        壬子（时）
        运属顺行,数至最近未来节之日时,生立春后，
        最近 之未来节即是惊蛰，万年历载明是年二月初二日寅时交
        惊蛰,由正月十五日子时，数至二月初二日寅时,共十六天又二时，(正月小)以三天为一岁折之，即知为五岁多一
        天二时，应在五岁百四十日后起运，每一运管十年，故第
        一部运，五岁起行,第二部运，为十五岁起行，列式如下。
        五岁 丁卯
        十五 戊辰
        二五 己已
        三五 庚午
        四五 辛未
        五五 王申
        """
        year_trunk = self.eightChar.yearTrunk
        prop = self.fiveElementTable.get_yinyang(year_trunk)
        plan_method = self.table.loc[self.sex][prop]
        print(plan_method)
        if plan_method == '顺':
            self.get_forward()
        elif plan_method == '逆':
            self.get_reverse()

    def get_forward(self):
        """
        正向推大运
        """
        month = self.eightChar.month
        print(month)

    def get_reverse(self):
        """
        反向推大运
        """
        month = self.eightChar.month
        print(month)

    def get_bazi_object(self, jdBirth, gender, jingduBirth, isUseZTY):
        """
        bzpp.JDBirth 普通出生时间
        bzpp.JDBirthZTY 出生时间真太阳时
        bzpp.Gender  性别，男或女
        bzpp.JingDuBirth  出生地经度
        bzpp.IsUseZTY     使用真太阳时排盘
        """
        self.bzpp.JDBirth = jdBirth  # 北京时间，不考虑真太阳
        self.bzpp.Gender = gender
        self.bzpp.JingDuBirth = jingduBirth
        self.bzpp.IsUseZTY = isUseZTY
        ###################/
        ##减去东八区的加时，经度按120度
        # 两个参数
        jd = jdBirth - (8.0 / 24) - J2000  # 转为UTC的J2000数
        J = jingduBirth / radd  # 经度的弧度
        jd2 = jd + dt_T(jd)  # 力学时
        w = self.XL.S_aLon(jd2 / 36525, -1)  # 此刻太阳视黄经
        k = int2((w / pi2 * 360 + 45 + 15 * 360) / 30)  # 1984年立春起算的节气数(不含中气)

        jd += pty_zty2(jd2 / 36525) + J / math.pi / 2  # 本地真太阳时(使用低精度算法计算时差)
        self.bzpp.JDBirthZTY = jd + J2000  # 补上J2000儒略日

        # 如果不用真太阳时，直接用北京时间
        if 0 == isUseZTY:
            # 不用真太阳
            jd = jdBirth - J2000
            self.curDD = self.JD.DD(jdBirth)
            # 公历对象
            self.curJD = jdBirth
        else:
            # 使用真太阳
            self.curDD = self.JD.DD(self.bzpp.JDBirthZTY)
            self.curJD = self.bzpp.JDBirthZTY
        jd += 13 / 24  # 转为前一日23点起算(原jd为本日中午12点起算)
        D = math.floor(jd)
        SC = int2((jd - D) * 12)  # 日数与时辰
        v = int2(k / 12 + 6000000)
        self.bzpp.iNianJZ = v % 60  # 年柱甲子序号
        v = k + 2 + 60000000
        self.bzpp.iYueJZ = v % 60
        v = D - 6 + 9000000
        self.bzpp.iRiJZ = v % 60
        v = (D - 1) * 12 + 90000000 + SC
        self.bzpp.iShiJZ = v % 60

        ###################
        # 节气列表
        # 判断应该获取今年节气表还是去年节气表
        # 八字的甲子数不等于阳历年甲子数，说明出生在立春之前

        if self.bzpp.iNianJZ != self.jie_qi.GetNianJiaZiShu(self.curDD.Y):
            self.jie_qi.get_jie_qi(self.curDD.Y - 1)
            # 立春前用去年节气表
        else:
            self.jie_qi.get_jie_qi(self.curDD.Y)
            # 立春后用今年节气表
        arrayJieQi = self.jie_qi.arrayJQ

        #################
        # bzpp.JQMing0  #前一个节气名称
        # bzpp.JQJD0    #前一个节气儒略日
        # bzpp.JQMing1  #后一个节气名称
        # bzpp.JQJD1    #后一个节气儒略日
        # bzpp.DaYunJD  #大运起运的儒略日
        # bzpp.isNiDaYun #是否大运逆序排列
        #
        # bzpp.iYueJZ 月柱甲子数计算月支，月支从 子丑寅卯辰。。。。
        # 寅月序号从2，加10，模12等于0，就是节气的序号
        jqYueOrder = (self.bzpp.iYueJZ % 12 + 10) % 12
        # 12个大节，变成24节气中气，要乘以2
        self.bzpp.JQMing0 = JieQiMing[jqYueOrder * 2]
        self.bzpp.JQJD0 = arrayJieQi[jqYueOrder * 2]
        # 后一个节气
        self.bzpp.JQMing1 = JieQiMing[jqYueOrder * 2 + 2]  # 下一个大节是加2，加1的是中气
        self.bzpp.JQJD1 = arrayJieQi[jqYueOrder * 2 + 2]
        # 判断大运顺逆
        # 年份阴阳
        if self.bzpp.iNianJZ % 2 == 0:  # 甲子0，阳年
            # 阳年，男顺，女逆
            if ("女" == gender):  # 女
                self.bzpp.isNiDaYun = 1  # 女
            else:
                self.bzpp.isNiDaYun = 0  # 男顺
        else:
            # 阴年，男逆，女顺
            if ("女" == gender):  # 女
                self.bzpp.isNiDaYun = 0  # 女顺
            else:
                self.bzpp.isNiDaYun = 1
                # 顺逆
            if 0 == self.bzpp.isNiDaYun:
                # 顺行计算起运，一年 365.2422 天，大运是三天一年
                # 顺行计算差值是后面节气减出生时间
                deltaShun = self.bzpp.JQJD1 - self.curJD  # 差值天数
                # 转为起运天数
                qiyunShun = (deltaShun / 3.0) * 365.2422
                self.bzpp.DaYunJD = self.curJD + qiyunShun

            else:
                # 逆行计算起运
                deltaNi = self.curJD - self.bzpp.JQJD0  # 逆行大运节气差值天数
                # console.log("逆行数：" + deltaNi) 
                # 转为起运天数
                qiyunNi = (deltaNi / 3.0) * 365.2422
                self.bzpp.DaYunJD = self.curJD + qiyunNi

                ######################
            # 胎元，月令甲子数减9，倒数前面第十个月
            self.bzpp.iTaiYuan = (self.bzpp.iYueJZ - 9 + 60) % 60
            # 命宫1，数字速查法，不考虑中气
            # 寅1，卯2，，，，，子11，丑12，先计算月份的
            nMCount = (self.bzpp.iYueJZ % 12) - 1  # 原本子为0，丑为1，寅为2，都少1
            if (nMCount <= 0):
                nMCount += 12  # 子11，丑是12
            # 再计算时辰的
            nHCount = (self.bzpp.iShiJZ % 12) - 1
            if (nHCount <= 0):
                nHCount += 12
                # 计算命宫地支数，1到12
            nMGDZ = 14 - (nMCount + nHCount)
            if (nMGDZ < 1):
                nMGDZ += 12  # 小于1的变成1到12月
                # 五虎遁年，查月干
            nYearOrder = (self.bzpp.iNianJZ) % 5
            nMG = ArrayDunNian[nYearOrder] + (nMGDZ - 1)
            self.bzpp.iMingGong = (nMG % 60)  # 60范围之内

            # 返回
            return self.bzpp

    def get_ten_big_fate(self):
        if 0 == self.bzpp.IsUseZTY:
            # 不用真太阳
            self.birthDD = self.JD.DD(self.bzpp.JDBirth)
        else:
            self.birthDD = self.JD.DD(self.bzpp.JDBirthZTY)

        self.qiyunDD = self.JD.DD(self.bzpp.DaYunJD)
        qiyunZhouSui = self.qiyunDD.Y - self.birthDD.Y
        self.tips = "起运周岁：" + str(qiyunZhouSui) + " 起运公历：" + str(self.qiyunDD.Y) + "年" + str(
            self.qiyunDD.M) + "月" + str(self.qiyunDD.D) + "日" + "（每过十年走下一个大运）"
        iQiYunJZ = None
        iYunDelta = 0  # 大运顺行是 + 1，逆行是 - 1
        if 0 == self.bzpp.isNiDaYun:  # 顺行
            iQiYunJZ = (self.bzpp.iYueJZ + 1 + 60) % 60
            iYunDelta = 1
        else:
            # 逆行
            iQiYunJZ = (self.bzpp.iYueJZ - 1 + 60) % 60
            iYunDelta = -1
        #  起年公历年、起年甲子数
        qiyunGLNian = self.qiyunDD.Y
        iQiYunGLNianJZ = self.jie_qi.GetNianJiaZiShu(qiyunGLNian) 
        # 开始排大运
        self.strDaYunJiaZi = "大运 "
        self.strDaYunNaYin = "纳音 "
        self.strDaYunZhouSui = "周岁 "
        self.strDaYunQiNian = "起年 "
        strDaYunZhiNian = "止年 "
        arrayDaYunJiaZi = []  # 八步大运的甲子数
        # 计算大运信息字符串
        i = 0
        while i < 8:
            arrayDaYunJiaZi.append((iQiYunJZ + i * iYunDelta + 60) % 60)
            self.strDaYunJiaZi += jia_zi[arrayDaYunJiaZi[i]] + " "
            self.strDaYunNaYin += NaYin[arrayDaYunJiaZi[i]] + " "
            self.strDaYunZhouSui += str(qiyunZhouSui + i * 10) + " "
            self.strDaYunQiNian += str(qiyunGLNian + i * 10) + " "
            strDaYunZhiNian += str(qiyunGLNian + 9 + i * 10) + " "
            i = i + 1
        # 添加到结果串
        self.strRet += self.strDaYunJiaZi + "<br>" 
        self.strRet += self.strDaYunNaYin + "<br>" 
        self.strRet += self.strDaYunZhouSui + "<br>" 
        self.strRet += self.strDaYunQiNian + "<br>" 
        self.strRet += "流年<br>" 
        self.syblArra = []
        syblCount = 0
        # 共十行
        j = 0
        while j < 10:
            strCurLine = "+" + str(j) + " "
            i = 0
            strCurLine = ''
            while i < 8:
                # 共八列
                # 当前年份甲子数
                curYJZ = (iQiYunGLNianJZ + j + i * 10) % 60 
                strCurLine += jia_zi[curYJZ] + " "
                # 是否岁运并临
                if curYJZ == arrayDaYunJiaZi[i]:  # 岁运并临
                    self.syblArray.append(qiyunGLNian + j + i * 10)
                    syblCount = syblCount + 1
                i = i + 1
            self.big_yun.append(strCurLine)
            self.strRet += strCurLine + "<br>" 
            j = j + 1


if __name__ == '__main__':
    jie_qi = JieQi()
    jie_qi.get_jie_qi(2022)

    """
    https://mp.weixin.qq.com/s/v6GH63_W5Ar8tfgewnDe6g
    """
    a = FatePlan("戊寅 癸亥 壬戌 丙午", '男')
    a.get_big_fate()
