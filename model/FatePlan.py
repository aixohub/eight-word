from base import int2, J2000
from base.Lunar import SSQ, Obb
from model.EightChar import EightChar
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


class BaZiObject:
    def __init__(self):
        self.JDBirth = None
        self.JDBirthZTY = None


class FatePlan:

    def __init__(self, eightChar, sex):
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
        self.eightChar = EightChar(eightChar)
        self.sex = sex
        self.fiveElementTable = FiveElementTable()

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


if __name__ == '__main__':
    jie_qi = JieQi()
    jie_qi.get_jie_qi(2022)
    """
    https://mp.weixin.qq.com/s/v6GH63_W5Ar8tfgewnDe6g
    """
    a = FatePlan("戊寅 癸亥 壬戌 丙午", '男')
    a.get_big_fate()
