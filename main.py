import streamlit as st

st.title("مرحبا مراجعنا العزيز")
st.write("يمكنك معرفة رقم عيادتك باختيارك لاسم الطبيب من القائمة المنسدلة أدناه")

with st.form("form1", clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("ادخل الاسم الأول")
    l_name= col2.text_input("ادخل الاسم الثاني")
    s_button= st.form_submit_button("ابحث")
    if s_button:
        if f_name == "" or l_name == "":
            st.warning("يجب ادخال قيمة في خانات الأسماء كما ورد في الرسالة النصية او موقع صحتي")
        elif f_name == "عبدالرحمن" and l_name == "الشهري":
            st.warning("فضلا توجه للعيادة رقم 18")
        elif f_name == "عبدالكريم" and l_name == "الشهري":
            st.warning("فضلا توجه للعيادة رقم 17")
        else:
            st.warning("يرجى إعادة المحاولة")

