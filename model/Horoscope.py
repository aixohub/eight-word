import pandas as pd


class DoublyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class BuildNode:
    def __init__(self, numbers):
        tail_node_l = None
        doubly_linked_list = None
        # Iterate through the list, converting each element into a doubly linked list node and adding it to the list
        for number in numbers:
            # Create a doubly linked list node
            node = DoublyLinkedNode(number)

            # If the list is empty, set the node as the head of the list
            if not doubly_linked_list:
                doubly_linked_list = node

            # Otherwise, add the node to the end of the list
            else:
                # Find the end of the list
                current_node = doubly_linked_list
                while current_node.next:
                    current_node = current_node.next

                # Add the node to the end of the list
                current_node.next = node
                node.prev = current_node
                tail_node_l = current_node.next

        head_node = doubly_linked_list
        tail_node = tail_node_l

        head_node.prev = tail_node
        tail_node.next = head_node
        self.data_node = doubly_linked_list
        self.size = len(numbers)

    def getTrunkNode(self, trunk, num):
        current_node = self.data_node
        while current_node.next:
            data = current_node.__getattribute__('data')
            if data == trunk:
                i = 1
                while current_node.prev:
                    if i == num:
                        return current_node.data
                    else:
                        i = i + 1
                        current_node = current_node.prev

            current_node = current_node.next

    def getBranchNode(self, trunk, num):
        current_node = self.data_node
        while current_node.next:
            data = current_node.__getattribute__('data')
            if data == trunk:
                i = 1
                while current_node.prev:
                    if i == num:
                        return current_node.data
                    else:
                        i = i + 1
                        current_node = current_node.prev
            current_node = current_node.next


class GetYear:
    def __init__(self):
        trunk = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        branch = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        self.trunk = trunk
        self.branch = branch

    def __str__(self):
        return self.__str__()

    def get_year_trunk(self, currentYear, age):
        """
           根据当前年的干支和命主的年龄，推算生年的年干
        """
        trunk = currentYear[0]
        rest_num = age % 10
        if rest_num == 0:
            rest_num = 10
        build_node = BuildNode(self.trunk)
        return build_node.getTrunkNode(trunk, rest_num)

    def get_year_branch(self, currentYear, age):
        """
            根据当前年的干支和命主的年龄，推算生年的年支
        """
        trunk = currentYear[1]
        rest_num = age % 12
        if rest_num == 0:
            rest_num = 12
        build_node = BuildNode(self.branch)
        return build_node.getBranchNode(trunk, rest_num)

    def get_year(self, currentYear, age):
        return self.get_year_trunk(currentYear, age) + self.get_year_branch(currentYear, age)


