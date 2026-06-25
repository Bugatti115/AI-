import streamlit as st

st.set_page_config(
    page_title="steramlit入门",
    page_icon="🧊",
    #布局
    layout="wide",
    #侧边栏
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': "https://www.baidu.com",
        'About': "# 加油 高墙!"
    }
)


#标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

st.write("高墙")
st.write("黄山位于中国安徽省南部，具体在黄山市境内。它横跨黄山市的汤口镇、谭家桥镇、焦村镇等地，核心景区距离黄山市区（屯溪）约50-60公里。")

st.image("./AI/b.jpg")
st.audio("AI/animal.ogg")
st.video("AI/apex.mp4")
st.logo("AI/b.jpg")

student_data = {
    "姓名": ["王宏宇","张三","张四","王五"],
    "学号": [446, 421, 433, 365],
    "语文": [99, 98, 91, 99]
}
st.table(student_data)

name = st.text_input("请输入姓名:")
st.write(f"输入的姓名为:{name}")

password = st.text_input("请输入姓密码:", type="password")
st.write(f"输入的密码为:{password}")

gender = st.radio("请选择性别",["man", "woman"], index=1)
st.write(f"您的性别为:{gender}")