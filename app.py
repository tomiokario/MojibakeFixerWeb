import streamlit as st
import ftfy

st.title("文字化け修正ツール")
st.write("txtファイルをアップロードして、文字化けを修正します。")

uploaded_file = st.file_uploader("txtファイルを選択", type=["txt"])
if uploaded_file is not None:
    # アップロードされたファイルはバイナリデータなので、UTF-8としてデコード
    original_text = uploaded_file.read().decode('utf-8', errors='replace')
    
    # ftfyを使って文字化け修正
    fixed_text = ftfy.fix_text(original_text)
    
    st.subheader("修正後のテキスト")
    st.text_area("結果", fixed_text, height=300)
    
    # 修正後のテキストをダウンロードできるボタンを用意
    st.download_button(
        label="修正後のテキストをダウンロード",
        data=fixed_text,
        file_name="fixed_output.txt",
        mime="text/plain"
    )

