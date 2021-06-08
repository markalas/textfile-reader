import tkinter as tk
from tkinter import *
from tkinter import filedialog
import subprocess
import pandas as pd
import os
import csv
import numpy as np
import time
import datetime
import openpyxl

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

      # import run_viewer as dataframe using pandas
      self.my_list = []
      self.run_list = []
      self.required_cols = [1]
      self.run_viewer = pd.read_excel(self.open_input_file, engine='openpyxl')
      print(self.run_viewer)

      # Append Run ID column as string to a separate empty list called run_list
      for i in self.run_viewer['col1']:
         self.run_list.append(str(i))
      print(self.run_list)

      # Iterate through root directory 
      # Find files that end in .txt with os.walk   
      # append line 1 of .txt files to my_list

      self.root_dir = self.openfd

      for root, dirs, files in os.walk(self.root_dir, onerror=None):
         for filename in files:
            if filename.endswith('.txt'):
               self.file_path = os.path.join(root, filename)
               print(self.file_path)
               self.openfile = open(self.file_path, 'r', encoding="utf8", errors='ignore')
               self.content = self.openfile.readlines()
               self.my_list.append(self.content[0])
            else:
               break
            print(self.my_list)

      # Create dataframe of files in self.openfd
      
      self.output = datetime.datetime.now().strftime(self.output_dir + r"/output_%Y-%m-%d.csv")

      with open(self.output, 'w', newline='') as file:
         self.writer = csv.writer(file, delimiter="\n", quoting=csv.QUOTE_NONE)
         self.writer.writerow(self.my_list)
         print(self.output)

      self.output_csv = pd.read_csv(self.output, header=None, error_bad_lines=False)
      self.output_csv_df = pd.DataFrame(self.output_csv)
      print(self.output_csv_df)

      # Compare dataframes
      # Compare column ID to my_list

      def check_value(x):
         for i in self.my_list:
            if str(x) in i:
               return True
         return False
      
      self.output_csv_df['Match'] = self.output_csv_df[0].apply(check_value)
      self.output_csv_df.to_csv(self.output, index=False)

      #subprocess.call(['C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE','C:/Users/Mark/Documents/Coding Practice/Python/Python_Practice/Random_projects/output/output_%Y-%m-%d.csv'], shell=True)


################################################################
################# Application Instance #########################
################################################################

root = tk.Tk()
root.title('Completion Tracker')

app = Application(master=root)

app.mainloop()

################################################################
################# Application Instance #########################
################################################################

 