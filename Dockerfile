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



