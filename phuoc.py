import streamlit as st
import pandas as pd
from PIL import Image
import base64
from io import BytesIO

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="Game Store Nebula",
    page_icon="🎮",
    layout="wide"
)

# CSS tùy chỉnh với tông màu xanh đen
st.markdown("""
<style>
    .main {
        background-color: #0A1A2F;
        color: #E6F0FA;
        font-family: 'Verdana', sans-serif;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 12px 24px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #104E8B;
    }
    h1, h2, h3 {
        color: #1E90FF;
        font-family: 'Verdana', sans-serif;
    }
    .game-card {
        background-color: #1C2A44;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        text-align: center;
        margin-bottom: 20px;
        transition: transform 0.3s;
    }
    .game-card:hover {
        transform: translateY(-5px);
    }
    .game-card img {
        max-width: 100%;
        border-radius: 8px;
        border: 2px solid #1E90FF;
    }
    .sidebar .sidebar-content {
        background-color: #1C2A44;
        color: #E6F0FA;
    }
    .stTextInput>div>input, .stTextArea>div>textarea {
        border: 2px solid #1E90FF;
        border-radius: 5px;
        padding: 8px;
        background-color: #2F4F7F;
        color: #E6F0FA;
    }
    .stForm {
        background-color: #1C2A44;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .stTextInput>label, .stTextArea>label {
        color: #1E90FF;
    }
</style>
""", unsafe_allow_html=True)

# Danh sách game mẫu
games = [
    {"id": 1, "name": "Cyber Odyssey", "price": 599000, "genre": "Action RPG", "image": "z6617045808026_9bb4fbfd86d1a1474c7bdd6094cf16d2.jpg", "description": "Game nhập vai hành động với đồ họa đỉnh cao."},
    {"id": 2, "name": "Starlight Tactics", "price": 499000, "genre": "Strategy", "image": "https://via.placeholder.com/200x200.png?text=Starlight+Tactics", "description": "Chiến thuật thời gian thực trong không gian vũ trụ."},
    {"id": 3, "name": "Neon Racer", "price": 299000, "genre": "Racing", "image": "https://via.placeholder.com/200x200.png?text=Neon+Racer", "description": "Đua xe tốc độ cao với hiệu ứng neon rực rỡ."},
    {"id": 4, "name": "Shadow Legends", "price": 799000, "genre": "MMORPG", "image": "https://via.placeholder.com/200x200.png?text=Shadow+Legends", "description": "Thế giới mở rộng lớn với hàng ngàn người chơi."},
]

# Hàm chuyển đổi hình ảnh thành base64
def get_image_base64(image_url):
    try:
        from urllib.request import urlopen
        with urlopen(image_url) as response:
            img = Image.open(response)
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode()
    except:
        return None

# Khởi tạo giỏ hàng trong session state
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Hàm thêm game vào giỏ hàng
def add_to_cart(game_id):
    game = next((g for g in games if g["id"] == game_id), None)
    if game:
        st.session_state.cart.append(game)
        st.success(f"Đã thêm {game['name']} vào giỏ hàng!")

# Hàm xóa game khỏi giỏ hàng
def remove_from_cart(index):
    st.session_state.cart.pop(index)
    st.success("Đã xóa game khỏi giỏ hàng!")

# Tiêu đề chính
st.title("🎮 Game Store Nebula")
st.markdown("Khám phá kho tàng game đỉnh cao với trải nghiệm chơi game không giới hạn!")

# Thanh tìm kiếm
search_query = st.text_input("Tìm kiếm game...", "")
filtered_games = [g for g in games if search_query.lower() in g["name"].lower() or search_query.lower() in g["description"].lower()]

# Hiển thị danh sách game
st.header("Kho Game Nổi Bật")
cols = st.columns(4)
for idx, game in enumerate(filtered_games):
    with cols[idx % 4]:
        st.markdown(f"""
        <div class="game-card">
            <img src="{game['image']}" alt="{game['name']}">
            <h3>{game['name']}</h3>
            <p>{game['description']}</p>
            <p><b>Thể loại: {game['genre']}</b></p>
            <p><b>Giá: {game['price']:,} VND</b></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Thêm vào giỏ", key=f"add_{game['id']}"):
            add_to_cart(game["id"])

# Sidebar hiển thị giỏ hàng và form đặt hàng
with st.sidebar:
    st.header("Giỏ Hàng")
    if st.session_state.cart:
        for idx, item in enumerate(st.session_state.cart):
            st.write(f"{item['name']} - {item['price']:,} VND ({item['genre']})")
            if st.button("Xóa", key=f"remove_{idx}"):
                remove_from_cart(idx)
        total = sum(item['price'] for item in st.session_state.cart)
        st.markdown(f"**Tổng cộng: {total:,} VND**")
    else:
        st.write("Giỏ hàng trống")

    # Form đặt hàng
    st.header("Đặt Hàng")
    with st.form("order_form"):
        name = st.text_input("Họ và Tên")
        email = st.text_input("Email")
        payment_method = st.selectbox("Phương thức thanh toán", ["Thanh toán khi nhận hàng", "Chuyển khoản ngân hàng", "Ví điện tử"])
        note = st.text_area("Ghi chú (nếu có)")
        submit = st.form_submit_button("Đặt Hàng")
        if submit and name and email and st.session_state.cart:
            st.success(f"Cảm ơn {name}! Đơn hàng của bạn đã được ghi nhận. Chúng tôi sẽ gửi mã kích hoạt game qua email.")
            st.session_state.cart = []  # Xóa giỏ hàng sau khi đặt
        else:
            if submit:
                st.error("Vui lòng điền đầy đủ thông tin và thêm game vào giỏ hàng!")

# Footer
st.markdown("""
<div style='text-align: center; padding: 20px; background-color: #1E90FF; color: white;'>
    <p>© 2025 Game Store Nebula. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
