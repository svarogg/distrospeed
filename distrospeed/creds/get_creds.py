import yaml


def get_creds():
    with open("~/.distrospeed/creds.yaml", "r") as stream:
        return yaml.safe_load(stream)
