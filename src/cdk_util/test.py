data = {"dev": "eu-central-1", "prod": "us-east-1"}


def get_data(env):
    return data.get(env)
