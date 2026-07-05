Customer Churn Prediction & Lifetime Value (LTV) Engine
Project Overview

Customer retention is one of the biggest challenges faced by subscription-based businesses. This project focuses on building an end-to-end machine learning solution that predicts customer churn and estimates Customer Lifetime Value (LTV). By combining predictive analytics with customer segmentation, the project helps identify customers who are likely to leave, understand the factors influencing churn, and estimate each customer's long-term value. These insights can support businesses in designing targeted retention strategies, improving customer satisfaction, and maximizing revenue.

Week 1 Completed ✅
Overview

The first week focused on understanding the dataset and preparing it for analysis. Before building any machine learning models, it was important to ensure that the data was clean, reliable, and well-structured. This phase also involved exploring customer behavior through visualizations and identifying meaningful business patterns.

Work Completed
Data Exploration
Loaded the customer churn dataset.
Examined the dataset structure, feature names, and data types.
Reviewed summary statistics to understand the distribution of variables.
Data Cleaning
Checked for missing values and handled them appropriately.
Removed duplicate records.
Corrected inconsistencies in the dataset where necessary.
Exploratory Data Analysis (EDA)
Analyzed customer demographics and service-related information.
Studied churn distribution across different customer groups.
Explored relationships between important variables using charts and visualizations.
Identified trends that may contribute to customer churn.
Outlier Analysis
Detected outliers using statistical methods and visual inspection.
Evaluated whether outliers required treatment before modeling.
Business Insights

Some early observations from the data included:

Customers with shorter tenure showed a higher tendency to churn.
Higher monthly charges were often associated with increased churn.
Contract type and payment method appeared to influence customer retention.
Long-term customers generally contributed higher business value.
Skills Applied
Data Cleaning
Data Preprocessing
Exploratory Data Analysis (EDA)
Data Visualization
Statistical Analysis
Business Understanding
Outcome

By the end of Week 1, the raw dataset had been transformed into a clean and structured dataset ready for machine learning. The exploratory analysis also provided valuable insights that guided the next stages of the project.

Status: Week 1 Successfully Completed ✅

Week 2 Completed ✅
Overview

The second week focused on preparing the cleaned dataset for machine learning and developing predictive models. In addition to churn prediction, Customer Lifetime Value (LTV) was calculated to better understand customer profitability and support business decision-making.

Work Completed
Data Preprocessing
Encoded categorical features into numerical values.
Applied feature scaling to numerical variables.
Verified data quality before model training.
Feature Engineering
Created additional business-related features.
Generated customer categories based on tenure and revenue.
Prepared the final feature set for machine learning.
Model Development

Developed and compared multiple machine learning models:

Logistic Regression
Decision Tree Classifier
Random Forest Classifier

Each model was evaluated using:

Accuracy Score
Classification Report
Confusion Matrix
ROC-AUC Score
Feature Importance
Identified the most influential features contributing to customer churn.
Visualized feature importance to improve business understanding.
Customer Lifetime Value (LTV)
Calculated Customer Lifetime Value using tenure and monthly charges.
Analyzed the distribution of customer value.
Segmented customers into:
Bronze
Silver
Gold
Platinum
Customer Segmentation
Grouped customers based on their lifetime value.
Identified high-value customers requiring focused retention strategies.
Skills Applied
Data Preprocessing
Feature Engineering
Machine Learning
Classification Modeling
Model Evaluation
Customer Segmentation
Business Analytics
Outcome

Week 2 transformed the cleaned dataset into a predictive analytics solution capable of estimating customer churn and customer lifetime value. The models and customer segments provide practical insights that businesses can use to improve customer retention and profitability.

Status: Week 2 Successfully Completed ✅

Week 3 Completed ✅
Overview

The third week focused on deploying the machine learning model by developing a REST API using FastAPI. This phase transformed the trained model into a deployable application capable of serving churn predictions for both individual customers and multiple customer records.

Work Completed
Model Serialization
Saved the trained machine learning model using Pickle.
Stored the feature column order required during prediction.
Generated reusable model files for deployment.
API Development

Developed a REST API using FastAPI with the following endpoints:

