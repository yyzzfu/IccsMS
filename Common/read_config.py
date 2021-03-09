import configparser


class ReadConfig:

    @staticmethod
    def get_config_data(file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]


if __name__ == '__main__':
    from Common import dir_path
    a = ReadConfig.get_config_data(dir_path.config_path, "archives.xlsx", "hall_gateway_add")
    print(eval(a))
    for i in eval(a):
        print(eval(a).get(i))

