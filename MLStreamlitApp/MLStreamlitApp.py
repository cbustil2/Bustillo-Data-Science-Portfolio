""" Machine Learning Streamlit App"""
# Note: I will only do three machine learning algorithms for this app: Linear Regression and 
# Logistic Regression
# IMPORTANT: Lots of the code and structure of this app is based off Ahmed Mohamed Sabri's own 
# Streamlit app that has a similar goal. Github link: https://github.com/Amsamms 

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.graphics.gofplots import qqplot
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import LinearRegression

st.title(":robot: Machine Learning Streamlit App :robot:")

st.write("Hello :wave:! This is a Streamlit app that is built to be interactive and allow you to \
         upload your own dataset and apply machine learning algorithms to it! \
         :smile: :chart_with_upwards_trend: :bar_chart:")

#I am going to make some tabs so one can understand how the app works and then 
# see the their data, and see how the machine learning algorithms work.

tab1, tab2, tab3, tab4 = st.tabs(["How to Use This App", "Raw Dataset Preveiw", \
                                  "Cleaned Dataset Preview", "Machine Learning Algorithms"])
#================================================================================
# Steps to use the App
#================================================================================

with tab1:
    st.header("How to Use This App")
    st.write("This app is designed to be interactive and generally simple to use. Hear the steps to use the app below:")
    st.markdown(
        """
        1. **Upload Your Dataset**: Use the sidebar to upload your dataset in CSV or Excel format.\
        or if you don''t have a dataset, you can use the Hitter dataset or Paris Housing dataset \
            that is put into the app from Kaggle. Hitter dataset contains information \
                about baseball players and their performance, while the Paris Housing dataset \
                    contains information about housing prices in Paris. \
        2. **Edit Your Dataset**: In the sidebar, you can choose to remove \
            any missing values from your dataset to ensure better performance\
                  of machine learning algorithms.
            - **Preview Your Data**: Once uploaded, you can preview your dataset. You will see there \
        are two tabs for previewing your data: 'Raw Dataset Preview' and 'Cleaned Dataset Preview'. \
            The raw dataset will show you the original data you uploaded, \
                while the cleaned dataset will show you the data after removing any \
                    missing values (if you chose to do so).
        3. **Apply Machine Learning Algorithms**: In the 'Machine Learning \
            Algorithms' tab, you can select and apply various algorithms to your dataset.
            - Note: look at the sidebar to pick a particular target variable and the features you\
                want to use for the machine learning algorithms. You can also choose what \
                algorithm you want to apply to your data.
        4. **Visualize Results**: After applying the algorithms, you can visualize the results using built-in charts and graphs.
        """
    )
    st.markdown("For the sample datasets, here is a link for the \
                [baseball](https://www.kaggle.com/datasets/mathchi/hitters-baseball-data) \
                dataset or [Paris housing](https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction) \
                dataset.")

# I really like how Sabri uses a sidebar, so I will use that as a way to pick what they want to 
# do with their data. 

st.sidebar.header(" Step 1: :file_folder: Upload Your Dataset")
use_sample_dataset_hitter = st.sidebar.checkbox("Use sample Hitter dataset instead of uploading")
use_sample_dataset_paris = st.sidebar.checkbox("Use sample Paris Housing dataset instead of uploading")
if use_sample_dataset_hitter:
    sample_file_path = "Hitters.xls"
    uploaded_file = sample_file_path
elif use_sample_dataset_paris:
    sample_file_path = "ParisHousing.xls"
    uploaded_file = sample_file_path
else:
    uploaded_file = st.sidebar.file_uploader("Choose a CSV, XLSX, or XLS file", type=["csv", "xlsx", "xls"])

raw_data = None #This will be useful for the interactiveness of the app
df = None

#================================================================================
# Data Upload and Cleaning
#================================================================================

# Note: I am going to do most of the sidebar under this if statement
# My goal here is to allow the user to make edits the data but also know what there target
# variable is so they can apply the machine learning algorithms to it later on. 
# I also want to make sure that they can see the difference in the data if they 
# choose to remove missing values or not.
# Link to code that I will be using for assistance: https://github.com/Amsamms/General-machine-learning-algorithm/blob/master/main.py

