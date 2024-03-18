import pandas as pd


def input_data_from_console():
    """This function receives data entered from the console.

    Returns:
        input_data (str): this function return a value input from the console.

    """

    input_data = input("Please enter your data: ")
    return input_data


def input_data_from_file(path_to_file):
    """this function return a value input from the file.

         Args:
            path_to_file (str): path of the file to read.

        Returns:
            input_data (str): this function return a value input from the console.

        Raises:
            FileNotFoundError: if file by path in the args of the function is not found.
        """
    with open(path_to_file, "r") as input_file:
        try:
            input_data = input_file.read()
        except FileNotFoundError:
            return f"File {path_to_file} not found"
        return input_data


def input_data_with_pandas(path_to_file):
    """this function return a value input from the file with pandas.

            Args:
               path_to_file (str): path of the file to read.

           Returns:
               input_data (str): this function return a value input from the console.

           Raises:
               FileNotFoundError: if file by path in the args of the function is not found.
           """
    try:
        input_data = pd.read_csv(path_to_file)
    except FileNotFoundError:
        return f"File {path_to_file} not found"
    return input_data
