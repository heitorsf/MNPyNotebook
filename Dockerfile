FROM dmiyamoto/neuron:jupyter
MAINTAINER DeboraMatoso
WORKDIR /work
ARG NB_USER=neuron
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

USER root

COPY jupyter_notebook_config.py /etc/jupyter/
COPY Notebook_run/* /work/Notebook_run/
COPY requirements.txt /work/config/

RUN pip install -r config/requirements.txt
RUN cd /work/nrn-7.4/src/nrnpython \
    python setup.py install
RUN chown -R neuron /work
RUN cd /work/Notebook_run \ 
    nrnivmodl
RUN pip install --no-cache-dir notebook
RUN pip install --no-cache-dir jupyterhub
RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix

EXPOSE 8888
USER neuron
CMD jupyter notebook
