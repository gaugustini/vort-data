import os
import pandas as pd

game_path = './p3-athena/'
files = ['arms', 'body', 'component', 'decoration', 'head', 'legs', 'skill', 'waist']


def delete_file(filename):
    file_path = game_path + 'data/' + filename + '.csv'
    try:
        os.remove(file_path)
    except OSError as e:
        print("Error: %s : %s" % (filename, e.strerror))

def create_csv_file(filename):
    file_path_input_key = game_path + 'English (TeamHGG)/' + filename + '.txt'
    file_path_input_value = game_path + 'English (TMO)/' + filename + '.txt'
    file_path_output =  game_path + 'data/' + filename + '.csv'

    csv_input_key = pd.read_csv(file_path_input_key, sep='?', header=None, encoding='utf-8', dtype=object)
    csv_input_value = pd.read_csv(file_path_input_value, sep='?', header=None, encoding='utf-8', dtype=object)
    csv_output = pd.DataFrame()

    try:
        csv_output['key'] = csv_input_key
        csv_output['value'] = csv_input_value
    except Exception as e:
        print("Error: %s[%s]: %s" % (filename, column, e))
    
    csv_output.to_csv(file_path_output, index=False, sep=';', encoding='utf-8')

def main():
    for file in files:
        delete_file(file)
        create_csv_file(file)

if __name__ == '__main__':
    main()
