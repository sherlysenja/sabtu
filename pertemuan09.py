import streamlit as st

st.title("Kuliah Praktikum Big Data")
st.write("Sherly Senja")
st.write("# Heading 1")
st.write("## Heading 2")
st.write("### Heading 3")

pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2)

makanan = st.radio('Makanan kesukaan',['Bakso','Mie Ayam','Nasi Goreng','Mie Goreng'])
st.write(makanan)

minuman = st.selectbox('Pilih minuman yang akan dipesan',['es teh','air mineral','kopi','jus'])
st.write(minuman)

bayar = st.multiselect('Bayar pakai:',['Tunai','Ovo','Gopay'])
st.write(bayar)

                