import collections
import math
from collections import Counter

from base.Paipan import Paipan
from model.EightChar import EightChar
from model.Nayin import na_yin_dict
from model.TenGodTable import VigorousWeakTable, FiveElementTable, TenGodTrunkTable, TenGodBranchTable, SheepBladeTable


class TempleWish:
    def __init__(self, eightChar):
        self.eightChar = EightChar(eightChar)
        trunkObj = collections.namedtuple("trunk", "year month day time")
        branchObj = collections.namedtuple("branch", "year month day time")
        self.trunkAll = trunkObj(year=self.eightChar.yearTrunk, month=self.eightChar.monthTrunk,
                                 day=self.eightChar.dayTrunk, time=self.eightChar.hourTrunk)
        self.branchAll = branchObj(year=self.eightChar.yearBranch, month=self.eightChar.monthBranch,
                                   day=self.eightChar.dayBranch, time=self.eightChar.hourBranch)
        self.eightWord = [item for item in zip(self.trunkAll, self.branchAll)]
        self.trunkTable = TenGodTrunkTable()
        self.branchTable = TenGodBranchTable()
        self.sheepBladeTable = SheepBladeTable()
        self.vigorousWeakTable = VigorousWeakTable()
        self.chang_sheng = None
        self.ten_god = None
        self.na_yin = None

    def exec_analyze(self):
        self.chang_sheng = [self.vigorousWeakTable.getResult(self.eightChar.dayTrunk + self.eightChar.yearBranch),
                            self.vigorousWeakTable.getResult(self.eightChar.dayTrunk + self.eightChar.monthBranch),
                            self.vigorousWeakTable.getResult(self.eightChar.dayTrunk + self.eightChar.dayBranch),
                            self.vigorousWeakTable.getResult(self.eightChar.dayTrunk + self.eightChar.hourBranch)]
        self.ten_god = [self.branchTable.getResult(self.eightChar.yearTrunk + self.eightChar.yearBranch),
                        self.branchTable.getResult(self.eightChar.monthTrunk + self.eightChar.monthBranch),
                        self.branchTable.getResult(self.eightChar.dayTrunk + self.eightChar.dayBranch),
                        self.branchTable.getResult(self.eightChar.hourTrunk + self.eightChar.hourBranch)]
        self.na_yin = []
        for item in self.eightWord:
            self.na_yin.append(na_yin_dict[item])

    def exec_analyze_match(self):
        trunk = self.eightChar.trunk
        branch = self.eightChar.branch
        eightChar = self.eightChar.eightChar
        ten_god_list = []

        print("--- trunk & trunk-----")
        for i, a in enumerate(trunk):
            for j, b in enumerate(trunk):
                if i != j:
                    trunk_key = self.trunkTable.getResult(a + b)
                    ten_god_list.append(trunk_key)

        print("--- trunk & branch-----")
        for a in trunk:
            for b in branch:
                god = self.branchTable.getResult(a + b)
                ten_god_list.append(god)

        print("--- trunk & branch sheepBladeTable -----")
        for a in trunk:
            for b in branch:
                god = self.sheepBladeTable.getResult(a + b)
                ten_god_list.append(god)
        print(Counter(ten_god_list))
        print(set(ten_god_list))

        print("----- five -------")
        five_element_list = []
        fiveElementTable = FiveElementTable()
        for char in eightChar:
            fiveElement = fiveElementTable.getResult(char)
            five_element_list.append(fiveElement)
        print(Counter(five_element_list))

        print("--- trunk & branch VigorousWeak-----")
        vigorous_weak_list = []
        vigorousWeakTable = VigorousWeakTable()
        for a in trunk:
            for b in branch:
                god = vigorousWeakTable.getResult(a + b)
                vigorous_weak_list.append(god)

        print(Counter(vigorous_weak_list))

    def exec_analyze_print(self):
        print("=" * 140)
        print("{:^28s}{:^28s}{:^28s}{:^28s}{:^28s}".format('--', ' 年', " 月", " 日", " 时"))
        print("-" * 140)
        print(
            "{:^28s}{:^28s}{:^28s}{:^28s}{:^28s}"
            .format('十神', self.ten_god[0], self.ten_god[1], self.ten_god[2], self.ten_god[3]))
        print("{:^28s}{:^28s}{:^28s}{:^28s}{:^28s}"
              .format('天干', self.eightChar.yearTrunk, self.eightChar.monthTrunk, self.eightChar.dayTrunk,
                      self.eightChar.hourTrunk))
        print("{:^28s}{:^28s}{:^28s}{:^28s}{:^28s}"
              .format('地支', self.eightChar.yearBranch, self.eightChar.monthBranch, self.eightChar.dayBranch,
                      self.eightChar.hourBranch))

        print("{:^28s}{:^28s}{:^28s}{:^28s}{:^28s}"
              .format('藏干', self.eightChar.yearBranch, self.eightChar.monthBranch, self.eightChar.dayBranch,
                      self.eightChar.hourBranch))

        print(
            "{:^28s}{:^28s}{:^28s}{:^28s}{:^28s}"
            .format('十二长生', self.chang_sheng[0], self.chang_sheng[1], self.chang_sheng[2], self.chang_sheng[3]))
        print("{:^28s}".format('纳音'), end=' ')
        for item in self.na_yin:
            print("{:^26s}".format(item), end=' ')
        print()
        print("-" * 140)


if __name__ == '__main__':
    pai_pan = Paipan()
    eight_char = pai_pan.get_eight_char('甘肃省', '兰州市', "2022-12-18", "12:2:41")
    print(eight_char)
    # a = TempleWish("辛未 辛卯 乙酉 戊寅")
    a = TempleWish("戊寅 癸亥 壬戌 丙午")

    # a = EightChar("辛未 辛卯 乙酉 丁丑")
    # a = EightChar("丁卯 甲辰 辛卯 戊子")
    # a = EightChar("乙卯 丙戌 癸酉 丙辰")
    # a = EightChar("辛丑 甲午 丙申 壬辰")
    # a = EightChar("甲子 丁卯 丙申 丁酉")
    a.exec_analyze()
    a.exec_analyze_print()
