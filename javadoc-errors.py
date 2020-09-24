import argparse
import subprocess

# Assign default values
env_api_build_dir = ""
env_modules = []
env_xdoclint_option = ""


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-build-dir', help='api-build-dir help')
    parser.add_argument('--modules', help='modules help')
    parser.add_argument('--xdoclint-option', help='xdoclint-option help')
    args = parser.parse_args()
    global env_api_build_dir
    global env_modules
    global env_xdoclint_option
    env_api_build_dir = args.api_build_dir
    env_xdoclint_option = args.xdoclint_option
    env_modules = args.modules


def run_javadoc():
    print(env_api_build_dir)
    print(env_modules)
    print(env_xdoclint_option)
    val = subprocess.check_call(["sh",
                                 "./javadoc-scripts/doc_command_generic.sh",
                                 env_api_build_dir, env_modules,
                                 env_xdoclint_option, "2>",
                                 str("logs/" + env_xdoclint_option + ".log")])


def main():
    arg_parser()
    run_javadoc()


if __name__ == "__main__":
    main()
