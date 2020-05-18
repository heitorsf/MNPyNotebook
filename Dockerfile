FROM dmiyamoto/neuron:jupyter
MAINTAINER DeboraMatoso
WORKDIR /work
USER root

COPY jupyter_notebook_config.py /etc/jupyter/
COPY Notebook_run/* /work/Notebook_run/
COPY requirements.txt /work/config/

RUN pip install -r config/requirements.txt
    cd /work/nrn-7.4/src/nrnpython \
    python setup.py install \
    chown -R neuron /work \
    cd /work/Notebook_run \
    nrnivmodl \
    jupyter nbextension enable --py widgetsnbextension --sys-prefix

EXPOSE 8888
USER neuron
CMD jupyter notebook


