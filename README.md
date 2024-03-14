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

6. **Running the Analysis**: Navigate to the project directory and execute the Jupyter Notebooks or Python scripts to perform our analysis pipeline.

5. **Dependency Installation**: To set up the project environment, install dependencies listed in `Dockerfile`. To do this, execute the following command in your terminal once working in the project directory: 

```console
foo@bar:~$ docker build --tag sample_name .
```
and

```console
foo@bar:~$ docker run -it --rm sample_name
```

Note: Ensure that you change sample_name to a desired name and ensure that when you run the container you include -rm in order for container to be ephemeral.

## List of Dependencies

The project utilizes the following dependencies and their versions as listed in the Dockerfile.

```yaml
FROM quay.io/jupyter/scipy-notebook:2024-02-24

RUN conda config --add channels conda-forge && \
    conda config --add channels anaconda && \
    conda config --add channels defaults

RUN conda install python=3.11

RUN conda install statsmodels==0.14.1

RUN conda install seaborn==0.13.2

RUN conda install pandas=2.2.0

RUN conda install numpy=1.26.4

RUN conda install altair=5.2.0

RUN conda install imbalanced-learn=0.12.0

RUN conda install matplotlib=3.8.3

RUN conda install scikit-learn=1.4.1.post1





```

## License
This project is licensed under the MIT License.

