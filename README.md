[![codecov](https://codecov.io/gh/d33pster/target-ports/graph/badge.svg?token=PW5VH9WBC8)](https://codecov.io/gh/d33pster/target-ports)
[![Features Test CI](https://github.com/d33pster/target-ports/actions/workflows/FeaturesTestCI.yml/badge.svg)](https://github.com/d33pster/target-ports/actions/workflows/FeaturesTestCI.yml)
![PyPI - Version](https://img.shields.io/pypi/v/target-ports)
![GitHub last commit](https://img.shields.io/github/last-commit/d33pster/target-ports)
![Static Badge](https://img.shields.io/badge/license-MIT(modified)-yellow)



# Overview

target-ports is a basic port scanner written in python and makes use of socket programming to identify open ports.

## Installation

```bash
# install using pip, check the latest pypi version badge from the top of the readme file

pip install target-ports==<version> # without the <>
```

## Usage

```console
# call from terminal

$ tports -h
usage:
    target-ports v0.1

    help text

    |  -h or --help      : show this help text and exit.
    |  -v or --version   : show version and exit.
    |  -c or --current   : scan localhost.
    |  -t or --target    : specify single target.
    |  -ts or --targets  : specify multiple targets.
    |  -p or --ports     : number of ports to scan (each, if more than one target is provided.)[optional: default -> 100]

    Note:
        (i) -t(or --target) and -ts(or --targets) are mutually exclusive.
       (ii) -p(or --ports) is optional.
      (iii) This tool is just for educational pursose. The author(s) are not responsible for any misuse (AS STATED IN THE LICENSE).
```

## Uninstallation

```bash
pip uninstall target-ports
```

## Note to Users [IMPORTANT]

READ LICENSE BEFORE USE.

BY USING THIS SOFTWARE, YOU ACKNOWLEDGE AND AGREE THAT THE AUTHOR(S) SHALL NOT BE
HELD RESPONSIBLE OR LIABLE FOR ANY MISUSE, ILLEGAL ACTIVITIES, OR DAMAGES ARISING
FROM THE USE OF THE SOFTWARE. THE RESPONSIBILITY FOR THE USE AND CONSEQUENCES OF THE
SOFTWARE RESTS SOLELY WITH THE USERS AND NOT WITH THE AUTHOR(S).