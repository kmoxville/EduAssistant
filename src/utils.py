import argparse

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='EduAssistant',
        description='What the program does',
        epilog='Text at the bottom of help')

    parser.add_argument('--token', 
        type=str,
        required=True,
        help='The token from Bot.Father')

    args = parser.parse_args()
    return args