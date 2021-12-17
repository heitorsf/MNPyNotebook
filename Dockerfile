FROM dmiyamoto/neuron:jupyter
MAINTAINER DeboraMatoso
WORKDIR /work
USER root

COPY jupyter_notebook_config.py /etc/jupyter/
COPY Notebook_run/* /work/Notebook_run/
COPY requirements.txt /work/config/
COPY runtime.txt /work/

EXPOSE 8888
USER neuron
CMD python -m jupyter notebook
