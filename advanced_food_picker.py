import streamlit as st
import random
import pandas as pd
import time
import os
from datetime import datetime, date

# ======================
# 页面配置
# ======================

st.set_page_config(
    page_title="🐛 小虫虫秘密基地",
    page_icon="❤️",
    layout="wide"
)

# ======================
# 温馨主题
# ======================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
    180deg,
    #fff7fb 0%,
    #fff0f5 100%);
}

h1,h2,h3{
    color:#ff4f8b !important;
}

.stButton>button{
    background:#ffb6c1;
    color:white;
    border-radius:15px;
    border:none;
    font-weight:bold;
}

.stButton>button:hover{
    background:#ff85a2;
}

[data-testid="stMetricValue"]{
    color:#ff4f8b;
}

</style>
""", unsafe_allow_html=True)

# ======================
# 数据文件
# ======================

DATA_FILE = "food_history.csv"

if not os.path.exists(DATA_FILE):

    pd.DataFrame(
        columns=["时间","分类","美食"]
    ).to_csv(
        DATA_FILE,
        index=False,
        encoding="utf-8-sig"
    )

# ======================
# 菜谱库
# ======================

foods = {

    "早餐":[
        "豆浆油条",
        "煎饼果子",
        "小笼包",
        "三明治",
        "牛奶麦片",
        "皮蛋瘦肉粥",
        "馄饨",
        "鸡蛋灌饼",
        "草莓三明治",
        "热牛奶"
    ],

    "午餐":[
        "黄焖鸡米饭",
        "麻辣香锅",
        "牛肉面",
        "寿司",
        "盖浇饭",
        "宫保鸡丁",
        "咖喱饭",
        "水饺",
        "三文鱼饭",
        "炙烧三文鱼",
        "韩国烤肉"
    ],

    "晚餐":[
        "火锅",
        "烤鱼",
        "烧烤",
        "牛排",
        "意大利面",
        "披萨",
        "韩式拌饭",
        "涮肉火锅",
        "韩国烤肉",
        "三文鱼刺身",
        "韩式部队锅"
    ],

    "夜宵":[
        "泡面",
        "小龙虾",
        "炸鸡",
        "关东煮",
        "炒粉",
        "煎饺"
    ],

    "下午茶":[
        "奶茶",
        "咖啡",
        "提拉米苏",
        "泡芙",
        "蛋糕",
        "冰淇淋",
        "冰糕",
        "草莓冰糕",
        "巧克力冰糕"
    ]
}

# ======================
# 甜蜜语录
# ======================

sweet_words = {

    "早餐":[
        "🌞 小虫虫记得认真吃早餐哦～",
        "🥛 今天也要元气满满呀～",
        "🍞 不许空腹出门，我会心疼的～"
    ],

    "午餐":[
        "🍱 小虫虫午饭时间到啦～",
        "💖 再忙也要好好吃饭哦～",
        "🌷 今天也要照顾好自己呀～"
    ],

    "晚餐":[
        "🌙 小虫虫晚饭一定不能省～",
        "🍲 吃饱饱才有好心情～",
        "💕 希望你每顿饭都吃得开心～"
    ],

    "夜宵":[
        "🌟 小虫虫饿了吗～",
        "🍜 夜宵快乐但不要太晚哦～"
    ],

    "下午茶":[
        "☕ 给努力的小虫虫一点奖励～",
        "🍰 甜甜的下午茶配甜甜的小虫虫～"
    ]
}

# ======================
# 标题
# ======================

st.title("🐛 小虫虫秘密基地")

st.markdown(
"""
### Matthew & Sofia's Secret House ❤️
"""
)

# ======================
# 恋爱天数
# ======================

start_date = date(2026,3,21)

days = (date.today() - start_date).days

st.success(
    f"💕 小虫虫已经陪伴你 {days} 天啦"
)

# ======================
# 今日留言
# ======================

daily_messages = [

    "💌 小虫虫今天也要记得好好吃饭呀～",
    "💌 不许饿肚子哦，我会心疼的～",
    "💌 希望今天也能开开心心～",
    "💌 再忙也别忘记吃饭和休息～",
    "💌 你负责快乐，我负责提醒你吃饭～"
]

st.info(
    random.choice(daily_messages)
)

# ======================
# 小虫虫最爱
# ======================

st.subheader("❤️ 小虫虫最爱")

col1,col2,col3,col4 = st.columns(4)

col1.metric("🍲","涮肉火锅")
col2.metric("🐟","三文鱼")
col3.metric("🥩","韩国烤肉")
col4.metric("🍨","冰糕")

st.divider()

# ======================
# 分类选择
# ======================

category = st.selectbox(
    "🍽️ 选择时段",
    list(foods.keys())
)

# ======================
# 抽奖
# ======================

if st.button("🎰 开始抽奖"):

    placeholder = st.empty()

    for _ in range(30):

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

    luck = random.randint(80,100)

    placeholder.success(
        f"""
🎉 推荐你吃：{result}

💖 今日幸福指数：{luck}%

{random.choice(sweet_words[category])}
"""
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

st.subheader("🍕 今日美食灵感")

image_dict = {

    "早餐":
    "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666",

    "午餐":
    "https://images.unsplash.com/photo-1546069901-ba9599a7e63c",

    "晚餐":
    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",

    "夜宵":
    "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38",

    "下午茶":
    "https://images.unsplash.com/photo-1511920170033-f8396924c348"
}

st.image(
    image_dict[category],
    use_container_width=True
)

# ======================
# 添加菜品
# ======================

st.divider()

st.subheader("➕ 添加新菜品")

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
            f"❤️ 已添加 {new_food}"
        )

# ======================
# 当前菜单
# ======================

st.divider()

st.subheader("📋 小虫虫菜单")

for k,v in foods.items():

    with st.expander(k):

        st.write(
            "、".join(v)
        )

# ======================
# 历史记录
# ======================

st.divider()

st.subheader("📜 我们吃过什么")

history = pd.read_csv(
    DATA_FILE
)

st.dataframe(
    history,
    use_container_width=True
)

# ======================
# 统计
# ======================

if len(history) > 0:

    st.divider()

    st.subheader(
        "📊 美食排行榜"
    )

    stat = history["美食"].value_counts()

    st.bar_chart(stat)

# ======================
# 一键随机
# ======================

st.divider()

if st.button(
    "🔥 今天别纠结了"
):

    c = random.choice(
        list(foods.keys())
    )

    food = random.choice(
        foods[c]
    )

    st.balloons()

    st.success(
        f"""
🔥 今天直接吃【{food}】

💖 今日幸福指数：
{random.randint(80,100)}%

🐛 小虫虫今天也要记得好好吃饭～
"""
    )

# ======================
# 页脚
# ======================

st.divider()

st.caption(
"""
🐛 小虫虫秘密基地

Matthew & Sofia's Secret House ❤️
"""
)