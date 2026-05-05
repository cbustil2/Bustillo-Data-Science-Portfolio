""" Machine Learning Unsupervised App """
# I will be referencing ricardoagonzalezc streamlit app for this project, specifically to find some inspiration for a particular design
# particularly with remembering how to have an interactive upload button and use example button. 

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.metrics import accuracy_score
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

#=== Page Title and Design setup ===========================================================================================================

st.set_page_config(page_title="ML Unsupervised App", page_icon=":bar_chart:", layout="wide")
st.markdown('<a name="top"></a>', unsafe_allow_html=True) #This is useful since the first tab is long

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

st.subheader("K-Means Clustering, Hierarchical Clustering and PCA Visualization", text_alignment= "center")

st.write("\n\n"
"### Objectives: \n"
"* Provide an interactive platform/app for you to interact with by either uploading datasets or use sample ones\n"
"* Tune the particular dataset to your preferences and focus on particular features to perform K-Means clustering, \
    Hierarchical clustering and PCA visualization\n"
"* Provide helpful insights and feedback to the results of the machine learning models and the visualizations"  
)

st.write("\n\n"
         "### Instructions:\n"
         "1. Upload a CSV, XLSX, or XLS file containing your dataset or click the 'Use Example Dataset' button to load a sample dataset.\n"
         "2. Select the number of clusters for K-Means clustering.\n"
         "3. View the clustering results and PCA visualization in the respective tabs." )

st.write("\n\n")

#=== Data Upload Section ===================================================================================================================

data_source = st.radio("**Choose data source:**", ["Use Sample Data", "Upload File"])

df = None

if data_source == "Use Sample Data": # Needs to fix streamlit issue here *********
    # Load the sample dataset from the data folder
    df = pd.read_csv('MLUnsupervisedApp/data/Mall_Customers.xlsx')
    st.success("Sample dataset loaded successfully!")

    st.write(df.head())

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
st.divider()
st.write("\n\n"
         "### Steps: \n\n" \
         "1. After uploading your dataset or using the sample dataset, go to the 'Tuning and Hyperparameter Selection' tab \
            to select the features you want to use for K-Means clustering, Hierarchical clustering and PCA visualization. You can \
                also select the number of clusters for K-Means and the linkage method for Hierarchical Clustering.\n" \
         "2. After selecting your preferences, go to the 'K-Means Clustering' tab to view the results of K-Means clustering \
            based on your selected features and number of clusters.\n" \
         "3. Next, go to the 'Hierarchical Clustering' tab to view the results of Hierarchical Clustering based on your \
            selected features and linkage method.\n"
         "4. Finally, go to the 'PCA Visualization' tab to view the PCA visualization of your dataset based on the selected features.\n"
         "5. Lastly, enjoy the insights and visualizations!! :smile:")
st.divider()
tab1, tab2, tab3, tab4= st.tabs(["Tuning and Hyperparameter Selection", "K-Means Clustering", "Hierarchical Clustering", "PCA Visualization"])
st.divider()
#=== Tuning and Hyperparameter Selection ====

