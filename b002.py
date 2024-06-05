import streamlit as st
#====================================================================================
# Radio菜单控制模式: “webapp简介”
#---------------------------------------------------------------
def Introduction_to_a_Webapp():
  # 编程模板简介
  st.link_button('访问streamlit主页', 'https://streamlit.io') 
  st.write('💯' + ':orange[MES技术课程编程作业可用的Streamlit-webapp模板简介:]')
  my_code = 
  st.code(my_code) # , line_numbers=True)  # 显示内容
  # 编程学习资源
  st.write('🗝️' + ':orange[Python编程学习资源:]')
  st.page_link('https://www.python.org/', label='(1) Python下载 ... ', icon='🕹️')
  st.page_link('https://code.visualstudio.com/', label='(2) 编辑器VSC下载 ... ', icon='🎙️')
  st.page_link('https://streamlit.io/', label='(3) Streamlit库主页 ... ', icon='📻')
  st.page_link('https://numpy.org/', label='(4) numpy库主页 ... ', icon='🎹')
  st.page_link('https://pandas.pydata.org/', label='(5) pandas库主页 ... ', icon='🎺')
  st.page_link('https://matplotlib.org/', label='(6) matplotlib库主页 ... ', icon='🪇')      
  st.page_link('https://plotly.com/python/', label='(7) plotly库主页 ... ', icon='🎸')
  st.page_link('https://scikit-learn.org/stable/index.html', label='(8) sklearn库主页 ... ', icon='🎧')
  st.page_link('https://pytorch.org/', label='(9) pytorch库主页 ... ', icon='🥁')
  st.page_link('https://www.sqlite.org/index.html', label='(10) SQLite库主页 ... ', icon='🎼') 
  st.page_link('https://tinydb.readthedocs.io/en/latest/index.html', label='(11) TinyDB库主页 ... ', icon='🎷') 
  return
#====================================================================================
# 处理Radio菜单项1：
#------------------------------------------------------------------------------------
def Handling_RadioMenu1():
  tab1, tab2, tab3 = st.tabs(['1️⃣ Tab区域1名称', '2️⃣ Tab区域2名称', '3️⃣ Tab区域3名称'])  # 设置webapp的若干个tab区域
  with tab1:  # 处理第一个tab1区域：采用tree控件作为左侧栏的主菜单的控制实现
    Handling_RadioMenu1_in_Tab1_Area()
  with tab2:  # 处理第二个tab2区域：采用radio按钮作为左侧栏的主菜单的控制实现
    Handling_RadioMenu1_in_Tab2_Area()
  with tab3:  # 处理第三个tab3区域: 调用mito表格处理工具进行如同excel的表格数据处理
    Handling_RadioMenu1_in_Tab3_Area()
  return
#---------------------------------------------------------------
def Handling_RadioMenu1_in_Tab1_Area():
  pass
#---------------------------------------------------------------
def Handling_RadioMenu1_in_Tab2_Area():
  pass
#---------------------------------------------------------------
def Handling_RadioMenu1_in_Tab3_Area():
  pass
#====================================================================================
# 处理Radio菜单项2：
#------------------------------------------------------------------------------------
def Handling_RadioMenu2():# Radio菜单控制模式：函数2
  return
#====================================================================================
# 处理Radio菜单项3：
#------------------------------------------------------------------------------------
def Handling_RadioMenu3():
  col1, col2 = st.columns([0.25, 0.75])  # 设置第一个菜单区为左侧树状菜单栏、右侧菜单项的流程与计算栏
  with col1:  # 设置左侧树装菜单 
    with st.container(border=True, height=650):    
      st.write('🤖' + ':blue[ 集成式设置:]') 
      Configuring_for_a_Function()
  with col2:  # 设置左侧树装菜单 
    with st.container(border=True, height=650):   
      st.write('💫' + ':blue[ 运行ing ... :]')      
      Running_for_a_Function()   
  return
#----------------------------------------------------------------
def Configuring_for_a_Function():
  pass
#----------------------------------------------------------------
def Running_for_a_Function():
  pass
#====================================================================================
def Showing_Source_Codes():
  st.write('🧾' + ':blue[ Streamlit-webapp的python源代码:]') 
  with st.container(border=True):
    st.write('显示源代码：')
    mycode = 
    st.code(mycode, language='python', line_numbers=True)
  return
#====================================================================================
# 虚拟主函数main():
#====================================================================================
def main(): 
  st.set_page_config(layout='wide')  # 设置UI界面适配web浏览器的宽度
  st.image('temp_title.jpg')  # 设置webapp标题
  col1, col2 = st.columns([0.2, 0.8])  # 设置第一个菜单区为左侧树状菜单栏、右侧菜单项的流程与计算栏
  with col1:  # 设置左侧树装菜单 
    with st.container(border=True, height=750):    
      # st.empty()
      st.write('🏠' + ':rainbow[ Radio按钮菜单:]') 
      # 定义radio按钮菜单并选择一个菜单项   
      # st.write('按钮菜单控制区域: ')
      myradio = str()
      myradio = st.radio('选择一个Radio按钮菜单项: ', ['webapp简介', 'Radio菜单项1', 'Radio菜单项2', 'Radio菜单项3', '源代码', '退出'])
      st.divider()
      mynote = 
      st.code(mynote)
  with col2:  # 设置左侧树装菜单 
    with st.container(border=True, height=750): 
      # st.empty()
      st.write('🤹‍♂️' + f':rainbow[ > 处理Radio菜单项: {myradio}]')
      if myradio == 'webapp简介':
        Introduction_to_a_Webapp()
      if myradio == 'Radio菜单项1':
        Handling_RadioMenu1()
      if myradio == 'Radio菜单项2':
        Handling_RadioMenu2()
      if myradio == 'Radio菜单项3':
        Handling_RadioMenu3()
      if myradio == '源代码':
        Showing_Source_Codes()
      if myradio == '退出':
        st.write('提示：暂停系统的运行，但不退出浏览器！如希望完全退出系统，请点击关闭浏览器的图标')
        st.stop()
  return
#***********************************************************************************************************
if __name__ == '__main__':
  main()
