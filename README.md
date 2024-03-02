# DSCI 310 Group Project: Laptop Price Predictor Model

## Authors: Anna Czarnocka, An Zhou, Yuechang Liu, Daniel Lima

## Summary
Our project aims to answer the question "How can we predict determinants of the laptop market price?". We used publically available Kaggle dataset ["Laptop Dataset (2024)"](https://www.kaggle.com/datasets/aniket1505/laptop-dataset-2023). We performed a robust data analysis in Python, spanning from importing data to sharing insights, prioritizing the creation of workflows that are both replicable and reliable. We used classification machine learning method to construct our predictive model. Our results are that the price can be predicted by determinaning its (...).

## How to run our data analysis
To successfully run our data analysis you should follow the following steps:
1. **Environment Setup**: Ensure Python is installed on your system. For installation guidance, refer to Python's official website.
3. **Repository Cloning**: Clone our GitHub repository to your local computer. Use the command: `git clone [[Repository URL](https://github.com/DSCI-310-2024/Laptops--market-prices-detemrinants-prediction.git)]`
4. **Editor Preparation**: Open the project in your preferred IDE, such as Visual Studio Code.
5. **Dependency Installation**: To set up the project environment, install dependencies listed in `environment.yml`. To do this, execute the following command in your terminal: `conda env create -f environment.yml`. Then, activate the created environment with: `conda activate project_env`.
6. **Running the Analysis**: Navigate to the project directory and execute the Jupyter Notebooks or Python scripts to perform our analysis pipeline.

## List of Dependencies
To replicate our analysis environment, ensure the following dependencies are installed:

```yaml
name: project_env
channels:
  - conda-forge
  - defaults
dependencies:
  - altair==5.2.0
  - jupyterlab==4.1.2
  - numpy==1.26.4
  - pandas==2.2.1
  - python==3.12.2
```

## License
This project is licensed under the MIT License.

