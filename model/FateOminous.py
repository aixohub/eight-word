from model.EightChar import EightChar
import pandas as pd


class FateOminous:
    """
    凶煞
    """

    def __init__(self):
        self.eightChar = None
        self.tips = ''

    def exec_fate_ominous(self, eightChar):
        self.eightChar = eightChar
        print("=" * 70 + " 凶煞 " + "=" * 70)
        self.sheep_blade_two()
        print("=" * 140)
        self.nine_kong_wang()

    def sky_land_one(self):
        """

        """
        print()

    def sheep_blade_two(self):
        """
        羊刃

        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3, ):  # more options can be specified also
            print(table.to_markdown())
        """
        table_header = ['日干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

        # 定义表数据'子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥'
        table_data = [
            ['甲', ' ', ' ', '禄', '刃', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['乙', ' ', ' ', '刃', '禄', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['丙', ' ', ' ', ' ', ' ', ' ', '禄', '刃', ' ', ' ', ' ', ' ', ' '],
            ['丁', ' ', ' ', ' ', ' ', ' ', '刃', '禄', ' ', ' ', ' ', ' ', ' '],
            ['戊', ' ', ' ', ' ', ' ', ' ', '禄', '刃', ' ', ' ', ' ', ' ', ' '],
            ['己', ' ', ' ', ' ', ' ', ' ', '刃', '禄', ' ', ' ', ' ', ' ', ' '],
            ['庚', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '禄', '刃', ' ', ' '],
            ['辛', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '刃', '禄', ' ', ' '],
            ['壬', '刃', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '禄'],
            ['癸', '禄', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '刃']
        ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("日干", inplace=True)
        #
        dayTrunk = self.eightChar.dayTrunk
        branch = self.eightChar.branch

        for item in branch:
            day_info = table.loc[dayTrunk, item]
            print("羊刃 day_info ：" + dayTrunk + item + " = " + day_info)

    def nine_kong_wang(self):
        """
        甲子、乙丑、丙寅、丁卯、戊辰、己巳、庚午、辛未、壬申、癸酉、此十天为甲子旬、凡生此十日，地支见戌或见亥，戌亥皆属旬空。
        甲戌、乙亥、丙子、丁丑、戊寅、己卯、庚辰、辛巳、壬午、癸未、此十天为甲戌旬。凡生此十日，地支见申或见酉，申酉皆属旬空。
        甲申、乙酉、丙戌、丁亥、戊子、己丑、庚寅、辛卯、壬辰、癸巳，此十天为甲申旬。凡生此十日，地支见午或见未，午未皆属旬空。
        甲午、乙未、丙甲、丁酉、戊戌、己亥、庚子、辛丑、壬寅，癸卯、此十天为甲午旬。凡生此十日，地支见辰或见巳，辰巳省属旬空。
        甲辰、乙巳、丙午、丁未、戊申、己酉、庚戌、辛亥、壬子、癸丑，此十天为甲辰旬。凡生此十日，地支见寅或见卯，寅卯皆属旬空。
        甲寅、乙卯、丙辰、丁巳、戊午、己未、庚申、辛酉、壬戌、癸亥，此十天为甲寅旬。凡生此十日，地支见子或见丑，子丑皆属旬空。

        空亡的查法．是以日为主，柱中年、月、时支见者为空亡。
        就是说、从甲子日到癸西日这十天中无戌亥二字，如四柱中见者．则为空亡。其他仿此。
        空．对实言。亡、对有言。空亡，用最简单的语言表示就是时间不到。
        如甲子旬中戌亥空，一旬只有十天、戌亥在第十一天和第十二天．如果到了成和亥这两天，就叫出空。
        出空则不空。四柱虽有空亡，但有冲有合有刑不为空，反之，才是真空。吉神空而喜见合，凶星空而忌见合。

        空在年支上，一是祖业空，二是母空、或辞世．或改嫁，或出走远离．或母不顾子，有母若无。
        空在月支上，多指无兄弟姐妹．或兄弟姐妹无靠。
        空在时支上，一是结婚后不能马上有孩子，二是无子女或子女无靠。
        如辛未年辛丑月丙戌日甲午时生人。丙戌日是在甲申旬中，“甲申旬中午未空”、四柱时上之午年柱未为旬空，此空在母位和儿女宫中。
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '戌亥', '否', '子丑', '否', '寅卯', '否', '辰巳', '否', '午未', '否', '申酉', '否'],
                      ['乙', '否', '戌亥', '否', '子丑', '否', '寅卯', '否', '辰巳', '否', '午未', '否', '申酉'],
                      ['丙', '申酉', '否', '戌亥', '否', '子丑', '否', '寅卯', '否', '辰巳', '否', '午未', '否'],
                      ['丁', '否', '申酉', '否', '戌亥', '否', '子丑', '否', '寅卯', '否', '辰巳', '否', '午未'],
                      ['戊', '午未', '否', '申酉', '否', '戌亥', '否', '子丑', '否', '寅卯', '否', '辰巳', '否'],
                      ['己', '否', '午未', '否', '申酉', '否', '戌亥', '否', '子丑', '否', '寅卯', '否', '辰巳'],
                      ['庚', '辰巳', '否', '午未', '否', '申酉', '否', '戌亥', '否', '子丑', '否', '寅卯', '否'],
                      ['辛', '否', '辰巳', '否', '午未', '否', '申酉', '否', '戌亥', '否', '子丑', '否', '寅卯'],
                      ['壬', '寅卯', '否', '辰巳', '否', '午未', '否', '申酉', '否', '戌亥', '否', '子丑', '否'],
                      ['癸', '否', '寅卯', '否', '辰巳', '否', '午未', '否', '申酉', '否', '戌亥', '否', '子丑']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        dayTrunk = self.eightChar.dayTrunk
        dayBranch = self.eightChar.dayBranch
        branch = self.eightChar.branch
        null_info = table.loc[dayTrunk, dayBranch]
        flag = False
        for item in null_info:
            for branch_item in branch:
                if item == branch_item:
                    flag = True
        if flag:
            print(null_info + " " + branch + " 旬空 ✅")
        else:
            print(null_info + " " + branch + " 旬空 ❌")


if __name__ == '__main__':
    a = EightChar("辛未 辛卯 乙酉 戊寅")
    ominous = FateOminous()
    ominous.exec_fate_ominous(a)
