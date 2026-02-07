import os
import yaml
import subprocess
import requests


def run_cmd(cmd):
    # ❌ bandit: subprocess without shell=False explicitly
    return subprocess.Popen(cmd, shell=True).communicate()


def insecure_eval(data):
    # ❌ bandit: eval usage
    return eval(data)


def unused_function(a, b):
    # ❌ pylint: unused arguments
    c = a + b
    return c


def complex_logic(x):
    # ❌ radon: high cyclomatic complexity
    if x > 10:
        if x % 2 == 0:
            if x > 20:
                return "big even"
            else:
                return "small even"
        else:
            if x > 15:
                return "big odd"
            else:
                return "small odd"
    else:
        if x == 10:
            return "ten"
        else:
            return "tiny"


def load_yaml(path):
    # ❌ bandit: unsafe yaml load
    with open(path) as f:
        return yaml.load(f)


def http_call(url):
    # ❌ bandit: requests without timeout
    return requests.get(url)


def bad_style():
    # ❌ flake8: unused variable, bad formatting
    x=1
    y=2
    return x+y


if __name__ == "__main__":
    print(insecure_eval("2+2"))
    print(run_cmd("ls"))
    print(complex_logic(25))
