FROM dmiyamoto/neuron:jupyter
MAINTAINER DeboraMatoso
WORKDIR /work
USER root

COPY jupyter_notebook_config.py /etc/jupyter/
COPY Notebook_run/* /work/Notebook_run/
COPY requirements.txt /work/config/

RUN pip install -r config/requirements.txt
RUN cd /work/nrn-7.4/src/nrnpython
RUN python setup.py install
RUN chown -R neuron /work
RUN cd /work/Notebook_run
RUN nrnivmodl
RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix

EXPOSE 8888
USER neuron
CMD jupyter notebook


