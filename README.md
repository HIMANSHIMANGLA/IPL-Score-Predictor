# IPL Score Predictor

## Project Overview

This IPL Score Predictor is a machine learning model designed to predict the first-inning score of an IPL (Indian Premier League) match based on various features such as team, overs, runs, wickets, and more. The project leverages multiple regression models and deploys the best-performing model using Streamlit, allowing users to input match details and predict the total score.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Feature Engineering](#feature-engineering)
- [Algorithms Used](#algorithms-used)
- [Model Evaluation](#model-evaluation)
- [Streamlit Application](#streamlit-application)
- [Installation](#installation)
- [Usage](#usage)

## Dataset

The dataset contains ball-by-ball data from IPL previous matches. It includes key features necessary for predicting the first-inning score:

### Features:
- `mid`: Match ID
- `date`: Date when the match was played
- `venue`: Venue of the match
- `bat_team`: Batting team
- `bowl_team`: Bowling team
- `batsman`: Batsman on strike
- `bowler`: Bowler
- `runs`: Runs scored on the ball
- `wickets`: Wickets fallen so far
- `overs`: Overs completed
- `runs_last_5`: Runs scored in the last 5 overs
- `wickets_last_5`: Wickets fallen in the last 5 overs
- `striker`: Batsman facing the ball
- `non-striker`: Partner batsman
- `total`: Total runs scored (target variable)

### Data Preprocessing:
- Dropped irrelevant columns like `mid`, `date`, `venue`, `batsman`, `bowler`, `striker`, and `non-striker`.
- Kept consistent teams: 
  - Kolkata Knight Riders, Chennai Super Kings, Rajasthan Royals, Mumbai Indians, Kings XI Punjab, Royal Challengers Bangalore, Delhi Daredevils, Sunrisers Hyderabad.
- Removed data from the first 5 overs as they tend to be volatile and less predictive.

## Feature Engineering

- **One-Hot Encoding**: Applied on categorical features such as `bat_team` and `bowl_team` to convert them into numerical format.
- **Label Encoding**: Used for encoding team names into numerical values.
- **Correlation Analysis**: Performed to understand relationships between numerical features and the target variable (`total`).

## Algorithms Used

The following machine learning algorithms were trained and evaluated for predicting the IPL score:

1. **Linear Regression**
2. **K-Nearest Neighbors (KNN)**
3. **XGBoost Regressor**
4. **RandomForest Regressor**
5. **Support Vector Regression (SVR)**
6. **Decision Tree Regressor**

## Model Evaluation

Each algorithm was evaluated using the following metrics:

- **Mean Absolute Error (MAE)**: Measures average magnitude of errors.
- **Mean Squared Error (MSE)**: Measures the average squared difference between actual and predicted values.
- **Root Mean Squared Error (RMSE)**: The square root of the MSE, providing error in the same units as the target variable.
- **R-squared Score**: Measures the percentage of variance in the dependent variable explained by the model.

### Results:

From the evaluations, the **Random Forest Regressor** emerged as the best-performing model, closely followed by **Decision Tree** and **KNN**. Therefore, the final model selected for deployment was RandomForest.

## Streamlit Application

The web application was developed using Streamlit, which allows users to input match details (teams, overs, runs, etc.) and generate score predictions using the trained model.

### Key Features:
- User-friendly interface.
- Input options for batting and bowling teams, current runs, wickets, overs, runs, and wickets in the last 5 overs.
- Display of the predicted score based on current inputs.


## Installation

To run the project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/HIMANSHIMANGLA/IPL-Score-Predictor.git
   cd IPL-Score-Predictor
   ```

2. **Install the Required Dependencies:**
   Make sure you have Python 3.x installed. Install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Application:**
   ```bash
   streamlit run app.py
   ```

## Usage

Once the Streamlit app is running, you can input match information such as the batting team, bowling team, current runs, wickets, overs, and statistics from the last 5 overs to predict the final score.
