import streamlit as st
import pandas as pd

# 创建三元组数据
data = {
    "实体1": ["接收区", "加工区", "组装区", "检验区", "包装区", "接收区"],
    "关系": ["邻接", "输出到", "邻接", "输出到", "邻接", "面积"],
    "实体2或属性值": ["加工区", "组装区", "检验区", "包装区", "仓储区", "100平米"]
}

df = pd.DataFrame(data)

# 应用标题
st.title("车间布局知识图谱")

# 显示数据框
st.dataframe(df)

# 允许用户查询特定关系或实体
query = st.text_input("查询关系或实体:", "邻接")
filtered_data = df[df.apply(lambda row: row.str.contains(query).any(), axis=1)]
st.write("查询结果:")
st.dataframe(filtered_data)
