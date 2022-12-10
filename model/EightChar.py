import re
from collections import Counter

from model.TenGodTable import TenGodTrunkTable, TenGodBranchTable, SheepBladeTable, FiveElementTable, VigorousWeakTable


class EightChar:

    def __init__(self, eightChar):
        self.eightCharFormat = eightChar
        self.eightChar = re.sub(r"\s+", "", eightChar)
        self.yearTrunk = self.eightChar[0]
        self.yearBranch = self.eightChar[1]
        self.monthTrunk = self.eightChar[2]
        self.monthBranch = self.eightChar[3]
        self.dayTrunk = self.eightChar[4]
        self.dayBranch = self.eightChar[5]
        self.hourTrunk = self.eightChar[6]
        self.hourBranch = self.eightChar[7]
        self.trunk = self.yearTrunk + self.monthTrunk + self.dayTrunk + self.hourTrunk
        self.branch = self.yearBranch + self.monthBranch + self.dayBranch + self.hourBranch

    def __str__(self):
        return self.eightCharFormat


"""
辛未年，辛卯月，乙酉日，戊寅时。

丁卯
甲辰
辛卯
戊子

丙子年，甲午月，甲辰日，己巳时

玉午
丙午
丙戍
庚寅

乙卯、丙戌、癸西、丙辰

辛丑 甲午 丙申 王辰
丁丙丁甲
酉申卯子
"""
if __name__ == '__main__':
    a = EightChar("辛未 辛卯 乙酉 戊寅")
    #a = EightChar("辛未 辛卯 乙酉 丁丑")
    # a = EightChar("丁卯 甲辰 辛卯 戊子")
    # a = EightChar("乙卯 丙戌 癸酉 丙辰")
    # a = EightChar("辛丑 甲午 丙申 壬辰")
    # a = EightChar("甲子 丁卯 丙申 丁酉")

    trunk = getattr(a, "trunk")
    branch = getattr(a, "branch")
    eightChar = getattr(a, "eightChar")

    trunkTable = TenGodTrunkTable()
    branchTable = TenGodBranchTable()
    sheepBladeTable = SheepBladeTable()

    ten_god_list = []

    print("--- trunk & trunk-----")
    for i, a in enumerate(trunk):
        for j, b in enumerate(trunk):
            if i != j:
                trunk_key = trunkTable.getResult(a + b)
                ten_god_list.append(trunk_key)

    print("--- trunk & branch-----")
    for a in trunk:
        for b in branch:
            god = branchTable.getResult(a + b)
            ten_god_list.append(god)

    print("--- trunk & branch sheepBladeTable -----")
    for a in trunk:
        for b in branch:
            god = sheepBladeTable.getResult(a + b)
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
