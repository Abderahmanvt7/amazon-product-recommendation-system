# Amazon Product Recommendation System

This project builds a recommendation system using the Apriori algorithm on the Amazon Fine Food Reviews dataset.

## Features

- Data cleaning and preparation
- Association rule mining
- Product recommendations

## Project Structure

    ```plaintext
    amazon-product-recommendation-system/
    │
    ├── data/                 # For storing sample data
    ├── notebooks/            # Colab notebooks
    ├── src/                  # Main Python scripts
    │   ├── data_prep.py      # Data preparation script
    │   ├── transformation.py # Transformation and transaction encoding
    │   ├── apriori_rules.py  # Association rule generation
    │   ├── recommend.py      # Recommendation functions
    │
    ├── README.md             # Project overview and details
    ├── requirements.txt      # Python dependencies
    ├── LICENSE               # License file
    └── .gitignore            # Files to ignore in Git
    ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abderahmanvt7/amazon-product-recommendation-system.git
   cd amazon-product-recommendation-system
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Prepare the dataset: Place the dataset in the data/ folder or update the file path in data_prep.py.

2. Run the scripts in order:

   - data_prep.py for data cleaning.
   - transformation.py for transaction encoding.
   - apriori_rules.py to generate rules.
   - recommend.py for recommendations.

3. Example:
   ```python
   from recommend import recommend
   recommendations = recommend("B002QWHJOU", rules)
   print(recommendations)
   ```

## Results

- Association rule metrics visualized.
- Recommendations for individual products.

## Dataset

[Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)

## Contributing

Contributions to improve the Arabic Sign Language Detector are welcome. Please feel free to submit pull requests or open issues to discuss potential enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have suggestions:

1. Check the [Issues](https://github.com/Abderahmanvt7/amazon-product-recommendation-system/issues) page
2. Create a new issue if needed
3. Contact the maintainers

---

This project is part of an ongoing effort to make technology more accessible and to bridge communication gaps. We hope it serves as a stepping stone towards more comprehensive sign language interpretation systems.

---

Made with ❤️ by [Abderahman HAMILI](https://abderahmanhamili.vercel.app/)
