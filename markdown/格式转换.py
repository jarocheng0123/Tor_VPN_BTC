# markdown 文本格式转换

import re

def convert_code(input_text):
    # 定义正则表达式模式，用于匹配原始代码
    pattern = r'<a href="(.*?)" style="display: inline-block; text-align: center;">\s*<img src="(.*?)" width="80" style="display: block;">\s*<span style="display: block;">(.*?)</span>\s*</a>'
    # 查找所有匹配项
    matches = re.findall(pattern, input_text)
    output = []
    for match in matches:
        href = match[0]
        img_src = match[1]
        text = match[2]
        # 构建转换后的代码
        new_code = f'    <td style="text-align: center;">\n      <a href="{href}">\n        <img src="{img_src}" width="80">\n        <br>\n        <span>{text}</span>\n      </a>\n    </td>'
        output.append(new_code)
    # 用转换后的代码替换原始代码
    result = re.sub(pattern, lambda x: output.pop(0), input_text)
    # 在开头和结尾添加表格标签
    result = '<table>\n  <tr>' + result + '  </tr>\n</table>'
    return result

# 1.0 版本 转 2.0格式

# 示例输入
input_text = '''
<a href="https://www.baidu.com/" style="display: inline-block; text-align: center;">
  <img src="https://raw.githubusercontent.com/jarocheng0123/beginner_guide/refs/heads/main/png/GFW/baidu.png" width="80" style="display: block;">
  <span style="display: block;">百度</span>
</a>
'''

# 调用转换函数
output_text = convert_code(input_text)
print(output_text)
