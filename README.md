# QR UUID Generator

This Python script generates a random Universal Unique Identifier (UUID) and converts it into a QR code that can be scanned using any mobile device with a QR code reader. The purpose of this tool is to provide a unique identification for embedded systems, allowing them to uniquely identify and determine individual machines.


### Dependencies

This project requires the following Python packages:

- `colorama==0.4.6`
- `flake8==7.0.0`
- `mccabe==0.7.0`
- `pycodestyle==2.11.1`
- `pyflakes==3.2.0`
- `pypng==0.20220715.0`
- `qrcode==7.4.2`
- `typing_extensions==4.10.0`

These dependencies will be automatically installed when running the provided shell script.


### Installation

1. Clone this repository to your local machine:

    ```
    $ git clone https://github.com/WannaCry081/QR-UUID-Python.git
    ```

2. Navigate to the project directory:

    ```
    $ cd qr-uuid-python
    ```

3. Run the provided shell script to install the necessary packages and to create and activate the virtual environment:

    ```
    $ ./run.sh
    ```


### Example

Here's a basic example of how to use the QR UUID generator:

```powershell
$ ./run.sh

or 

$ python main.py 
```

This will generate a UUID, create a corresponding QR code image, and save it to the output directory.


### Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.
