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
When you click **[here](https://bustillo-data-science-portfolio-hzbraez8mlwqqbefvofgds.streamlit.app/)**, it should take you to the app (Note: deployment may still be unstable, so local use is recommended). Once inside the app, there are three main steps:

1) **Upload or Select a Dataset**  
2) **Apply Unsupervised Learning Algorithms**  
3) **Visualize and Interpret Results**

You can also click **[here](https://github.com/cbustil2/bustillo-data-science-portfolio/blob/main/MLUnsupervisedApp/MLUnsupervisedStreamlit.py)** to view the full code used to build the app. Running the script locally avoids the deployment issues.

---

## Notes and Considerations

### Applications and Code
Some applications and libraries used include:

- Streamlit  
- Python  
- Pandas  
- NumPy  
- Seaborn  
- Scikit‑Learn  

### Sample Datasets
I selected two sample datasets that work well for unsupervised learning:

- **Mall Customer Segmentation Dataset** — ideal for K‑means clustering because it contains clear numeric features like income, spending score, and age.  
- **Wholesale Customers Dataset** — useful for PCA and clustering because it contains multiple spending categories that naturally form groups.

### Assistance
To assist in building the app, I looked at Ahmed Mohammed Sabri’s Streamlit machine learning app, which helped me understand file‑upload workflows and clean UI structure. You can find his work **[here](https://github.com/Amsamms)**.

When I encountered errors—especially during deployment and while integrating PCA and clustering—I used Copilot to debug and refine my code.
