from app.io.input import input_data_from_console, input_data_from_file, input_data_with_pandas
from app.io.output import output_data_to_console, output_data_to_file, output_data_with_pandas


def main():
    console_input = input_data_from_console()
    input_from_file = input_data_from_file('data/for_test.txt')
    input_data_from_file_pandas = input_data_with_pandas('data/for_test_pandas.csv')
    output_file = 'data/test_outputs.txt'
    output_data_to_console(console_input)
    output_data_to_file(console_input, output_file)
    output_data_to_console(input_from_file)
    output_data_to_file(input_from_file, output_file)
    output_data_to_console(input_data_from_file_pandas)
    output_data_to_file(input_data_from_file_pandas, output_file)
    output_data_with_pandas(input_data_from_file_pandas, output_file)


if __name__ == '__main__':
    main()
