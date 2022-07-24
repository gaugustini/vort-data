import pandas as pd
import numpy as np
import os

game_path = './gu/'
files = ['arms', 'body', 'head', 'legs', 'waist', 'decoration', 'skill']

columns_armor = ['name', 'skill_one', 'skill_two', 'skill_three', 'skill_four', 'skill_five',
                'material_one','material_two','material_three','material_four']
columns_decoration = ['name','skill_one', 'skill_two',
                'material_one', 'material_two', 'material_three','material_four',
                'alt_material_one','alt_material_two', 'alt_material_three', 'alt_material_four']
columns_skill = ['name', 'family']

def delete_file(filename):
    file_path = game_path + filename + '.csv'
    try:
        os.remove(file_path)
    except OSError as e:
        print("Error: %s : %s" % (filename, e.strerror))

def create_csv_file(filename, columns):
    file_path_input = game_path + filename + '.csv'
    file_path_output = game_path + 'data/' + filename + '.csv'

    csv_input = pd.read_csv(file_path_input, sep=',', encoding='utf-8', dtype=object)
    csv_output = pd.DataFrame()

    for column in columns:
        try:
            csv_output[column] = csv_input[column]

            if column == 'slots':
                csv_output[column] = csv_output[column].replace('---','0')
                csv_output[column] = csv_output[column].replace('O--','1')
                csv_output[column] = csv_output[column].replace('OO-','2')
                csv_output[column] = csv_output[column].replace('OOO','3')
            if column == 'gender':
                csv_output[column] = csv_output[column].replace('Male/Female','0')
                csv_output[column] = csv_output[column].replace('Male/ Female','0')
                csv_output[column] = csv_output[column].replace('Male','1')
                csv_output[column] = csv_output[column].replace('Female','2')
            if column == 'type':
                csv_output[column] = csv_output[column].replace('Blade/Gunner','0')
                csv_output[column] = csv_output[column].replace('Blade/ Gunner','0')
                csv_output[column] = csv_output[column].replace(np.nan,'0')
                csv_output[column] = csv_output[column].replace('Blade','1')
                csv_output[column] = csv_output[column].replace('Gunner','2')
            if column == 'hr' or column == 'village':
                csv_output[column] = csv_output[column].str.split('!').str[0]
                csv_output[column] = csv_output[column].replace('99','-1')
            if column == 'rarity':
                csv_output[column] = csv_output[column].replace('X','99')

        except Exception as e:
            print("Error: %s[%s]: %s" % (filename, column, e))

    csv_output.to_csv(file_path_output, index=False, sep=';', encoding='utf-8')

def replace_names(filename, columns):
    # For fu and p3
    # file_path_reference = './p3-athena/data/' + filename + '.csv'
    # file_path_skill_reference = './p3-athena/data/skill.csv'
    # file_path_material_reference = './p3-athena/data/component.csv'

    # For others game
    file_path_reference = game_path + 'data/languages/' + filename + '.csv'
    file_path_skill_reference = game_path + 'data/languages/skill.csv'
    file_path_material_reference = game_path + 'data/languages/component.csv'

    file_path_input = game_path + 'data/' + filename + '.csv'
    file_path_output = game_path + filename + '.csv'

    csv_reference = pd.read_csv(file_path_reference, sep=';', encoding='utf-8', dtype=object)
    csv_skill_reference = pd.read_csv(file_path_skill_reference, sep=';', encoding='utf-8', dtype=object)
    csv_material_reference = pd.read_csv(file_path_material_reference, sep=';', encoding='utf-8', dtype=object)
    csv_input = pd.read_csv(file_path_input, sep=';', encoding='utf-8', dtype=object)
    csv_output = pd.DataFrame()

     # For fu and p3
    # dict_ref = csv_reference.set_index('key')['value'].to_dict()
    # dict_skill_ref = csv_skill_reference.set_index('key')['value'].to_dict()
    # dict_material_ref = csv_material_reference.set_index('key')['value'].to_dict()

    # For others game
    dict_ref = csv_reference.set_index('japanese')['english'].to_dict()
    dict_skill_ref = csv_skill_reference.set_index('japanese')['english'].to_dict()
    dict_material_ref = csv_material_reference.set_index('japanese')['english'].to_dict()

    for column in columns:
        try:
            csv_input[column] = csv_input[column].replace(dict_ref)
            csv_input[column] = csv_input[column].replace(dict_skill_ref)
            csv_input[column] = csv_input[column].replace(dict_material_ref)
        except Exception as e:
            print("Error: %s[%s]: %s" % (filename, column, e))

    csv_output = csv_input
    csv_output.to_csv(file_path_output, index=False, sep=';', encoding='utf-8')


def main():
    for file in files:
        delete_file(file)
        if file == 'decoration':
            replace_names(file, columns_decoration)
        elif file == 'skill':
            replace_names(file, columns_skill)
        else:
            replace_names(file, columns_armor)

if __name__ == '__main__':
    main()
