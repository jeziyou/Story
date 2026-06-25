import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="儿童故事集 | Children's Story Collection",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded"
)

IMAGE_DIR = "images"

stories = [
    {
        "id": "little_star",
        "title_cn": "小星星找朋友",
        "title_en": "The Little Star Who Found Friends",
        "reading_time_cn": "约7分钟",
        "reading_time_en": "About 7 minutes",
        "cover_image": "little_star_cover.png",
        "pages": [
            {
                "text_cn": """在很远很远的天上，住着一颗小小的星星，名字叫闪闪。

闪闪是夜空中最小的一颗星星。每天晚上，当太阳公公回家睡觉后，闪闪就和其他星星一起出来，把夜空点亮。

可是，闪闪有一点不开心。因为她太小了，其他星星都比她亮、比她大，她觉得没有人注意到她。

"要是我能有朋友就好了。"闪闪叹了口气说。""",
                "text_en": """Far, far up in the sky, there lived a tiny little star named Twinkle.

Twinkle was the smallest star in the night sky. Every evening, when Mr. Sun went home to sleep, Twinkle would come out with the other stars to light up the night.

But Twinkle was a little sad. Because she was so small, all the other stars were brighter and bigger than her, and she felt like nobody noticed her.

"If only I could have a friend," Twinkle said with a sigh.""",
                "image": "little_star_page1.png"
            },
            {
                "text_cn": """这天晚上，闪闪决定要去找朋友。她先去找月亮阿姨。

"月亮阿姨，月亮阿姨！我能和你做朋友吗？"闪闪小声地问。

月亮阿姨温柔地笑了："小闪闪，我当然愿意做你的朋友呀！不过我每天晚上都要照亮整个世界，可能没办法一直陪你玩。你为什么不往下看看呢？大地上有很多可爱的小朋友呢！"

闪闪听了，眼睛一亮。她从来没有仔细看过下面的大地呢！""",
                "text_en": """That night, Twinkle decided to go find a friend. First, she went to see Aunt Moon.

"Aunt Moon, Aunt Moon! Can I be your friend?" Twinkle asked softly.

Aunt Moon smiled gently, "Little Twinkle, of course I'll be your friend! But I have to light up the whole world every night, so I might not be able to play with you all the time. Why don't you look down below? There are many lovely little friends on the earth!"

Twinkle's eyes lit up when she heard this. She had never looked closely at the earth below before!""",
                "image": "little_star_page2.png"
            },
            {
                "text_cn": """闪闪低下头，往大地上看去。

哇！大地上好美啊！她看到了闪烁着灯光的城市，看到了静静流淌的小河，还看到了连绵起伏的大山。

闪闪找呀找，找呀找，忽然看到一片黑黑的森林。在森林深处，有一只小小的萤火虫正在哭泣。

"你怎么啦？"闪闪关心地问。

萤火虫抬起头，眼泪汪汪地说："我...我的光太弱了，找不到回家的路了..."

闪闪想了想，说："别害怕，我来帮你！"虽然闪闪很小，但她努力地发出最亮的光芒，给萤火虫照亮了前方的路。""",
                "text_en": """Twinkle looked down towards the earth.

Wow! The earth was so beautiful! She saw cities twinkling with lights, a quietly flowing river, and rolling mountains that stretched far away.

Twinkle looked and looked, when suddenly she saw a dark forest. Deep in the forest, a little firefly was crying.

"What's wrong?" Twinkle asked with concern.

The firefly looked up, teary-eyed, and said, "I... my light is too weak, I can't find my way home..."

Twinkle thought for a moment and said, "Don't be afraid, I'll help you!" Even though Twinkle was small, she tried her best to shine her brightest light, lighting the path ahead for the firefly.""",
                "image": "little_star_page3.png"
            },
            {
                "text_cn": """萤火虫顺着闪闪的光，终于找到了家！萤火虫的爸爸妈妈正在门口焦急地等着呢。

"谢谢你，小星星！"萤火虫开心地说，"你愿意做我的朋友吗？以后每天晚上你在天上发光，我就在地上发光，我们一起照亮夜晚好不好？"

"好呀！好呀！"闪闪高兴得直眨眼睛。

闪闪又继续往前飞。她飞到了一个小院子上空，看到一个小女孩正坐在窗边，手里拿着画笔。

小女孩抬起头，看到了闪闪，惊喜地说："哇，好可爱的小星星！你是在对我眨眼睛吗？"

闪闪赶紧眨了眨眼睛，发出温柔的光芒。""",
                "text_en": """Following Twinkle's light, the firefly finally found home! The firefly's mom and dad were waiting anxiously at the door.

"Thank you, little star!" the firefly said happily. "Will you be my friend? Every night from now on, you shine in the sky and I'll shine on the ground, and we can light up the night together, okay?"

"Yes! Yes!" Twinkle blinked happily with excitement.

Twinkle continued flying forward. She flew over a small yard and saw a little girl sitting by the window, holding a paintbrush.

The little girl looked up, saw Twinkle, and said in surprise, "Wow, what a cute little star! Are you blinking at me?"

Twinkle quickly blinked her eyes, casting a gentle glow.""",
                "image": "little_star_page4.png"
            },
            {
                "text_cn": """小女孩拿出画纸，开始画天上的星星。她画了好多好多星星，其中有一颗最小的星星，画得最亮、最可爱。

"这就是你！"小女孩对闪闪说，"你是我见过的最特别的小星星。每天晚上我都要和你说晚安！"

闪闪心里暖暖的。她从来没有这么开心过！

就在这时，远处传来了呜呜的哭声。原来是一只迷路的小鸟，在树枝上瑟瑟发抖。

"别怕，小鸟！"闪闪说，"我来给你照亮，你往有光的方向飞，就能找到你的鸟妈妈啦！"

闪闪发出温柔的光，小鸟顺着光，终于找到了在窝里焦急等待的鸟妈妈。""",
                "text_en": """The little girl took out drawing paper and started painting the stars in the sky. She painted many, many stars, and among them was the smallest star—the brightest and cutest one of all.

"This is you!" the little girl said to Twinkle. "You're the most special little star I've ever seen. Every night I'll say goodnight to you!"

Twinkle felt warm inside. She had never been so happy!

Just then, the sound of whimpering came from afar. It was a lost little bird, trembling on a tree branch.

"Don't be afraid, little bird!" Twinkle said. "I'll light the way for you—fly towards the light, and you'll find your mommy bird!"

Twinkle cast a gentle light, and following the light, the little bird finally found its mother bird waiting anxiously in the nest.""",
                "image": "little_star_page5.png"
            },
            {
                "text_cn": """这时候，其他星星们也注意到了闪闪。

"看呀，"一颗大星星说，"虽然闪闪很小，但是她发出的光帮了好多小动物呢！"

"是呀，是呀！"另一颗星星说，"她的光虽然小，但是却很温暖！"

月亮阿姨也笑着说："每颗星星都有自己的光芒，不管是大是小，都能照亮别人呢。"

闪闪听了，不好意思地笑了。她低头看去：萤火虫在森林里闪着光，小女孩的窗边还亮着灯，小鸟在窝里甜甜地睡着。

""",
                "text_en": """By this time, the other stars had also noticed Twinkle.

"Look," said a big star, "even though Twinkle is small, her light has helped so many little animals!"

"Yes, yes!" said another star. "Her light may be small, but it's so warm!"

Aunt Moon also smiled and said, "Every star has its own light—whether big or small, everyone can brighten someone else's way."

Twinkle smiled shyly when she heard this. She looked down below: the firefly was glowing in the forest, the little girl's window still had a warm light on, and the little bird was sleeping sweetly in its nest.""",
                "image": "little_star_page6.png"
            },
            {
                "text_cn": """从那以后，闪闪每天晚上都开心地挂在天上。

她不再觉得自己小就没有用了。因为她知道，萤火虫在等着她的光，小女孩在等着和她说晚安，还有很多很多需要光明的小家伙们，都在仰望着她呢。

而且，闪闪还发现了一个秘密：当你帮助别人的时候，你自己也会变得更加明亮！

现在的闪闪，虽然还是天空中最小的那颗星星，但是你知道吗？她的笑容，是整个夜空中最美、最温暖的光芒。

晚安，小星星。晚安，小朋友。愿你也能像闪闪一样，用自己的方式，发出温暖的光。

✨ 故事结束 ✨""",
                "text_en": """From then on, Twinkle hung happily in the sky every night.

She no longer felt that being small made her useless. Because she knew—the firefly was waiting for her light, the little girl was waiting to say goodnight to her, and many, many other little ones who needed light were looking up at her.

And Twinkle discovered a secret: when you help others, you become brighter yourself!

Twinkle is still the smallest star in the sky, but you know what? Her smile is the most beautiful, warmest glow in the entire night sky.

Goodnight, little star. Goodnight, little friend. May you too, like Twinkle, shine your warm light in your own special way.

✨ The End ✨""",
                "image": "little_star_page7.png"
            }
        ]
    }
]

