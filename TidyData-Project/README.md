# [Tidy Data Project](https://github.com/cbustil2/Bustillo-Data-Science-Portfolio/blob/main/TidyData-Project/tidying_rd_budget.ipynb)

In this project, I am working on the process of tidying and analyzing data from a dataset. I have decided to look into the data from the Federal R&D Budgets. In the data, you can find the federal research budgets by department, year, research & development dollars (rd_budget), total discretionary federal government spending (discretionary_outlays), and total U.S. Gross Domestic Product. (ref. [jonthegeek](https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-02-12))

## Terminology Guide

| Abbreviation  | Department    | Description                                                |
|---------------|---------------|------------------------------------------------------------|
| DOD           | Department of Defense | Responsible for national security, providing military forces to deter war, and protecting national interests |
| NASA          | National Aeronautics and Space Administration | Responsible for the nation's civilian space program, aeronautics research, and space exploration. |
| DOE           | Department of Energy | Ensures America’s security and prosperity by addressing energy, environmental, and nuclear challenges through transformative science and technology | 
| HHS           | Department of Health and Human Services | Responsible for protecting the health of Americans and providing essential human services |
| NIH           | National Institute of Health | Responsible for biomedical and health-related research, aimed at improving health, lengthening life, and reducing illness |
| NSF           | National Science Foundation | Supports fundamental research and education in all non-medical fields of science and engineering |
| USDA          | US Department of Agriculture | Responsible for developing policy on farming, agriculture, forestry, and food |
| Interior      | Department of Interior | Manages and conserves most federal land, natural resources, and cultural heritage |
| DOT           | Deparment of Transportation | ensures a safe, efficient, and modern national transportation system covering aviation, highways, rail, and transit |
| DHS           | Department of Homeland Security | Protects the United States from threats, including terrorism, cyberattacks, and natural disasters, while managing borders, immigration, and maritime security |
| VA            | Department of Veterans Affairs | Provides comprehensive services to military veterans and their dependents, including healthcare, disability compensation, education assistance (GI Bill), home loan guarantees, and burial benefits |
| Other         | other research and development spending |                                                              |

*all descriptions found by Google Gemini*

## Cleaning and Analyzing Data
Since the data is quite simple and provides me the rd_budget, melting the data wasn't too difficult. However one major problem I faced was dealing with the how the columns were named.
There wasn't too many missing values with the exception of the DHS, which wasn't created until 2002. 
To see more of the step by step process of the project, follow my [code](https://github.com/cbustil2/Bustillo-Data-Science-Portfolio/blob/main/TidyData-Project/tidying_rd_budget.ipynb)
Much of the code that I used was gudied by the [Pandas Cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## General Outline:
1) Identify any missing values
2) Assess how to melt the columns and understand what are the given variables
3) Melt and split() to visualize the cleaned data (Both with and without NaN values)
4) Create a aggregate table using pivot()

## Skills and Tools learned:

In this project, I learned how to melt data, tidy datasets, make pivot tables, and analyze the information given. I practiced using pandas and seaborn as a way to help me tidy data. Below are the programs I used  

<div align="center" style="display: flex; justify-content: center; gap: 30px; margin: 30px 0; flex-wrap: wrap;">
  <img src="https://www.python.org/static/community_logos/python-logo.png" width="80" alt="Python">
  <img src="https://pandas.pydata.org/static/img/pandas.svg" width="80" alt="Pandas">
  <img src="https://seaborn.pydata.org/_images/logo-wide-lightbg.svg" width="100" alt="Seaborn">
</div>

