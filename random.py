import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {'percentage': [85, 78, 92, 87, 80, 95, 88, 75, 89, 82],
        'educational_resources': ['good', 'satisfactory', 'poor', 'good', 'satisfactory', 'good', 'satisfactory', 'poor', 'good', 'satisfactory'],
        'parents_education': ['graduate', 'undergraduate', 'PhD', 'graduate', 'undergraduate', 'PhD', 'graduate', 'undergraduate', 'graduate', 'undergraduate'],
        'personality': ['extroverted', 'ambiverted', 'introverted', 'extroverted', 'ambiverted', 'introverted', 'extroverted', 'ambiverted', 'extroverted', 'introverted'],
        'passion': ['yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes'],
        'ott_time': [2, 1.5, 3, 2, 2.5, 3.5, 2, 1.5, 3, 2],
        'sm_time': [1, 1.5, 0.5, 1, 1, 0.5, 1, 1.8, 0.7, 1.2],
        'travel_time': [0.5, 1, 0.3, 0.8, 0.5, 0.2, 1, 0.7, 0.5, 0.6],
        'eduvids_time': [3, 2.5, 2, 2.5, 2, 2, 2.5, 3, 2.5, 2],
        'game_time': [1, 1.5, 0.5, 1, 1, 0.2, 1, 1, 0.8, 1],
        'extra_time': [2, 1, 3, 2, 1, 4, 1.5, 0.5, 2, 1],
        'ai_usage': ['regular', 'occasional', 'never', 'occasional', 'regular', 'regular', 'occasional', 'occasional', 'regular', 'occasional']}

df = pd.DataFrame(data)

# Label encoding for categorical variables
label_encoder = LabelEncoder()
df['educational_resources'] = label_encoder.fit_transform(df['educational_resources'])
df['parents_education'] = label_encoder.fit_transform(df['parents_education'])
df['personality'] = label_encoder.fit_transform(df['personality'])
df['passion'] = label_encoder.fit_transform(df['passion'])
df['ai_usage'] = label_encoder.fit_transform(df['ai_usage'])

# Define features and target variable
features = ['percentage', 'educational_resources', 'parents_education', 'personality', 'passion', 'ott_time', 'sm_time', 'travel_time', 'eduvids_time', 'game_time', 'extra_time', 'ai_usage']
target = 'future_marks'

# Extract features and target variable
X = df[features]
y = df[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
