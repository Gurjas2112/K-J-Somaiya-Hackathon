import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle

data = pd.read_csv("C:/Users/Admin/OneDrive/Desktop/3rd Year Project/performance.csv")
df=pd.DataFrame(data)

print(df)

df.isnull().sum()

null_values=df.isnull()
print(null_values)

total_null_values=df.isnull().sum()
print(total_null_values)

# Map educational_resources values to numerical representations
# convert categorical variable to numerical
df['passion'] = df['passion'].apply(lambda x: 1 if x =='yes' else 0)
print(df)

df.columns

df.info()

df['percentage']=df['percentage'].astype(int)

mapping_dict1 = {'good': 1, 'poor': 0.01, 'satisfactory': 0.5}

# Apply the mapping to the DataFrame column
df['educational_resources'] = df['educational_resources'].map(mapping_dict1)

# Apply the mapping to the DataFrame column
mapping_dict2 = {'extroverted': 0.01, 'introverted': 1, 'ambiverted': 0.5}
df['personality'] = df['personality'].map(mapping_dict2)

mapping_dict3 = {'regular': 0.01, 'never': 1, 'occasional': 0.5}

# Apply the mapping to the DataFrame column
df['ai_usage'] = df['ai_usage'].map(mapping_dict3)

# Apply the mapping to the DataFrame column
mapping_dict4 = {'below10': 0.20, '10': 0.22, '12': 0.25, 'undergraduate': 0.5, 'graduate': 0.65, 'PhD': 0.75}
df['parents_education'] = df['parents_education'].map(mapping_dict4)

df['study_time'] = 9-df['ott_time']-df['sm_time']-df['travel_time']+df['eduvids_time']-df['game_time']-df['extra_time']

# Print the modified DataFrame
print(df)
import matplotlib.pyplot as plt
df[  ['percentage', 'educational_resources', 'parents_education', 'passion', 'ai_usage', 'study_time']].hist(bins=30, figsize=(10,12))
import seaborn as sns
# plot pairplot
sns.pairplot(df[  ['percentage', 'educational_resources', 'parents_education', 'passion', 'ai_usage', 'study_time']])
#regplot=regression plotting
plt.figure(figsize = (15, 6))
sns.regplot(x = 'study_time', y = 'percentage', data = df)
plt.show()
df.corr()
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True)
X = df.drop(columns=['percentage'])
y = data['percentage']
X = pd.get_dummies(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.4, random_state=10)

print(X_train.shape)
print(X_test.shape)

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import pickle
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=40)

# Initialize the random forest regressor
rf_model = RandomForestRegressor()

# Define hyperparameters to tune
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Use GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Print the best hyperparameters
best_params = grid_search.best_params_
print(f"Best Hyperparameters: {best_params}")

# Train the model with the best hyperparameters
best_rf_model = RandomForestRegressor(**best_params)
best_rf_model.fit(X_train, y_train)

# Save the trained model to a file using pickle
with open('C:/Users/Admin/OneDrive/Desktop/3rd Year Project/random_forest_model.pkl', 'wb') as model_file:
    pickle.dump(best_rf_model, model_file)

# Load the trained model from the file (for deployment)
with open('C:/Users/Admin/OneDrive/Desktop/3rd Year Project/random_forest_model.pkl', 'rb') as model_file:
    deployed_model = pickle.load(model_file)

# Make predictions on the test set
y_pred = best_rf_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

# Get feature importances from the trained model
feature_importances = best_rf_model.feature_importances_

# Create a DataFrame to display feature importances
feature_importance_df = pd.DataFrame({'Feature': df.drop(columns=['percentage']).columns, 'Importance': feature_importances})

# Sort the DataFrame by importance in descending order
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Plot feature importances
plt.figure(figsize=(12, 8))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title('Feature Importances')
plt.show()

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Visualize the first tree in the random forest (you can choose any tree index)
plt.figure(figsize=(20, 10))
plot_tree(best_rf_model.estimators_[0], feature_names=df.drop(columns=['percentage']).columns, filled=True, rounded=True)
plt.show()
print(y_pred)
# Create a DataFrame
df = pd.DataFrame({'predicted_score': y_pred})
# Save to a CSV file
df.to_csv('performance.csv', index=False)

# Create a DataFrame with the predicted scores
recommendation_df = pd.DataFrame({'predicted_score': y_pred})


# Define a threshold for recommendations
threshold = 80

# Create a new column 'recommendation' based on the threshold
recommendation_df['recommendation'] = recommendation_df['predicted_score'].apply(lambda x: 'High' if x >= threshold else 'Low')

# Display the recommendation DataFrame
print(recommendation_df.head())

# Save the recommendation DataFrame to a new CSV file
recommendation_df.to_csv('performance.csv', index=False)
print("Recommendations saved to 'performance.csv'")






















