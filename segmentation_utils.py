# segmentation_utils.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from imblearn.over_sampling import SMOTE
import plotly.express as px
import os

def generate_segmentation_plots():
    # Ensure plots directory exists
    os.makedirs("static/plots", exist_ok=True)

    # Load dataset
    df = pd.read_csv("customer_churn_dataset.csv")
    df = df[:12000]  # optional subset

    # One-hot encode categorical columns
    df = pd.get_dummies(df, columns=['Gender', 'Subscription Type', 'Contract Length'], dtype='int')

    # Features and target
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    # Scaling
    cols_to_scale = X.columns.tolist()
    scaler = MinMaxScaler()
    X[cols_to_scale] = scaler.fit_transform(X[cols_to_scale])

    # Handle imbalance with SMOTE
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)

    # KMeans clustering
    k = 7
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_resampled)

    # Resampled DataFrame
    df_resampled = pd.DataFrame(X_resampled, columns=X.columns)
    df_resampled['Cluster'] = labels

    # PCA for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_resampled)
    df_resampled['PCA1'] = X_pca[:, 0]
    df_resampled['PCA2'] = X_pca[:, 1]

    # Cluster Profiling Heatmap
    cluster_profile = df_resampled.groupby('Cluster').mean()
    plt.figure(figsize=(12,6))
    sns.heatmap(cluster_profile.drop(['PCA1','PCA2'], axis=1), annot=True, cmap="YlGnBu")
    plt.title("Cluster Profiling Heatmap")
    plt.tight_layout()
    plt.savefig("static/plots/cluster_heatmap.png")
    plt.close()

    # PCA Scatter Plot
    fig = px.scatter(
        df_resampled,
        x='PCA1',
        y='PCA2',
        color='Cluster',
        title=f"KMeans Clusters (k={k}) visualized with PCA",
        width=800,
        height=500
    )
    fig.write_html("static/plots/cluster_pca.html", include_plotlyjs='cdn')
