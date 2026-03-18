# 示例功能：将输入文本转为大写
def your_core_function(input_text):
    if not input_text:
        raise ValueError("输入内容不能为空！")
    return f"处理结果：{input_text.upper()}"
