import pandas as pd
import os

game_path = './gu/'
files = ['arms', 'body', 'head', 'legs', 'waist', 'decoration', 'skill']

columns_armor = ['name', 'hr', 'village', 'slots', 'gender', 'type', 'rarity', 'defense',
                'fire', 'thunder', 'dragon', 'water', 'ice',
                'skill_one', 'skill_one_points', 'skill_two', 'skill_two_points', 'skill_three', 'skill_three_points',
                'skill_four', 'skill_four_points', 'skill_five', 'skill_five_points',
                'material_one', 'amount_one', 'material_two', 'amount_two', 'material_three','amount_three',
                'material_four', 'amount_four']
columns_decoration = ['name', 'hr', 'village', 'slots', 'skill_one', 'skill_one_points',
                        'skill_two', 'skill_two_points', 'material_one', 'amount_one',
                        'material_two', 'amount_two', 'material_three', 'amount_three', 'material_four', 'amount_four',
                        'alt_material_one', 'alt_amount_one', 'alt_material_two', 'alt_amount_two',
                        'alt_material_three', 'alt_amount_three', 'alt_material_four', 'alt_amount_four']
columns_skill = ['name', 'family', 'points', 'type']

def delete_file(filename):
    file_path = game_path + 'data/' + filename + '.csv'
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

def main():
    for file in files:
        delete_file(file)
        if file == 'decoration':
            create_csv_file(file, columns_decoration)
        elif file == 'skill':
            create_csv_file(file, columns_skill)
        else:
            create_csv_file(file, columns_armor)

if __name__ == '__main__':
    main()
