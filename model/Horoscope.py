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

    def __str__(self):
        return self.table.to_string()

    def get_month(self, year, month):
        year = year[0]
        return self.table.loc[month, year]


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
