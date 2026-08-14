# ==========================================
# NumPy Challenges
# ==========================================
# These challenges simulate real-world AI/ML preprocessing tasks.
# Solutions are provided immediately below each challenge.
# ==========================================

import numpy as np

# ============================================================
# Challenge 1 : Feature Normalization (Min-Max Scaling)
# ============================================================

print("\n========== Challenge 1 ==========")

marks = np.array([45, 62, 78, 90, 55, 71])

# Scale between 0 and 1

normalized = (marks - np.min(marks)) / (np.max(marks) - np.min(marks))

print("Original :", marks)
print("Normalized :", normalized)



# ============================================================
# Challenge 2 : Detect Outliers using IQR
# ============================================================

print("\n========== Challenge 2 ==========")

salary = np.array([30000,32000,31000,29500,30500,31500,120000])

Q1 = np.percentile(salary,25)
Q3 = np.percentile(salary,75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = salary[(salary < lower) | (salary > upper)]

print("Q1 :", Q1)
print("Q3 :", Q3)
print("IQR :", IQR)
print("Outliers :", outliers)



# ============================================================
# Challenge 3 : One-Hot Encoding
# ============================================================

print("\n========== Challenge 3 ==========")

labels = np.array([0,2,1,2,0,1])

one_hot = np.eye(np.max(labels)+1)[labels]

print(one_hot)



# ============================================================
# Challenge 4 : Build Confusion Matrix
# ============================================================

print("\n========== Challenge 4 ==========")

y_true = np.array([0,1,1,0,1,0,1,0,1,1])
y_pred = np.array([0,1,0,0,1,1,1,0,0,1])

TP = np.sum((y_true == 1) & (y_pred == 1))
TN = np.sum((y_true == 0) & (y_pred == 0))
FP = np.sum((y_true == 0) & (y_pred == 1))
FN = np.sum((y_true == 1) & (y_pred == 0))

confusion_matrix = np.array([
    [TN, FP],
    [FN, TP]
])

print(confusion_matrix)



# ============================================================
# Challenge 5 : Linear Regression Forward Pass
# ============================================================

print("\n========== Challenge 5 ==========")

X = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])

W = np.array([0.8,1.4])

b = 2

prediction = np.dot(X,W) + b

print("Predictions :")
print(prediction)



# ============================================================
# Challenge 6 : Cosine Similarity
# ============================================================

print("\n========== Challenge 6 ==========")

vector1 = np.array([1,2,3])
vector2 = np.array([4,5,6])

dot_product = np.dot(vector1,vector2)

magnitude1 = np.linalg.norm(vector1)
magnitude2 = np.linalg.norm(vector2)

cosine_similarity = dot_product / (magnitude1 * magnitude2)

print("Cosine Similarity :", cosine_similarity)



# ============================================================
# Challenge 7 : Pairwise Euclidean Distance
# ============================================================

print("\n========== Challenge 7 ==========")

points = np.array([
    [2,3],
    [5,7],
    [8,1]
])

distance = np.sqrt(
    np.sum(
        (points[:,None,:] - points[None,:,:])**2,
        axis=2
    )
)

print(distance)



# ============================================================
# Challenge 8 : Cricket Batting Analytics
# ============================================================

print("\n========== Challenge 8 ==========")

runs = np.array([4,6,2,1,0,4,1,6,2,4])

total_runs = np.sum(runs)

balls = len(runs)

strike_rate = (total_runs / balls) * 100

boundary_runs = np.sum(runs[(runs == 4) | (runs == 6)])

dot_balls = np.sum(runs == 0)

print("Total Runs :", total_runs)
print("Strike Rate :", strike_rate)
print("Boundary Runs :", boundary_runs)
print("Dot Balls :", dot_balls)



# ============================================================
# Challenge 9 : Feature Standardization (Z-Score)
# ============================================================

print("\n========== Challenge 9 ==========")

height = np.array([165,172,180,175,169,182])

z_score = (height - np.mean(height)) / np.std(height)

print(z_score)



# ============================================================
# Challenge 10 : Monte Carlo Estimation of π
# ============================================================

print("\n========== Challenge 10 ==========")

points = 100000

x = np.random.rand(points)
y = np.random.rand(points)

inside_circle = (x**2 + y**2) <= 1

pi = 4 * np.mean(inside_circle)

print("Estimated π :", pi)