with tab1:
    st.header("Tuning and Hyperparameter Selection")
    st.write("In this section, you can select the features you want to use for K-Means clustering and PCA visualization. " \
    "You can also choose the number of clusters for K-Means.")

    if df is not None:
        #Select features for K-Means Hierarchical and PCA
        all_features = df.columns.tolist()
        with st.expander("What is the purpose of selecting features for K-Means, Hierarchical and PCA? :thought_balloon:"): #This 
            #is just to allow for a really good interactive explanation of particular parts of the modeling process. 
            st.markdown("""
            Feature selection for K-Means, Hierarchical and PCA is imporrtant because it allows you 
            to <span style="background-color: #FFFF00;">focus on the most relevant information in your dataset</span>. 
            By choosing specific features, you can <span style="background-color: #FFFF00;">improve the performance of your clustering 
            algorithms, hierarchical clustering and PCA visualization</span>. It helps in <span style="background-color: \
                        #FFFF00;">reducing noise and irrelevant data</span>, 
            which can lead to *better insights* and more *meaningful clusters*. Additionally, selecting 
            the right features can enhance the **interpretability** of your results and make it easier to 
            understand the underlying patterns in your data.
            """, unsafe_allow_html=True)

        st.write("\n")
    
        selected_features = st.multiselect("Select features for K-Means, Hierarchical and PCA", options=all_features, default=all_features[:2], key="selected_features")
        st.success(f"You have selected {len(selected_features)} features for K-Means, Hierarchical and PCA.")
        #Warning
        st.warning("Note: The more features you select, the more dimensions your data will have, in some ways, improving the " \
        "clustering results but also making it more difficult to visualize and interpret the results. " )
        #Select number of clusters for K-Means
        num_clusters = st.slider("Select number of clusters for K-Means", min_value=2, max_value=100, value=3, key="num_clusters")
        with st.expander("What is the purpose of selecting the number of clusters for K-Means? :thought_balloon:"):
            st.markdown("""
            Selecting the number of clusters for K-Means is important because it impacts **directly** to the quality and interpretability of 
            your clustering results. The number of clusters <span style="background-color: #FFFF00;">determines how the algorithm 
            groups your data points</span>, and choosing an appropriate value can help you find meaningful patterns and 
            insights from your dataset. If you select too few clusters, <span style="background-color: #FFB3B3;">you may oversimplify 
            the data and miss important distinctions between groups</span>. Now, if you select too many clusters, 
            <span style="background-color: #FFB3B3;">you may overfit the data and create groups that are not meaningful or actionable</span>. 
            Therefore, selecting the right number of clusters is *crucial* for producing accurate and insightful clustering results.
            """, unsafe_allow_html=True)

        linkage_method = st.selectbox("Select linkage method for Hierarchical Clustering", options=["ward", "complete", \
                                                                                                    "average", "single"], index=0)
        with st.expander("What is the purpose of selecting the linkage method for Hierarchical Clustering? :thought_balloon:"):
            st.markdown("""
            The linkage method for Hierarchical Clustering helps determines how the algorithm <span style="background-color: #FFFF00;">calculates 
            the distance between clusters and how it merges them</span>. Different linkage methods can lead to different clustering results, 
            and choosing the appropriate one can help you find meaningful patterns in your data. For example, the *"ward"* method 
            minimizes the variance within clusters, while the *"complete"* method considers the maximum distance between points 
            in different clusters. The *"average"* method calculates the average distance between points in different clusters, 
            and the *"single"* method considers the minimum distance between points in different clusters. Therefore, selecting 
            the right linkage method is crucial for producing accurate and insightful hierarchical clustering results.
            """, unsafe_allow_html=True)

        st.write(f"***Summary***: You have selected the following features: ***{', '.join(selected_features)}***. \
                 You have selected ***{num_clusters}*** clusters for K-Means and the ***{linkage_method}*** method for Hierarchical Clustering."
                 )
        
        #=== Data Preview Section =========================================================================================================
        st.divider()
        st.subheader("📊 Data Preview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Dataset Overview:**")
            st.metric("Total Rows", df.shape[0])
            st.metric("Total Columns", df.shape[1])
            st.metric("Selected Features", len(selected_features))
        
        with col2:
            st.write("**Selected Features Info:**")
            feature_info = pd.DataFrame({
                'Feature': selected_features,
                'Data Type': [str(df[col].dtype) for col in selected_features],
                'Missing Values': [df[col].isnull().sum() for col in selected_features]
            })
            st.dataframe(feature_info, use_container_width=True)
        
        st.write("**Sample of Selected Features:**")
        st.dataframe(df[selected_features].head(10), use_container_width=True)
        
        st.write("**Statistical Summary:**")
        st.dataframe(df[selected_features].describe(), use_container_width=True)
        
        #=== Dealing with missing values ==== [taken from a previous assignment]
        st.divider()
        st.subheader("Handle Missing Values")
        if df[selected_features].isnull().sum().sum() > 0:
            missing_strategy = st.selectbox(
                "Choose how to handle missing values:",
                options=[
                    "Remove missing values",
                    "Fill missing values with mean",
                    "Fill missing values with mode",
                ],
            )
            
            df_processed = df.copy()
            
            if missing_strategy == "Remove missing values":
                df_processed.dropna(inplace=True)
                st.success("Missing values removed! ✓")
            elif missing_strategy == "Fill missing values with mean":
                mean_values = df_processed.mean(numeric_only=True).to_dict()
                df_processed = df_processed.fillna(mean_values)
                st.success("Missing numeric values filled with column mean! ✓")
            elif missing_strategy == "Fill missing values with mode":
                mode_values = {}
                for col in df_processed.columns:
                    mode = df_processed[col].mode(dropna=True)
                    if not mode.empty:
                        mode_values[col] = mode.iloc[0]
                df_processed = df_processed.fillna(mode_values)
                st.success("Missing values filled with column mode! ✓")
            
            st.info(f"Dataset shape after handling missing values: {df_processed.shape}")
            
            # Store processed data in session state for use in other tabs
            st.session_state.df_processed = df_processed
        else:
            st.success("No missing values detected in the selected features! ✓")
        st.markdown("""
            <a href="#top">
            <div style="
                background-color:#90EE90;
                padding:10px 20px;
                border-radius:25px;
                display:inline-block;
                color:#003300;
                font-weight:600;
                margin-top:20px;
                cursor:pointer;
            ">
            ⬆ Back to Top
            </div>
            </a>
            """, unsafe_allow_html=True)

        
    else:
        st.warning("Please upload a dataset to select features and hyperparameters for K-Means, Hierarchical and PCA.")
        
