FROM dmiyamoto/neuron:jupyter
MAINTAINER DeboraMatoso
WORKDIR /work

USER root

RUN apt-get install python3

CMD jupyter lab
