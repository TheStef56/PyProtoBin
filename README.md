# PyProtoBin

PyProtoBin is a simple command line tool that lets you generate C structs and equivalent python classes, but having to describe their structure in just one file. Useful for binary protocol applications that, for example need to handle binary data from an IoT device (like arduino for example) to a python backend.

## Requirements

Python3

## Usage

```bash
usage: pyprotobin.py [-h] [-py PYTHON_OUTPUT] [-c C_OUTPUT] [input_file]

Generate Python and C structs from proto file.

positional arguments:
  input_file            Input proto file (default: proto.ppb)

options:
  -h, --help            show this help message and exit
  -py PYTHON_OUTPUT, --python_output PYTHON_OUTPUT
                        Python output file (default: ./proto.py)
  -c C_OUTPUT, --c_output C_OUTPUT
                        C header output file (default: ./proto.h)

```

## License

[MIT](https://choosealicense.com/licenses/mit/)