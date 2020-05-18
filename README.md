# An interactive tool to study motor neuron electrophysiology aspects at healthy and at disease conditions 


<p style='text-align: justify;'> The objective of this study is to propose an interactive Jupyter notebook as a computational alternative to simulate how the MN firing properties are influenced by changes in monoaminergic drive and, biophysical and morphological MN characteristics. The proposed model also allows studies related to amyotrophic lateral sclerosis (ALS), since increases in L-type calcium conductances (gCaL) are observed during the progression of this disease and are related to MN bistability. A monoaminergic decrease observed in patients with spinal cord injury can also be simulated, consisting of another example of the exploration with this tool.</p>

The developed interactive model utilizes Jupyter Notebook with the NEURON simulator in Python and the environment can be easily set through Docker (which is an open source containerizing tool) or through MyBinder.

## Using Docker environment

First of all, we give you two options for using docker:

 * Installing Docker in your computer following the instructions presented at the Docker website:
      https://docs.docker.com/engine/install/
 * Don't install anything and use the online Docker Lab Environment:
      https://labs.play-with-docker.com/#

### 1) With Docker Lab Environment

If you are using the Docker Lab Environment, add a new instance and run the following line in the terminal:

                                    $ docker run -it -p 8888:8888 28102018/decm_first_repo:cbeb_2020

Wait until it is done and a link will be prompted at the terminal, it will look like this:

http://localhost:8888/?token=95c53108298f4fb7e6af53cf3fac1b3afd09d

Please select and copy the characters after 'token='. Then, click at the 8888 link that will appear on the top of the page. This will open another page and at "Password or token" just paste the token you copied. Click at login. 

### 2) With Docker installation

If you have installed Docker in your computer, run locally the following line in a command terminal:

                                    $ docker run -it -p 8888:8888 28102018/decm_first_repo:cbeb_2020

If you are using a Linux machine, use:

                                    $ sudo docker run -it -p 8888:8888 28102018/decm_first_repo:cbeb_2020

Follow the link that will be prompted on the screen.

### Using MyBinder environment

If you can use the tool with another online environment, please access the link:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/deboramatoso/CBEB_2020/master)

And insert the follow line under the first import to compile the mechanisms: 

$ !nrnivmodl

## Using the tool

Once in the Jupyter Notebook, please enter the folder "Notebook_run" and run the script (**DECM_HSF_LAE_CBEB2020.ipynb**). You will observe the outputs after clicking the "Run interact" buttons. You can modify the values of the widgets to observe other scenarios interesting for you.

## An application example

For an example of the study with the tool, please follow the steps in the script (**DECM_HSF_LAE_CBEB2020.ipynb**) along with the scientific communication submited to the XXVII Brazilian Congress in Biomedical Engineering - CBEB 2020 (**DECM_HSF_LAE_CBEB2020.pdf**).

## Usability survey
To finish your experience with the tool, if it is comfortable for you, please take a short test and answer the survey to help us understanding the usability of the interactive tool developed: https://docs.google.com/forms/d/e/1FAIpQLSewYiuRmT3B4MQd9LP9WRLqW_YjXODcE8oNQ5yBcn8wdMK2Ag/viewform
