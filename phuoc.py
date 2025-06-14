import streamlit as st
import pandas as pd
from PIL import Image
import base64
from io import BytesIO

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="Cửa Hàng Vàng Rực Rỡ",
    page_icon="🛒",
    layout="wide"
)

# CSS tùy chỉnh với tông màu vàng
st.markdown("""
<style>
    .main {
        background-color: #FFF8E1;
    }
    .stButton>button {
        background-color: #FFC107;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FFA000;
    }
    h1, h2, h3 {
        color: #FFB300;
        font-family: 'Arial', sans-serif;
    }
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .product-card img {
        max-width: 100%;
        border-radius: 8px;
    }
    .sidebar .sidebar-content {
        background-color: #FFECB3;
    }
    .stTextInput>div>input {
        border: 2px solid #FFC107;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Danh sách sản phẩm mẫu
products = [
    {"id": 1, "name": "Áo Thun Vàng Nắng", "price": 250000, "image": "https://via.placeholder.com/200x200.png?text=Ao+Thun", "description": "Áo thun cotton thoáng mát, màu vàng rực rỡ."},
    {"id": 2, "name": "Quần Jeans Cao Cấp", "price": 450000, "image": "https://via.placeholder.com/200x200.png?text=Quan+Jeans", "description": "Quần jeans phong cách hiện đại."},
    {"id": 3, "name": "Giày Sneaker Vàng", "price": 750000, "image": "https://via.placeholder.com/200x200.png?text=Giay+Sneaker", "description": "Giày sneaker thời thượng, năng động."},
    {"id": 4, "name": "Túi Xách Da", "price": 350000, "image": "https://via.placeholder.com/200x200.png?text=Tui+Xach", "description": "Túi xách da sang trọng, phù hợp mọi dịp."},
]

# Hàm chuyển đổi hình ảnh thành base64 để hiển thị
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

# Hàm thêm sản phẩm vào giỏ hàng
def add_to_cart(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        st.session_state.cart.append(product)
        st.success(f"Đã thêm {product['name']} vào giỏ hàng!")

# Hàm xóa sản phẩm khỏi giỏ hàng
def remove_from_cart(index):
    st.session_state.cart.pop(index)
    st.success
