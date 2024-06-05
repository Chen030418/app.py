import streamlit as st
import pandas as pd


st.title("汽车制造车间知识图谱")
data = {
    "实体1": ["原料仓库", "原料仓库", "加工区", "机床", "组装区", "成品仓库"],
    "关系": ["存放", "位于", "包含", "用于", "进行", "存放"],
    "实体2或属性值": ["金属材料", "车间西侧", "机床", "金属零件加工", "汽车组装", "完工汽车"]
}
df = pd.DataFrame(data)
st.dataframe(df)
selected_relation = st.selectbox("选择关系", options=df["关系"].unique())
filtered_data = df[df["关系"] == selected_relation]
st.dataframe(filtered_data)
st.bar_chart(df['关系'].value_counts())
