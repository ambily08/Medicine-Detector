import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    file_path = "A_Z_medicines_dataset_with_usage.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/609/609091.png", width=100)  
st.sidebar.title("💊 Medicine Finder")
st.sidebar.write("🔍 Search for medicines and get their usage details instantly.")
st.sidebar.markdown("---")
st.sidebar.write("📌 **Data Source:** Medicine Database")
st.sidebar.write("📅 **Entries:**", len(df))

st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
    }
    .medicine-name {
        font-size: 22px;
        font-weight: bold;
        color: #2E86C1;
    }
    .usage-text {
        font-size: 18px;
        color: #555;
    }
    .info-box {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        border-left: 5px solid #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="main-title">💊 Medicine Usage Lookup</p>', unsafe_allow_html=True)
st.write("Search for a medicine to find its usage and details.")


medicine_list = df["name"].dropna().unique()
medicine_name = st.selectbox("Select or type medicine name:", [""] + list(medicine_list))

if medicine_name:
    results = df[df["name"].str.contains(medicine_name, case=False, na=False)]
    
    if not results.empty:
        for _, row in results.iterrows():
            st.markdown(f'<p class="medicine-name">{row["name"]}</p>', unsafe_allow_html=True)
            st.write(f"**Manufacturer:** {row['manufacturer_name']}")
            st.write(f"**Type:** {row['type']}")
            st.write(f"**Price:** ₹{row['price(₹)']}")
            st.markdown(f'<div class="info-box"><p class="usage-text"><b>Usage:</b> {row["usage"]}</p></div>', unsafe_allow_html=True)
            st.write("---")
    else:
        st.error("❌ No matching medicine found.")
