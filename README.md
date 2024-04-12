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
3. **Repository Cloning**: Clone our GitHub repository to your local computer. Use the command: git clone https://github.com/DSCI-310-2024/Group_13-Laptop-market-price-analysis
4. **Editor Preparation**: Open the project in your preferred IDE, such as Visual Studio Code.

6. **Running the Analysis**: Navigate to the project directory and execute the Jupyter Notebooks or Python scripts to perform our analysis pipeline.

5. **Dependency Installation**: To set up the project environment, install dependencies listed in `Dockerfile`. 2. Open the terminal and navigate to the DSCI-310_group-10_crime-prediction directory.

Note: Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running in the background

Run `docker-compose build`, this will create a docker image.

```console
foo@bar:~$ docker-compose build
```

Run `docker-compose run environment` 

```console
foo@bar:~$ docker-compose run environment
```

Necessary files found within the `home/jovyan/work` directory.

To shut down and exit the container use `Ctrl + c`.

## List of Dependencies

The project utilizes the following dependencies and their versions as listed in the Dockerfile.

```yaml
FROM continuumio/anaconda3:2024.02-1

RUN conda config --add channels conda-forge && \
    conda config --add channels anaconda && \
    conda config --add channels defaults

USER root

RUN apt update -y && \
    apt install sudo -y && \
    apt install gdebi -y && \
    sudo dpkg --add-architecture arm64 && \
    curl -o quarto-1.4.551-linux-arm64.deb -L https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.551/quarto-1.4.551-linux-arm64.deb && \
    gdebi --non-interactive quarto-1.4.551-linux-arm64.deb && \
    apt install -y perl && \
    wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh

RUN conda install python==3.11 \
    statsmodels==0.14.1 \
    seaborn==0.13.2 \
    pandas=2.2.0 \
    numpy=1.26.4 \
    altair=5.2.0 \
    imbalanced-learn=0.12.0 \
    matplotlib=3.8.3 \
    scikit-learn=1.4.1.post1 \
    statsmodels==0.14.1 \
    tabulate==0.9.0 \
    click==8.1.7 \
    pillow==10.2.0 \
    ipython==8.20.0 \
    make==4.2.1 \
    vl-convert-python==1.3.0 \
    pytest==8.1.1

```

## License
This project is licensed under the MIT License.

