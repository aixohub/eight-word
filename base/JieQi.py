from base import int2, J2000
from base.Lunar import SSQ, Obb


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
            zq = self.ssq.ZQ[i]
            self.arrayJQ.append(self.obb.qi_accurate2(zq) + J2000)
            i = i + 1
        # 计算下一年的节气表，提取冬至到立春4个
        self.ssq.calcY(int2((y + 1 - 2000) * 365.2422 + 180))
        i = 0
        while i < 4:  # 立春到大雪，21个
            zq = self.ssq.ZQ[i]
            self.arrayJQ.append(self.obb.qi_accurate2(zq) + J2000)
            i = i + 1
        return self.arrayJQ

    # 快捷函数，根据年数字获取甲子数
    def GetNianJiaZiShu(self, yy):
        iJZ = (yy - 1984 + 6000000) % 60
        return iJZ