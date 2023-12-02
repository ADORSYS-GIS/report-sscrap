from sklearn.cluster import KMeans

def analyze_data(data):
    if data is not None and 'Data' in data.columns:
        # Calculate average word count and image count
        data['WordCount'] = data['Data'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))
        data['ImageCount'] = data['Data'].apply(count_images)

        # Check if 'WordCount' and 'ImageCount' columns exist in the DataFrame
        if 'WordCount' in data.columns and 'ImageCount' in data.columns:
            average_word_count = data['WordCount'].mean()
            average_image_count = data['ImageCount'].mean()

            return {'average_word_count': average_word_count, 'average_image_count': average_image_count}
        else:
            return None
    else:
        return None


def count_images(text):
    img_tags = re.findall(r'<img[^>]+>', str(text))
    return len(img_tags)


def perform_cluster_analysis(data):
    # Analyze the data
    # TODO Why are we calling analyze_data() here?
    analysis_result = analyze_data(data)

    # Extract relevant features for clustering
    features = data[['WordCount', 'ImageCount']]

    # Check if there are any samples to cluster
    if not features.empty:
        # Use K-Means clustering
        kmeans = KMeans(n_clusters=3, random_state=42)  
        data['Cluster'] = kmeans.fit_predict(features)

        return data[['Data', 'Cluster']]
    else:
        # Handle the case when there are no samples to cluster
        return None

