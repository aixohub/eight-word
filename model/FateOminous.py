from model.EightChar import EightChar
import pandas as pd


class FateOminous:
    """

    """

    def __init__(self, eightChar):
        self.eightChar = eightChar
        self.tips = ''

    def sky_land(self):
        print()

    def sheep_blade_two(self):
        """
        羊刃
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


if __name__ == '__main__':
    a = EightChar("辛未 辛卯 乙酉 戊寅")
    ominous = FateOminous(a)
    ominous.sheep_blade_two()
