### API Generation Scripts
This repository contains tools related to resolving bugs associated with
[JDK-8252636](https://bugs.openjdk.java.net/browse/JDK-8252636).

### Usage
To use these scripts, an environment variable `API_BUILD_DIR` must first be
declared. This should point to the build directory you wish to output your
documentation to. It can be declared like so:
```bash
export API_BUILD_DIR=<path-to-jdk-build-dir>
```

After that, a run of all kinds of Xdoclint modes can be initiated with `sh run_all.sh` in the repository root. This will output error and warning logs for each individual run (6 in total) in a `/logs` directory.

### Future Improvements
The following improvemnts are planned for this toolset.
 - Easy configuration of modules to run Xdoclint checks on (right now only looking at java.base)
 - Tools to further breakdown log files for easier processing in the review process.
