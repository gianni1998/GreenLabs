from typing import List
from datetime import datetime
import pandas as pd
import os


NAME = 'Name'
RUN = 'Run'
TOTAL_CONSUMPTION = 'TotalEnergyConsumption'
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

PATH_TO_DATA = ''


def read_files(folder: str) -> List[str]:
    files = list()

    for file in os.listdir(folder):
        if file.startswith('results_'):
            files.append(os.path.abspath(folder + '/' + file))

    return files

# screen dark
# wifi running
# wifi scan
# gps
# core 0 cpu_idle start
# core 0 cpu_idle
# core 0 cpu_frequency
# core 1 cpu_idle start
# core 1 cpu_idle
# core 1 cpu_frequency
# core 2 cpu_idle start
# core 2 cpu_idle
# core 2 cpu_frequency
# core 3 cpu_idle start
# core 3 cpu_idle
# core 3 cpu_frequency
# core 4 cpu_idle start
# core 4 cpu_idle
# core 4 cpu_frequency
# core 5 cpu_idle start
# core 5 cpu_idle
# core 5 cpu_frequency
# core 6 cpu_idle start
# core 6 cpu_idle
# core 6 cpu_frequency
# core 7 cpu_idle start
# core 7 cpu_idle
# core 7 cpu_frequency

def transform(files: List[str], app: str, is_android: int) -> pd.DataFrame:
    result_df = pd.DataFrame(columns=[NAME, RUN, TOTAL_CONSUMPTION, SCREEN_CONSUMPTION, WIFI_CONSUMPTION, GPS_CONSUMPTION, CPU_CONSUMPTION, ANDROID_APP])

    for i in range(0, len(files)):
        df = pd.read_csv(files[i])
        new_row = pd.DataFrame({NAME: app, RUN: i,
                                TOTAL_CONSUMPTION: pd.Series(df[TOTAL_CONSUMPTION], dtype="float64").sum(),
                                SCREEN_CONSUMPTION: 0,
                                WIFI_CONSUMPTION: 0,
                                GPS_CONSUMPTION: 0,
                                CPU_CONSUMPTION: 0,
                                ANDROID_APP: is_android}, index=[0])

        result_df = pd.concat([result_df, new_row], ignore_index=True)

    return result_df


def save_df(df: pd.DataFrame):
    date = datetime.utcnow().strftime("%Y%m%d")
    df.to_csv(f'complete_results_{date}.csv', index=False)


if __name__ == "__main__":
    df = pd.DataFrame()

    # Apps
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'com-facebook-katana/batterystats'), 'Facebook', 1)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'com-flickr-android/batterystats'), 'Flickr', 1)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'com-google-android-youtube/batterystats'), 'Youtube', 1)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'com-instagram-android/batterystats'), 'Instagram', 1)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'com-linkedin-android/batterystats'), 'LinkedIn', 1)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'com-pinterest/batterystats'), 'Pinterest', 1)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'com-reddit-frontpage/batterystats'), 'Reddit', 1)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'com-tumblr/batterystats'), 'Tumblr', 1)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'com-twitter-android/batterystats'), 'Twitter', 1)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'com-facebook-katana/batterystats'), 'Tiktok', 1)], ignore_index=True)

    # Web
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'https-www-facebook-com/chrome/batterystats'), 'Facebook', 0)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'https-www-flickr-com/chrome/batterystats'), 'Flickr', 0)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'https-www-youtube-com/chrome/batterystats'), 'Youtube', 0)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'https-www-instagram-com/chrome/batterystats'), 'Instagram', 0)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'https-www-linkedin-com/chrome/batterystats'), 'LinkedIn', 0)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'https-www-pinterest-com/chrome/batterystats'), 'Pinterest', 0)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'https-www-reddit-com/chrome/batterystats'), 'Reddit', 0)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'https-www-tumblr-com/chrome/batterystats'), 'Tumblr', 0)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'https-www-twitter-com/chrome/batterystats'), 'Twitter', 0)], ignore_index=True)
    df = pd.concat([df, transform(read_files(PATH_TO_DATA + 'https-www-tiktok-com/chrome/batterystats'), 'Tiktok', 0)], ignore_index=True)

    save_df(df)
    print(df.head())