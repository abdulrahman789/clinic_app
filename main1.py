import streamlit as st
from PIL import Image

image = Image.open('logo.png')
st.image(image)

st.markdown("<h1 style='text-align: center;'>مرحبا بك مراجعنا العزيز</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>يمكنك معرفة رقم عيادتك باختيارك لاسم الطبيب من القائمة المنسدلة أدناه</h3>", unsafe_allow_html=True)

DoctorName = st.selectbox(
    ' ',
    ('الرجاء الاختيار','عبدالرحمن الشهري', 'عبدالكريم الشهري', 'موسى العسيري','شريفة عبدالوهاب',
     ' ',' ',' ',' ',
     ' ',' ',' ',' ',' '))

ClinicNum = ""


if DoctorName == "عبدالرحمن الشهري":
    ClinicNum = "18"
elif DoctorName == "عبدالكريم الشهري":
    ClinicNum = "17"
elif DoctorName == "موسى العسيري":
    ClinicNum = "18"
elif DoctorName == "شريفة عبدالوهاب":
    ClinicNum = "17"

elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
elif DoctorName == " ":
    ClinicNum = " "
else:
    st.warning("الرجاء التحقق من اختيارك")
    DoctorName = "تحقق من اختيارك"
    ClinicNum = "تحقق من اختيارك"

ddd = st.markdown("<h5 style='text-align: right;'>  طبيبك هو  </h5>", unsafe_allow_html=True)
st.write(DoctorName)
st.markdown("<h5 style='text-align: right;'> رقم عيادتك هو</h5>", unsafe_allow_html=True)
st.write(ClinicNum)


