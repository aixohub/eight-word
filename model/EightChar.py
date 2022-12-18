import collections
import re


class EightChar:

    def __init__(self, eightChar):
        self.eightChar = re.sub(r"\s+", "", eightChar)
        self.yearTrunk = self.eightChar[0]
        self.yearBranch = self.eightChar[1]
        self.year = self.eightChar[0] + self.eightChar[1]
        self.monthTrunk = self.eightChar[2]
        self.monthBranch = self.eightChar[3]
        self.month = self.eightChar[2] + self.eightChar[3]
        self.dayTrunk = self.eightChar[4]
        self.dayBranch = self.eightChar[5]
        self.day = self.eightChar[4] + self.eightChar[5]
        self.hourTrunk = self.eightChar[6]
        self.hourBranch = self.eightChar[7]
        self.hour = self.eightChar[6] + self.eightChar[7]

        self.trunk = self.yearTrunk + self.monthTrunk + self.dayTrunk + self.hourTrunk
        self.branch = self.yearBranch + self.monthBranch + self.dayBranch + self.hourBranch
        trunkObj = collections.namedtuple("trunk", "year month day time")
        branchObj = collections.namedtuple("branch", "year month day time")
        self.trunkAll = trunkObj(year=self.yearTrunk, month=self.monthTrunk,
                                 day=self.dayTrunk, time=self.hourTrunk)
        self.branchAll = branchObj(year=self.yearBranch, month=self.monthBranch,
                                   day=self.dayBranch, time=self.hourBranch)
        self.eightWord = [item for item in zip(self.trunkAll, self.branchAll)]


"""

"""
if __name__ == '__main__':
    #  a = EightChar("辛未 辛卯 乙酉 戊寅")
    a = EightChar("戊寅 癸亥 壬戌 丙午")
    print(a)
    # a = EightChar("辛未 辛卯 乙酉 丁丑")
    # a = EightChar("丁卯 甲辰 辛卯 戊子")
    # a = EightChar("乙卯 丙戌 癸酉 丙辰")
    # a = EightChar("辛丑 甲午 丙申 壬辰")
    # a = EightChar("甲子 丁卯 丙申 丁酉")
