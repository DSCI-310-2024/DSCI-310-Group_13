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

RUN conda install tabulate==0.9.0

RUN conda install click==8.1.7

RUN conda install pillow==10.2.0

RUN conda install ipython==8.20.0

RUN conda install make==4.2.1

RUN conda install vl-convert-python==1.3.0

# RUN pip3 install quarto==0.1.0

USER root

RUN apt update -y

RUN apt install sudo -y

RUN apt install gdebi -y

# RUN sudo -S \ apt-get install -y \ make \ gdebi

RUN sudo dpkg --add-architecture arm64


ARG QUARTO_VERSION="1.4.537"
RUN curl -o quarto-1.4.551-linux-arm64.deb -L https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.551/quarto-1.4.551-linux-arm64.deb

RUN gdebi --non-interactive quarto-1.4.551-linux-arm64.deb

RUN apt install -y perl

# RUN tlmgr update --self

RUN wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh

# RUN conda install jupyter

