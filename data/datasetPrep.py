from typing import List
from datetime import datetime
import pandas as pd
import os


NAME = 'Name'
RUN = 'Run'
CONSUMPTION = 'Energy Consumption (Joule)'
ANDROID_APP = 'Android app'

PATH_TO_DATA = ''


def read_files(folder: str) -> List[str]:
    files = list()

    for file in os.listdir(folder):
        if file.startswith('results_'):
            files.append(os.path.abspath(folder + '/' + file))

    return files


def transform(files: List[str], app: str, is_android: int) -> pd.DataFrame:
    result_df = pd.DataFrame(columns=[NAME, RUN, CONSUMPTION, ANDROID_APP])

    for i in range(0, len(files)):
        df = pd.read_csv(files[i])
        new_row = pd.DataFrame({NAME: app, RUN: i, CONSUMPTION: pd.Series(df[CONSUMPTION], dtype="float64").sum(), ANDROID_APP: is_android}, index=[0])

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