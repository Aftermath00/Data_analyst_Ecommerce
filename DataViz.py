import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

st.title('Belajar Analisis Data')

st.subheader('Ini tabel')
st.write(pd.DataFrame({
    'c1': [1,2,3,4],
    'c2': [10, 20, 30, 40]
})
)

st.subheader('Kalo ini kode python')
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.subheader('Yang ini latex')
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

st.subheader("Ini dataframe")
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.dataframe(data=df, width=500, height=150)
 
st.subheader("Ini tabel")
st.table(data=df)

st.subheader("Yang ini metric")
st.metric(label="Batam Temperature", value="30 °C", delta="1.2 °C")

st.subheader("Yang ini JSON")
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.subheader("Yang ini chart")
x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

st.subheader("Ini input")
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama saya adalah', name)

st.subheader("Text area")
text = st.text_area('Feedback')
st.write('Feedback: ', text)

st.subheader("Number input")
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

st.subheader("Date input")
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

st.subheader("File uploader")
uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.subheader("Camera input")
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)

st.subheader("Button")
if st.button('Say hello'):
    st.write('Hello there')

st.subheader("Checkbox")
agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')

st.subheader("Radio button")
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

st.caption('Copyright (c) 2024')