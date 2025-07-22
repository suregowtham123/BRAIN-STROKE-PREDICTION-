import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset with tab delimiter
data = pd.read_csv('brain_stroke.csv', delimiter='\t')

# Clean up column names (strip any extra spaces)
data.columns = data.columns.str.strip()

# Separate features and target
X = data.drop(columns=['stroke'])  # Features
y = data['stroke']  # Target

# Handle categorical columns using Label Encoding
label_encoder = LabelEncoder()
for col in X.select_dtypes(include=['object']).columns:
    X[col] = label_encoder.fit_transform(X[col])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model using RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'model.pkl')

# Print model accuracy (optional)
accuracy = model.score(X_test, y_test)
print(f'Model Accuracy: {accuracy * 100:.2f}%')
