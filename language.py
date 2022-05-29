import os
import glob
import pandas as pd

def get_dir_names(path):
    return [f.name.lower() for f in os.scandir(path) if f.is_dir() and f.name != '.git']

def get_games_name():
    return get_dir_names('./')

def get_languages_for_each_game(games):
    languages = {}
    for game in games:
        languages[game] = get_dir_names('./' + game + '/athena/languages')
    return languages

def get_files_from_a_game(game, languages, filename):
    files = {}
    for language in languages[game]:
        files[language] = './' + game + '/athena/languages/' + language.capitalize() + '/' + filename + '.txt'

    return files

def clear_files(games):
    for game in games:
        path = './' + game + '/data/**/*.csv'
        files = glob.glob(path, recursive=True)

        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))

def main(games, languages, filenames):
    language_columns = ['english', 'spanish', 'french', 'italian', 'german', 'japanese', 'chinese']
    for game in games:
        for filename in filenames:
            files = get_files_from_a_game(game, languages, filename)
            
            csv_output = pd.DataFrame()

            for language_column in language_columns:
                if language_column in files:
                    try:
                        csv_input = pd.read_csv(files[language_column], header=None, sep='?', encoding='utf-8')
                        csv_output[language_column] = csv_input
                        path_output = './' + game + '/data/languages/' + filename + '.csv'
                        csv_output.to_csv(path_output, index=False, sep=';', encoding='utf-8')
                    except Exception:
                        print(game + ': file: ' + files[language_column])
                else:
                    try:
                        csv_output[language_column] = ""
                        path_output = './' + game + '/data/languages/' + filename + '.csv'
                        csv_output.to_csv(path_output, index=False, sep=';', encoding='utf-8')
                    except Exception:
                        print(game + language_column)

if __name__ == '__main__':

    games = get_games_name()
    languages = get_languages_for_each_game(games)
    filenames = ['arms', 'body', 'components', 'decorations', 'head', 'legs', 'skills', 'waist']

    clear_files(games)
    main(games, languages, filenames)
