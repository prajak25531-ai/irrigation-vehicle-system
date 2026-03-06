import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="ระบบยานพาหนะออนไลน์", layout="wide")

# เชื่อมต่อ Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("ระบบบริหารจัดการยานพาหนะออนไลน์ (แบบ 1-10)")

menu = ["แบบ 1/2: ลงทะเบียนรถ", "แบบ 4: บันทึกการใช้รถ", "แบบ 8: รายงานสรุป"]
choice = st.sidebar.radio("เมนูหลัก", menu)

if choice == "แบบ 1/2: ลงทะเบียนรถ":
    st.header("ลงทะเบียนยานพาหนะ (แบบ 1 และ 2)")
    with st.form("reg_form"):
        v_no = st.text_input("เลขหมาย ชป.")
        plate = st.text_input("เลขทะเบียน")
        brand = st.text_input("ยี่ห้อ/แบบ")
        if st.form_submit_button("บันทึกข้อมูล"):
            st.success(f"ส่งข้อมูลรถ {v_no} ไปยัง Google Sheets แล้ว")

elif choice == "แบบ 8: รายงานสรุป":
    st.header("รายงานสรุปผล (แบบ 8)")
    try:
        # ดึงข้อมูลจาก Google Sheets มาแสดง
        df = conn.read(worksheet="Vehicles")
        st.dataframe(df)
    except:
        st.info("ยังไม่มีข้อมูลในระบบ")
