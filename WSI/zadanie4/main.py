import experiments as exp
import tools
import yaml


def main():

    with open('args.yaml', 'r') as file:
        args = yaml.safe_load(file)

    data_path = args['data_path']
    bankdata = tools.load_databank(data_path)
    exp.experiment1(bankdata)


if __name__ == '__main__':
    main()
