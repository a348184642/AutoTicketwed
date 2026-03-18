from flask import Flask, render_template, request, jsonify
# 导入你的Python仓库核心功能
from your_repo.core_functions import your_core_function

app = Flask(__name__)

# 首页路由：返回前端页面
@app.route('/')
def index():
    return render_template('index.html')

# 功能接口：接收前端参数，调用仓库函数，返回结果
@app.route('/run_function', methods=['POST'])
def run_function():
    try:
        # 获取前端传入的参数（示例：获取用户输入的文本）
        input_data = request.form.get('input_text')
        # 调用你的Python仓库核心函数
        result = your_core_function(input_data)
        # 返回JSON结果给前端
        return jsonify({'status': 'success', 'result': result})
    except Exception as e:
        return jsonify({'status': 'error', 'msg': str(e)})

if __name__ == '__main__':
    # 本地运行：debug=True开发模式，端口5000
    app.run(debug=True, host='0.0.0.0', port=5000)
