import pickle
import subprocess


def insecure_deserialize(data):
    return pickle.loads(data)


def run_command(cmd):
    subprocess.Popen(cmd, shell=True)
