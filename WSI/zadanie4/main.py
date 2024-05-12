import experiments as exp
import parameters as pars
import tools


def main(pars):
    data_path = pars.DATA_PATH
    bankdata = tools.load_databank(data_path)
    exp.experiment1(bankdata)


if __name__ == '__main__':
    main(pars)
