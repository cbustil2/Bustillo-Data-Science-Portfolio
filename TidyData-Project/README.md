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
