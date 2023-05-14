import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist
from sklearn.preprocessing import MinMaxScaler

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

data = pd.read_csv('Obesity_Dataset.csv')
print("Dataset Shape:")
print(data.shape, end="\n\n")

print("Dataset Values:")
print(data.head(), end="\n\n")
data = data.drop("NObeyesdad", axis=1)

categorical_columns = ["Gender", "family_history_with_overweight", "FAVC", "CAEC", "SMOKE", "SCC", "CALC", "MTRANS"]
data = pd.get_dummies(data, columns=categorical_columns)

print("Dataset Values after one-hot-encoding:")
print(data.head(), end="\n\n")

print("Dropping rows with missing values...")
data = data.dropna()

print("Scaling the data...")
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

number_of_clusters = 7
fuzzy_param = 2
alpha = 0.001
max_iter = 200

np.random.seed(211)
n_samples = data_scaled.shape[0]
coefficients = np.random.rand(n_samples, number_of_clusters)
coefficients /= coefficients.sum(axis=1, keepdims=True)

for _ in range(max_iter):

    centroids = coefficients.T @ data_scaled / coefficients.sum(axis=0, keepdims=True).T

    distances = cdist(data_scaled, centroids, metric='euclidean')

    fuzzy_mem_val = 1 / (1 + (distances / np.max(distances)) ** (2 / (fuzzy_param - 1)))
    fuzzy_mem_val /= fuzzy_mem_val.sum(axis=1, keepdims=True)

    if np.max(np.abs(fuzzy_mem_val - coefficients)) < alpha:
        break

    coefficients = fuzzy_mem_val

max_belonging_cluster = np.argmax(fuzzy_mem_val, axis=1)

original_data = pd.read_csv('Obesity_Dataset.csv')
weight_type_mapping = {"Insufficient_Weight": 0, "Normal_Weight": 1, "Overweight_Level_I": 2, "Overweight_Level_II": 3,
                       "Obesity_Type_I": 4, "Obesity_Type_II": 5, "Obesity_Type_III": 6}
original_data["NObeyesdad"] = original_data["NObeyesdad"].map(weight_type_mapping)

original_data = original_data.dropna()


def normalize_matrix(matrix):
    row_sums = matrix.sum(axis=1, keepdims=True) + 1e-8
    normalized_matrix = matrix / row_sums
    return normalized_matrix


matrix = np.zeros((number_of_clusters, len(weight_type_mapping)), dtype=int)
for i in range(len(original_data)):
    cluster = max_belonging_cluster[i]
    weight_type = original_data["NObeyesdad"].iloc[i]
    matrix[cluster, weight_type] += 1

weight_type_labels = ["Insufficient Weight", "Normal Weight", "Overweight Level I", "Overweight Level II",
                      "Obesity Type I", "Obesity Type II", "Obesity Type III"]

final_count_mat = pd.DataFrame(matrix, columns=weight_type_labels)
final_count_mat.index.name = "Cluster"
final_count_mat = final_count_mat.reset_index()
print()
print("Final Output:\n", final_count_mat)
