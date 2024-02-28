import io
import json
import re


# # 定义目标JSON文件路径
# target_json_file = "target.json"
#

import json
import io

import json
import io

def compare_json(target_json_file, src_json_file):
    # 加载目标JSON文件
    with open(target_json_file, "r") as target_file, open(src_json_file, "r") as generated_file:
        target_content = target_file.read().strip('"').replace("'", "\"").replace("\\n", "")
        target_data = json.load(io.StringIO(target_content))

        generated_content = generated_file.read().strip('"').replace("'", "\"").replace("\\n", "")
        generated_data = json.load(io.StringIO(generated_content))

        # 过滤 "action" 类型为 "move" 的数据并忽略 "time", "x", "y" 属性
        filtered_data1 = [{k: v for k, v in item.items() if k not in ('time', 'x', 'y')} for item in target_data if
                          item.get("type") != "mouse" or item.get("action") != "move"]
        filtered_data2 = [{k: v for k, v in item.items() if k not in ('time', 'x', 'y')} for item in generated_data if
                          item.get("type") != "mouse" or item.get("action") != "move"]

    # 比较过滤后的数据
    return filtered_data1 == filtered_data2