#=== K-Means Clustering =====================================================================================================================
with tab2:
    k = num_clusters
    st.header("K-Means Clustering")
    st.write("In this section, you can view the results of K-Means clustering based on your selected features and number of clusters.")
    kmeans = KMeans(n_clusters=k, random_state=42)
    if df is not None and selected_features:
        # Use processed data if available, otherwise use raw data
        df_to_use = st.session_state.get('df_processed', df)
        X = df_to_use[selected_features].copy()
        
        #For One-hot encode categorical columns if there are any, since K-Means cannot handle categorical data directly.
        categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
        if len(categorical_cols) > 0:
            X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
            st.info(f"One-hot encoded categorical columns: {', '.join(categorical_cols)}")
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        kmeans.fit(X_scaled)
        df['KMeans_Cluster'] = kmeans.labels_
        st.write(df.head())
        silhouette_avg = silhouette_score(X_scaled, kmeans.labels_)
        st.write(f"Silhouette Score for K-Means Clustering: {silhouette_avg:.2f}")
        
        # 2D Scatter Plot of Clustering Results Using PCA
        pca_2d = PCA(n_components=2)
        X_pca = pca_2d.fit_transform(X_scaled)
        
        st.write(f"**PCA Explained Variance Ratio:** PC1: {pca_2d.explained_variance_ratio_[0]:.2%}, PC2: {pca_2d.explained_variance_ratio_[1]:.2%}")
        
        plt.figure(figsize=(10, 6))
        
        # Iterate over unique cluster labels and plot each cluster separately
        for cluster_label in np.unique(kmeans.labels_):
            # Get indices of data points belonging to the current cluster
            indices = np.where(kmeans.labels_ == cluster_label)[0]
            
            # Scatter plot for the current cluster
            plt.scatter(X_pca[indices, 0], X_pca[indices, 1],
                       label=f'Cluster {cluster_label}', alpha=0.6, s=100, edgecolor='k')
        
        # Plot cluster centers (transformed to PCA space)
        centers_pca = pca_2d.transform(kmeans.cluster_centers_)
        plt.scatter(centers_pca[:, 0], centers_pca[:, 1], c='red', marker='X', 
                   s=300, edgecolor='black', linewidth=2, label='Centroids')
        
        plt.title("K-Means Clustering - 2D PCA Visualization")
        plt.xlabel(f"Principal Component 1 ({pca_2d.explained_variance_ratio_[0]:.1%})")
        plt.ylabel(f"Principal Component 2 ({pca_2d.explained_variance_ratio_[1]:.1%})")
        plt.legend(loc='best')
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)
        with st.expander("What am I looking at? :thought_balloon:"):
            st.markdown("""
            The K-Means clustering results can be interpreted by looking at the silhouette score and the 
            PCA visualization of the clusters. A silhouette score close to 1, which is high, indicates that the clusters are 
            well-defined and distinct, while a score close to 0 suggests that the clusters are overlapping or 
            not well-separated. The PCA visualization shows the distribution of the clusters in a 
            reduced dimensional space, allowing you to see how the data points are grouped together based on the 
            selected features. These cluster centers and the spread of the data points help provide insights 
            into the characteristics of each cluster and identify any patterns or trends in your dataset.
            """, unsafe_allow_html=True)

        #Evaluating the optimal number of clusters using silhouette score
        st.subheader("Silhouette Score Optimization for K-Means Clustering")
        a1 = st.slider("Select minimum number of clusters to evaluate for silhouette score", min_value=2, max_value=10, value=2, key="kmeans_silhouette_min")
        b1 = st.slider("Select maximum number of clusters to evaluate for silhouette score", min_value=2, max_value=100, value=10, key="kmeans_silhouette_max")
        k_range = range(a1, b1)
        silhouette_scores = []  
        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            labels = kmeans.fit_predict(X_scaled)
            silhouette_avg = silhouette_score(X_scaled, labels)
            silhouette_scores.append(silhouette_avg)
        optimal_k = k_range[np.argmax(silhouette_scores)]
        st.write(f"Optimal number of clusters based on silhouette score: {optimal_k}")
        #Plotting the curve
        plt.figure(figsize=(10, 6))
        plt.plot(k_range, silhouette_scores, marker='o')
        plt.title("Silhouette Scores for K-Means Clustering")
        plt.xlabel("Number of Clusters (k)")
        plt.ylabel("Silhouette Score")
        plt.xticks(k_range)
        plt.grid(True)
        st.pyplot(plt)
        with st.expander("What am I looking at? :thought_balloon:"):
            st.markdown("""
            The silhouette score optimization helps you determine the optimal number of clusters in your data. 
            You can identify the value of k that maximizes the silhouette score, indicating the best-defined clusters, by looking at the 
            plot of silhouette scores. The plot of silhouette scores allows you to see how the quality of clustering 
            changes with different values of k, helping you make a decision about the number of clusters to use for
            your K-Means clustering analysis.
            """, unsafe_allow_html=True)
        st.markdown("""
            ***Next step***: Go to the "Hierarchical Clustering" tab"""
                    , unsafe_allow_html=True)

    else:
        st.warning("Please select features and upload a dataset to view K-Means clustering results.")


        
