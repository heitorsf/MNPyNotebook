FROM dmiyamoto/neuron:jupyter
MAINTAINER DeboraMatoso
WORKDIR /work
USER root

COPY jupyter_notebook_config.py /etc/jupyter/
COPY Notebook_run/* /work/Notebook_run/
COPY requirements.txt /work/config/

RUN pip install -r config/requirements.txt
RUN cd /work/nrn-7.4/src/nrnpython \
    python setup.py install
RUN chown -R neuron /work
RUN nrnivmodl /work/Notebook_run
RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix

EXPOSE 8888
USER neuron
RUN nrnivmodl Notebook_run/
CMD jupyter notebook
