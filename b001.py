import streamlit as st
import pandas as pd
from pyvis.network import Network
import networkx as nx

# 定义知识三元组
triples = [
    ('车间', '包含', '原材料库'),
    ('原材料库', '位置', '车间西侧'),
    ('原材料库', '功能', '存放原材料'),
    ('原材料库', '配置', '货架'),
    ('原材料库', '配置', '叉车'),
    ('车间', '包含', '加工区'),
    ('加工区', '位置', '车间中部'),
    ('加工区', '功能', '原材料初步加工'),
    ('加工区', '配置', '机床'),
    ('加工区', '配置', '切割机'),
    ('加工区', '配置', '钻孔机'),
    ('车间', '包含', '装配区'),
    ('装配区', '位置', '车间东侧'),
    ('装配区', '功能', '零件组装'),
    ('装配区', '配置', '装配线'),
    ('装配区', '配置', '工具'),
    ('车间', '包含', '检测区'),
    ('检测区', '位置', '加工区与装配区之间'),
    ('检测区', '功能', '质量检测'),
    ('检测区', '配置', '检测仪器'),
    ('检测区', '配置', '测试设备'),
    ('车间', '包含', '成品库'),
    ('成品库', '位置', '车间南侧'),
    ('成品库', '功能', '存放成品'),
    ('成品库', '配置', '货架'),
    ('成品库', '配置', '包装设备'),
    ('车间', '包含', '员工休息区'),
    ('员工休息区', '位置', '车间东北角'),
    ('员工休息区', '功能', '员工休息'),
    ('员工休息区', '配置', '茶水间'),
    ('员工休息区', '配置', '座椅'),
    ('车间', '包含', '办公室'),
    ('办公室', '位置', '车间北侧'),
    ('办公室', '功能', '管理和行政办公'),
    ('办公室', '配置', '办公桌'),
    ('办公室', '配置', '电脑'),
    ('办公室', '配置', '会议室'),
]

st.title("车间布局知识图谱")

# 创建NetworkX图
G = nx.DiGraph()
for h, r, t in triples:
    G.add_edge(h, t, relation=r)

# 使用Pyvis网络图
net = Network(height="750px", width="100%", directed=True)
net.from_nx(G)

# 显示网络图
net.show("knowledge_graph.html")
st.components.v1.html(open("knowledge_graph.html", "r", encoding='utf-8').read(), height=750)
