# Tidy Data Project

In this project, I am working on the process of tidying and analyzing data from a dataset. I have decided to look into the data from the Federal R&D Budgets. In the data, you can find the federal research budgets by department, year, research & development dollars (rd_budget), total discretionary federal government spending (discretionary_outlays), and total U.S. Gross Domestic Product. (ref. [jonthegeek](https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-02-12))

## Terminology Guide

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="border: none;">
    
- DOD - Deparment of Defense
- NASA - National Aeronautics and Space Administration
- DOE - Department of Energy
- HHS - Department of Health and Human Services
- NIH - National Institute of Health
- NSF - National Science Foundation
- USDA - US Department of Agriculture

    </td>
    <td style="border: none;">
    
- Interior - Department of Interior
- DOT - Deparment of Transportation
- EPA - Environmental Protection Agency
- DOC - Department of Corrections
- DHS - Department of Homeland Security
- VA - Department of Veterands Affairs
- Other - other research and development spending

    </td>
  </tr>
</table>

## Cleaning and Analyzing Data
Since the data is quite simple and provides me the rd_budget, melting the data wasn't too difficult. However one major problem I faced was dealing with the how the columns were named.  