#=== Hierarchical Clustering ==============================================================================================================
with tab3:
    st.header("Hierarchical Clustering")
    st.write("In this section, you can view the results of Hierarchical Clustering based on your selected features and linkage method.")

    if df is not None and selected_features:
        # Use processed data if available, otherwise use raw data
        df_to_use = st.session_state.get('df_processed', df)
        X = df_to_use[selected_features].copy()
        
        #For One-hot encode categorical columns if there are any, since Hierarchical Clustering cannot handle categorical data directly.
        categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
        if len(categorical_cols) > 0:
            X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
            st.info(f"One-hot encoded categorical columns: {', '.join(categorical_cols)}")
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        Z = linkage(X_scaled, method=linkage_method)
        
        plt.figure(figsize=(12, 6))
        dendrogram(Z, truncate_mode='level', p=5)
        plt.title(f"Hierarchical Clustering Dendrogram ({linkage_method.capitalize()} Linkage)")
        plt.xlabel("Sample Index")
        plt.ylabel("Distance")
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)
        
        with st.expander("What am I looking at? :thought_balloon:"):
            st.markdown("""
            The hierarchical clustering results can be interpreted by looking at the dendrogram.
            The dendrogram shows how the data points are merged together based on their similarity. 
            The height of the branches represents the distance between clusters, and the vertical lines 
            indicate where clusters are formed. By cutting the dendrogram at a certain height, you can determine 
            the number of clusters in your data. The choice of linkage method (ward, complete, average, single) 
            affects how the distances between clusters are calculated and can lead to different clustering results. 
            Analyzing the dendrogram helps you understand the structure of your data and identify meaningful clusters.
            """, unsafe_allow_html=True)
        #Sillhouete Score Optimization for Hierarchical Clustering
        st.subheader("Silhouette Score Optimization for Hierarchical Clustering")
        #Set the range for number of clusters to evaluate
        a2 = st.slider("Select minimum number of clusters to evaluate for silhouette score", min_value=2, max_value=10, value=2, key="hierarchical_silhouette_min")
        b2 = st.slider("Select maximum number of clusters to evaluate for silhouette score", min_value=2, max_value=100, value=10, key="hierarchical_silhouette_max")

        
        k_range = range(a2, b2)
        silhouette_scores = []
        for k in k_range:
            hierarchical = AgglomerativeClustering(n_clusters=k, linkage=linkage_method)
            labels = hierarchical.fit_predict(X_scaled)
            silhouette_avg = silhouette_score(X_scaled, labels)
            silhouette_scores.append(silhouette_avg)
        optimal_k = k_range[np.argmax(silhouette_scores)]
        st.write(f"Optimal number of clusters based on silhouette score: {optimal_k}")

        #Plotting the curve
        plt.figure(figsize=(10, 6))
        plt.plot(k_range, silhouette_scores, marker='o')
        plt.title(f"Silhouette Scores for Hierarchical Clustering ({linkage_method.capitalize()} Linkage)")
        plt.xlabel("Number of Clusters (k)")
        plt.ylabel("Silhouette Score")
        plt.xticks(k_range)
        plt.grid(True)
        st.pyplot(plt)
        with st.expander("What am I looking at? :thought_balloon:"):
            st.markdown("""
            The silhouette score optimization helps you determine the optimal number of clusters in your data. 
            By looking at the silhouette scores, you can identify the value of k that maximizes the silhouette score, 
            indicating the best-defined clusters. The plot of silhouette scores allows you to visually 
            see how the quality of clustering changes with different values of k, helping you make an informed
            decision about the number of clusters to use for your hierarchical clustering analysis.
            """, unsafe_allow_html=True)
        st.markdown("""
            ***Next step***: Go to the "PCA Visualization" tab"""
                    , unsafe_allow_html=True)   
    
    else:
        st.warning("Please select features and upload a dataset to view Hierarchical Clustering results.")


