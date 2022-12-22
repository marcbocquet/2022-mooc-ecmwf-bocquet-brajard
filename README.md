# 2022-mooc-ecmwf-bocquet-brajard

This jupyter notebook has been created by Marc Bocquet and Julien Brajard
for the ECMWF MOOC of 2023 on Machine Learning in Weather & Climate. It has been reviewed and improved by Alban Farchi.
It also benefited from pieces of code previously developed by Marc Bocquet, Julien Barjard and Alban Farchi.
It explains how data assimilation and machine learning can be combined to achieve model discovery or model error correction.
It consists of an introduction, easily convertible into preliminary slides, and of three parts, meant to be used in sequence.

See https://lms.ecmwf.int/ for the full ECMWF event.

## Before running the notebook
Have a look at the introductory part. For that, you to install the jupyter addon rise https://rise.readthedocs.io/ via pip install rise in your conda mooc environment.
Run the introductory notebook:
- Part Intro [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) ](https://colab.research.google.com/github/marcbocquet/2022-mooc-ecmwf-bocquet-brajard/blob/main/mooc_ecmwf_bocquet_brajard_intro.ipynb)
and then activate the rise slideshow mode.

It can also be displayed from its html output: ???

## Run the notebooks on google colab
Just run each notebook starting with the part 1:
- Part 1 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) ](https://colab.research.google.com/github/marcbocquet/2022-mooc-ecmwf-bocquet-brajard/blob/main/mooc_ecmwf_bocquet_brajard_part1.ipynb)
- Part 2 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) ](https://colab.research.google.com/github/marcbocquet/2022-mooc-ecmwf-bocquet-brajard/blob/main/mooc_ecmwf_bocquet_brajard_part2.ipynb)
- Part 3 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) ](https://colab.research.google.com/github/marcbocquet/2022-mooc-ecmwf-bocquet-brajard/blob/main/mooc_ecmwf_bocquet_brajard_part3.ipynb)

## Run the notebooks on you machine
1. Create the conda enviromment: ```conda env create -f environment.yml```
2. Activagte the enviromnment: ```conda activate mooc```
3. Run jupyter lab: ```jupyter lab```
4. Run the notebooks from the first (part 1) to the last (part 3)
