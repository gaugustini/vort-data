# vort-data

<p>
  <a href="https://opensource.org/licenses/MIT"><img alt="License" src="https://img.shields.io/github/license/gaugustini/vort"/></a>
  <a href="https://github.com/gaugustini"><img alt="Profile" src="https://img.shields.io/badge/-gaugustini-blue?logo=github"/></a> 
</p>

Armor data from Monster Hunter games used in the [Vort App](https://github.com/gaugustini/vort).

This repository contains data from the following games:
* Monster Hunter Freedom (f1)
* Monster Hunter Freedom Unite (fu)
* Monster Hunter Portable 3rd (p3)
* Monster Hunter 3 Ultimate (3u)
* Monster Hunter 4 (4)
* Monster Hunter 4 Ultimate (4u)
* Monster Hunter Generations (gen)
* Monster Hunter Generations Ultimate (gu)


## Data

*Note: The csv files use semicolons(;) instead of commas(,).*

All data were collected through the Athena's ASS data, they were formatted to be standardized and simple to use.

Data has not been fully reviewed and checked, however there are some known errors, check [issues](https://github.com/gaugustini/vort-data/issues) for more information, if you want to help see the [Contributing](#contributing) topic.

The files are organized in the same way in all games, for each game there is a folder that contains the files with the main data and a folder "languages" with files with names in different languages.


### Tables

For some data numbers were used instead of words:

* Gender:
    * 0 = Both (Male/Female)
    * 1 = Male
    * 2 = Female
    
* Type:
    * 0 = Both (Blademaster/Gunner)
    * 1 = Blademaster
    * 2 = Gunner

* Rarity:
    * 99 = X (Generations/Generations Ultimate Only)

For ranks with values "-1" means it is not available to get the item in that rank.

Most of the data has no translation to other languages, so there will be empty spaces in the language files.


#### Armor (Head, Body, Arms, Waist, Legs)

| Headers                                                | Description             |
| ------------------------------------------------------ |-------------------------|
| name                                                   | Armor name              |
| hr                                                     | Hunter rank             |
| village                                                | Village rank            |
| slots                                                  | Number of slots         |
| gender                                                 | Gender                  |
| type                                                   | Type of hunter          |
| rarity                                                 | Rarity of armor         |
| defense                                                | Minimal defense         |
| Element Resistance (Fire, Thunder, Dragon, Water, Ice) | Resistance value        |
| Skill Pairs                                            | Skill name and value    |
| Material Pairs                                         | Material name and value |


#### Decoration

| Headers                    | Description                         |
| -------------------------- |-------------------------------------|
| name                       | Decoration name                     |
| hr                         | Hunter rank                         |
| village                    | Village rank                        |
| slots                      | Number of slots                     |
| Skill Pairs                | Skill name and value                |
| Material Pairs             | Material name and value             |
| Alternative Material Pairs | Alternative material name and value |


#### Skill

| Headers | Description                  |
| ------- |------------------------------|
| name    | Skill name                   |
| family  | Skill tree                   |
| points  | Points to activate the skill |
| type    | Type of hunter               |


#### Language Files

| Headers  | Description      |
| -------- |------------------|
| english  | name in english  |
| spanish  | name in spanish  |
| french   | name in french   |
| german   | name in german   |
| japanese | name in japanese |
| chinese  | name in chinese  |


## Credits
* [AthenaADP](https://github.com/AthenaADP) - for all the data.
* [Monster Hunter Wiki](https://monsterhunter.fandom.com/), [Kiranico](https://kiranico.com/) - for eventual research.


## Contributing

If you want to contribute to the project and make it better, your help is very welcome. You can open an issue or submit a new pull request, for that follow the instructions below:

1. Fork the repo on GitHub
1. Clone the project to your own machine
1. Commit changes to your own branch
1. Push your work back up to your fork
1. Submit a Pull request


## License
```
MIT License

Copyright (c) 2022 Gustavo Augustini

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
