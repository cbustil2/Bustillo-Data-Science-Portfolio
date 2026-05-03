""" Machine Learning Unsupervised App """
# I will be referencing ricardoagonzalezc streamlit app for this project, specifically to find some inspiration for a particular design
# particularly with remembering how to have an interactive upload button and use example button. 

import streamlit as st
import pandas as pd
from pathlib import Path

#=== Page Title and Design setup ====

st.set_page_config(page_title="ML Unsupervised App", page_icon=":bar_chart:", layout="wide")

st.markdown("""
    <div style="
        background-color:#90EE90;
        padding:20px;
        border-radius:40px;
        display:inline-block;
        font-size:46px;
        font-weight:700;
        color:#003344;
        text-align:center;
        width:100%;
            font-family: 'Times New Roman', sans-serif;
    ">
        Machine Learning Unsupervised App
    </div>
""", unsafe_allow_html=True)

st.subheader("K-Means Clustering and PCA Visualization", text_alignment= "center")

st.write("\n\n"
"### Objectives: \n"
"* Provide an interactive platform/app for you to interact with by either uploading datasets or use sample ones\n"
"* Tune the particular dataset to your preferences and focus on particular features to perform K-Means clustering and PCA visualization\n"
"* Provide helpful insights and feedback to the results of the machine learning models and the visualizations"  
)

st.write("This app allows you to perform K-Means clustering and visualize the results using PCA. Upload your dataset or use\
          the example dataset to get started!")

st.write("\n\n"
         "### Instructions:\n"
         "1. Upload a CSV, XLSX, or XLS file containing your dataset or click the 'Use Example Dataset' button to load a sample dataset.\n"
         "2. Select the number of clusters for K-Means clustering.\n"
         "3. View the clustering results and PCA visualization in the respective tabs." )

st.write("\n\n")

#=== Data Upload Section ====

data_source = st.radio("**Choose data source:**", ["Use Sample Data", "Upload File"])

df = None

if data_source == "Use Sample Data":
    # Load the sample dataset from the data folder using an absolute path
    sample_path = Path(__file__).resolve().parent / "data" / "Mall_Customers.xls"
    if sample_path.exists():
        try:
            df = pd.read_excel(sample_path, engine='xlrd')
            st.success("Sample dataset loaded successfully!")
            st.write(df.head())
        except ImportError as err:
            st.error("The sample dataset requires the 'xlrd' package to read .xls files."
                     " Please install it or upload a CSV/XLSX file instead.")
            st.write(f"Error details: {err}")
            df = None
    else:
        st.error(f"Sample dataset not found: {sample_path}")
        df = None

elif data_source == "Upload File":
    uploaded_file = st.file_uploader("Upload your data file (CSV, XLSX, XLS)", type=["csv", "xlsx", "xls"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xlsx', '.xls')):
            if uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file, engine='openpyxl')
            else:  # .xls
                df = pd.read_excel(uploaded_file, engine='xlrd')
        else:
            st.error("Unsupported file type. Please upload CSV, XLSX, or XLS.")
            df = None
        if df is not None:
            st.success("Dataset uploaded successfully!")
            st.write(df.head())
    else:
        st.warning("Please upload a data file to proceed.")


tab1, tab2, tab3 = st.tabs(["Tuning and Hyperparameter Selection", "K-Means Clustering", "PCA Visualization"])

with tab1:
    st.header("Tuning and Hyperparameter Selection")
    st.write("In this section, you can select the features you want to use for K-Means clustering and PCA visualization. You can also choose the number of clusters for K-Means.")

    if df is not None:
        # Select features for K-Means and PCA
        all_features = df.columns.tolist()
        selected_features = st.multiselect("Select features for K-Means and PCA", options=all_features, default=all_features[:2])

        # Select number of clusters for K-Means
        num_clusters = st.slider("Select number of clusters for K-Means", min_value=2, max_value=10, value=3)
        st.write(f"You have selected the following features: {', '.join(selected_features)}")

