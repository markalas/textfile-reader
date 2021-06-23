# <h1 align=center> Textfile Reader </h1>
# Description
A text file reader that will match strings found in an input file

GUI app created with tkinter. The app traverses through a directory specified by userinput, finds .txt files, reads the first line of all .txt files and creates a dataframe.
Lines from the .txt files are then compared against an input file.

# Demo
<img src='https://media.giphy.com/media/8LhD9OvghLsxtbIFep/giphy.gif' width=50% height=auto >

# Usage
Clone this repository <br>
```
$ git clone
```
Run main.py <br>
```
$ python main.py
```
Select directory to traverse <br>
<img src='https://user-images.githubusercontent.com/73659708/123164679-43c6d900-d441-11eb-8f62-b74e72887167.png'> <br>

Select an excel input file with search values stored in column 1 <br>
<img src='https://user-images.githubusercontent.com/73659708/123164882-8092d000-d441-11eb-911c-73be3d6c9fd9.png'> <br>

Hit Run <br>
<img src='https://user-images.githubusercontent.com/73659708/123165472-470e9480-d442-11eb-8aed-e8e935007137.png'>

Output <br><br>
<img src='https://user-images.githubusercontent.com/73659708/123165326-175f8c80-d442-11eb-95e1-4e4f80bffff9.png'>

# Limitations
- Currently the app only looks for textfile mimetypes and read the first line

# Future Updates
- [ ] Allow user to select mimetypes
- [ ] Allow user to select output directory
- [ ] Allow app to find keywords in documents

# Libraries Used
- tkinter
- pandas
- csv
- mimetypes
- openpyxl
