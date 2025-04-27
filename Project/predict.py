# File: scan_fault_predictor.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

data = {
    "scan_len": [8]*16,
    "pattern_bit": [i & 1 for i in range(16)],
    "fault_pos": [3]*16,
    "fault_type": [0]*16,
    "scan_out": [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],  # simulate response
}

df = pd.DataFrame(data)

# Features & Labels
X = df[["scan_len", "pattern_bit", "fault_pos", "fault_type"]]
y = df["scan_out"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train ML Model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Prediction
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"Accuracy: {acc*100:.2f}%")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Plot feature importances
plt.bar(X.columns, clf.feature_importances_)
plt.title("Feature Importances")
plt.show()
