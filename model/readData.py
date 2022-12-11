import json

if __name__ == '__main__':
    # 读取 JSON 文件
    with open('../data/sky.json') as json_file:
        sky = json.load(json_file)

    # 输出解析后的数据
    print(sky)

    with open('../data/land.json') as json_file:
        land = json.load(json_file)

        # 输出解析后的数据
    print(land)
