FROM dmiyamoto/neuron:jupyter
MAINTAINER DeboraMatoso
WORKDIR /work
USER root

COPY jupyter_notebook_config.py /etc/jupyter/
COPY Notebook_run/* /work/Notebook_run/
COPY requirements.txt /work/config/
COPY runtime.txt /work/

RUN echo $(python --version)
RUN python --version
RUN echo $(jupyter kernelspec list)
RUN python -m pip install --upgrade pip
RUN python -m pip install -r config/requirements.txt
RUN cd /work/nrn-7.4/src/nrnpython \
    python setup.py install
RUN chown -R neuron /work
RUN cd /work/Notebook_run \ 
    nrnivmodl
RUN python -m jupyter nbextension enable --py widgetsnbextension --sys-prefix

EXPOSE 8888
USER neuron
CMD python -m jupyter notebook
