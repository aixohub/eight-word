from model.EightChar import EightChar
import pandas as pd


class LuckyGod:
    def __init__(self, eightChar):
        self.eightChar = eightChar
        self.tips = ''

    def one_tian_yi(self):
        """
        天乙贵人
        甲戊并牛羊，乙己鼠猴乡，
        丙丁猪鸡位，壬癸蛇兔藏，
        庚辛逢虎马，此是贵人方。
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '空', '天乙', '空', '空', '空', '空', '空', '天乙', '空', '空', '空', '空'],
                      ['乙', '天乙', '空', '空', '空', '空', '空', '空', '空', '天乙', '空', '空', '空'],
                      ['丙', '空', '空', '空', '空', '空', '空', '空', '空', '空', '天乙', '空', '天乙'],
                      ['丁', '空', '空', '空', '空', '空', '空', '空', '空', '空', '天乙', '空', '天乙'],
                      ['戊', '空', '天乙', '空', '空', '空', '空', '空', '天乙', '空', '空', '空', '空'],
                      ['己', '天乙', '空', '空', '空', '空', '空', '空', '空', '天乙', '空', '空', '空'],
                      ['庚', '空', '空', '天乙', '空', '空', '空', '天乙', '空', '空', '空', '空', '空'],
                      ['辛', '空', '空', '天乙', '空', '空', '空', '天乙', '空', '空', '空', '空', '空'],
                      ['壬', '空', '空', '空', '天乙', '空', '天乙', '空', '空', '空', '空', '空', '空'],
                      ['癸', '空', '空', '空', '天乙', '空', '天乙', '空', '空', '空', '空', '空', '空']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearTrunk = self.eightChar.yearTrunk
        dayTrunk = self.eightChar.dayTrunk
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearTrunk, item]
            print("天乙 year_info ：" + yearTrunk + item + " = " + year_info)
            day_info = table.loc[dayTrunk, item]
            print("天乙 day_info ：" + dayTrunk + item + " = " + day_info)

    def second_tai_ji(self):
        """
        太极贵人

        """

    def three_gui(self):
        """

        """
        print()


if __name__ == '__main__':
    # a = EightChar("戊寅 癸亥 壬戌 丙午")
    a = EightChar("乙丑 乙酉 甲戌 辛未")
    b = LuckyGod(a)
    b.one_tian_yi()
    print()
