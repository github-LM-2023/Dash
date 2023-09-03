import dash
import dash_table
import pandas as pd

# 读取本地Excel文件
df = pd.read_excel("flight.xlsx",index_col=0)

# 创建Dash应用
app = dash.Dash(__name__)

# 设置表格布局
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'name': col, 'id': col} for col in df.columns],
    page_size=10,  # 每页显示10行数据
    style_table={'height': '300px', 'overflowY': 'scroll'},
)

if __name__ == '__main__':
    app.run_server(debug=False)
