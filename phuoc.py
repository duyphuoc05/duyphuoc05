import streamlit as st

# Danh sách tài khoản mẫu
USER_CREDENTIALS = {
    "admin": "admin123",
    "user1": "123456",
    "guest": "guest"
}

def login(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        return True
    return False

def main():
    st.set_page_config(page_title="Login Page", page_icon="🔐")

    st.title("🔐 Login Page")
    st.write("Please enter your credentials:")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.success(f"Welcome, {username}!")
            st.balloons()
            # Hiển thị nội dung chính ở đây
            st.write("✅ You have successfully logged in.")
        else:
            st.error("❌ Invalid username or password.")

if __name__ == "__main__":
    main()
