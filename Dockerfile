FROM continuumio/anaconda3

RUN conda config --add channels conda-forge && \
    conda config --add channels anaconda && \
    conda config --add channels defaults


RUN conda install python==3.11

RUN conda install statsmodels==0.14.1

RUN conda install seaborn==0.13.2

RUN conda install pandas=2.2.0

RUN conda install numpy=1.26.4

RUN conda install altair=5.2.0

RUN conda install imbalanced-learn=0.12.0

RUN conda install matplotlib=3.8.3

RUN conda install scikit-learn=1.4.1.post1


RUN conda install statsmodels==0.14.1

RUN conda install tabulate==0.8.9
RUN conda install click==8.1.7
RUN conda install pillow==10.2.0
RUN conda install ipython==8.20.0
RUN conda install make==4.2.1
RUN conda install altair_saver=0.1.0

# RUN conda install jupyter

