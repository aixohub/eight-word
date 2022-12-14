from model.EightChar import EightChar
import pandas as pd


class FateGodLucky:
    """


    """

    def __init__(self):
        self.eightChar = None
        self.tips = ''

    def exec_god_lucky(self, eightChar):
        self.eightChar = eightChar
        print("=" * 70 + " 吉神 " + "=" * 70)
        self.one_tian_yi()
        print("=" * 140)
        self.second_tai_ji()
        print("=" * 140)
        self.three_tina_de()
        self.three_yue_de()
        print("=" * 140)
        self.five_fu_star()
        print("=" * 140)
        self.ten_de_xiu()
        print("=" * 140)
        self.eleven_stage_horse()
        print("=" * 140)
        self.twelve_canopy()
        print("=" * 140)
        self.sixteen_sky_doctor()

    def format_print(self, flag):
        if flag == '是':
            return ' ✅'
        elif flag == '否':
            return ' ❌'
        else:
            return ' 🎾🏌🤺'

    def one_tian_yi(self):
        """
        天乙贵人
        甲戊并牛羊，乙己鼠猴乡，
        丙丁猪鸡位，壬癸蛇兔藏，
        庚辛逢虎马，此是贵人方。
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '否', '是', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否'],
                      ['乙', '是', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否'],
                      ['丙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '是'],
                      ['丁', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '是'],
                      ['戊', '否', '是', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否'],
                      ['己', '是', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否'],
                      ['庚', '否', '否', '是', '否', '否', '否', '是', '否', '否', '否', '否', '否'],
                      ['辛', '否', '否', '是', '否', '否', '否', '是', '否', '否', '否', '否', '否'],
                      ['壬', '否', '否', '否', '是', '否', '是', '否', '否', '否', '否', '否', '否'],
                      ['癸', '否', '否', '否', '是', '否', '是', '否', '否', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearTrunk = self.eightChar.yearTrunk
        dayTrunk = self.eightChar.dayTrunk
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearTrunk, item]
            print("天乙贵人 year_info ：" + yearTrunk + item + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[dayTrunk, item]
            print("天乙贵人 day_info ：" + dayTrunk + item + " = " + day_info + self.format_print(day_info))

    def second_tai_ji(self):
        """
        太极贵人
        甲乙生人子午中，丙丁鸡兔定享通，
        戊已两干临四季，庚辛寅亥禄丰隆，
        壬癸巳申偏喜美，值此应当福气钟，
        更须贵格来相扶，侯封万户到三公。

        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '是', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否'],
                      ['乙', '是', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否'],
                      ['丙', '否', '否', '否', '是', '否', '否', '否', '否', '否', '是', '否', '否'],
                      ['丁', '否', '否', '否', '是', '否', '否', '否', '否', '否', '是', '否', '否'],
                      ['戊', '否', '是', '否', '否', '是', '否', '否', '是', '否', '否', '是', '否'],
                      ['己', '否', '是', '否', '否', '是', '否', '否', '是', '否', '否', '是', '否'],
                      ['庚', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '是'],
                      ['辛', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '是'],
                      ['壬', '否', '否', '否', '否', '否', '是', '否', '否', '是', '否', '否', '否'],
                      ['癸', '否', '否', '否', '否', '否', '是', '否', '否', '是', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearTrunk = self.eightChar.yearTrunk
        dayTrunk = self.eightChar.dayTrunk
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearTrunk, item]
            print("太极贵人 year_info ：" + yearTrunk + item + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[dayTrunk, item]
            print("太极贵人 day_info ：" + dayTrunk + item + " = " + day_info + self.format_print(day_info))

    def three_tina_de(self):
        """
        天德贵人
        正月生者见丁，二月生者见申，
        三月生者见壬，四月生者见辛，
        五月生者见亥，六月生者见甲，
        七月生者见癸，八月生者见寅，
        九月生者见丙，十月生者见乙，
        十一月生者巳，十二月生者见庚。
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否'],
                      ['乙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是'],
                      ['丙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否'],
                      ['丁', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['戊', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['己', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['庚', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['辛', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否'],
                      ['壬', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否'],
                      ['癸', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否'],

                      ['子', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丑', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['寅', '否', '否', '是', '否', '否', '否', '否', '否', '否', '是', '否', '否'],
                      ['卯', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['辰', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['巳', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['午', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['未', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['申', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['酉', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['戌', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['亥', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        monthBranch = self.eightChar.monthBranch
        trunk = self.eightChar.trunk
        branch = self.eightChar.branch
        for item in trunk:
            year_info = table.loc[item, monthBranch]
            print("天德贵人 year_info ：" + item + monthBranch + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[item, monthBranch]
            print("天德贵人 day_info ：" + item + monthBranch + " = " + day_info + self.format_print(day_info))

    def three_yue_de(self):
        """
        月德贵人
        寅午戌月生者见丙，申子辰月生者见王，
        亥卯未月生者见甲，已西丑月生者见庚。
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['乙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丁', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['戊', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['己', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['庚', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['辛', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['壬', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['癸', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        monthBranch = self.eightChar.monthBranch
        trunk = self.eightChar.trunk
        branch = self.eightChar.branch
        for item in trunk:
            year_info = table.loc[item, monthBranch]
            print("月德贵人 year_info ：" + item + monthBranch + " = " + year_info + self.format_print(year_info))

    def four__back(self):
        """
        back
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['乙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丁', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['戊', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['己', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['庚', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['辛', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['壬', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['癸', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearTrunk = self.eightChar.yearTrunk
        dayTrunk = self.eightChar.dayTrunk
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearTrunk, item]
            print("月德贵人 year_info ：" + yearTrunk + item + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[dayTrunk, item]
            print("月德贵人 day_info ：" + dayTrunk + item + " = " + day_info + self.format_print(day_info))

    def four_san_qi(self):
        """
        三奇贵人

        天上三奇甲戊庚，
        地下三奇乙丙丁，
        人中三奇壬癸辛。
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['乙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丁', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['戊', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['己', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['庚', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['辛', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['壬', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['癸', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearTrunk = self.eightChar.yearTrunk
        dayTrunk = self.eightChar.dayTrunk
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearTrunk, item]
            print("月德贵人 year_info ：" + yearTrunk + item + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[dayTrunk, item]
            print("月德贵人 day_info ：" + dayTrunk + item + " = " + day_info + self.format_print(day_info))

    def five_fu_star(self):
        """
        福星贵人
        甲丙相遂入虎乡，更游鼠穴最高强，
        戊猴己未丁宜亥，乙癸逢生卯禄昌，
        庚赶马头辛到巳，壬骑龙背喜非常，
        此为有福文昌贵，遇者应知受宠光。
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '是', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['乙', '否', '是', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丙', '是', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丁', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是'],
                      ['戊', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否'],
                      ['己', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否'],
                      ['庚', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否'],
                      ['辛', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否'],
                      ['壬', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否'],
                      ['癸', '否', '是', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearTrunk = self.eightChar.yearTrunk
        dayTrunk = self.eightChar.dayTrunk
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearTrunk, item]
            print("福星贵人 year_info ：" + yearTrunk + item + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[dayTrunk, item]
            print("福星贵人 day_info ：" + dayTrunk + item + " = " + day_info + self.format_print(day_info))

    def six_wen_chang(self):
        """
        文昌贵人
        甲乙巳午报君知，丙戊申官丁己鸡。
        庚猪辛鼠壬逢虎，癸人见卯入云梯。

        文昌者，居食神之临官长生之故。
        甲以丙为食神，丙临官于巳，故甲以巳为文昌。
        乙以丁为食神，丁临临官于午，故乙以午为文昌。
        丙以戊为食神，戊寄生于申，故丙以申为文昌。
        戊以庚为食神，庚临官于申，故戊以申为文昌。
        丁以己为食神，己长生于酉，故丁以酉为文昌。
        庚辛壬癸仿此。
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否'],
                      ['乙', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否'],
                      ['丙', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否'],
                      ['丁', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否'],
                      ['戊', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否'],
                      ['己', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否'],
                      ['庚', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是'],
                      ['辛', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['壬', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['癸', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearTrunk = self.eightChar.yearTrunk
        dayTrunk = self.eightChar.dayTrunk
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearTrunk, item]
            print("文昌贵人 year_info ：" + yearTrunk + item + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[dayTrunk, item]
            print("文昌贵人 day_info ：" + dayTrunk + item + " = " + day_info + self.format_print(day_info))

    def seven_yue_back(self):
        """
        魁罡


        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['乙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丙', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丁', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['戊', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['己', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['庚', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['辛', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['壬', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['癸', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearTrunk = self.eightChar.yearTrunk
        dayTrunk = self.eightChar.dayTrunk
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearTrunk, item]
            print("魁罡贵人 year_info ：" + yearTrunk + item + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[dayTrunk, item]
            print("魁罡贵人 day_info ：" + dayTrunk + item + " = " + day_info + self.format_print(day_info))

    def ten_de_xiu(self):
        """
        德秀贵人

        以生月为主，看四柱天干中有否，具体查询方法如下：
        寅午戌月，丙丁为德，戊癸为秀；
        申子辰月，壬癸戊己为德，丙辛甲己为秀；
        巳酉丑月，庚辛为德，乙庚为秀；
        亥卯未月，甲乙为德，丁壬为秀。

        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌','亥'
        table_data = [['甲', '秀', '否', '否', '德', '秀', '否', '否', '德', '秀', '否', '否', '德'],
                      ['乙', '否', '秀', '否', '德', '否', '秀', '否', '德', '否', '秀', '否', '德'],
                      ['丙', '秀', '否', '德', '否', '秀', '否', '德', '否', '秀', '否', '德', '否'],
                      ['丁', '否', '否', '德', '秀', '否', '否', '德', '秀', '否', '否', '德', '秀'],
                      ['戊', '德', '否', '秀', '否', '德', '否', '秀', '否', '德', '否', '秀', '否'],
                      ['己', '德秀', '否', '否', '否', '德秀', '否', '否', '否', '德秀', '否', '否', '否'],
                      ['庚', '否', '德秀', '否', '否', '否', '德秀', '否', '否', '否', '德秀', '否', '否'],
                      ['辛', '秀', '德', '否', '否', '秀', '德', '否', '否', '秀', '德', '否', '否'],
                      ['壬', '德', '否', '否', '秀', '德', '否', '否', '秀', '德', '否', '否', '秀'],
                      ['癸', '德', '否', '秀', '否', '德', '否', '秀', '否', '德', '否', '秀', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        monthBranch = self.eightChar.monthBranch
        trunk = self.eightChar.trunk
        for item in trunk:
            info = table.loc[item, monthBranch]
            print("德秀贵人 info ：" + item + monthBranch + " = " + info + self.format_print(info))


    def eight_yue_back(self):
        """
        back zhi

        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌',  '亥'
        table_data = [['子', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丑', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['寅', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['卯', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['辰', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['巳', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['午', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['未', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['申', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['酉', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['戌', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['亥', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearTrunk = self.eightChar.yearTrunk
        dayTrunk = self.eightChar.dayTrunk
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearTrunk, item]
            print("back year_info ：" + yearTrunk + item + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[dayTrunk, item]
            print("back day_info ：" + dayTrunk + item + " = " + day_info + self.format_print(day_info))

    def eleven_stage_horse(self):
        """
        驿马

        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌',  '亥'
        table_data = [['子', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['丑', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是'],
                      ['寅', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否'],
                      ['卯', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否'],
                      ['辰', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['巳', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是'],
                      ['午', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否'],
                      ['未', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否'],
                      ['申', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['酉', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是'],
                      ['戌', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否'],
                      ['亥', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearBranch = self.eightChar.yearBranch
        dayBranch = self.eightChar.dayBranch
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearBranch, item]
            print("驿马 year_info ：" + yearBranch + item + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[dayBranch, item]
            print("驿马 day_info ：" + dayBranch + item + " = " + day_info + self.format_print(day_info))

    def twelve_canopy(self):
        """
        华盖

        寅午戌见戌，亥卯未见未，
        申子辰见辰，巳酉丑见丑。
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌',  '亥'
        table_data = [['子', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否'],
                      ['丑', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['寅', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否'],
                      ['卯', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否'],
                      ['辰', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否'],
                      ['巳', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['午', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否'],
                      ['未', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否'],
                      ['申', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否'],
                      ['酉', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['戌', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否'],
                      ['亥', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        yearBranch = self.eightChar.yearBranch
        dayBranch = self.eightChar.dayBranch
        branch = self.eightChar.branch
        for item in branch:
            year_info = table.loc[yearBranch, item]
            print("华盖 year_info ：" + yearBranch + item + " = " + year_info + self.format_print(year_info))
        for item in branch:
            day_info = table.loc[dayBranch, item]
            print("华盖 day_info ：" + dayBranch + item + " = " + day_info + self.format_print(day_info))

    def sixteen_sky_doctor(self):
        """
        天医

        正月生见丑，二月生见寅，三月生见卯，
        四月生见辰，五月生见巳，六月生见午，
        七月生见未，八月生见申，九月生见酉，
        十月生见戌，十一月生见亥，十二月生见子。
        """
        table_header = ['干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        # 定义表数据          '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌',  '亥'
        table_data = [['子', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是'],
                      ['丑', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['寅', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['卯', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['辰', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否'],
                      ['巳', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否'],
                      ['午', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否', '否'],
                      ['未', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否', '否'],
                      ['申', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否', '否'],
                      ['酉', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否', '否'],
                      ['戌', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否', '否'],
                      ['亥', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '是', '否']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("干", inplace=True)
        monthBranch = self.eightChar.monthBranch
        branch = self.eightChar.branch
        for item in branch:
            day_info = table.loc[monthBranch, item]
            print("天医 day_info ：" + monthBranch + item + " = " + day_info + self.format_print(day_info))


if __name__ == '__main__':
    # a = EightChar("戊寅 癸亥 壬戌 丙午")
    # a = EightChar("乙丑 乙酉 甲戌 辛未")
    a = EightChar("辛未 辛卯 乙酉 戊寅")
    b = FateGodLucky()
    b.exec_god_lucky(a)
