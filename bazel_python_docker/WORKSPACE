###################################################################
###### Download the rules_docker repository at release v0.12.1#####
###################################################################

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "14ac30773fdb393ddec90e158c9ec7ebb3f8a4fd533ec2abbfd8789ad81a284b",
    strip_prefix = "rules_docker-0.12.1",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.12.1/rules_docker-v0.12.1.tar.gz"],
)

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)

container_repositories()

######################
#####Load python3#####
######################

load(
    "@io_bazel_rules_docker//python3:image.bzl",
    _py_image_repos = "repositories",
)

_py_image_repos()

##########################
#####Load deps module#####
##########################

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()

################################################
#####Load Bazel federation module (for pip)#####
################################################

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_federation",
    url = "https://github.com/bazelbuild/bazel-federation/releases/download/0.0.1/bazel_federation-0.0.1.tar.gz",
    sha256 = "506dfbfd74ade486ac077113f48d16835fdf6e343e1d4741552b450cfc2efb53",
)

##########################
#####Load Python deps#####
##########################

load("@bazel_federation//:repositories.bzl", "rules_python_deps")

rules_python_deps()
load("@bazel_federation//setup:rules_python.bzl",  "rules_python_setup")
rules_python_setup(use_pip=True)

##################################################
#####Load Python pip and install requirements#####
##################################################

load("@rules_python//python:pip.bzl", "pip_import")

pip_import(
   name = "my_deps",
   requirements = "//app:requirements.txt",
)

load("@my_deps//:requirements.bzl", "pip_install")
pip_install()