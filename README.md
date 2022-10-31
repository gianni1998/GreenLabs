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
Install Android version 6.0.1 on the smartphone and download the native applications from the selected application list. Install the tools ***Android runner***, ***Monkey runner*** and ***Batterystats*** on a Raspberry Pi. To install these tools, follow the guidelines provided by the [S2-group/android-runner](https://github.com/S2-group/android-runner) repository.   

### Set up
Connect the Android smartphone with a raspberry Pi using a USB cable to control the smartphone. Ensure the smartphone is unlocked and the screen is on the lowest brightness. Use a laptop to SSH into the Raspberry Pi and execute the python script in the experiments/config directory. Specify in the python script whether to run the scripts to measure the energy consumption of the Android apps or Web apps.     

### R scripts
Use the complete_results_20221029.csv when executing the R script in the results directory.
