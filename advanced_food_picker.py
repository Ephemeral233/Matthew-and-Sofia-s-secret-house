import streamlit as st
import random
import pandas as pd
import time
import os
from datetime import datetime

st.set_page_config(
    page_title="今天吃什么Pro",
    page_icon="🍜",
    layout="wide"
)

# ======================
# 数据文件
# ======================

DATA_FILE = "food_history.csv"

if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["时间", "分类", "美食"]).to_csv(
        DATA_FILE,
        index=False,
        encoding="utf-8-sig"
    )

# ======================
# 菜单库
# ======================

foods = {
    "早餐": [
        "豆浆油条","煎饼果子","小笼包",
        "三明治","牛奶麦片","皮蛋瘦肉粥",
        "馄饨","鸡蛋灌饼"
    ],
    "午餐": [
        "黄焖鸡米饭","麻辣香锅","牛肉面",
        "寿司","盖浇饭","宫保鸡丁",
        "咖喱饭","水饺"
    ],
    "晚餐": [
        "火锅","烤鱼","烧烤",
        "牛排","意大利面",
        "披萨","韩式拌饭"
    ],
    "夜宵": [
        "泡面","小龙虾",
        "炸鸡","关东煮",
        "炒粉","煎饺"
    ],
    "下午茶": [
        "奶茶","咖啡",
        "提拉米苏","泡芙",
        "蛋糕","冰淇淋"
    ]
}

# ======================
# 标题
# ======================

st.title("🍽️ 今天吃什么 Pro Max")

st.markdown("""
### 不知道吃什么？
点击下面按钮，让系统帮你决定！
""")

# ======================
# 分类选择
# ======================

category = st.selectbox(
    "选择时段",
    list(foods.keys())
)

# ======================
# 转盘效果
# ======================

if st.button("🎰 开始抽奖"):

    placeholder = st.empty()

    for i in range(30):

        rolling = random.choice(
            foods[category]
        )

        placeholder.markdown(
            f"# 🎲 {rolling}"
        )

        time.sleep(0.05)

    result = random.choice(
        foods[category]
    )

    placeholder.success(
        f"🎉 推荐你吃：{result}"
    )

    history = pd.read_csv(DATA_FILE)

    history.loc[len(history)] = [
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        category,
        result
    ]

    history.to_csv(
        DATA_FILE,
        index=False,
        encoding="utf-8-sig"
    )

# ======================
# 图片展示
# ======================

st.divider()

st.subheader("🍕 美食图片")

image_dict = {
    "早餐":"https://images.unsplash.com/photo-1533089860892-a7c6f0a88666",
    "午餐":"https://images.unsplash.com/photo-1546069901-ba9599a7e63c",
    "晚餐":"https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
    "夜宵":"https://images.unsplash.com/photo-1565299624946-b28f40a0ae38",
    "下午茶":"https://images.unsplash.com/photo-1511920170033-f8396924c348"
}

st.image(
    image_dict[category],
    use_container_width=True
)

# ======================
# 添加菜品
# ======================

st.divider()

st.subheader("➕ 添加菜品")

col1,col2 = st.columns(2)

with col1:

    add_category = st.selectbox(
        "分类",
        list(foods.keys()),
        key="add"
    )

with col2:

    new_food = st.text_input(
        "菜品名称"
    )

if st.button("添加"):

    if new_food:

        foods[add_category].append(
            new_food
        )

        st.success(
            f"已添加 {new_food}"
        )

# ======================
# 当前菜单
# ======================

st.divider()

st.subheader("📋 当前菜单")

for k,v in foods.items():

    with st.expander(k):

        st.write("、".join(v))

# ======================
# 历史记录
# ======================

st.divider()

st.subheader("📜 历史记录")

history = pd.read_csv(DATA_FILE)

st.dataframe(
    history,
    use_container_width=True
)

# ======================
# 统计
# ======================

if len(history) > 0:

    st.divider()

    st.subheader("📊 抽奖统计")

    stat = history["美食"].value_counts()

    st.bar_chart(stat)

# ======================
# 一键随机
# ======================

st.divider()

if st.button("🔥 今天别纠结了"):

    c = random.choice(
        list(foods.keys())
    )

    food = random.choice(
        foods[c]
    )

    st.balloons()

    st.success(
        f"今天直接吃【{food}】"
    )

# ======================
# 页脚
# ======================

st.divider()

st.caption(
    "今天吃什么 Pro Max v2.0"
)