from random import randint
import subprocess


def runweb():
    for n in range(0, 10):
        commands = [
            "python3 android-runner android-runner/experiments/batterystats/config/web/facebook.json",
            "python3 android-runner android-runner/experiments/batterystats/config/web/flickr.json",
            "python3 android-runner android-runner/experiments/batterystats/config/web/instagram.json",
            "python3 android-runner android-runner/experiments/batterystats/config/web/linkedin.json",
            "python3 android-runner android-runner/experiments/batterystats/config/web/pinterest.json",
            "python3 android-runner android-runner/experiments/batterystats/config/web/reddit.json",
            "python3 android-runner android-runner/experiments/batterystats/config/web/tumblr.json",
            "python3 android-runner android-runner/experiments/batterystats/config/web/twitter.json",
            "python3 android-runner android-runner/experiments/batterystats/config/web/youtube.json"
        ]

        while(len(commands) > 0):
            i = randint(0, len(commands))
            command = commands.pop(i-1)
            subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).wait()


def run_app():
    for n in range(0, 10):
        commands = [
            "python3 android-runner android-runner/experiments/batterystats/config/native/facebook.json",
            "python3 android-runner android-runner/experiments/batterystats/config/native/flickr.json",
            "python3 android-runner android-runner/experiments/batterystats/config/native/instagram.json",
            "python3 android-runner android-runner/experiments/batterystats/config/native/linkedin.json",
            "python3 android-runner android-runner/experiments/batterystats/config/native/pinterest.json",
            "python3 android-runner android-runner/experiments/batterystats/config/native/reddit.json",
            "python3 android-runner android-runner/experiments/batterystats/config/native/tumblr.json",
            "python3 android-runner android-runner/experiments/batterystats/config/native/twitter.json",
            "python3 android-runner android-runner/experiments/batterystats/config/native/youtube.json"
        ]

        while(len(commands) > 0):
            i = randint(0, len(commands))
            command = commands.pop(i-1)
            subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).wait()


if __name__ == "__main__":
    #run_web()
    run_app()