import yaml


def test_yaml():
    secret = {"contact": "T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw", "agent": "xxxxx"}
    with open("config2.yml", "w") as f:
        yaml.dump(secret, f)