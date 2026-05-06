# Unsupervised Machine Learning Application Project

## Data Science Assignment 🖥️
As we are learning how to utilize Unsupervised Machine Learning models, we were asked to build a Streamlit app that allows us to practice coding algorithms such as **K‑means clustering**, **hierarchical clustering**, and **Principal Component Analysis (PCA)**. The goals of the app are:

1) Invite the user to upload their own dataset or choose a sample dataset to explore using unsupervised learning models.

2) Allow the user to clean their data, select features, and prepare the dataset for clustering or dimensionality reduction.

3) Help the user observe and interpret the results of unsupervised learning through built‑in graphs, PCA visualizations, and cluster summaries.

## My Objectives
1) I want to make an app that allows the user to pick between different unsupervised learning methods.  
   - Since K‑means and PCA are among the most common unsupervised learning tools, I coded the app so the user can run both and compare how they behave on the same dataset.

2) I want to give the user the option to either upload their own dataset or choose from sample datasets.  
   - This required me to code multiple paths through the app depending on whether the user selects a built‑in dataset or imports their own.

3) I want to help the user understand what the unsupervised learning model is doing.  
   - I include visualizations such as PCA scatter plots, cluster assignments, elbow curves, and silhouette scores, along with explanations of what these values mean and how to interpret them.


## Process
- I began by figuring out how to allow users to upload their own data as well as pick a dataset to as a sample.  
- Next, I organized the app into tabs so the user can move step‑by‑step through the workflow.  
- Starting with tuning and hyperameter selection as the current tab, this allows the user to make their edits and determine the focus of their unsupervised learning model before seeing the calculations. 
- I made sure to include in the tab information about the raw data and to allow the user to utilize missing data.  
- 
- I added comments and explanations throughout the app to help the user understand what each graph and metric represents and what patterns they should expect to see.

---

## How to Use the App
When you click **[here](https://bustillo-data-science-portfolio-hzbraez8mlwqqbefvofgds.streamlit.app/)**, it should take you to the app. Once inside the app, there are three main steps:

1) **Upload or Select a Dataset**  
2) **Apply Unsupervised Learning Algorithms**  
3) **Visualize and Interpret Results**

You can also click **[here](https://github.com/cbustil2/bustillo-data-science-portfolio/blob/main/MLUnsupervisedApp/MLUnsupervisedStreamlit.py)** to view the full code used to build the app. Running the script locally avoids the deployment issues.

---

## Notes and Considerations

### Applications and Code
Some applications and libraries used include:

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=seaborn&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)


### Sample Datasets
I selected only one sample datasets that works well for unsupervised learning: **Mall Customer Segmentation Dataset** — ideal for K‑means clustering because it contains clear numeric features like income, spending score, and age. Click [here](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) to look into the Kaggle dataset. 

### Assistance
I based much of the layout on my previous app, supervised machine learnign. When I encountered errors—especially during deployment and while integrating PCA and clustering—I used Copilot to debug and refine my code.
