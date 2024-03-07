<!-- Add banner here -->
![Banner](./header.png)

# Pasig House Prices Prediction

<!-- Add buttons here -->

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ralphcajipe/pasig-house-prices-prediction?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/ralphcajipe/pasig-house-prices-prediction)
![GitHub issues](https://img.shields.io/github/issues-raw/ralphcajipe/pasig-house-prices-prediction)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ralphcajipe/pasig-house-prices-prediction)
![GitHub](https://img.shields.io/github/license/ralphcajipe/pasig-house-prices-prediction)

(Describe project in brief here)


# Quickstart/Demo

(Add a Simple ML video demo for your project here)

<img src="./assets/flask-web-app.jpg" alt="Flask Web App" width="720">


# Table of Contents

- [Project Title](#project-title)
- [Quickstart/Demo](#quickstartdemo)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contribute](#contribute)
- [License](#license)

# Installation
[(Back to top)](#table-of-contents)


To set up the project on your local machine, follow these steps:

1. Clone the repository: 

```shell 
git clone https://github.com/ralphcajipe/pasig-house-prices-prediction.git
```

2. Navigate to the project directory: 
```shell 
cd pasig-house-prices-prediction
```
3. Install the required dependencies: 
```shell
pip install -r requirements.txt
```

# Data Source 

The project uses the following data source:

- [Philippine Real Estate](https://www.kaggle.com/datasets/arloblanco/philippine-real-estate)

The data for this project comes from the `PH_houses_v2.csv` file, which contains information about house prices in the Philippines. The dataset includes the following columns:

- `Description`: A brief description of the house.
- `Location`: The city where the house is located.
- `Price (PHP)`: The price of the house in Philippine Pesos.
- `Bedrooms`: The number of bedrooms in the house.
- `Bath`: The number of bathrooms in the house.
- `Floor_area (sqm)`: The floor area of the house in square meters.
- `Land_area (sqm)`: The land area of the house in square meters.
- `Latitude`: The latitude coordinate of the house.
- `Longitude`: The longitude coordinate of the house.
- `Link`: A link to the online listing of the house.

# Code Structure
[(Back to top)](#table-of-contents) 

The project is organized as follows:

```shell
.
├── data/           - Contains the raw data files.
├── models/         - Contains the trained models.
├── notebooks/      - Contains the Jupyter notebooks.
├── scripts/        - Contains the Python scripts.
├── requirements.txt - Lists the Python dependencies.
└── README.md       - The file that you are currently reading.
```

# Results and Evaluation
[(Back to top)](#table-of-contents)

The project achieves a Root Mean Squared Error (RMSE) of 1162.05 on the training set. The evaluation methodology used is RMSE because the label (Price_PHP) of the model is a numerical column, the model is trained to do regression, and the reported metrics will include such as RMSE. See the jupyter notebook located in the `notebooks` directory for the full details of the evaluation.

# Usage
[(Back to top)](#table-of-contents)

1. (Simple ML Sheets)

2. Run the Flask server (development) using the following command:
   ```bash
   python server.py
   ```
   If you want to run the server in production, you can use the following command:
   ```bash
   waitress-serve --host 127.0.0.1 server:app
   ```


# Contribute
[(Back to top)](#table-of-contents)

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# License
[(Back to top)](#table-of-contents)

[MIT license](./LICENSE)
