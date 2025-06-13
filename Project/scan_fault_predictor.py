import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report
)

# Load CSV output from SystemVerilog
df = pd.read_csv("scan_results.csv")

print("Data Sample:")
print(df.head(), "\n")

# Features and Labels
features = ["scan_len", "pattern_bit", "fault_pos", "fault_type"]
target = "scan_out"
X = df[features]
y = df[target]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ---- Decision Tree Classifier ----
print("Training Decision Tree...")
dt_model = DecisionTreeClassifier(max_depth=4, random_state=42)
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)

dt_acc = accuracy_score(y_test, dt_preds)
print(f"\nDecision Tree Accuracy: {dt_acc:.4f}")
print("Classification Report:\n", classification_report(y_test, dt_preds))

# Confusion Matrix
cm = confusion_matrix(y_test, dt_preds)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=["0", "1"], yticklabels=["0", "1"])
plt.title("Decision Tree Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# Feature Importances
plt.figure(figsize=(8, 4))
plt.bar(features, dt_model.feature_importances_)
plt.title("Decision Tree Feature Importances")
plt.show()

# ---- Random Forest Classifier ----
print("Training Random Forest...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

rf_acc = accuracy_score(y_test, rf_preds)
print(f"\nRandom Forest Accuracy: {rf_acc:.4f}")
print("Classification Report:\n", classification_report(y_test, rf_preds))

# Confusion Matrix
cm_rf = confusion_matrix(y_test, rf_preds)
plt.figure(figsize=(6, 5))
sns.heatmap(cm_rf, annot=True, fmt='d', cmap="Greens", xticklabels=["0", "1"], yticklabels=["0", "1"])
plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# Feature Importances
importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(8, 4))
plt.bar([features[i] for i in indices], importances[indices])
plt.title("Random Forest Feature Importances")
plt.tight_layout()
plt.show()

# ---- Prediction on New Input ----
new_samples = pd.DataFrame({
    "scan_len": [8, 8],
    "pattern_bit": [1, 0],
    "fault_pos": [3, 3],
    "fault_type": [0, 0]
})

new_predictions = rf_model.predict(new_samples)
print("\nPredictions for new input data:")
for i, pred in enumerate(new_predictions):
    print(f"Sample {i+1}: {'Fault Detected' if pred == 1 else 'No Fault'}")
