# DSCI 310 Group Project: Laptop Price Predictor Model

## Authors: Anna Czarnocka, An Zhou, Yuechang Liu, Daniel Lima

## Summary
Our project aims to address the question "How can we predict determinants of laptop market prices?" Utilizing the publicly available Kaggle dataset ["Laptop Dataset (2024)"](https://www.kaggle.com/datasets/aniket1505/laptop-dataset-2023), we conducted a comprehensive data analysis in Python. Our approach encompassed tasks ranging from data importing to insights sharing, with a focus on establishing replicable and reliable workflows. Employing regression analysis, specifically Ordinary Least Squares (OLS) regression, we explored the relationship between various laptop features and their prices.

The results of our analysis indicate that several laptop features significantly influence prices. These include the laptop's rating, number of cores, number of threads, RAM memory, primary storage capacity, and display resolution. Each of these factors demonstrated a statistically significant impact on laptop prices, as evidenced by their respective coefficients in the regression model.

However, it's important to note that while our model explains a considerable portion (approximately 74.6%) of the variance in laptop prices, the presence of multicollinearity or omitted variable bias cannot be entirely discounted. Further diagnostics may be necessary to thoroughly assess the assumptions and validity of our model.

In conclusion, our study provides valuable insights into the determinants of laptop market prices, offering a foundation for future research and decision-making within the industry.

## How to run our data analysis
To successfully run our data analysis you should follow the following steps:
1. **Environment Setup**: Ensure Python is installed on your system. For installation guidance, refer to Python's official website.
3. **Repository Cloning**: Clone our GitHub repository to your local computer. Use the command: git clone [[Repository URL](https://github.com/DSCI-310-2024/Laptops--market-prices-detemrinants-prediction.git)]
4. **Editor Preparation**: Open the project in your preferred IDE, such as Visual Studio Code.
5. **Dependency Installation**: To set up the project environment, install dependencies listed in `environment.yml`. To do this, execute the following command in your terminal: `conda env create -f environment.yml`. Then, activate the created environment with: `conda activate project_env`.
6. **Running the Analysis**: Navigate to the project directory and execute the Jupyter Notebooks or Python scripts to perform our analysis pipeline.

## List of Dependencies
To replicate our analysis environment, ensure the to build the project container utilizing the following commands:

docker build -t sampleapp:v1

```console
foo@bar:~$ docker build -t Sample_name
```

## License
This project is licensed under the MIT License.

