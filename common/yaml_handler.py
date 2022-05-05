
import yaml


class YamlConfig(object):
    def __init__(self):
        pass

    def read_yaml(self, file, encoding='utf-8'):
        with open(file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self, file, wtdata, encoding='utf-8'):
        with open(file, encoding=encoding, mode='w') as f:
            yaml.dump(wtdata, stream=f, allow_unicode=True)


if __name__ == '__main__':
    ya = YamlConfig()
    data = (ya.read_yaml('api.yaml'))
    print(data)
    ya.write_yaml('api111.yaml', data)






