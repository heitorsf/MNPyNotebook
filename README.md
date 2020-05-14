# CBEB_2020
New version


Researchers have sought both computational and experimental approaches to study the motor neuron electrophysiology aspects. Nonetheless, understanding how the individual MN characteristics influence the firing properties is a difficult task. Thus, the objective of this study is to propose an interactive Jupyter notebook as a computational alternative to simulate how the MN firing properties are influenced by changes in monoaminergic drive and, biophysical and morphological MN characteristics. The proposed model also allows studies related to amyotrophic lateral sclerosis (ALS), since increases in L-type calcium conductances (gCaL) are observed during the progression of this disease and are related to MN bistability. A monoaminergic decrease observed in patients with spinal cord injury can also be simulated, consisting of another example of the exploration with this tool.

The developed interactive model utilizes Jupyter Notebook with the NEURON simulator in Python and the environment can be easily set through Docker (which is an open source containerizing tool).

1) First of all, we give you two options for using docker:
    - Installing Docker in your computer following the instructions presented at the Docker website:
      https://docs.docker.com/engine/install/
    - Don't install anything and use the online Docker Lab Environment:
      https://labs.play-with-docker.com/#

2) If you are using the Docker Lab Environment, add a new instance and run the following line in the terminal:

                                    $ docker run -it -p 8888:8888 28102018/decm_first_repo

A link will be prompted the terminal and will look like this:

http://localhost:8888/?token=95c53108298f4fb7e6af53cf3fac1b3afd09d

Please select and copy the characters after 'token='. Then, click at the 8888 link that will appear on the top of the page. This will open another page and at "Password or token" just paste the token you copied. Click at login. 

3) If you have installed Docker in your computer, run locally the following line in a command terminal:

                                    $ docker run -it -p 8888:8888 28102018/decm_first_repo

If you are using a Linux machine, use:

                                   $ sudo docker run -it -p 8888:8888 28102018/decm_first_repo

Follow the link that will be prompted on the screen.

4) So, please enter the folder "Notebook_run" and run the Jupyter Notebook script ("CBEB_2020_2.ipynb"). You will observe the outputs after clicking the "Run interact" buttons. You can modify the values of the widgets to observe other scenarios interesting for you.

5) For an example of the study with the tool, please read the scientific communication submit to the XXVII Brazilian Congress in Biomedical Engineering - CBEB 2020 ("DECM_HSF_LAE_CBEB2020.pdf").

6) To finish your experience with the tool, if it is comfortable for you, please make a test present at the link: https://docs.google.com/forms/d/1YYfg_csWUCQQs_RUqjEU8fQO1kmzd5DI2lANDz3ksYE/edit and answer the usability survey to help us understand the usability of the interactive tool developed.