#=== PCA Visualization ==================================================================================================================
with tab4:
    st.header("PCA Visualization")
    st.write("In this section, you can view the PCA visualization of your dataset based on the selected features.")

    if df is not None and selected_features:
        # Use processed data if available, otherwise use raw data
        df_to_use = st.session_state.get('df_processed', df)
        X = df_to_use[selected_features].copy()
        
        #For One-hot encode categorical columns if there are any, since PCA cannot handle categorical data directly.
        categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
        if len(categorical_cols) > 0:
            X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
            st.info(f"One-hot encoded categorical columns: {', '.join(categorical_cols)}")
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)
        
        st.write(f"**PCA Explained Variance Ratio:** PC1: {pca.explained_variance_ratio_[0]:.2%}, PC2: {pca.explained_variance_ratio_[1]:.2%}")
        
        plt.figure(figsize=(10, 6))

        # If K-Means labels exist, color points by cluster. Otherwise, show all points in one group.
        if 'KMeans_Cluster' in df_to_use.columns:
            labels = df_to_use['KMeans_Cluster'].values
            unique_labels = np.unique(labels)
            colors = plt.cm.get_cmap('tab10', len(unique_labels))
            for i, label in enumerate(unique_labels):
                indices = np.where(labels == label)[0]
                plt.scatter(X_pca[indices, 0], X_pca[indices, 1],
                            color=colors(i), alpha=0.7, edgecolor='k', s=100,
                            label=f'Cluster {label}')
            plt.legend(loc='best')
        else:
            plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7, s=100, edgecolor='k', color='navy', label='Data points')
            plt.legend(loc='best')

        plt.title("PCA Visualization of Selected Features")
        plt.xlabel(f"Principal Component 1 ({pca.explained_variance_ratio_[0]:.1%})")
        plt.ylabel(f"Principal Component 2 ({pca.explained_variance_ratio_[1]:.1%})")
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)
        
        with st.expander("What am I looking at? :thought_balloon:"):
            st.markdown("""
            The PCA visualization shows how the data points are distributed in a reduced dimensional space based on the selected features. 
            The explained variance ratio shows how much of the original variance in the data is captured by each principal component. 
            A higher explained variance ratio means that the principal component captures more of the variability in the data. 
            By looking at the scatter plot of the PCA results, you can identify patterns, clusters, or trends in your dataset that
            may not be apparent in the original high-dimensional space. This visualization can help you gain insights into the
             structure of your data and understand the relationships between different features.""")
            
    # PCA Loadings
        st.subheader("PCA Loadings")
        loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2'], index=X.columns)
        st.dataframe(loadings, use_container_width=True)
        with st.expander("What are PCA loadings? :thought_balloon:"):
            st.markdown("""
            PCA loadings represent the contribution of each original feature to the principal components. 
            They indicate how much each feature influences the direction of the principal components in the reduced dimensional space. 
            A higher absolute value of a loading indicates that the feature has a stronger influence on that principal component. 
            By analyzing the loadings, you can understand which features are most important in explaining the variance captured by each principal component and gain insights into the underlying structure of your data.
            """, unsafe_allow_html=True)
    # PCA Horizontal Bar Plot of Loadings
        st.subheader("PCA Loadings Bar Plot")
        
        # Build a DataFrame from pca.components_ (shape: n_components x n_features).
        # Each row is a principal component; each column is a feature's loading weight.
        loadings_df = pd.DataFrame(
            pca.components_,
            columns=X.columns,
            index=[f'PC{i+1}' for i in range(pca.n_components_)]
        )
        
        # Set up positions for the horizontal bars — one slot per feature
        features = loadings_df.columns.tolist()
        y_pos = np.arange(len(features))
        bar_height = 0.3  # Controls how thick each bar is
        
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Plot PC1 and PC2 loadings side by side for each feature.
        # We offset each set by half the bar height so they don't overlap.
        ax.barh(y_pos + bar_height/2, loadings_df.loc['PC1'], bar_height,
                label='PC1', color='#1b2a4a', edgecolor='none')
        ax.barh(y_pos - bar_height/2, loadings_df.loc['PC2'], bar_height,
                label='PC2', color='#c5a829', edgecolor='none')
        
        # Label the y-axis with feature names and the x-axis with loading weight
        ax.set_yticks(y_pos)
        ax.set_yticklabels(features)
        ax.set_xlabel('Loading Weight')
        ax.set_title('PCA Loadings (how each feature contributes)', fontweight='bold', loc='left')
        
        # Add a vertical reference line at 0 so we can see positive vs. negative loadings
        ax.axvline(0, color='grey', linewidth=0.8)
        
        ax.legend(loc='upper right', frameon=True)
        ax.invert_yaxis()          # Put the first feature at the top of the chart
        ax.grid(axis='x', alpha=0.3)
        ax.set_frame_on(False)     # Remove the border box for a cleaner look
        plt.tight_layout()
        st.pyplot(fig)
        with st.expander("What am I looking at? :thought_balloon:"):
            st.markdown("""
            The PCA loadings bar plot shows the contribution of each original feature to the principal components. 
            By looking at the bar plot, you can easily identify which features have the strongest influence on each principal component. 
            This helps you understand the underlying structure of your data and which features are most important 
            in explaining the variance captured by the PCA.
            """, unsafe_allow_html=True)

    else:
        st.warning("Please select features and upload a dataset to view PCA visualization results.")
