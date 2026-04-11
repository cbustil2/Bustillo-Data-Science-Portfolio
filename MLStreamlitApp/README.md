# Machine Learnning Application Project

## Data Science Assignment 🖥️
As we are learning how to utilize Supervised Machine Learning models, we are asked to make a Streamlit app that allows us to practice coding a linear, logistic, or any other supervised machine learning model. So, the goals of the app is: 

1) Invite the user of the app to upload their own data or choose a sample dataset to analyze and run a machine learning model.

2) Allow the user to make changes regarding any missing values and choose their target values and features

3) Observe the chosen machine learning model (e.g., linear regression, logistic regression, decision tree, k-nearest neighbors) by the built-in graphs and calculations. 

## My Objectives
1) I want to make an app that allows the user to pick between a linear or logistic machine learning. 
    - Since I noticed the most common machine learning models are linear and logistic models, I want to have the app utilize both. This required me to code both a linear and logistic model.

2) I want to make an that not only provides the user an example or sample dataset that would be helpful to see how the machine learning works, but I also want to provide them an opportunity to upload their own data. 
    - I had to particularly code where there are different paths in proceeding with the app. 

3) I want to help the user understand what the machine learning model does for them.
    - I not only include graphs and calculations, I also include what some of the values may mean as well as what they should expect in a graph. 

## How to Use the App

When you click [here](https://cbustilmachinelearning.streamlit.app/), it should take you to the app (Note: there has been a confusing error so the app is not exactly active). When you enter the app, there are three main steps:
1) Upload Your Dataset:
2) Apply Machine Learning Algorithms
3) Visualize Results

Click [here](https://github.com/cbustil2/Bustillo-Data-Science-Portfolio/blob/main/MLStreamlitApp/MLStreamlitApp.py) to see all the code that was put into the making of the app. This may be the better way of trying out the app since it seems to not face any issue when locally deploying the app. 

## Notes and Considerations

### Applications and Code
Some applications that I used was:

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io) [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org) [![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org) [![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org) [![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=seaborn&logoColor=white)](https://seaborn.pydata.org) [![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)

### Sample Datasets
I have chosen two sample datasets, [baseball hitters](https://www.kaggle.com/datasets/wasiqaliyasir/hitters-dataset) and [Paris housing](https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction). The baseball hitters dataset is a sample set that helps with linear regression modeling while the Paris housing, focusing more on the classification, is better for logistic regression modeling. 

### Assistance

To assist in the making of the app, I looked at Ahmed Mohammed Sabri's Machine Learning stremalit app. His app was very helpful in knowing what code can be used to upload files as well as having a clean and organized app structure. You can find his work [here](https://github.com/Amsamms).

When I faced a lot of errors especially when transitioning to Streamlit and deploying the app, I used CoPilot to check my work and adjust my code as needed. 
