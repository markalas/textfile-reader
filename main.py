import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd
import os
import csv
import numpy as np
import time
import datetime
import openpyxl
import mimetypes

class Application(tk.Frame):
   def __init__(self, master=None):
      super().__init__(master)
      self.master = master
      self.master.geometry('280x250')
      self.pack()  
      self.create_widgets()

   def create_widgets(self):
      self.label_1 = tk.Label(self, text="Select Target Location") 
      self.label_1.pack()
      self.entry_1 = tk.Entry(self, width=30, textvariable='')
      self.entry_1.pack()
      self.button_1 = tk.Button(self, width=15, text='Browse', command = self.browse_target_location)
      self.button_1.pack()

      self.label_2 = tk.Label(self, text="Select Input File")
      self.label_2.pack()
      self.entry_2 = tk.Entry(self, width=30, textvariable='')
      self.entry_2.pack()
      self.button_2 = tk.Button(self, width=15, text='Import', command = self.select_input_file)
      self.button_2.pack()

      self.button_3 = tk.Button(self, width=4, text='RUN', fg="blue", command = self.run_script)
      self.button_3.pack()

      self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
      self.quit.pack(side="bottom")

   def browse_target_location(self):       
      self.openfd = tk.filedialog.askdirectory()   
      self.entry_1.insert(tk.END, self.openfd)

   def select_input_file(self):
      self.open_input_file = tk.filedialog.askopenfilename()
      self.entry_2.insert(tk.END, self.open_input_file)
      print(self.open_input_file)

   def run_script(self):
      # Define current working directory and relative filepaths
      self.current_dir = os.curdir
      self.output_dir = os.path.join(self.current_dir, "output_files")

      # import run_viewer as dataframe using pandas; run_viewer contains values of interest
      self.oswalk_dict = {}
      self.run_list = []
      self.required_cols = [1]
      self.run_viewer = pd.read_excel(self.open_input_file, engine='openpyxl')

      # Append Run ID column as string to a separate empty list called run_list
      for i in self.run_viewer['col1']:
         self.run_list.append(str(i))

      # Iterate through root directory 
      # Find files that end in .txt with os.walk   
      # append line 1 of .txt files to my_list
      # Create dataframe containing content[0] and filepath for each

      self.root_dir = self.openfd

      for root, dirs, files in os.walk(self.root_dir, onerror=None):
         for filename in files:
            self.file_path = os.path.join(root, filename)
            self.filetypes = mimetypes.guess_type(self.file_path)
            for types in self.filetypes:
               if types == 'text/plain':
                  self.openfile = open(self.file_path, 'r', encoding="utf8", errors='ignore')
                  self.content = self.openfile.readlines()
                  self.oswalk_dict[self.content[0]] = self.file_path # store kv pairs to oswalk_dict
               else:
                  break
      print(self.oswalk_dict)

      # Create dataframe of files in self.root_dir
      self.output_columns = ['File_Content', 'File_Content_Dir']
      self.output = datetime.datetime.now().strftime(self.output_dir + r"/output_%Y-%m-%d.csv")
      
      # Transform self.oswalk_dict to .csv
      with open(self.output, 'w', newline='') as file:
         self.writer = csv.DictWriter(file, quoting=csv.QUOTE_NONE, fieldnames=self.output_columns)
         self.writer.writeheader()
         for key in self.oswalk_dict:
            self.writer.writerow({'File_Content': key, 'File_Content_Dir': self.oswalk_dict[key]})

      self.output_csv = pd.read_csv(self.output, error_bad_lines=False)
      self.output_csv_df = pd.DataFrame(self.output_csv)
      print(self.output_csv_df)

      # Compare dataframes
      # Compare column ID to my_list
      # Create new column 'File_Location' and store self.file_path

      def check_value(x):
         for i in self.oswalk_dict:
            if str(x) in i:
               return True
         return False
      
      self.output_csv_df['Match'] = self.output_csv_df['File_Content'].apply(check_value)
      self.output_csv_df = self.output_csv_df[['File_Content', 'Match', 'File_Content_Dir']]
      self.output_csv_df.to_csv(self.output, index=False)
      print(self.output_csv_df)

     
################################################################
################# Application Instance #########################
################################################################

root = tk.Tk()
root.title('File Content Matcher')

app = Application(master=root)

app.mainloop()

################################################################
################# Application Instance #########################
################################################################

 