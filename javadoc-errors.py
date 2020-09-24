import argparse
import subprocess


# Help messages
msg_jdk_src_dir = "Specify source directory of openjdk i.e. ~/Workspace/openjdk/src"
msg_api_build_dir = "Specify build output i.e ~/Workspace/openjdk/build/<platform-specific-build>"
msg_modules = "Comma seperated list of modules to inspect i.e java.base,java.desktop,java.compiler"
msg_xdoclint_option = "Xdoclint option to use. Enable or disable specific checks for problems in javadoc. Options are accessibility, html, missing, reference, or syntax."

# Assign default values
env_jdk_src_dir = ""
env_api_build_dir = ""
env_modules = []
env_xdoclint_option = ""


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--jdk-src-dir', help=msg_jdk_src_dir)
    parser.add_argument('--api-build-dir', help=msg_api_build_dir)
    parser.add_argument('--modules', help=msg_modules)
    parser.add_argument('--xdoclint-option', help=msg_xdoclint_option)
    args = parser.parse_args()
    global env_jdk_src_dir
    global env_api_build_dir
    global env_modules
    global env_xdoclint_option
    env_jdk_src_dir = args.jdk_src_dir
    env_api_build_dir = args.api_build_dir
    env_xdoclint_option = args.xdoclint_option
    modules = args.modules
    env_modules = modules.split(",")


def run_javadoc():
    print(env_jdk_src_dir)
    print(env_api_build_dir)
    print(env_modules)
    print(env_xdoclint_option)
    for module in env_modules:
        print(module)
        try:
            err_log = open(str("./logs/" + module + "_" + env_xdoclint_option
                               + ".log"), "w")
            cmd = ["sh", "./javadoc-scripts/doc_command_generic.sh",
                   env_jdk_src_dir, env_api_build_dir, module,
                   env_xdoclint_option]
            subprocess.check_call(cmd, stderr=err_log)
        except subprocess.CalledProcessError as sub_err:
            print(sub_err)
        finally:
            print("Done")


def main():
    arg_parser()
    run_javadoc()


if __name__ == "__main__":
    main()
