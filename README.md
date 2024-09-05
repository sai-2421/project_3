# project_3
#**Airbnb Data Analysis**

>## Overview

This project focuses on analyzing Airbnb data from 2019, with an emphasis on key aspects of property listings like descriptions, pricing, location, and reviews. The analysis involves transforming raw data into meaningful insights, integrating it with a database for efficient storage and retrieval, and creating interactive visualizations to explore trends and patterns. These visualizations will provide a comprehensive view of the Airbnb market, helping users understand various factors that influence property performance, such as location-based pricing trends, popular listing descriptions, and guest feedback through reviews.

>## Process

Here's the updated summary:

1.**Data Extraction & Preprocessing:**

-Extracted and cleaned the Airbnb 2019 dataset, transforming it into structured DataFrames for analysis.

2.**Database Integration:**

-Integrated the data into MongoDB for efficient storage and management.

3.**Data Visualization:**

-Developed an interactive dashboard using Streamlit.
Leveraged Plotly for dynamic visualizations, providing insightful data exploration and trends.

>## Features:

**Home**: Provides detailed hotel information by country, including pricing, room type, descriptions, and ratings.

**Discover**: Allows users to explore countries with geo-visualizations and price insights, while filtering by property and room type.

**Insight**: Offers both 'Top Insights' for general analysis and 'Filtered Insights' for customized visualizations based on specific criteria.

>## Skills & Tools

- **Skills**: Python, Data Preprocessing, Visualization, Exploratory Data Analysis (EDA), Streamlit, Power BI
- **Tools**:
  - Python 3.12.2
  - MySQL
  - Streamlit
  - Plotly
  - Power BI
 
>## Packages & Libraries

```python
import pymongo
import pandas as pd
import datetime as dt
import scipy.stats as st
from statsmodels.multivariate.manova import MANOVA
import numpy as np
import statistics as s
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image



