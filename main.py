from task_1_list.main import main as run_list_app
from task_2_recursion.main import main as run_recursion_app
from task_3_trees.main import main as run_trees_app
from task_4_pyramid.main import main as run_pyramid_app
from task_5_binary_tree.main import main as run_binary_tree_app
from task_6_greedy_algorithm.main import main as run_greedy_algorithm_app
from task_7_monte_carlo.main import main as run_monte_carlo_app


def main():
    try:
        print("Which app do you want to run? \n  (1) List \n  (2) Recursion \n  (3) Trees \n  (4) Pyramid \n  (5) Binary Tree \n  (6) Greedy Algorithm \n  (7) Monte Carlo \n  (q) Quit \n")
        action = input()

        if action == "1":
            run_list_app()

        elif action == "2":
            run_recursion_app()
        
        elif action == "3":
            run_trees_app()
        
        elif action == "4":
            run_pyramid_app()

        elif action == "5":
            run_binary_tree_app()
        
        elif action == "6":
            run_greedy_algorithm_app()
        
        elif action == "7":
            run_monte_carlo_app()

        elif action == "q":
            print("\nGood bye!")
            return
        else:
            print("\033[91mI don't understand that command\033[0m")

    except KeyboardInterrupt:
        print("\nGood bye!")
        return


if __name__ == "__main__":
    main()
