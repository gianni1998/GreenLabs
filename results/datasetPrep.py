from typing import List, Tuple
from datetime import datetime
import pandas as pd
import os


NAME = 'Name'
RUN = 'Run'
TOTAL_CONSUMPTION = 'TotalEnergyConsumption'
ENERGY_CONSUMPTION = 'Energy Consumption (Joule)'
SCREEN_CONSUMPTION = 'ScreenEnergyConsumption'
WIFI_CONSUMPTION = 'WiFiEnergyConsumption'
GPS_CONSUMPTION = 'GPSEnergyConsumption'
CPU_CONSUMPTION = 'CPUEnergyConsumption'
CORE_0_CONSUMPTION = 'Core0EnergyConsumption'
CORE_1_CONSUMPTION = 'Core1EnergyConsumption'
CORE_2_CONSUMPTION = 'Core2EnergyConsumption'
CORE_3_CONSUMPTION = 'Core3EnergyConsumption'
CORE_4_CONSUMPTION = 'Core4EnergyConsumption'
CORE_5_CONSUMPTION = 'Core5EnergyConsumption'
CORE_6_CONSUMPTION = 'Core6EnergyConsumption'
CORE_7_CONSUMPTION = 'Core7EnergyConsumption'
ANDROID_APP = 'AndroidApp'

PATH_TO_DATA = '/mnt/c/Users/Gianni/Documents/School/VU/GreenLabs/results/'


def save_df(df: pd.DataFrame):
    date = datetime.utcnow().strftime("%Y%m%d")
    df.to_csv(f'complete_results_{date}.csv', index=False)


def get_file_n_names(is_android: bool) -> List[tuple]: 
    file_paths = []
    directory = PATH_TO_DATA + 'Android' if is_android else PATH_TO_DATA + 'Web'
    data_folders = [ f.path for f in os.scandir(directory) if f.is_dir() ]

    batterystats = '/batterystats/' if is_android else '/chrome/batterystats/'

    for folder in data_folders:  
        try:
            app = [ f.name for f in os.scandir(folder + '/data/samsung/') if f.is_dir() ][0]

            for file in os.listdir(folder + '/data/samsung/' + app + batterystats):
                if file.startswith('results_'):
                    file_paths.append((app,os.path.abspath(folder + '/data/samsung/' + app + batterystats + file)))
        except:
            print(folder)
    
    return file_paths


def transform(name_files: List[Tuple[str, str]], is_android: int):
    result_df = pd.DataFrame(columns=[NAME, RUN, TOTAL_CONSUMPTION, SCREEN_CONSUMPTION, WIFI_CONSUMPTION, GPS_CONSUMPTION, CPU_CONSUMPTION, ANDROID_APP])

    for pair in name_files:
        df = pd.read_csv(pair[1])
        name = pair[0]

        new_row = pd.DataFrame({NAME: name, 
                                RUN: (result_df[NAME] == name).sum(),
                                TOTAL_CONSUMPTION: pd.Series(df[ENERGY_CONSUMPTION], dtype="float64").sum(),
                                SCREEN_CONSUMPTION: pd.Series(df[df['Component'].str.contains('screen')][ENERGY_CONSUMPTION]).sum(),
                                WIFI_CONSUMPTION: pd.Series(df[df['Component'].str.contains('wifi')][ENERGY_CONSUMPTION]).sum(),
                                GPS_CONSUMPTION: pd.Series(df[df['Component'].str.contains('gps')][ENERGY_CONSUMPTION]).sum(),
                                CPU_CONSUMPTION: pd.Series(df[df['Component'].str.contains('core')][ENERGY_CONSUMPTION]).sum(),
                                ANDROID_APP: is_android}, index=[0])

        result_df = pd.concat([result_df, new_row], ignore_index=True)

    return result_df


if __name__ == "__main__":
    df = pd.DataFrame()

    # App
    app_n_paths = get_file_n_names(True)
    df = pd.concat([df, transform(app_n_paths, 1)])

    # Web
    web_n_paths = get_file_n_names(False)
    df = pd.concat([df, transform(web_n_paths, 0)])

    save_df(df)
    print(df.head())