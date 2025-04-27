# Egyptian Apartment Price Prediction AI

![Real Estate Prediction](https://img.shields.io/badge/Python-3.8%2B-blue) 
![Scikit-Learn](https://img.shields.io/badge/ML-XGBoost%20%7C%20RandomForest-orange) 
![Data](https://img.shields.io/badge/Data-50K%2B%20listings-brightgreen)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-yellowgreen)

An end-to-end machine learning system that predicts apartment prices in Egypt with **80%+ accuracy**, functioning as an AI-powered real estate broker.

## 🔍 Project Overview

**Objective:** Build an AI model to predict apartment prices based on:
- Location (City/District)
- Property features (Area, Rooms, Bathrooms)
- Amenities (Furnishing, Finishing status)
- Special features (Compound, sea view, etc.)

**Data Pipeline:**
1. **Web Scraping**: Collected 50K+ listings using `BeautifulSoup` and `Selenium`
2. **ETL**: Processed raw data via SSIS packages into SQL Server  
   ![ETL Package](https://github.com/HossamElsrah/AI-NeuroRealtor/blob/main/Project%20Photos/Etl%20Package.png)
3. **Feature Engineering**: Extracted 10+ key features from Arabic text descriptions
4. **Modeling**: Optimized XGBoost achieves **R²=0.80** on test data
5. **Deployment**: Production-ready API built with FastAPI

## 📊 Data Analysis Dashboard
![Analysis Dashboard](https://github.com/HossamElsrah/AI_NeuroRealtor/blob/main/Project%20Photos/Analysis%20Dashboard.png)

## 🖥️ Web Interface
The user-friendly frontend allows seamless interaction with the AI model:
![Web Interface](https://github.com/HossamElsrah/AI_NeuroRealtor/blob/main/Project%20Photos/Web%20Site.png)

## 🛠️ Technical Stack

### Data Collection
- **Tools**: BeautifulSoup, Selenium
- **Data Volume**: 50,000+ listings
- **Storage**: SQL Server (ETL via SSIS)

### Machine Learning
```python
Core Libraries:
- pandas, numpy (Data processing)
- scikit-learn (Preprocessing/Modeling)
- xgboost (Final model)
- pyodbc (SQL connectivity)

ML Pipeline:
1. Advanced feature extraction from Arabic text
2. Custom outlier detection (5th-95th percentile bounds)
3. Hybrid encoding (OneHot + BinaryEncoder)
4. Ensemble modeling (XGBoost + RandomForest)
```

### Deployment
- **API**: FastAPI (`POST /predict`)
- **Web Interface**: HTML/CSS/JS
- **Model Serving**: Joblib serialization

## 📊 Key Insights

### Data Analysis Highlights
1. **Price Distribution**: 
   - 68% of apartments priced between 1M-11M EGP
   - Strong right skew (log transformation applied)

2. **Top Premium Areas**:
   - Season Resort (Avg: 15M EGP)
   - Marassi (Avg: 12M EGP) 
   - Katameya Coast (Avg: 10M EGP)

3. **Feature Impact**:
   ```markdown
   | Feature       | Price Increase |
   |---------------|----------------|
   | Furnished     | +18%           |
   | Sea View      | +32%           |
   | Compound      | +25%           |
   ```

## 🚀 How It Works

### Prediction API
```python
# Sample Request
curl -X POST "http://api/predict" \
-H "Content-Type: application/json" \
-d '{
    "Area": 150,
    "Rooms": 3,
    "City": "القاهرة",
    "District": "التجمع الخامس"
}'

# Response
{
    "predicted_price": "4,250,000 EGP",
    "confidence": "82%"
}
```

### Model Performance
| Model          | Train R² | Test R² | RMSE    |
|----------------|----------|---------|---------|
| XGBoost        | 0.97     | 0.80    | 0.38    |
| RandomForest   | 0.95     | 0.78    | 0.42    |
| KNN            | 0.88     | 0.72    | 0.51    |

## 📂 Repository Structure
```
├── api/
│   ├── app.py               # FastAPI endpoints
│   └── ml_model/            # Serialized models
├── notebooks/
│   └── Analysis.ipynb       # EDA & modeling
├── web/                     # Frontend interface
└── README.md
```

## 🏗️ Development Steps

1. **Data Collection**
   - Built scraping scripts for major Egyptian real estate sites
   - Automated data validation checks

2. **ETL Process**
   - SSIS packages for:
     - Data cleaning
     - Geocoding locations
     - Loading to SQL Server

3. **Feature Engineering**
   - Arabic NLP techniques for:
     - Furnishing detection (`مفروشة|أثاث`)
     - Compound identification (`كمبوند`)
     - View extraction (`واجهة|إطلالة`)

4. **Model Optimization**
   - Hyperparameter-tuned XGBoost:
     ```python
     XGBRegressor(
         n_estimators=350,
         max_depth=20,
         learning_rate=0.1
     )
     ```

5. **Deployment**
   - API endpoint with input validation
   - Error handling for Arabic text inputs
   - Mobile-responsive web interface

## 💡 Business Value

- **For Buyers**: Instant price estimates
- **For Agents**: Market trend analysis
- **For Developers**: Demand forecasting

## 👨‍💻 Contact
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/hossam-taha-41b724288)
