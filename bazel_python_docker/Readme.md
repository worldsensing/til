# How to create a python Distroless image with Bazel ?


## Project Structure

```bash
.
├── app
│   ├── BUILD
│   ├── env
│   ├── requirements.txt
│   └── src
│       └── main.py
├── BUILD
├── docker-compose.yml
├── run
└── WORKSPACE
```

## run

```sh
#!/bin/bash

sudo bazel run //app:app    # Create a docker image
```

## WORKSPACE

```sh
## Download the rules_docker repository at release v0.12.1##

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

##Load python3##                                     #####USE THIS ONE FOR PYTHON 3

load(
    "@io_bazel_rules_docker//python3:image.bzl",
    _py_image_repos = "repositories",
)

_py_image_repos()

##Load python2##                                     #####USE THIS ONE FOR PYTHON 2

load(
    "@io_bazel_rules_docker//python2:image.bzl",
    _py_image_repos = "repositories",
)

_py_image_repos()

##Load deps module##

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()

##Load Bazel federation module (for pip)##

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_federation",
    url = "https://github.com/bazelbuild/bazel-federation/releases/download/0.0.1/bazel_federation-0.0.1.tar.gz",
    sha256 = "506dfbfd74ade486ac077113f48d16835fdf6e343e1d4741552b450cfc2efb53",
)

##Load Python deps##

load("@bazel_federation//:repositories.bzl", "rules_python_deps")

rules_python_deps()
load("@bazel_federation//setup:rules_python.bzl",  "rules_python_setup")
rules_python_setup(use_pip=True)

##Load Python pip and install requirements##

load("@rules_python//python:pip.bzl", "pip_import")

pip_import(
   name = "my_deps",
   requirements = "//app:requirements.txt",
)

load("@my_deps//:requirements.bzl", "pip_install")
pip_install()
```

## docker-compose.yml
```sh
version: "3"
services:
  connector:
    image: bazel/app:app
    env_file: ./app/env
```

## BUILD

EMPTY FILE (Required because of bazel bug...)

## app/env
Write all your environment variables.  
Example:
```sh
PATH=/usr/bin/
INTERVAL=30
```
## app/requirement.txt
Write all the python libraries you want to install.  
Example:
```sh
pygame
flask
```
## app/src
Put in app/src all the files needed to run your app.
```sh
src
└── main.py
```
## app/BUILD
### py_library
Create your python library with all the libraries you have put in requirement.txt
```sh
load("@my_deps//:requirements.bzl", "requirement")

py_library(
    name = "mylib",
    deps = [
	requirement("pygame"),
	requirement("flask"),
    ]
)
```
### py_image / py3_image
Create your python 2 or python 3 image.

```sh
###Python3
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

py3_image(
    name = "src/main",
    srcs = glob(["src/*.py"]),           # Copy all your .py sources files
    main = "main.py",
    deps = [
        ":mylib",                        # Use the py_library you have created
    ],
    data = glob(["src/**"]),             # Copy all the files and folders that are in /src
)

###Python 2
load("@io_bazel_rules_docker//python:image.bzl", "py_image")

py_image(    
    name = "src/main",
    srcs = glob(["src/*.py"]),           # Copy all your .py sources files
    main = "main.py",
    deps = [
        ":mylib",                        # Use the py_library you have created
    ],
    data = glob(["src/**"]),             # Copy all the files and folders that are in /src

)
```
### container_image
```sh
container_image(
    name = "app",                        # Name of the container you will create 
    base = "src/main",                   # Name of the py_image
    cmd = ["ARG1"],                      # You can add arguments for the execution
    env = {                              # (example: python main.py arg1 arg2 arg3)
        "PATH": "",                      # Remove PATH, to disable execution of container
    }					 # This part is very important. Because with this, nobody can "enter" 
)					 # in your container because there is no shell available. Without shell
					 # the security improves a lot, preventing an attacker to create files 
					 # in mounted volumes or grant access to the Docker host server for example.
```
# Sources
https://github.com/GoogleContainerTools/distroless
https://github.com/bazelbuild/rules_docker