if uploaded_file is not None: #This is so I have a raw daata variable that won't be changed if
                    # user wants to remove data with missing values.
    try:
        raw_data = pd.read_csv(uploaded_file, encoding_errors='ignore')
    except:
        pass
    try:
        raw_data = pd.read_excel(uploaded_file, engine='openpyxl')
    except:
        pass
    try:
        raw_data = pd.read_excel(uploaded_file, engine='openpyxl')
    except:
        pass
    st.sidebar.success("File uploaded successfully! :white_check_mark:")
    st.sidebar.header("Step 2: :pencil2: Edit Your Dataset")
    st.sidebar.write("Before looking at your dataset under the tab\
                     you can choose how to handle missing values in your dataset.\
                      This can help with the machine learning algorithms later on.")
    st.sidebar.write("Here are the number of data that has missing values in each column:")
    st.sidebar.dataframe(raw_data.isnull().sum())
    # Choosing missing-value strategy
    missing_strategy = st.sidebar.selectbox(
        "Choose how to handle missing values:",
        options=[
            "Remove missing values",
            "Fill missing values with mean",
            "Fill missing values with mode",
        ],
    )
    df = raw_data.copy() #this allows the user to upload either a .csv or\
                # .xlsx file and it will read it accordingly.

    if missing_strategy == "Remove missing values":
        df.dropna(inplace=True)
        st.sidebar.success("Missing values removed! :white_check_mark:")
    elif missing_strategy == "Fill missing values with mean":
        mean_values = df.mean(numeric_only=True).to_dict()
        df = df.fillna(mean_values)
        st.sidebar.success("Missing numeric values with column mean! :white_check_mark:")
    elif missing_strategy == "Fill missing values with mode":
        mode_values = {}
        for col in df.columns:
            mode = df[col].mode(dropna=True)
            if not mode.empty:
                mode_values[col] = mode.iloc[0]
        df = df.fillna(mode_values)
        st.sidebar.success("Missing values filled with column mode! :white_check_mark:")
    else:
        st.sidebar.info("Missing values not changed. The app will not continue with the original dataset.")
    
    st.sidebar.header("Step 3: :chart_with_upwards_trend: Apply Machine Learning Algorithms")

    # Choosing target variable and features for machine learning algorithms
    st.sidebar.write("Choose your target variable and features for machine learning algorithms.")
    if df is not None: 
        st.sidebar.write("Note: Since you chose to remove missing values, the target variable \
                         and features will be based on the cleaned dataset.")
        target_variable = st.sidebar.selectbox("**Select Target Variable**", options=df.columns)
        features = st.sidebar.multiselect("**Select Features**", options=df.columns)
    else:
        st.sidebar.write("Note: Since you chose to keep missing values, the target variable \
                         and features will be based on the original dataset.")
        target_variable_raw = st.sidebar.selectbox("**Select Target Variable**", options=raw_data.columns)
        features_raw = st.sidebar.multiselect("**Select Features**", options=raw_data.columns)
    
    #Choosing machine learning algorithm
    st.sidebar.subheader("Choose Machine Learning Algorithm")
    algorithm = st.sidebar.selectbox("Select Algorithm", options=["Linear Regression",\
                                                                   "Logistic Regression"])
with tab2:
    if uploaded_file is not None: 
        st.header("Raw Dataset Preview")
        st.write("Here is a preview of your raw dataset:")
        st.dataframe(raw_data.head()) #I want to show the raw data here so that if they choose to remove missing values, they can see the difference in the dataset.
        
        st.write("Raw Dataset Summary:")
        st.write(raw_data.describe())
    else: 
        st.write("Please upload a dataset to preview :smile:")

with tab3:
    if df is not None: 
        st.header("Cleaned Dataset Preview")
        st.write("Here is a preview of your cleaned dataset:")
        st.dataframe(df.head()) #I want to show the cleaned data here so that if they choose to remove missing values, they can see the difference in the dataset.
        
        st.write("Cleaned Dataset Summary:")
        st.write(df.describe())
    elif uploaded_file is not None:
        st.write("Please go to the sidebar and remove missing values so a cleaned dataset can be created.")
    else:
        st.write("If you would like to see a cleaned dataset preview, " \
        "please upload a dataset and edit it from the sidebar! :smile:")




