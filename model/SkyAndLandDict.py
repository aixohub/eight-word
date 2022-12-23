import json


class SkyAndLandDict:
    def __init__(self):
        self.trunk_dict = {}
        self.branch_dict = {}
        with open('../data/sky.json') as json_file:
            self.sky = json.load(json_file)
        for sky_item in self.sky:
            self.trunk_dict.setdefault(sky_item['code'], sky_item)

        with open('../data/land.json') as json_file:
            self.land = json.load(json_file)
        for land_item in self.land:
            self.branch_dict.setdefault(land_item['code'], land_item)

    def get_hidde_trunk(self, code):
        brunch = self.branch_dict.get(code)
        return brunch['藏干']


if __name__ == '__main__':
    # 读取 JSON 文件
    dict = SkyAndLandDict()
    s = dict.get_hidde_trunk('子')
    print(s)
