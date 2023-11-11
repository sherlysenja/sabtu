import streamlit as st

# Ini bagian heading aplikasi streamlit
st.title("Kuliah Praktikum Big Data")
st.write("Sherly Senja")
st.write("# Heading 1")
st.write("## Heading 2")
st.write("### Heading 3")
st.write("#### Heading 4")

# Kinerja unit
st.metric("Kinerja",40, -1)
st.metric("Response Time",30, 20)
st.metric("Saham", 100, 20)

#Pilihan checkbox
pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2)

'''
Ini komentar harusnya
'''
makanan = st.radio('Makanan kesukaan',['Bakso','Mie Ayam','Nasi Goreng','Mie Goreng'])
st.write(makanan)

minuman = st.selectbox('Pilih minuman yang akan dipesan',['es teh','air mineral','kopi','jus'])
st.write(minuman)

bayar = st.multiselect('Bayar pakai:',['Tunai','Ovo','Gopay'])
st.write(bayar)

                