class GetMonthByYear:
    """
    甲己之丙作首,乙庚之岁戊为头，
    丙辛必定寻康起,丁壬壬位顺行流,
    更有戊癸何方觅,甲寅之上好追求，

    '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥'
    """

    def __init__(self):
        table_header = ['月', '月柱', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']

        # 定义表数据                 '甲',   '乙',   '丙',  '丁',  '戊',  '己',   '庚',   '辛',   '壬',  '癸'
        table_data = [['01', '寅', '丙寅', '戊寅', '庚寅', '壬寅', '甲寅', '丙寅', '戊寅', '庚寅', '壬寅', '甲寅'],
                      ['02', '卯', '丁卯', '己卯', '辛卯', '癸卯', '乙卯', '丁卯', '己卯', '辛卯', '癸卯', '乙卯'],
                      ['03', '辰', '戊辰', '庚辰', '壬辰', '甲辰', '丙辰', '戊辰', '庚辰', '壬辰', '甲辰', '丙辰'],
                      ['04', '巳', '己巳', '辛巳', '癸巳', '乙巳', '丁巳', '己巳', '辛巳', '癸巳', '乙巳', '丁巳'],
                      ['05', '午', '庚午', '壬午', '甲午', '丙午', '戊午', '庚午', '壬午', '甲午', '丙午', '戊午'],
                      ['06', '未', '辛未', '癸未', '乙未', '丁未', '己未', '辛未', '癸未', '乙未', '丁未', '己未'],
                      ['07', '申', '壬申', '甲申', '丙申', '戊申', '庚申', '壬申', '甲申', '丙申', '戊申', '庚申'],
                      ['08', '酉', '癸酉', '乙酉', '丁酉', '已酉', '辛酉', '癸酉', '乙酉', '丁酉', '已酉', '辛酉'],
                      ['09', '戌', '甲戌', '丙戌', '戊戌', '庚戌', '壬戌', '甲戌', '丙戌', '戊戌', '庚戌', '壬戌'],
                      ['10', '亥', '乙亥', '丁亥', '己亥', '辛亥', '癸亥', '乙亥', '丁亥', '己亥', '辛亥', '癸亥'],
                      ['11', '子', '丙子', '戊子', '庚子', '壬子', '甲子', '丙子', '戊子', '庚子', '壬子', '甲子'],
                      ['12', '丑', '丁丑', '已丑', '辛丑', '癸丑', '乙丑', '丁丑', '已丑', '辛丑', '癸丑', '乙丑']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("月", inplace=True)
        # 构造表
        self.table = table


class GetDay:
    """
    乘五除四九加日，
    双月间隔三十天。
    一二自加整少一，
    三五七八十尾前。

    解释如下：

    【年份的后两位乘5+年的后两位除4+9+阳历日子数+单月（为0）双月（30）+每个月的调节数(大月数,三五七八十,无1)】÷60＝取余数个位数为天干，余数除12取余为地支，

    * 2000年后需用100加上后两位数，如2009年就用100+09然后再去计算。
    这里我们计算2018年09月18日的日干支如下:
    ((100+18)*5+(100+18)/4+9+18+4)%60=50 个位0对应癸 50%12=2 对应丑 即癸丑日

    """

    def __init__(self):
        trunk = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        branch = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        self.trunk = trunk
        self.branch = branch


def __str__(self):
    return self.__str__()


def get_day(self, hour, day):
    day = day[0]
    return self.table.loc[hour, day]

class GetHour:
    """
     甲己还加甲，乙庚丙作初，
     丙辛从戊起,丁壬庚子居,
     戊癸何方发,壬子是真途。

    '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥'
    """

    def __init__(self):
        table_header = ['时', '时柱', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']

        # 定义表数据                 '甲',   '乙',   '丙',  '丁',  '戊',  '己',   '庚',   '辛',   '壬',  '癸'
        table_data = [['01', '子', '甲子', '丙子', '庚子', '壬寅', '壬子', '甲子', '丙子', '戊子', '庚子', '壬子'],
                      ['02', '丑', '乙丑', '丁丑', '辛丑', '癸卯', '癸丑', '乙丑', '丁丑', '己丑', '辛丑', '癸丑'],
                      ['03', '寅', '丙寅', '戊寅', '壬寅', '甲辰', '甲寅', '丙寅', '戊寅', '庚寅', '壬寅', '甲寅'],
                      ['04', '卯', '丁卯', '己卯', '癸卯', '乙巳', '乙卯', '丁卯', '己卯', '辛卯', '癸卯', '乙卯'],
                      ['05', '辰', '戊辰', '庚辰', '甲辰', '丙午', '丙辰', '戊辰', '庚辰', '壬辰', '甲辰', '丙辰'],
                      ['06', '已', '己巳', '辛已', '乙巳', '丁未', '丁巳', '己巳', '辛已', '癸巳', '乙巳', '丁巳'],
                      ['07', '午', '庚午', '壬午', '丙午', '戊申', '戌午', '庚午', '壬午', '甲午', '丙午', '戌午'],
                      ['08', '未', '辛未', '癸未', '丁未', '已酉', '己未', '辛未', '癸未', '乙未', '丁未', '己未'],
                      ['09', '申', '壬中', '甲申', '戊申', '庚戌', '庚申', '壬中', '甲申', '丙申', '戊申', '庚申'],
                      ['10', '酉', '癸酉', '乙酉', '己酉', '辛亥', '辛酉', '癸酉', '乙酉', '丁酉', '己酉', '辛酉'],
                      ['11', '戌', '甲戌', '丙戌', '庚戌', '壬子', '壬戌', '甲戌', '丙戌', '戊戌', '庚戌', '壬戌'],
                      ['12', '亥', '乙亥', '丁亥', '辛亥', '癸丑', '癸亥', '乙亥', '丁亥', '己亥', '辛亥', '癸亥']
                      ]
        table = pd.DataFrame(table_data, columns=table_header)
        table.set_index("时", inplace=True)
        # 构造表
        self.table = table


def __str__(self):
    return self.table.to_string()


def get_hour(self, hour, day):
    day = day[0]
    return self.table.loc[hour, day]


def get_year_str(currentYear, age, month):
    get_year = GetYear()
    print("====== 年 =======")
    year_b = get_year.get_year(currentYear, age)
    print(year_b)
    print("====== 月 =======")
    get_month_by_year = GetMonthByYear()
    print(get_month_by_year.get_month(year_b, month))


if __name__ == '__main__':
    get_year_str('壬寅', 32, '02')
