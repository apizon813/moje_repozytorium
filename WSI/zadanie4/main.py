import experiments as exp
from tools import load_databank
import yaml


def main():
    with open("args.yaml", "r") as file:
        args = yaml.safe_load(file)

    data_path = args["data_path"]
    bankdata = load_databank(data_path)

    exp.experiment_svm_regularization(args, bankdata)
    exp.experiment_svm_kernel(args, bankdata)
    exp.experiment_svm_iterations(args, bankdata)

    exp.experiment_tree_criterion(args, bankdata)
    exp.experiment_tree_splitter(args, bankdata)
    exp.experiment_tree_depth(args, bankdata)


if __name__ == "__main__":
    main()
