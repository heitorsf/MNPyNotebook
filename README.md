# An interactive Python notebook to study motor neuron electrophysiology in healthy and diseased conditions

<p style='text-align: justify;'> The objective of this project is to provide an interactive Jupyter notebook as an aid to investigate how MN firing properties are influenced by changes in MN morphological and electrotonic properties, as well as the intensity of monoaminergic drive (which regulates the magnitude of persistent inward currents). The proposed tool can also be used to investigate neurological diseases that affect the MN electrophysiology. For instance, it is known that MN morphology changes during the progression of amyotrophic lateral sclerosis (ALS), thereby influencing the electrophysiological responses of the cell. Also, increased MN excitability, which is observed in ALS and spinal cord injuries, can be simulated by changing the magnitude of persistent currents and monoaminergic drive. Therefore, the proposed interactive notebook can be used in MN neurophysiology research and as an educational tool.</p>

The Jupyter notebook was coded in Python programming language and the libraries of the NEURON simulator. The environment can be easily set up on [Docker](https://www.docker.com/) or [MyBinder](https://mybinder.org/).

## Using Docker environment

You might use Docker after install Docker on your computer. Please, follow the [instructions](https://docs.docker.com/engine/install/) presented at the Docker website.


### Running on your own computer

After install the Docker on your computer, you can run the notebook typing the following line on your terminal:

```
$ docker run -it -p 8888:8888 28102018/decm_first_repo:mnpynotebook
```

If you are using a Unix OS, the following code should be used:

```
$ sudo docker run -it -p 8888:8888 28102018/decm_first_repo:mnpynotebook
```

Follow the link that will be prompted on the screen.


## Using MyBinder environment

The notebook can also be accessed on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/deboramatoso/mnpynotebook/master).

## Using the interactive notebook

Once you enter the Jupyter environment, select the folder "Notebook_run" and run the script (**MNPyNotebook.ipynb**). If you want to use the notebook with the MyBinder environment, uncomment the line `!nrnivmodl` to compile the Neuron mechanisms.

You will get the model outputs after clicking on "Run interact" buttons. You can modify model and input parameters with the widgets to observe other scenarios. Please, feel free to explore the tool at your leisure.

## Survey
We prepared a brief (anonymous) survey in order to assess your experience with the tool. Please, help us to improve our project by filling the [form](https://docs.google.com/forms/d/e/1FAIpQLSewYiuRmT3B4MQd9LP9WRLqW_YjXODcE8oNQ5yBcn8wdMK2Ag/viewform).
