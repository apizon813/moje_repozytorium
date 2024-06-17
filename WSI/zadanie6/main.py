import yaml
from experiments import experiment_a, experiment_g, experiment_e, experiment_t
from tools import save_group_plot


def main():
    with open("arguments.yaml", "r") as file:
        args = yaml.safe_load(file)

    if args["run_exp_a"]:
        experiment_a(args)
    if args["save_exp_a_plot"]:
        data_path = args["results_path"] + "exp_a/a_"
        save_path = args["results_path"] + "plots/exp_a.png"
        par_values = args["a_values"]
        save_group_plot(args, data_path, save_path, par_values, "a")

    if args["run_exp_g"]:
        experiment_g(args)
    if args["save_exp_g_plot"]:
        data_path = args["results_path"] + "exp_g/g_"
        save_path = args["results_path"] + "plots/exp_g.png"
        par_values = args["g_values"]
        save_group_plot(args, data_path, save_path, par_values, "g")

    if args["run_exp_e"]:
        experiment_e(args)
    if args["save_exp_e_plot"]:
        data_path = args["results_path"] + "exp_e/e_"
        save_path = args["results_path"] + "plots/exp_e.png"
        par_values = args["e_values"]
        save_group_plot(args, data_path, save_path, par_values, "e")

    if args["run_exp_t"]:
        experiment_t(args)
    if args["save_exp_t_plot"]:
        data_path = args["results_path"] + "exp_t/t_"
        save_path = args["results_path"] + "plots/exp_t.png"
        par_values = args["t_values"]
        save_group_plot(args, data_path, save_path, par_values, "t")


if __name__ == "__main__":
    main()
