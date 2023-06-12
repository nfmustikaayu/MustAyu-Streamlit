import streamlit as st

# Sidebar
selected = st.sidebar.selectbox(
    "hitung luas bangun datar",
    [
        "hitung luas persegi",
        "hitung luas persegi panjang",
        "hitung luas segitiga",
        "hitung luas lingkaran",
        "hitung luas trapesium",
        "hitung luas jajargenjang",
        "hitung luas belah ketupat",
        "hitung luas layang-layang",
    ],
    index=0,
)

# hitung luas persegi
if selected == "hitung luas persegi":
    st.title("hitung luas persegi")

    sisi = st.number_input("masukkan nilai sisi:", 0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = sisi * sisi
        st.write("luas persegi =", luas)
        st.success(f"luas persegi = {luas}")

# hitung luas persegi panjang
elif selected == "hitung luas persegi panjang":
    st.title("hitung luas persegi panjang")

    panjang = st.number_input("masukkan nilai panjang:", 0)
    lebar = st.number_input("masukkan nilai lebar:", 0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = panjang * lebar
        st.write("luas persegi panjang =", luas)
        st.success(f"luas persegi panjang = {luas}")

# hitung luas segitiga
elif selected == "hitung luas segitiga":
    st.title("hitung luas segitiga")

    alas = st.number_input("masukkan nilai alas:", 0)
    tinggi = st.number_input("masukkan nilai tinggi:", 0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = 0.5 * alas * tinggi
        st.write("luas segitiga =", luas)
        st.success(f"luas segitiga = {luas}")

# hitung luas lingkaran
elif selected == "hitung luas lingkaran":
    st.title("hitung luas lingkaran")

    r = st.number_input("masukkan nilai jari-jari:", 0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = 3.14 * r * r
        st.write("luas lingkaran =", luas)
        st.success(f"luas lingkaran = {luas}")

# hitung luas trapesium
elif selected == "hitung luas trapesium":
    st.title("hitung luas trapesium")

    a = st.number_input("masukkan nilai a:", 0)
    b = st.number_input("masukkan nilai b:", 0)
    t = st.number_input("masukkan nilai t:", 0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = 0.5 * (a + b) * t
        st.write("luas trapesium =", luas)
        st.success(f"luas trapesium = {luas}")

# hitung luas jajargenjang
elif selected == "hitung luas jajargenjang":
    st.title("hitung luas jajargenjang")

    alas = st.number_input("masukkan nilai alas:", 0)
    tinggi = st.number_input("masukkan nilai tinggi:", 0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = alas * tinggi
        st.write("luas jajargenjang =", luas)
        st.success(f"luas jajargenjang = {luas}")

# hitung luas belah ketupat
elif selected == "hitung luas belah ketupat":
    st.title("hitung luas belah ketupat")

    d1 = st.number_input("masukkan nilai diagonal 1:", 0)
    d2 = st.number_input("masukkan nilai diagonal 2:", 0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = 0.5 * d1 * d2
        st.write("luas belah ketupat =", luas)
        st.success(f"luas belah ketupat = {luas}")

# hitung luas layang-layang
elif selected == "hitung luas layang-layang":
    st.title("hitung luas layang-layang")

    d1 = st.number_input("masukkan nilai diagonal 1:", 0)
    d2 = st.number_input("masukkan nilai diagonal 2:", 0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = 0.5 * d1 * d2
        st.write("luas layang-layang =", luas)
        st.success(f"luas layang-layang = {luas}")
