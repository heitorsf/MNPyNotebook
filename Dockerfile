FROM dmiyamoto/neuron:gcc-ompi
MAINTAINER DeboraMatoso
WORKDIR /work
USER root

COPY jupyter_notebook_config.py /etc/jupyter/
COPY Notebook_run/* /work/Notebook_run/ 
COPY requirements.txt /work/config/

RUN pip install -r config/requirements.txt \
    && cd /work/nrn-7.4/src/nrnpython \
    && python setup.py install \
    && chown -R neuron /work \ 
    && cd /work/Notebook_run \
    && nrnivmodl

EXPOSE 8888
USER neuron
CMD jupyter notebook


