import streamlit as st
import pandas as pd


st.title("汽车制造车间知识图谱")
data = {
    "实体1": ["接收区", "加工区", "组装区", "检验区", "包装区", "接收区"],
    "关系": ["邻接", "输出到", "邻接", "输出到", "邻接", "面积"],
    "实体2或属性值": ["加工区", "组装区", "检验区", "包装区", "仓储区", "100平"]
}
df = pd.DataFrame(data)
st.dataframe(df)
selected_relation = st.selectbox("选择关系", options=df["关系"].unique())
filtered_data = df[df["关系"] == selected_relation]
st.dataframe(filtered_data)
st.bar_chart(df['关系'].value_counts())
