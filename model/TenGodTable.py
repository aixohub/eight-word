import pandas as pd


class TenGodTrunkTable:
    """
    请述财官印等之构成。
    生我者，阳见阳，或阴见阴，为枭神。阴见阳，或阳见阴，为正印。
    我生者。阳见阳，或阴见阴，为食神。阴见阳,或阳见阴,为伤官。
    克我者，阳见阳，或阴见阴，为七杀。阴见阳，或阳见阴，为正官。
    我克者。阳见阳，或阴见阴，为偏财。阴见阳，或阳见阴,为正财。
    仝我者。阳见阳,或阴见阴,为比肩。阴见阳，或阳见阴，为劫财。

    再请举例明之，我字指何物。
    我字即日干，例如甲木日干，遇丁火，甲为阳
    木，丁为阴火，甲木能生丁火，丁乃我生而阳
    见阴，即伤官也，
    又如辛金日干,遇乙木。辛为阴金，乙为阴木,
    辛金能克乙木，乙乃我克而阴见阴，即偏财也,
    特立表于后,以便检查。
    '日干', '伤官', '食柛', '正官', '七杀', '正财', '偏财', '正印', '枭神', '劫财', '比肩'
     [ '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    """

    def __init__(self):
        table_header = ['日干', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']

        # 定义表数据           '甲',   '乙',   '丙',   '丁',  '戊',  '己',   '庚',   '辛',   '壬',  '癸'
        table_data = [['甲', '比肩', '劫财', '食柛', '伤官', '偏财', '正财', '七杀', '正官', '枭神', '正印'],
                      ['乙', '劫财', '比肩', '伤官', '食柛', '正财', '偏财', '正官', '七杀', '正印', '枭神'],
                      ['丙', '枭神', '正印', '比肩', '劫财', '食柛', '伤官', '偏财', '正财', '七杀', '正官'],
                      ['丁', '正印', '枭神', '劫财', '比肩', '伤官', '食柛', '正财', '偏财', '正官', '七杀'],
                      ['戊', '七杀', '正官', '枭神', '正印', '比肩', '劫财', '食柛', '伤官', '偏财', '正财'],
                      ['己', '正官', '七杀', '正印', '枭神', '劫财', '比肩', '伤官', '食柛', '偏财', '偏财'],
                      ['庚', '偏财', '正财', '七杀', '正官', '枭神', '正印', '比肩', '劫财', '食柛', '伤官'],
                      ['辛', '正财', '偏财', '正官', '七杀', '正印', '枭神', '劫财', '比肩', '伤官', '食柛'],
                      ['壬', '食柛', '伤官', '偏财', '正财', '七杀', '正官', '枭神', '正印', '比肩', '劫财'],
                      ['癸', '伤官', '食柛', '正财', '偏财', '正官', '七杀', '正印', '枭神', '劫财', '比肩']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("日干", inplace=True)
        # 构造表
        self.table = table

    def __str__(self):
        return self.table.to_string()

    def getResult(self, str):
        dayTrunk = str[0]
        match = str[1]
        res = self.table.loc[dayTrunk, match]
        print(str + ": " + res)
        return res


class TenGodBranchTable:
    """
    甲、乙、丙、丁、戊、己、庚、辛、壬、癸 此为十天干,
    子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥 此为十二地支。
    '日干', '伤官', '食柛', '正官', '七杀', '正财', '偏财', '正印', '枭神', '劫财', '比肩'
     [ '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    """

    def __init__(self):
        table_header = ['日干', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

        # 定义表数据  '子',  '丑',   '寅',   '卯',   '辰',   '巳',  '午',  '未',   '申',   '酉',   '戌',  '亥'
        table_data = [
            ['甲', '正印', '正财', '比肩', '劫财', '偏财', '食柛', '伤官', '正财', '七杀', '正官', '偏财', '枭神'],
            ['乙', '枭神', '偏财', '劫财', '比肩', '正财', '伤官', '食柛', '偏财', '正官', '七杀', '正财', '正印'],
            ['丙', '正官', '伤官', '枭神', '正印', '食柛', '比肩', '劫财', '伤官', '偏财', '正财', '食柛', '七杀'],
            ['丁', '七杀', '食柛', '正印', '枭神', '伤官', '劫财', '比肩', '食柛', '正财', '偏财', '伤官', '正官'],
            ['戊', '正财', '劫财', '七杀', '正官', '比肩', '枭神', '正印', '劫财', '食柛', '伤官', '比肩', '偏财'],
            ['己', '偏财', '比肩', '正官', '七杀', '劫财', '正印', '枭神', '比肩', '伤官', '食柛', '劫财', '正财'],
            ['庚', '伤官', '正印', '偏财', '正财', '枭神', '七杀', '正官', '正印', '比肩', '劫财', '枭神', '食柛'],
            ['辛', '食柛', '枭神', '正财', '偏财', '正印', '正官', '七杀', '枭神', '劫财', '比肩', '正印', '伤官'],
            ['壬', '劫财', '正官', '食柛', '伤官', '七杀', '偏财', '正财', '正官', '枭神', '正印', '七杀', '比肩'],
            ['癸', '比肩', '七杀', '伤官', '食柛', '正官', '正财', '偏财', '七杀', '正印', '枭神', '正官', '劫财']
        ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("日干", inplace=True)
        # 构造表
        self.table = table

    def __str__(self):
        return self.table.to_string()

    def getResult(self, str):
        dayTrunk = str[0]
        match = str[1]
        res = self.table.loc[dayTrunk, match]
        print(str + ": " + res)
        return res


class SheepBladeTable:
    """
    禄之构成，我之本气也。如甲木本气在寅,寅即甲之禄也。
    按甲见寅，乙见卯, 丙戊见巳，丁己见午，庚见申，辛见酉, 壬见亥，癸见子，皆为禄。

    刃之构成
    禄前一位为刃。如甲之禄在寅,卯乃寅前一位,故为
    甲之刃惟阳顺阴逆，阴千以后作前，故禄前一位为刃，即
    禄后-位为刃,如乙之禄在卵,寅乃卯后一位，故为乙之刃。
    按甲见卯,乙见寅,丙戊见午，丁已见巳，庚见酉，辛见申，壬见子，癸见亥，皆为刃

    甲、乙、丙、丁、戊、己、庚、辛、壬、癸 此为十天干,
    子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥 此为十二地支。
    '日干', '伤官', '食柛', '正官', '七杀', '正财', '偏财', '正印', '枭神', '劫财', '比肩'
     [ '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    """

    def __init__(self):
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
        # 构造表
        self.table = table

    def __str__(self):
        return self.table.to_string()

    def getResult(self, str):
        dayTrunk = str[0]
        match = str[1]
        res = self.table.loc[dayTrunk, match]
        print(str + ": " + res)
        return res


class FiveElementTable:
    """
    甲乙寅卯皆为木,
    丙丁己午皆为火，
    戊己辰戌丑末皆为土，
    庚辛申酉皆为金，
    王癸亥子皆为水。
    寅辰已申戌亥为阳,子丑卯午未酉为阴。
     [ '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
     '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥'
    """

    def __init__(self):
        table_header = ['日干', '五行', '阴阳']

        # 定义表数据 '五行','阴阳','寅','卯','辰','巳','午','未','申','酉','戌','亥'
        table_data = [
            ['甲', '木', '阳'],
            ['乙', '木', '阴'],
            ['丙', '火', '阳'],
            ['丁', '火', '阴'],
            ['戊', '土', '阳'],
            ['己', '土', '阴'],
            ['庚', '金', '阳'],
            ['辛', '金', '阴'],
            ['壬', '水', '阳'],
            ['癸', '水', '阴'],

            ['子', '水', '阴'],
            ['丑', '土', '阴'],
            ['寅', '木', '阳'],
            ['卯', '木', '阴'],
            ['辰', '土', '阳'],
            ['己', '火', '阳'],
            ['午', '火', '阴'],
            ['未', '土', '阴'],
            ['申', '金', '阳'],
            ['酉', '金', '阴'],
            ['戌', '土', '阳'],
            ['亥', '水', '阳']
        ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("日干", inplace=True)
        # 构造表
        self.table = table

    def __str__(self):
        return self.table.to_string()

    def getResult(self, Str):
        res = self.table.loc[Str]
        print(Str + ": " + res['阴阳'] + res['五行'])
        return res['阴阳'] + res['五行']


if __name__ == '__main__':
    ten_god = TenGodTrunkTable()
    print(ten_god)
    print(ten_god.getResult('甲甲'))

    branch = TenGodBranchTable()
    print(branch)
    print(branch.getResult('甲午'))

    sheepBladeTable = SheepBladeTable()
    print(sheepBladeTable)

    fiveElementTable = FiveElementTable()
    print(fiveElementTable)
    fiveElementTable.getResult('甲')
