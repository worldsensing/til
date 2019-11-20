load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@my_deps//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//container:container.bzl", "container_image")

py_library(
    name = "mylib",
    deps = [
	    #requirement(""),
    ]
)

py3_image(
    name = "src/main",
    srcs = glob(["src/*.py"]),
    main = "main.py",
    deps = [
        ":mylib",
    ],
    data = glob(["src/**"]),
)

container_image(
    name = "app",
    base = "src/main",
    cmd = ["ARG1"],
    env = {
        "PATH": "",
    }
)