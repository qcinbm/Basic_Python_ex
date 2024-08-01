import streamlit as st
from textblob import TextBlob

st.title("Word Correction Application")

st.write("Nhập vào văn bản có thể chứa lỗi chính tả, ứng dụng sẽ tự động sửa lỗi cho bạn.")

# Nhập văn bản
user_input = st.text_area("Văn bản đầu vào:", "Ví dụ: This is a smple text with speling erors.")

# Nếu văn bản không rỗng
if user_input:
    # Tạo đối tượng TextBlob
    blob = TextBlob(user_input)
    
    # Sửa lỗi chính tả
    corrected_text = blob.correct()

    # Hiển thị kết quả
    st.subheader("Văn bản đã được sửa:")
    st.write(corrected_text)