# Green Lab - Updog 
This repository contains the replication package for the research paper: "Who drained my battery? An empirical study on energy consumption of Android apps VS Web counterparts". The repository contains the scripts used to run the experiment, the test results and the scripts to analyze the data. 

## Team members
1. Gianni van der Galiën - 2693280
2. Quinn Ceuppens - 2693281
3. Mathieu Bosse - 2693279
4. Latife Dağ - 2736983
5. Ayşenur Şeref - 2702062

## How to run the experiment?
### Preparation
Install Android version 9 on the smartphone and download the native applications from the selected application list. Install the tools ***Python***, ***Android runner***, ***Monkey runner*** and ***Batterystats*** on a Raspberry Pi. To install these tools, follow the guidelines provided by the [S2-group/android-runner](https://github.com/S2-group/android-runner) repository. Also make sure to install the R programming language for the visualisations and calculations after running the experiment.

First make sure the Raspberry Pi is connected with power. Afterwards connect the Android smartphone with a Raspberry Pi using a USB data cable so that the Raspberry Pi can control the smartphone. Ensure the smartphone is unlocked, is connected to WiFi and the screen is on the lowest brightness. Use a laptop to connect to the hotspot of the Raspberry py, SSH into it and direct to the GreenLabs folder on the Raspberry Pi.

### Execution
The Python script responsible for running the tests are located in the **GreenLabs/experiments/config** directory. Specify in the Python command whether to run the scripts to measure the energy consumption of the Android apps or Web apps. When executing the command for running the scripts, make sure you are above the main GreenLabs folder and not inside the folder. To run the experiments for Android apps and Web apps run the following commands respectively:

```
python3 GreenLabs GreenLabs/experiments/config.json
python3 GreenLabs GreenLabs/experiments/config_web.json
```

### R scripts
When running the data analysis files in the results directory, make sure to change the paths accordingly. First we pre processed the data into a single CSV file using the datasetPrep.py script located in the results directory. This makes the completed_results file that is used for the visualisations and calculations using R. Make sure that when running both the R and the Python script, that the paths are edited to the right locations for the files. For running the R scripts we recommend using the complete_results_20221029.csv file. This file has been pre compiled and are the exact findings where our results and graphs are based off of.