Home endpoint to verify API status.
Single customer prediction endpoint.
Batch prediction endpoint for multiple customer records.
Prediction Pipeline
Loaded the trained model automatically during API startup.
Validated incoming customer data.
Ensured input features matched the training feature order.
Returned predictions in JSON format.
API Testing
Tested all endpoints using Swagger UI.
Verified both single and batch prediction functionality.
Confirmed prediction accuracy using sample customer records.
Project Deployment Preparation
Organized the project into reusable files.
Included notebooks, model files, API code, and documentation.
Uploaded project files to GitHub for version control and collaboration.
Skills Applied
FastAPI
REST API Development
Machine Learning Deployment
JSON Handling
API Testing
Pickle
Git
GitHub
Python
Outcome

Week 3 successfully transformed the machine learning model into a deployable REST API capable of serving churn predictions in real time. This makes the predictive model easier to integrate with future applications and dashboards.

Status: Week 3 Successfully Completed ✅

Week 4 Completed ✅
Overview

The fourth and final week focused on building an interactive Power BI dashboard to visualize customer churn patterns, Customer Lifetime Value (LTV), and key business metrics. The dashboard transforms the machine learning outputs into an easy-to-understand analytical solution that enables business users to monitor customer behavior and make data-driven decisions.

Work Completed
Dashboard Design
Designed a professional multi-page Power BI dashboard.
Applied a consistent Emerald Odyssey theme across all report pages.
Added interactive slicers for dynamic data filtering.
Executive Overview Dashboard
Displayed key performance indicators (KPIs) including:
Total Customers
Churn Rate
Retention Rate
Average Monthly Charges
Average Tenure
Visualized customer distribution by:
Gender
Contract Type
Internet Service
Payment Method
Customer Demographics & Churn Analysis
Analyzed churn across different customer demographics.
Compared churn based on:
Senior Citizen status
Partner status
Dependents
Contract Type
Payment Method
Highlighted customer segments with higher churn risk.
Service Usage & Customer Behavior Analysis
Examined churn trends based on subscribed services.
Analyzed service adoption including:
Online Security
Online Backup
Device Protection
Tech Support
Streaming TV
Streaming Movies
Created tenure-based customer distribution analysis.
Built scatter plot visualizations to study the relationship between Monthly Charges and Total Charges.
Customer Lifetime Value (LTV) Dashboard
Visualized Customer Lifetime Value distribution.
Displayed customer segmentation into:
Bronze
Silver
Gold
Platinum
Compared churn across tenure groups.
Identified high-value customers with high churn risk.
Highlighted business opportunities for customer retention.
Dashboard Features
Interactive filtering using slicers.
Cross-filtering between visuals.
Dynamic KPI cards.
Clean and business-friendly report layout.
Consistent color palette and formatting.
Insight-driven visualizations for decision-making.
Skills Applied
Power BI
Data Visualization
Dashboard Design
DAX
Business Intelligence
KPI Development
Interactive Reporting
Data Storytelling
Outcome

Week 4 successfully transformed the predictive analytics solution into a fully interactive business intelligence dashboard. The completed dashboard enables stakeholders to explore churn trends, customer value, service usage, and business performance through intuitive visualizations, making the machine learning insights more accessible and actionable.

Status: Week 4 Successfully Completed ✅

Project Progress

Over the four weeks, this project has evolved from raw customer data into a complete end-to-end customer analytics solution.

Progress So Far
Data cleaning and preprocessing
Exploratory Data Analysis (EDA)
Feature engineering
Customer churn prediction
Customer Lifetime Value (LTV) estimation
Customer segmentation
Machine learning model evaluation
FastAPI REST API development
Model deployment preparation
Interactive Power BI dashboard development
Business Intelligence reporting
Git and GitHub version control

The completed project can now predict customer churn, estimate Customer Lifetime Value (LTV), expose predictions through a FastAPI REST API, and present business insights through an interactive Power BI dashboard. Together, these components provide a comprehensive analytics solution that supports customer retention strategies and informed business decision-making.

Final Project Deliverables
Cleaned and preprocessed customer dataset
Exploratory Data Analysis (EDA)
Feature-engineered dataset
Customer churn prediction models
Customer Lifetime Value (LTV) estimation
Customer segmentation
Model evaluation reports
FastAPI REST API
Interactive Power BI Dashboard
GitHub repository with complete project files and documentation
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
FastAPI
Uvicorn
Pickle
Power BI
DAX
Jupyter Notebook
Git
GitHub
Project Status

Current Status: ✅ Project Successfully Completed
