# 🚀 Applied Data Science Capstone


## 📄 Project Background

SpaceX is a leading company in the commercial space industry, known for making space travel more affordable. The Falcon 9 rocket launches are advertised at a cost of $62 million, compared to other providers whose costs exceed $165 million. This cost difference is largely due to SpaceX's ability to reuse the first stage of the rocket. This project aims to predict whether the first stage of Falcon 9 will land successfully based on various factors. By accurately predicting the success of landings, we can better understand and forecast launch costs.

## 📄 Questions to be Answered

1. How do variables such as payload mass, launch site, number of flights, and orbits affect the success of the first stage landing?
2. Does the rate of successful landings increase over the years?
3. What is the best algorithm for binary classification in this context?

## 📄 Methodology

1. **Data Collection:**
   - **Using SpaceX REST API**: Fetch launch data.
   - **Using Web Scraping from Wikipedia**: Extract additional launch information.

2. **Data Wrangling:**
   - **Filtering the Data**: Clean and filter relevant data.
   - **Dealing with Missing Values**: Handle any missing data points.
   - **Using One Hot Encoding**: Prepare data for binary classification.

3. **Exploratory Data Analysis (EDA):**
   - **Visualization**: Use charts and graphs to understand data patterns.
   - **SQL**: Perform data queries for deeper insights.

4. **Interactive Visual Analytics:**
   - **Folium**: Build interactive maps to visualize geographical data.
   - **Plotly Dash**: Create interactive dashboards for data analysis.

5. **Predictive Analysis:**
   - **Building Models**: Develop and train classification models.
   - **Tuning and Evaluation**: Optimize model parameters and evaluate performance.

## 📂 Files

- **DataWrangling.ipynb**: Notebook for data wrangling tasks.
- **Datacollection.ipynb**: Notebook for data collection from SpaceX API and Wikipedia.
- **EDA.ipynb**: Notebook for exploratory data analysis and visualization.
- **Foliummaps.ipynb**: Notebook for creating interactive maps using Folium.
- **MLmodels.ipynb**: Notebook for building, tuning, and evaluating classification models.
- **SpaceX-Dashboard.py**: Python script for generating interactive dashboards with Plotly Dash.
- **dataset_part_1.csv**: CSV file containing part 1 of the dataset.
- **dataset_part_2.csv**: CSV file containing part 2 of the dataset.
- **dataset_part_3.csv**: CSV file containing part 3 of the dataset.
- **my_data1.db**: SQLite database file with additional data.
- **spacex_launch_dash.csv**: CSV file with SpaceX launch data for dashboard.
- **spacex_web_scraped.csv**: CSV file with SpaceX launch data scraped from Wikipedia.

## 🛠 Tools and Technologies

- **Python**: Programming language used for data analysis and modeling.
- **Pandas**: Data manipulation and analysis library.
- **NumPy**: Numerical computing library.
- **Matplotlib & Seaborn**: Data visualization libraries.
- **SQL**: Database querying language.
- **Folium**: Library for creating interactive maps.
- **Plotly Dash**: Framework for building interactive web dashboards.
- **Scikit-learn**: Machine learning library for model building and evaluation.