with tab4:
    st.header("Machine Learning Algorithms.")

    if algorithm == "Linear Regression":
        st.write("Linear Regression will be implemented here.")
        st.write(f"You have selected *{target_variable}* as your target variable \
                 and *{features}* as your features for Linear Regression.")
        st.write("Important: for a good model, make sure that the MSE is low and the R-squared value\
                  is close to 1. Also, make sure to check the scatter plot of \
                 actual vs predicted values to check for linearity, the VIF (Variance Inflation Factor)\
                 for multicollinearity, and the Q-Q plot \
                 of residuals to check for normality of residuals, which are assumptions \
                 of linear regression.")
#================================================================================
#Linear Regression
#================================================================================
# Note: I am going to use the same code for all three algorithms,
#  but I will change the algorithm and the metrics used for each one.  
        if df is not None:
            X = df[features] 
            y = df[target_variable]
            from sklearn.model_selection import train_test_split #Spltting data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            from sklearn.linear_model import LinearRegression
            model = LinearRegression()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            from sklearn.metrics import mean_squared_error, r2_score
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            st.write(f"Mean Squared Error: {mse}")
            st.write(f"R-squared: {r2}")
            
            # Scatterplot and checking for linearity

            st.subheader("Scatter Plot of Actual vs Predicted Values For Linearity Check")
            st.write("This scatter plot helps to check the linearity of the relationship between " \
            "           actual and predicted values. If the points in the scatter plot \
                    approximately follow a straight line, then there is likely a linear \
                        relationship between the actual and predicted values.")
            
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            ax.scatter(y_test, y_pred, label='Data Points')
            ax.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label='Perfect Prediction Line')  # Line for perfect predictions
            ax.set_xlabel("Actual Values")
            ax.set_ylabel("Predicted Values")
            ax.set_title("Actual vs Predicted Values")
            # Add legend to help identify the data points and the perfect prediction line
            ax.legend()
            # Build the linear regression equation
            equation = f"y = {model.intercept_:.2f}"
            for i, coef in enumerate(model.coef_):
                sign = "+" if coef >= 0 else ""
                equation += f" {sign}{coef:.2f} * {features[i]}"
            # Add equation as text on the plot
            ax.text(0.05, 0.95, f"Regression Equation:\n{equation}", transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
            st.pyplot(fig)

            # VIF for multicollinearity
            st.subheader("Variance Inflation Factor (VIF) for Multicollinearity Check")
            st.write("We assess multicollinearity by computing the Variance Inflation Factor (VIF)\
                      for each predictor. VIF values below 5 (or sometimes 10) generally \
                     indicate that multicollinearity is not a concern.")   
            try:
                vif_data = pd.DataFrame()
                vif_data["Feature"] = features  
                vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
                st.dataframe(vif_data)
            except Exception as e:
                st.warning("VIF calculation could not be completed for this dataset. Continuing without VIF.")

            #Checking homoscedasticity with residuals plot
            st.subheader("Residuals Plot for Homoscedasticity Check")
            st.write("To assess homoscedasticity (constant variance of residuals),\
                      we plot the residuals versus the predicted values. A random \
                     scatter around zero suggests constant variance.")
            residuals = y_test - y_pred
            fig, ax = plt.subplots()
            ax.scatter(y_pred, residuals)
            ax.axhline(0, color='r', linestyle='--')
            ax.set_xlabel("Predicted Values")
            ax.set_ylabel("Residuals")
            ax.set_title("Residuals vs Predicted Values")
            st.pyplot(fig)

            # Visual comparison of actual vs predicted values 
            comparison_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
            st.subheader("Actual vs Predicted Values")
            st.dataframe(comparison_df.head())
            # Q-Q plot for residuals - I will use this to check for normality of residuals,
            #  which is an assumption of linear regression.
            st.subheader("Q-Q Plot of Residuals for Normality Check")
            st.write("This plot helps to check the normality of residuals, \
                     which is an assumption of linear regression. \
                     If the points in the Q-Q plot approximately follow a straight line, \
                     then the residuals are likely to be normally distributed.")
            import matplotlib.pyplot as plt
            import scipy.stats as stats
            residuals = y_test - y_pred
            fig, ax = plt.subplots()
            stats.probplot(residuals, dist="norm", plot=ax)
            ax.set_title("Q-Q Plot of Residuals")
            st.pyplot(fig)

        else:
            st.warning("Please upload a dataset and select \
                       missing-value removal options in the sidebar before running Linear Regression.")
    

    elif algorithm == "Logistic Regression":
        st.write("Logistic Regression will be implemented here.")
        st.write(f"You have selected *{target_variable}* as your target variable \
                 and *{features}* as your features for Logistic Regression.")
        st.write("Important: for a good model, make sure that the accuracy is \
                 high and the ROC AUC score is close to 1. Also, make sure to check \
                 the confusion matrix and the classification report to evaluate the \
                 performance of your logistic regression model.")
        #Splitting Data
        if df is not None:
            X = df[features] 
            y = df[target_variable]
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            from sklearn.linear_model import LogisticRegression
            model = LogisticRegression(max_iter=1000)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            # Evaluating the model
            from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, classification_report
            accuracy = accuracy_score(y_test, y_pred)
            roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
            st.write(f"Accuracy: {accuracy}")
            st.write(f"ROC AUC Score: {roc_auc}")
            
            # Logistic Regression Equation and Dataset Points
            st.subheader("Logistic Regression Equation and Dataset Points")
            try:
                y_prob = model.predict_proba(X_test)[:, 1]
                
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.scatter(range(len(y_test)), y_test, alpha=0.6, label='Actual Data Points', s=80, color='blue')
                ax.plot(range(len(y_prob)), y_prob, 'r-', linewidth=2, label='Logistic Regression Curve')
                ax.set_xlabel("Sample Index")
                ax.set_ylabel("Probability")
                ax.set_title("Logistic Regression: Dataset Points and Equation")
                ax.legend()
                
                # Add equation
                equation = f"log(p/(1-p)) = {model.intercept_[0]:.2f}"
                for i, feat in enumerate(features):
                    sign = "+" if model.coef_[0][i] >= 0 else ""
                    equation += f" {sign}{model.coef_[0][i]:.2f} * {feat}"
                ax.text(0.05, 0.95, f"Equation:\n{equation}", transform=ax.transAxes, fontsize=9, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
                st.pyplot(fig)
            except Exception as e:
                st.warning("Unable to create logistic regression plot.")
            
            st.subheader("Confusion Matrix")
            st.write("The confusion matrix shows the counts of true positives, \
                     true negatives, false positives, and false negatives. \
                     A good model will have high counts of true positives and \
                     true negatives, and low counts of false positives and false negatives.")
            cm = confusion_matrix(y_test, y_pred)
            fig, ax = plt.subplots()
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
            ax.set_xlabel("Predicted Labels")
            ax.set_ylabel("True Labels")
            ax.set_title("Confusion Matrix")
            st.pyplot(fig)
            st.subheader("Classification Report")
            report = classification_report(y_test, y_pred, output_dict=True)
            report_df = pd.DataFrame(report).transpose()
            st.dataframe(report_df)
            # ROC Curve
            st.subheader("ROC Curve")
            from sklearn.metrics import roc_curve
            fpr, tpr, thresholds = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
            fig, ax = plt.subplots()
            ax.plot(fpr, tpr, label='ROC Curve (area = {:.2f})'.format(roc_auc))
            ax.plot([0, 1], [0, 1], 'k--')  # Diagonal line for random guessing
            ax.set_xlabel("False Positive Rate")
            ax.set_ylabel("True Positive Rate")
            ax.set_title("Receiver Operating Characteristic (ROC) Curve")
            ax.legend(loc='lower right')
            st.pyplot(fig)
            

        else:
            st.warning("Please upload a dataset and select \
                       missing-value removal options in the sidebar before running Logistic Regression.")
        






