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



RUN conda install altair_saver==0.5.0 \
    altair_viewer \
    vega_datasets \
    statsmodels==0.13.1 \
    tabulate==0.8.9 \
    click \
    requests \
    selenium \
    pillow \
    ipython==8.0.1 \
    jupyter \
    pyyaml
