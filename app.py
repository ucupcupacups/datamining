import streamlit as st
import pandas as pd

# ==========================
# STATE UNTUK NEXT BUTTON
# ==========================
menu_list = [
    "Topik Skripsi",
    "Penelitian Terkait",
    "Metode Penelitian",
    "Dataset BMKG",
    "Distribusi Variabel",
    "Implementasi Model",
    "Evaluasi Model",
    "Kesimpulan",
]

if "menu_index" not in st.session_state:
    st.session_state.menu_index = 0

# ===== HEADER TOPI SKRIPSI =====
# CSS untuk header fix di pojok kiri atas
st.markdown("""
<style>

.header-container {
    position: fixed;
    top: 100px;
    left: 15px;
    display: flex;
    align-items: center;
    gap: 14px;
    z-index: 999;
}

.header-text {
    font-size: 18px;
    font-weight: bold;
    line-height: 1.4;
}

.stApp {
    background: linear-gradient(120deg, #e0eafc, #cfdef3);
}

</style>

<div class="header-container">
    <div class="header-text">
        PROGRAM STUDI TEKNIK INFORMATIKA<br>
        FAKULTAS ILMU KOMPUTER<br>
        UNIVERSITAS PAMULANG
    </div>
</div>
""", unsafe_allow_html=True)

