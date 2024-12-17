import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv('data/student_data.csv')

# Map grades to numerical values (if categorical)
grade_map = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
df['final_grade'] = df['final_grade'].map(grade_map)

# Split data into features and target
X = df[['attendance', 'assignments', 'test_scores']]
y = df['final_grade']

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
