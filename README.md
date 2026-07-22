# 📊 Student Performance Prediction using Machine Learning

## 📖 Project Overview

This project aims to predict **student performance** using Machine Learning regression techniques. By analyzing various academic and behavioral factors, the model estimates a student's performance index. The project follows a complete machine learning workflow, including data preprocessing, feature scaling, model training, evaluation, hyperparameter tuning, and prediction on new data.

The primary objective is to build an accurate and reliable regression model that can assist in predicting student performance based on the given input features.

---

# 🎯 Objectives

* Develop a regression model to predict student performance.
* Compare the performance of multiple regression algorithms.
* Improve model accuracy through hyperparameter tuning.
* Evaluate the model using standard regression metrics.
* Demonstrate prediction on unseen data.

---

# 📂 Dataset

The dataset contains student-related attributes that influence academic performance.

### Input Features

* Gender	
* HoursStudied/Week	
* Tutoring	
* Region	
* Attendance(%)	
* Parent Education

### Target Variable

* Performance Index (Predicted Score)

---

# 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Google Colab

---

# 🔄 Project Workflow

### 1. Data Collection

* Load the dataset using Pandas.
* Explore the dataset structure and understand the available features.

### 2. Data Preprocessing

* Check for missing values.
* Remove duplicate records.
* Encode categorical variables if required.
* Separate features and target variable.

### 3. Feature Scaling

* Standardize numerical features using **StandardScaler**.
* Improve model performance by ensuring all features are on a similar scale.

### 4. Train-Test Split

* Split the dataset into training and testing sets.
* Use the training data to build the model and the testing data to evaluate its performance.

### 5. Model Training

The following regression algorithms were trained and compared:

* Decision Tree Regressor
* Random Forest Regressor
* K-Nearest Neighbors (KNN) Regressor

### 6. Model Evaluation

Each model was evaluated using regression metrics:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

The best-performing model was selected based on the highest R² Score and the lowest prediction error.

### 7. Hyperparameter Tuning

To improve model performance, **GridSearchCV** was applied to the selected model.

Hyperparameter tuning helps identify the optimal parameter values, resulting in better prediction accuracy and improved generalization on unseen data.

### 8. Final Model

The optimized model obtained from GridSearchCV was used as the final prediction model.

### 9. Prediction on New Data

The trained model was tested with new student input data to demonstrate its ability to predict unseen observations successfully.

---

# 📈 Evaluation Metrics

The regression model was evaluated using:

* **R² Score** – Measures how well the model explains the variance in the target variable.
* **Mean Absolute Error (MAE)** – Average absolute difference between predicted and actual values.
* **Mean Squared Error (MSE)** – Average squared prediction error.
* **Root Mean Squared Error (RMSE)** – Square root of MSE, expressed in the same units as the target.

---

# 🚀 Key Features

* Complete machine learning workflow
* Multiple regression model comparison
* Feature scaling using StandardScaler
* Hyperparameter tuning with GridSearchCV
* Regression-based performance evaluation
* Prediction on unseen data
* Clean and modular Python implementation

---

# 📁 Project Structure

```text
Student-Performance-Prediction/
│
├── dataset/
│   └── student_performance.csv
│
├── notebooks/
│   └── Student_Performance_Prediction.ipynb
│
├── models/
│   └── trained_model.pkl
│
├── README.md
└── requirements.txt
```

---

# ▶️ How to Run the Project

1. Clone the repository.
2. Install the required Python libraries.
3. Open the Jupyter Notebook or Google Colab notebook.
4. Run all cells in sequence.
5. Train the model.
6. Perform hyperparameter tuning.
7. Evaluate the model.
8. Predict results for new student data.

---

# 📌 Results

After comparing multiple regression algorithms, the best-performing model was selected based on the evaluation metrics. Hyperparameter tuning further improved the model's predictive performance. The final model successfully generated predictions for unseen student data, demonstrating good generalization and reliability.

---

# 🔮 Future Enhancements

* Train on larger and more diverse datasets.
* Perform advanced feature engineering.
* Explore ensemble methods such as XGBoost and LightGBM.
* Deploy the model using Flask, FastAPI, or Streamlit.
* Build a user-friendly web interface for real-time predictions.

---

# 👨‍💻 Author

**Nischay **
