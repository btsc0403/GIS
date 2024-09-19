import os
import csv
import json

def csv_a2_to_json(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            csv_path = os.path.join(folder_path, filename)
            
            # 打开CSV文件并读取A2格的内容
            with open(csv_path, mode='r', encoding='utf-8') as csvfile:
                csvreader = csv.reader(csvfile)
                # 跳过第一行，读取第二行
                next(csvreader)
                a2_content = next(csvreader)[0]  # 假设A2对应的是第二行的第一列
                
                # 准备JSON数据
                json_data = {"A2_content": a2_content}
                
                # 保存为JSON文件
                json_filename = os.path.splitext(filename)[0] + '.json'
                json_path = os.path.join(folder_path, json_filename)
                
                with open(json_path, mode='w', encoding='utf-8') as jsonfile:
                    json.dump(json_data, jsonfile, ensure_ascii=False, indent=4)
                
                print(f"{filename} 的A2内容已转换并保存为 {json_filename}")

# 调用函数，将“your_folder_path”替换为你的文件夹路径
csv_a2_to_json(r'E:\项目\GIS\mars2d-vue-template-master\mars2d-vue3-vite\public\buildingDescriptions')
