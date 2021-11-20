# (utils) Flutter languages strings manager
Python script generating languages.dart from xlsx file (or the other way around) to manage string in differents languages for a flutter app with LocalizationsDelegate

![1](screens/1.png)

# How to use ?

![2](screens/2.png)

Create strings.xlsx with Column headers [Title, LanguageCode1, ..., LanguageCodeN]

The second row needs to be #your_category_name

Then the variable name and its translations

![3](screens/3.png)

Run 'generate_languages_files.py' in the same folder to generate one languages.dart and the languages_LanguageCodeN.dart for each language

![4](screens/4.png)


To do it the other way around, first edit 'generate_strings_xlsx.py' to modify the line 'codes = ["en", "fr"]' with what you need (it needs to be the same as the column header names)

![a](screens/a.png) ![b](screens/b.png)

