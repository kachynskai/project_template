import pandas as pd


def output_data_to_console(output_data):
    """this function outputs the data of the passed argument to the console.

       Args:
           output_data(Any): data to be printed.
       Returns:
           None: this function returns nothing.

       """
    data_string = str(output_data)
    print('Output data : \n')
    print(data_string + '\n\n')
    return None


def output_data_to_file(output_data, filename):
    """this function outputs the data of the passed first argument to the file in second arg.

       Args:
           output_data(Any): data to be output.
           filename(str): name of the file in which the entered data will be written.
       Returns:
           None: this function returns nothing.

       """
    with open(filename, 'a') as output_file:
        output_file.write('\n' + str(output_data) + '\n')
    return None


def output_data_with_pandas(output_data, filename):
    """this function outputs the data of the passed first argument to the file in second arg with pandas dataframe.

           Args:
               output_data(Any): data to be output.
               filename(str): name of the file in which the entered data will be written.
           Returns:
               None: this function returns nothing.

           """
    output_data_frame = pd.DataFrame(output_data)
    output_data_frame.to_csv(filename, mode='a', index=False, header=False)
    return None
