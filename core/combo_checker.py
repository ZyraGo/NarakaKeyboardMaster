import io
import json
import re


# # 定义目标JSON文件路径
# target_json_file = "target.json"
#

# 比较两个JSON数据，忽略 "action" 类型为 "move" 的数据
def compare_json(target_json_file, src_json_file):
    # 加载目标JSON文件
    with open(target_json_file, "r") as target_file, open(src_json_file, "r") as generated_file:
        target_content = target_file.read().strip('"')
        target_content = target_content.replace("'","\"")
        target_content = target_content.replace("\\n","")
        # target_content = re.sub(r'<(.*?)>', r'<"\1">', target_content)
        target_content = re.sub(r'<([^<>]*)>', r'"\1"', target_content)

        # target_content = target_content.replace("<","\"")
        # target_content = target_content.replace(">","\"")
        target_data = json.load(io.StringIO(target_content))

        generated_content = generated_file.read().strip('"')
        generated_content = generated_content.replace("'","\"")
        generated_content = generated_content.replace("\\n","")
        # generated_content = re.sub(r'<(.*?)>', r'<"\1">', generated_content)
        generated_content = re.sub(r'<([^<>]*)>', r'"\1"', generated_content)

        # generated_content = generated_content.replace("<","\"")
        # generated_content = generated_content.replace(">","\"")
        generated_data = json.load(io.StringIO(generated_content))

        # 过滤 "action" 类型为 "move" 的数据
        filtered_data1 = [item for item in target_data if item.get("type") != "mouse" or item.get("action") != "move"]
        filtered_data2 = [item for item in generated_data if item.get("type") != "mouse" or item.get("action") != "move"]
    # 比较过滤后的数据
    return filtered_data1 == filtered_data2
