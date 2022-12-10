import re

from model.TenGodTable import TenGodTrunkTable, TenGodBranchTable


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
"""
if __name__ == '__main__':
    a = EightChar("辛未 辛卯 乙酉 戊寅")
    #a = EightChar("丁卯 甲辰 辛卯 戊子")

    trunk = getattr(a, "trunk")
    branch = getattr(a, "branch")
    trunkTable = TenGodTrunkTable()
    branchTable = TenGodBranchTable()
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

    print(set(ten_god_list))
