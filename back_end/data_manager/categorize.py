import json

def parse_taxonomy(file_path, output_path):
    """解析路径文件并生成JSON"""
    root = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去掉两端的空白字符
            path = line.strip()
            if not path:
                continue

            # 将路径分割
            nodes = path.split(' > ')

            # 构建嵌套字典
            current_level = root
            for node in nodes:
                if node not in current_level:
                    current_level[node] = {}
                current_level = current_level[node]

    # 保存为JSON
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(root, json_file, indent=4, ensure_ascii=False)
    print(f"JSON saved to {output_path}")

def count_leaf_nodes(node):
    """递归计算JSON中所有末端节点的数量"""
    if not isinstance(node, dict) or not node:  # 如果不是字典或字典为空，说明是末端节点
        return 1
    return sum(count_leaf_nodes(child) for child in node.values())

def get_num_ends(json_file):
      # 加载JSON为字典
    return count_leaf_nodes(data)


def get_leaf_nodes(node):
    if not isinstance(node, dict) or not node:  # 如果不是字典或字典为空，说明是末端节点
        return [node] if node else []  # 返回节点名称
    leaf_nodes = []
    for key, child in node.items():
        # 递归调用
        leaf_nodes.extend(get_leaf_nodes(child))
    return leaf_nodes

# 使用示例
file_path = "taxonomy.en-US"  # 替换为实际文件路径
output_path = "taxonomy.json"  # 输出的JSON文件路径


if __name__== "__main__":
    #parse_taxonomy(file_path, output_path)
    #keys=get_first_level_keys("taxonomy.json")
    with open(output_path,'r', encoding='utf-8') as file:
        data = json.load(file)
    for key in list(data.keys()):
        print(key+":",count_leaf_nodes(data[key]))
    for key in list(data["Office Supplies"].keys()):
        print(key+":",get_leaf_nodes(data["Office Supplies"][key]))