@st.cache_data(show_spinner=False)
def load_local_image(image_filename):
    image_path = os.path.join(IMAGE_DIR, image_filename)
    if os.path.exists(image_path):
        return Image.open(image_path)
    return None

def main():
    if 'language' not in st.session_state:
        st.session_state.language = 'cn'
    if 'current_page' not in st.session_state:
        st.session_state.current_page = -1
    if 'current_story' not in st.session_state:
        st.session_state.current_story = 0
    if 'font_size' not in st.session_state:
        st.session_state.font_size = 18

    lang = st.session_state.language

    with st.sidebar:
        st.markdown("### 🌐 语言 / Language" if lang == 'cn' else "### 🌐 Language / 语言")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("中文", use_container_width=True, type="primary" if lang == 'cn' else "secondary"):
                st.session_state.language = 'cn'
                st.rerun()
        with col2:
            if st.button("English", use_container_width=True, type="primary" if lang == 'en' else "secondary"):
                st.session_state.language = 'en'
                st.rerun()

        st.divider()

        st.markdown("### 📚 " + ("故事目录" if lang == 'cn' else "Story Library"))
        story_options = [s["title_cn"] if lang == 'cn' else s["title_en"] for s in stories]
        selected_story = st.selectbox(
            "选择故事" if lang == 'cn' else "Select a story",
            range(len(stories)),
            format_func=lambda i: story_options[i],
            index=st.session_state.current_story
        )
        if selected_story != st.session_state.current_story:
            st.session_state.current_story = selected_story
            st.session_state.current_page = -1
            st.rerun()

        st.divider()

        st.markdown("### 🔤 " + ("字体大小" if lang == 'cn' else "Font Size"))
        st.session_state.font_size = st.slider(
            "Aa", 14, 28, st.session_state.font_size,
            label_visibility="collapsed"
        )

    story = stories[st.session_state.current_story]
    title = story["title_cn"] if lang == 'cn' else story["title_en"]
    reading_time = story["reading_time_cn"] if lang == 'cn' else story["reading_time_en"]
    total_pages = len(story["pages"])

    is_cover = st.session_state.current_page == -1

    st.markdown(
        f"""
        <h1 style='text-align: center; color: #FFD700; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);'>
            📖 {title}
        </h1>
        <p style='text-align: center; color: #888; font-size: 14px;'>
            ⏱️ {reading_time}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    if is_cover:
        progress_value = 0.0
        page_display = "封面" if lang == 'cn' else "Cover"
    else:
        progress_value = (st.session_state.current_page + 1) / total_pages
        page_display = f"{'第' if lang == 'cn' else 'Page'} {st.session_state.current_page + 1} / {total_pages}"

    progress = st.progress(progress_value)
    page_col1, page_col2, page_col3 = st.columns([1, 3, 1])
    with page_col2:
        st.markdown(
            f"<p style='text-align: center; color: #666;'>{page_display}</p>",
            unsafe_allow_html=True
        )

    if is_cover:
        cover_image = load_local_image(story["cover_image"])
        if cover_image:
            st.image(cover_image, use_container_width=True)
        
        st.markdown(
            f"""
            <div style='
                background: linear-gradient(135deg, #FFF8E7 0%, #FFE4B5 100%);
                padding: 40px;
                border-radius: 20px;
                margin: 20px 0;
                text-align: center;
                color: #4A4A4A;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                border: 2px solid #FFD700;
            '>
                <h2 style='color: #FFD700; margin-bottom: 20px;'>{'✨ 欢迎来到故事世界 ✨' if lang == 'cn' else '✨ Welcome to Storyland ✨'}</h2>
                <p style='font-size: {st.session_state.font_size}px; line-height: 2;'>
                    {'点击下方的「开始阅读」按钮，开启一段奇妙的冒险旅程吧！' if lang == 'cn' else 'Click the "Start Reading" button below to begin a wonderful adventure!'}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        current_page_data = story["pages"][st.session_state.current_page]
        text = current_page_data["text_cn"] if lang == 'cn' else current_page_data["text_en"]
        image = load_local_image(current_page_data["image"])

        if image:
            st.image(image, use_container_width=True)

        st.markdown(
            f"""
            <div style='
                background: linear-gradient(135deg, #FFF8E7 0%, #FFE4B5 100%);
                padding: 30px;
                border-radius: 20px;
                margin: 20px 0;
                font-size: {st.session_state.font_size}px;
                line-height: 2;
                color: #4A4A4A;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                border: 2px solid #FFD700;
            '>
                {text.replace(chr(10), '<br><br>')}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])

    with nav_col1:
        if not is_cover and st.session_state.current_page > 0:
            if st.button("⬅️ " + ("上一页" if lang == 'cn' else "Previous"), use_container_width=True):
                st.session_state.current_page -= 1
                st.rerun()
        elif not is_cover and st.session_state.current_page == 0:
            if st.button("🏠 " + ("返回封面" if lang == 'cn' else "Back to Cover"), use_container_width=True):
                st.session_state.current_page = -1
                st.rerun()

    with nav_col3:
        if is_cover:
            if st.button("🚀 " + ("开始阅读" if lang == 'cn' else "Start Reading"), use_container_width=True, type="primary"):
                st.session_state.current_page = 0
                st.rerun()
        elif st.session_state.current_page < total_pages - 1:
            if st.button("➡️ " + ("下一页" if lang == 'cn' else "Next"), use_container_width=True, type="primary"):
                st.session_state.current_page += 1
                st.rerun()
        else:
            if st.button("🔄 " + ("重新开始" if lang == 'cn' else "Read Again"), use_container_width=True, type="primary"):
                st.session_state.current_page = -1
                st.rerun()

    with nav_col2:
        if not is_cover:
            if st.button("📖 " + ("返回封面" if lang == 'cn' else "Cover Page"), use_container_width=True):
                st.session_state.current_page = -1
                st.rerun()

    st.markdown(
        "<p style='text-align: center; color: #aaa; font-size: 12px; margin-top: 40px;'>"
        "✨ Children's Story Collection ✨<br>"
        "Made with ❤️ for all the little dreamers"
        "</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