# Garis pemisah
st.markdown("""
<hr style="border: 2px solid #000; margin-top: 20px;">
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(120deg, #e0eafc, #cfdef3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ======================
# SIDEBAR MENU
# ======================
st.sidebar.image("assets/logo.png", width=100)
st.sidebar.title("Analisis Perbandingan Teknik Data Mining")
st.sidebar.subheader("Prediksi Curah Hujan di Kota Tangerang Selatan")

# Radio menu dikontrol dari session_state
menu = st.sidebar.radio(
    "Pilih Menu:",
    menu_list,
    index=st.session_state.menu_index
)

# Update session_state saat user klik manual
if menu_list.index(menu) != st.session_state.menu_index:
    st.session_state.menu_index = menu_list.index(menu)

# Spacer dan Footer
st.sidebar.markdown("", unsafe_allow_html=True)
st.sidebar.markdown("""
---
Teknik Informatika<br>
Fakultas Ilmu Komputer <br>
Universitas Pamulang 
<br> 2025
""", unsafe_allow_html=True)


# ======================
# CONTROLLER (Routing)
# ======================

if menu == "Topik Skripsi":
    # ============================
    # TOPIK SKRIPSI / INTRO SECTION
    # ============================

    # Styling global (biar font paragraf ga kecil)
    st.markdown("""
        <style>
            .divider {
                border-top: 2px solid #888;
                margin: 25px 0px;
            }
            .subjudul {
                font-size: 24px;
                font-weight: bold;
                margin-top: 20px;
            }
            .paragraf {
                font-size: 18px;
                text-align: justify;
            }
        </style>
    """, unsafe_allow_html=True)
    st.title("Analisis Perbandingan Teknik Data Mining K-Nearest Neighbor dan Decission Tree untuk Prediksi Curah Hujan di Kota Tangerang Selatan")
    st.subheader("Nama: Rizky Agung Setiawan - 211011400559")
    st.write("Dosem Pembimbing: Ir. Bodi Santoso, S.Kom., M.T. - 0401066805")
   
   # Divider garis pembatas
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ====== Latar Belakang (disingkat & dibuat poin) ======
    st.markdown("### 🌦️ Latar Belakang")
    st.markdown("""
    - **Fenomena:** Curah hujan di Kota Tangerang Selatan sangat variatif dan sering menimbulkan hujan ekstrem berdurasi singkat.  
    - **Masalah:** Ketidakpastian pola hujan harian menyulitkan mitigasi banjir dan perencanaan tata wilayah.  
    - **Solusi:** Diperlukan pendekatan berbasis data historis melalui teknik data mining untuk mengenali pola cuaca secara akurat.  
    """)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ====== Identifikasi Masalah ======
    st.markdown("### ⚠️ Identifikasi Masalah")
    st.markdown("""
    1. Tingginya variabilitas curah hujan menyulitkan klasifikasi cuaca.  
    2. Masih terbatasnya penelitian komparatif yang membandingkan kinerja dua algoritma (KNN dan Decision Tree C4.5).  
    """)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ====== Rumusan Masalah ======
    st.markdown("### ❓ Rumusan Masalah")
    st.markdown("""
    1. Bagaimana perbandingan kinerja metode K-Nearest Neighbor dan Decision Tree C4.5 dalam melakukan klasifikasi kategori cuaca berdasarkan data curah hujan di Kota Tangerang Selatan yang memiliki variabilitas tinggi?.  
    2. Metode klasifikasi manakah antara K-Nearest Neighbor dan Decision Tree C4.5 yang menghasilkan tingkat performa dan akurasi tertinggi dalam mengenali pola curah hujan harian di wilayah Kota Tangerang Selatan?. 
    """)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ====== Tujuan Penelitian ======
    st.markdown("### 🎯 Tujuan Penelitian")
    st.markdown("""
    1. Menganalisis dan membandingkan kinerja metode K-Nearest Neighbor dan Decision Tree C4.5 dalam dalam klasifikasi kategori cuaca berdasarkan data historis curah hujan harian di Kota Tangerang Selatan.  
    2. Menentukan metode klasifikasi yang memiliki tingkat performa dan akurasi tertinggi antara K-Nearest Neighbor dan Decision Tree C4.5 dalam mengenali pola curah hujan harian di wilayah Kota Tangerang Selatan.  
    """)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ====== Batasan Masalah ======
    st.markdown("### 🚧 Batasan Masalah")
    st.markdown("""
    - Data bersumber dari BMKG Online periode 2022–2024.  
    - Tidak membahas integrasi sistem kedalam bentuk website atau aplikasi, melainkan hanya hasil analisis dan perbandingan kinerja metode.
    - Tidak memprediksi curah hujan numerik secara langsung, melainkan menggunakan klasifikasi kategori cuaca sebagai representasi intensitas curah hujan.  
    - Terbatas pada evaluasi kemampuan algoritma terhadap akurasi klasifikasi dalam mengenali pola curah hujan tanpa sistem prediksi curah hujan realtime. 
    """)

#==================================================================================================
elif menu == "Penelitian Terkait":
    st.title("📄 Penelitian Terkait")
    st.write("Berikut adalah penelitian terdahulu yang terkait topik skripsi ini")
    # Template tabel penelitian terkait (BARIS = penelitian, KOLOM = item)
    data = {
        "Judul": ["Implementasi Teknik Data Mining terhadap Klasifikasi Data Prediksi Curah Hujan BMKG di Sulawesi Selatan", "Perbandingan Metode Data Mining Untuk Prediksi Curah Hujan dengan Algoritma C4.5, Naïve Bayes, dan KNN"],
        "Penulis": ["Andi Sandri Agung,dkk. (2023)", "Al Arif, A., Firdaus, M., dkk (2022)"],
        "Metode": ["K-Nearest Neighbor (K=3 & K=5)", "Decision Tree C4.5, K-Nearest Neighbor,Naive Bayes"],
        "Hasil": ["Akurasi dengan K=3 adalah 82,21% Dengan K=5 pelatihan 84,54% & pengujian 79,31%","C4.5 dengan akurasi 88,03%. KNN dengan akurasi 85,61%. Naive Bayes 81,15%"]
    }

    df = pd.DataFrame(data, index=["1.", "2."])

    st.data_editor(df)  # editable table
#==================================================================================================
elif menu == "Metode Penelitian":
    st.title("⚙️ Metode Penelitian")

    st.markdown("""
    <style>
        .paragraf {font-size: 18px; text-align: justify;}
        .divider {border-top: 2px solid #999; margin: 25px 0;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='paragraf'>
    Penelitian ini dilakukan melalui beberapa tahapan utama yang saling berurutan, 
    dimulai dari <b>preprocessing data</b>, <b>penerapan algoritma (modeling)</b>, 
    <b>evaluasi performa model</b>, hingga <b>pengujian cross validation</b>. 
    Setiap tahap dilakukan secara sistematis untuk memastikan hasil analisis 
    dapat menggambarkan kinerja algoritma dengan akurat dan konsisten.
    </div>
    """, unsafe_allow_html=True)

    # ================== Diagram Alur Penelitian ==================
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("📈 Alur Penelitian")
    st.image("assets/metode.png", caption="Alur Penelitian Prediksi Curah Hujan", use_container_width=True)
    st.caption("Alur penelitian ini diimplementasikan menggunakan RapidMiner dan divisualisasikan melalui streamling  untun memaparkan hasil penelitian guna memperjelas setiap tahapan proses penelitian.")

    # ================== Tahapan Penelitian ==================
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("🧩 Tahapan Penelitian")
    st.markdown("""
    <div class='paragraf'>
    Proses penelitian dibagi menjadi empat tahap utama, yaitu:
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **1️⃣ Preprocessing Data**  
    - Menggabungkan data cuaca dari BMKG (periode 2022–2024).  
    - Menangani missing values menggunakan interpolasi dan median imputasi.  
    - Melakukan normalisasi dan pembersihan data untuk memastikan kualitas dataset siap digunakan pada tahap modeling.  
    - Melakukan Pemberian Label Target pada Kolom baru Cuaca dengan ketentuan BMKG
    """)

    st.markdown("""
    **2️⃣ Penerapan Algoritma Klasifikasi**  
    - Menggunakan dua metode: K-Nearest Neighbor dan Decision Tree C4.5.  
    - Parameter KNN: nilai K=3.  
    - Parameter Decision Tree C4.5: **gain ratio** sebagai pemilihan atribut dan **confidence factor=0.25**.  
    - Melakukan Split Data dengan **80% Data Training dan 20% Data Testing**
    - Tujuan tahap ini adalah mengklasifikasikan kategori cuaca (cerah, ringan, sedang, lebat) berdasarkan data historis curah hujan.
    """)

    st.markdown("""
    **3️⃣ Evaluasi Model**  
    - Model diuji menggunakan metrik: Akurasi, Precision, Recall, F1-score, dan Kappa.  
    - Evaluasi dilakukan untuk mengukur tingkat keandalan algoritma dalam mengenali pola data.
    """)

    st.markdown("""
    **4️⃣ Cross Validation**  
    - Pengujian dilakukan dengan skenario **5-Fold dan 10-Fold Cross Validation**.  
    - Tujuannya untuk menilai stabilitas performa algoritma dan menghindari overfitting.
    """)

    # ================== Input & Output Tiap Tahap ==================
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("🔄 Hubungan Input & Output Setiap Tahap")
    st.markdown("""
    | Tahapan | Input | Output |
    |----------|--------|---------|
    | Preprocessing | Data mentah BMKG | Dataset bersih dan terstruktur |
    | Modeling | Dataset bersih | Model KNN & Decision Tree C4.5 |
    | Evaluasi | Model hasil pelatihan | Nilai metrik performa (Accuracy, Precision, Recall, Kappa) |
    | Cross Validation | Model terlatih | Nilai rata-rata performa antar fold |
    """)
    
    # ================== Catatan Penjelasan ==================
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.info("""
    Urutan tahapan di atas mengikuti prinsip metodologi data mining, 
    di mana preprocessing harus dilakukan sebelum modeling agar model 
    dapat belajar dari data yang bersih dan terstandar. 
    Evaluasi dan cross-validation digunakan untuk memastikan bahwa hasil prediksi 
    tidak hanya akurat, tetapi juga konsisten stabil pada data yang berbeda.
    """)

#==================================================================================================
elif menu == "Dataset BMKG":
    import plotly.express as px
    st.title("📄 Dataset Curah Hujan - BMKG")
    st.markdown("""
    <style>
        .paragraf {font-size: 18px; text-align: justify;}
        .divider {border-top: 2px solid #999; margin: 25px 0;}
    </style>
    """, unsafe_allow_html=True)

    # ===================== Paragraf pembuka =====================
    st.markdown("""
    <div class='paragraf'>
    Dataset final merupakan hasil dari tahap preprocessing yang mencakup 
    penggabungan data BMKG periode 2022–2024, penanganan missing value 
    menggunakan interpolasi linear dan median imputasi, serta normalisasi data. 
    Dataset inilah yang digunakan pada proses pemodelan KNN dan Decision Tree C4.5.
    </div>
    """, unsafe_allow_html=True)

     # ===================== Screenshot Data Mentah BMKG =====================
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("🌐 Dataset Mentah dari Web BMKG Online")

    try:
        st.image("assets/datamentah.png", caption="Data Mentah dari Website Resmi BMKG", use_container_width=True)
    except:
        st.warning("⚠️ Gambar 'datamentah.png' tidak ditemukan. Pastikan file berada di folder assets.")
    
    # ===================== Hyperlink Sumber =====================
    st.markdown("""
    <div style='font-size:16px; margin-top: -10px;'>
    Sumber data asli diambil dari:  
    <a href='https://dataonline.bmkg.go.id/dataonline-home ' target='_blank'>
    🌐 Website Resmi BMKG – Prakiraan Cuaca Harian
    </a>
    </div>
    """, unsafe_allow_html=True)

    # ===================== Narasi Keterangan Data Mentah =====================
    st.markdown("""
    <div style='font-size:16px; margin-top:15px; text-align:justify;'>

    <strong>Keterangan Kolom Data Mentah BMKG:</strong><br>

    • <strong>8888</strong>: Data tidak terukur (alat cuaca tidak membaca nilai)<br>
    • <strong>9999</strong>: Tidak ada data (tidak dilakukan pengukuran pada hari tersebut)<br>
    • <strong>Tavg</strong>: Temperatur rata-rata (°C) yang diukur harian<br>
    • <strong>RH_avg</strong>: Kelembapan rata-rata (%)<br>
    • <strong>RR</strong>: Curah hujan (mm) berdasarkan intensitas hujan harian<br>
    • <strong>ss</strong>: Durasi penyinaran matahari (jam)<br>
    • <strong>ff_avg</strong>: Kecepatan angin rata-rata (m/s)
    </div>
    """, unsafe_allow_html=True)

    # ===================== Load Dataset =====================
    df = pd.read_csv("datasetbmkg_clean_final.csv")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("📌 Tabel Dataset Final")
    st.write("Berikut adalah dataset final yang sudah melalui tahap Preprocessing")
    st.dataframe(df, use_container_width=True)
    # ===================== Statistik =====================
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("📊 Statistik Dataset")

    col1, col2, col3 = st.columns(3)
    col1.metric("Jumlah Baris", df.shape[0])
    col2.metric("Jumlah Kolom", df.shape[1])
    col3.metric("Jumlah Kategori Cuaca", df["cuaca"].nunique())

    st.write("Distribusi kategori cuaca:")
    st.write(df["cuaca"].value_counts())

    # ===================== Diagram Distribusi Cuaca =====================
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("🌦️ Distribusi Kategori Cuaca")

    cuaca_count = df["cuaca"].value_counts()
    cuaca_percent = (cuaca_count / cuaca_count.sum()) * 100

    cuaca_df = pd.DataFrame({
        "Kategori Cuaca": cuaca_count.index,
        "Jumlah": cuaca_count.values,
        "Persentase (%)": cuaca_percent.round(2)
    })

    fig = px.bar(
        cuaca_df,
        x="Kategori Cuaca",
        y="Persentase (%)",
        text="Persentase (%)",
        title="Persentase Data Berdasarkan Kategori Cuaca",
    )
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

    # ===================== Kategori Cuaca Berdasarkan BMKG =====================
    st.markdown("""
    <div style='font-size:18px; font-weight:bold; margin-top:25px;'>
    Kategori Cuaca Berdasarkan Intensitas Curah Hujan (Standar BMKG)
    </div>
    """, unsafe_allow_html=True)

    data_bmkg = {
        "Kategori Cuaca": ["Cerah", "Hujan Ringan", "Hujan Sedang", "Hujan Lebat"],
        "Rentang Curah Hujan (mm)": ["0 mm", "0.1 – 20 mm", "20 – 50 mm","50 mm++"]
    }

    df_bmkg = pd.DataFrame(data_bmkg)
    st.table(df_bmkg)

    st.markdown("""
    <div style='font-size:15px; text-align:justify; margin-top:10px;'>
    Kategori cuaca di atas digunakan sebagai dasar pelabelan pada dataset penelitian ini.
    Rentang intensitas curah hujan mengacu pada standar resmi Badan Meteorologi, Klimatologi,
    dan Geofisika (BMKG). Proses pelabelan ini penting untuk memastikan bahwa hasil klasifikasi
    mengikuti definisi yang valid secara meteorologis.
    </div>
    """, unsafe_allow_html=True)
    # ===================== Penjelasan =====================
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.info("""
    Distribusi kategori cuaca ini menunjukkan komposisi data pada setiap kelas. 
    Informasi ini penting untuk mengetahui apakah dataset seimbang atau tidak, 
    karena ketidakseimbangan data dapat mempengaruhi performa algoritma, terutama KNN.
    """)

#==================================================================================================
elif menu == "Distribusi Variabel":
    import seaborn as sns
    import matplotlib.pyplot as plt

    st.title("📊 Distribusi & Analisis Variabel")

    df = pd.read_csv("datasetbmkg_clean_final.csv")

    st.write("Silakan pilih jenis visualisasi yang ingin ditampilkan:")

    option = st.selectbox(
        "Pilih Visualisasi:",
        [
            "Histogram",
            "Boxplot",
            "Pairplot",
            "Heatmap Korelasi"
        ]
    )

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    # =========================
    # 1. HISTOGRAM
    # =========================
    if option == "Histogram":
        variabel = st.selectbox("Pilih variabel:", numeric_cols)

        st.write(f"Histogram variabel **{variabel}**")
        st.bar_chart(df[variabel])


    # =========================
    # 2. BOXPLOT
    # =========================
    elif option == "Boxplot":
        variabel = st.selectbox("Pilih variabel:", numeric_cols)

        st.write(f"Boxplot variabel **{variabel}**")
        fig, ax = plt.subplots()
        sns.boxplot(x=df[variabel], ax=ax)
        st.pyplot(fig)


    # =========================
    # 3. PAIRPLOT
    # =========================
    elif option == "Pairplot":
        st.write("Pairplot untuk melihat hubungan antar variabel numerik.")

        # batasi 5 variabel biar tidak berat
        selected = st.multiselect(
            "Pilih maksimal 5 variabel untuk pairplot:",
            numeric_cols,
            default=numeric_cols[:4]
        )

        if len(selected) > 0:
            fig = sns.pairplot(df[selected])
            st.pyplot(fig)
        else:
            st.warning("Pilih minimal 1 variabel.")


    # =========================
    # 4. HEATMAP KORELASI
    # =========================
    elif option == "Heatmap Korelasi":
        st.write("Heatmap korelasi antar variabel numerik.")

        corr = df[numeric_cols].corr()

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            linewidths=0.5,
            ax=ax
        )
        st.pyplot(fig)

        # Kasih insight otomatis
        st.subheader("📌 Interpretasi Otomatis (Insight Korelasi)")
        target = "curah_hujan"

        if target in corr.columns:
            pengaruh = corr[target].sort_values(ascending=False)

            st.write("Variabel dengan pengaruh paling kuat terhadap curah hujan:")
            st.write(pengaruh)
        else:
            st.warning("Kolom 'curah_hujan' tidak ditemukan untuk analisis korelasi.")

    st.markdown("<hr>", unsafe_allow_html=True)
    
    # ============================
    #   GRAFIK KHUSUS CURAH HUJAN
    # ============================
    
    st.markdown("<h3 style='margin-top:40px;'>📈 Tren Curah Hujan (2022–2024)</h3>", unsafe_allow_html=True)
    
    df = pd.read_csv("datasetbmkg_clean_final.csv")
    
    # Pastikan kolom tanggal menjadi datetime
    df['tanggal'] = pd.to_datetime(df['tanggal'])
    
    # Extract tahun & bulan
    df['tahun'] = df['tanggal'].dt.year
    df['bulan'] = df['tanggal'].dt.month
    
    # ---------------------------
    # PILIHAN FILTER
    # ---------------------------
    pilih_tahun = st.selectbox(
        "Pilih Tahun:",
        ["Semua Tahun", 2022, 2023, 2024]
    )
    
    pilih_mode = st.radio(
        "Pilih Mode Tampilan:",
        ["Per Tahun (Rata-rata)", "Per Bulan", "Timeline Full"]
    )
    
    # ---------------------------
    # FILTER DATA BERDASARKAN TAHUN
    # ---------------------------
    if pilih_tahun != "Semua Tahun":
        df_filtered = df[df['tahun'] == pilih_tahun]
    else:
        df_filtered = df.copy()
    
    # ---------------------------
    # MODE 1 : RATA-RATA PER TAHUN
    # ---------------------------
    if pilih_mode == "Per Tahun (Rata-rata)":
        df_yearly = df_filtered.groupby("tahun")["curah_hujan"].mean().reset_index()
    
        st.write("**Rata-rata Curah Hujan per Tahun (mm)**")
        st.bar_chart(df_yearly, x="tahun", y="curah_hujan")
    
    # ---------------------------
    # MODE 2 : PER BULAN
    # ---------------------------
    elif pilih_mode == "Per Bulan":
        df_monthly = df_filtered.groupby(["tahun", "bulan"])["curah_hujan"].sum().reset_index()
    
        df_monthly['label'] = df_monthly['tahun'].astype(str) + "-" + df_monthly['bulan'].astype(str)
    
        st.write("**Total Curah Hujan per Bulan (mm)**")
        st.line_chart(df_monthly, x="label", y="curah_hujan")
    
    # ---------------------------
    # MODE 3 : TIMELINE FULL (HARIAN)
    # ---------------------------
    elif pilih_mode == "Timeline Full":
        df_daily = df_filtered.sort_values("tanggal")
    
        st.write("**Curah Hujan Harian**")
        st.line_chart(df_daily, x="tanggal", y="curah_hujan")

#==================================================================================================
elif menu == "Implementasi Model":
    st.title("📄 Implementasi Model")
   
    st.write("Berikut adalah dokumentasi proses implementasi model KNN dan Decision Tree C4.5 di RapidMiner:")

    # ========================
    # PROSES KNN TANPA CV
    # ========================
    st.subheader("🔹 Proses KNN (Tanpa Cross Validation)")
    st.image("assets/knn_proses.png", caption="Proses KNN di RapidMiner", use_container_width=True)
    st.markdown("""
    Pada percobaan pertama tanpa cross validation, model K-Nearest Neighbor dikonfigurasi dengan parameter:
    - **k = 3**, dipilih karena menghasilkan jarak tetangga yang lebih stabil pada dataset berskala kecil-menengah.
    - **Similarity Measure**: Euclidean Distance.
    - **Weighting**: Equal untuk setiap tetangga.
    - **Split Data**: 80% data training dan 20% data testing.
    Pemilihan rasio 80:20 digunakan karena menjadi standar umum untuk pembagian dataset pada proses klasifikasi ketika tidak menggunakan cross validation.""")
    st.markdown("<hr>", unsafe_allow_html=True)

    # ========================
    # PROSES DECISION TREE / C4.5 TANPA CV
    # ========================
    st.subheader("🔹 Proses Decision Tree C4.5 (Tanpa Cross Validation)")
    st.image("assets/c45_proses.png", caption="Proses Decision Tree C4.5", use_container_width=True)
    
    st.markdown("""
    Konfigurasi parameter untuk C4.5 meliputi:
- **Criterion**: Gain Ratio (paling umum untuk menangani variabel dengan skala berbeda).
- **Minimal Gain**: 0.1
- **Confidence**: 0.25 (default RapidMiner untuk pruning pohon, menjaga generalisasi model).
- **Maximal Depth**: None (pohon dibiarkan berkembang secara alami).
- **Split Data**: 80% training, 20% testing.
Parameter Gain Ratio dipilih untuk meningkatkan kestabilan pemilihan atribut terbaik.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

    # ========================
    # CORSS VALIDATION
    # ========================

    st.markdown("""
    ### 🔁 Parameter Cross Validation (5-Fold & 10-Fold)
    Cross Validation digunakan untuk mengukur kestabilan model pada data yang berbeda.
    Konfigurasi CV meliputi:
    - **K-Fold = 5 DAN K-Fold = 10** 
    - Data dibagi secara acak tetapi tetap mempertahankan distribusi kelas.
    - Perhitungan evaluasi menggunakan rata-rata setiap fold.
    """)

    # ========================
    # PROSES KNN DENGAN CV
    # ========================
    st.subheader("🔹 Proses KNN + Cross Validation")
    st.image("assets/knn_cv.png", caption="Cross Validation pada KNN", use_container_width=True)
    st.write("Berikut proses didalam Operator Cross Validation:")
    st.image("assets/knn_cv_in.png", caption="Proses Cross Validation", use_container_width=True)
    st.markdown("<hr>", unsafe_allow_html=True)


    # ========================
    # PROSES DECISION TREE DENGAN CV
    # ========================
    st.subheader("🔹 Proses Decision Tree C4.5 + Cross Validation")
    st.image("assets/c45_cv.png", caption="Cross Validation pada C4.5", use_container_width=True)
    st.write("Berikut proses didalam Operator Cross Validation:")
    st.image("assets/c45_cv_in.png", caption="Proses Cross Validation", use_container_width=True)
    st.markdown("<hr>", unsafe_allow_html=True)
   #================================================================================================== 

elif menu == "Evaluasi Model":
    st.title("📈 Hasil Evaluasi Model")

    # ============================
    # Narasi Pembuka
    # ============================
    st.write("""
    Pada tahap evaluasi, performa kedua algoritma dianalisis menggunakan metrik 
    **Accuracy, Precision, Recall, F1-Score, dan Kappa**.  
    Evaluasi dilakukan dalam dua skenario:

    1. **Tanpa Cross Validation (Split 80:20)**
    2. **Dengan Cross Validation (5-Fold & 10-Fold)**

    Tujuan evaluasi adalah mengetahui algoritma mana yang paling akurat dan stabil dalam
    mengenali pola curah hujan berdasarkan kategori cuaca.
    """)

    # ============================
    # Definisi Metrik
    # ============================
    st.markdown("""
    ### 📌 Definisi Metrik Evaluasi
    - **Accuracy** → Persentase prediksi yang benar.
    - **Precision** → Ketepatan model dalam memprediksi kelas tertentu.
    - **Recall** → Kemampuan model dalam menemukan seluruh data pada kelas tertentu.
    - **F1-Score** → Rata-rata harmonis Precision & Recall.
    - **Kappa** → Mengukur akurasi model dibandingkan tebakan acak.

    Kategori nilai Kappa:
    - < 0 : Buruk  
    - 0–0.20 : Lemah  
    - 0.21–0.40 : Cukup  
    - 0.41–0.60 : Baik  
    - ++0.60 : Sangat Baik  
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ============================
    # TABEL TANPA CROSS VALIDATION
    # ============================
    st.subheader("📊 Perbandingan Evaluasi (Tanpa Cross Validation)")

    data = {
        "Model": ["KNN", "C4.5"],
        "Akurasi": [67.92, 75.94],
        "Precision": [26.53, 43.01],
        "Recall": [31.29, 35.60],
        "F1-Score": [28.71, 38.96],
        "Kappa": [-0.011, 0.270]
    }

    df_eval = pd.DataFrame(data)

    styled_df = (df_eval.style
        .apply(lambda x: [
                '' if x.name == 'Model' else
                ('background-color: lightgreen' if v == x.max() else '')
                for v in x
            ], axis=0)
        .format({
            "Akurasi": "{:.2f}",
            "Precision": "{:.2f}",
            "Recall": "{:.2f}",
            "F1-Score": "{:.2f}",
            "Kappa": "{:.3f}"
        })
    )

    st.dataframe(styled_df, use_container_width=True)

    # ============================
    # CROSS VALIDATION
    # ============================
    st.subheader("🔁 Perbandingan Cross Validation")

    # KNN CV
    data_cv_knn = {
        "Fold": ["10-Fold", "5-Fold"],
        "Akurasi": [60.41, 56.03],
        "Precision": [25.29, 22.11],
        "Recall": [32.77, 29.77],
        "F1-Score": [28.58, 25.46],
        "Kappa": [0.127, 0.076]
    }
    df_cv_knn = pd.DataFrame(data_cv_knn)

    # Decision Tree CV
    data_cv_dt = {
        "Fold": ["10-Fold", "5-Fold"],
        "Akurasi": [78.70, 71.20],
        "Precision": [43.92, 49.57],
        "Recall": [35.50, 35.13],
        "F1-Score": [39.29, 41.17],
        "Kappa": [0.247, 0.235]
    }
    df_cv_dt = pd.DataFrame(data_cv_dt)

    st.markdown("### 🔹 KNN (Cross Validation)")
    st.dataframe(df_cv_knn)

    st.markdown("### 🔹 Decision Tree C4.5 (Cross Validation)")
    st.dataframe(df_cv_dt)

    st.markdown("<hr>", unsafe_allow_html=True)
    
    # ============================
    # GRAFIK 10-FOLD (tanpa Kappa)
    # ============================
    st.subheader("📊 Grafik Perbandingan Cross Validation (10-Fold)")

    import plotly.graph_objects as go

    metrics = ["Akurasi", "Precision", "Recall", "F1-Score"]

    knn_values = [
        df_cv_knn["Akurasi"][0],
        df_cv_knn["Precision"][0],
        df_cv_knn["Recall"][0],
        df_cv_knn["F1-Score"][0],
    ]

    dt_values = [
        df_cv_dt["Akurasi"][0],
        df_cv_dt["Precision"][0],
        df_cv_dt["Recall"][0],
        df_cv_dt["F1-Score"][0],
    ]

    fig = go.Figure(data=[
        go.Bar(name="KNN", x=metrics, y=knn_values),
        go.Bar(name="C4.5", x=metrics, y=dt_values)
    ])

    fig.update_layout(
        barmode="group",
        title="Perbandingan Hasil Cross Validation 10-Fold"
    )

    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    # ============================
    # INTERPRETASI
    #===============
    st.markdown("""
    ### 📌 Analisis Perbandingan Kinerja
    ## 1. Akurasi  
    Decision Tree C4.5 menunjukkan akurasi yang lebih tinggi dan stabil dibandingkan K-Nearest Neighbor (KNN).  
    - **KNN**: 67.92% tanpa CV → turun menjadi **60.41% ± 20.20%** (10-fold) dan **56.03% ± 26.42%** (5-fold).  
    - **Decision Tree C4.5**: 75.94% tanpa CV → stabil di **78.70% ± 1.72%** (10-fold) dan **78.70% ± 1.47%** (5-fold).  

    Performa KNN lebih buruk dan tidak stabil karena sangat sensitif terhadap distribusi data dan dipengaruhi ketidakseimbangan kelas (kelas hujan ringan mendominasi ±76.6%).  
    Decision Tree C4.5 mampu menangkap pola data lebih baik sehingga memberikan akurasi yang konsisten.

    ---

    ## 2. Weighted Mean Recall  
    - **KNN**: 31.29% → **32.77% ± 5.87%** (10-fold) → **29.77% ± 6.97%** (5-fold).  
    - **C4.5**: 35.60% → **35.60% ± 5.21%** (10-fold) → **35.13% ± 4.06%** (5-fold).

    Kedua model memiliki recall rendah karena ketidakseimbangan kelas, namun C4.5 tetap lebih stabil dibanding KNN.

    ---

    ## 3. Weighted Mean Precision  
    - **KNN**: 26.53% → turun menjadi **25.29% ± 9.76%** (10-fold) dan **22.11% ± 11.14%** (5-fold).  
    - **C4.5**: 43.01% → meningkat menjadi **43.92% ± 12.39%** (10-fold) dan **49.57% ± 13.67%** (5-fold).

    C4.5 memberikan pemisahan fitur yang lebih baik sehingga kesalahan prediksi lebih kecil dibanding KNN.

    ---

    ## 4. Kappa  
    - **KNN**: -0.011 (tanpa CV) → meningkat sedikit menjadi **0.127 ± 0.120** (10-fold) dan **0.076 ± 0.118** (5-fold).  
    - **C4.5**: 0.270 (tanpa CV) → tetap stabil di **0.247 ± 0.082** (10-fold) dan **0.235 ± 0.058** (5-fold).

    Hal ini menunjukkan bahwa KNN hampir setara dengan tebakan acak, sedangkan C4.5 jauh lebih reliable dalam klasifikasi.

    ---

    ## 5. Stabilitas Model  
    KNN memiliki deviasi yang sangat besar di semua metrik, menunjukkan performa yang tidak stabil dan sangat dipengaruhi perubahan komposisi data tiap fold.  
    Sebaliknya, Decision Tree C4.5 menunjukkan deviasi kecil dan performa yang konsisten, sehingga dinilai jauh lebih stabil.

    ---

    """)

    # ============================
    # Kesimpulan
    # ============================
elif menu == "Kesimpulan":
    st.title("🔹Penutup")
    st.subheader("🔹 Kesimpulan")
    # ===== Kesimpulan =====
    st.markdown("<div class='subjudul'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='paragraf'>
    1. Berdasarkan hasil analisis perbandingan kinerja K-Nearest Neighbor dan Decision Tree menunjukan decision Tree C4.5 memiliki kinerja lebih baik dalam klasifikasi dan mengenal pola data curah hujan dibandingkan K-Nearest Neighbor.<br>
    2. Berdasarkan hasil pengujian performa dan akurasi, Decision Tree C4.5 menghasilkan akurasi dan performa tertinggi, baik tanpa ataupun dengan cross-validation, sehingga ditentukan menjadi metode paling efektif untuk prediksi cuaca di wilayah Kota Tangerang Selatan<br><br>
    </div>
    """, unsafe_allow_html=True)
    st.subheader("🔹 Saran")
    # ===== Saran =====
    st.markdown("<div class='subjudul'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='paragraf'>
    1. Penelitian selanjutnya disarankan memperluas lokasi dan variasi data, agar model dapat diuji pada kondisi geografis dan pola cuaca yang berbeda. Selain itu, dapat mencoba algoritma lain seperti Random Forest atau metode ensemble untuk meningkatkan akurasi dan keandalan prediksi. <br>
    2. Kualitas dan periode data historis perlu ditingkatkan, serta dikembangkan menuju sistem prediksi cuaca real-time agar hasil analisis dapat dimanfaatkan langsung oleh instansi terkait dalam mitigasi banjir dan perencanaan wilayah.<br>
    </div>
    """, unsafe_allow_html=True)

# ======================
# NEXT BUTTON TANPA experimental_rerun
# ======================
st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("Next"):
    if st.session_state.menu_index < len(menu_list) - 1:
        st.session_state.menu_index += 1
    else:
        st.session_state.menu_index = 0  # kembali ke menu pertama
