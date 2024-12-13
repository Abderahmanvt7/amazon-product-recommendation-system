from sklearn.preprocessing import MultiLabelBinarizer

def transform_transactions(cleaned_data):
    user_transactions = cleaned_data.groupby('UserId')['ProductId'].apply(list)
    mlb = MultiLabelBinarizer()
    binary_matrix = pd.DataFrame(
        mlb.fit_transform(user_transactions),
        index=user_transactions.index,
        columns=mlb.classes_
    )
    return binary_matrix
