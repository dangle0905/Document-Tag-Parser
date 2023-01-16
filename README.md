# **Document_Tag_Parser**
An application created in Spring 2022 for CSULA's Senior Design Class. <br/>
![](https://github.com/dangle0905/devportfolio/blob/master/images/dtp.png)


### **Packages Used**

- pdf2image==1.16.0
- PyMuPDF==1.19.5
- pytesseract==0.3.8
- tk==0.1.0

### **Development setup**

1.  It is recommended to create a virtual environment for testing and installing dependencies. After cloning the code, use the following commands from within your project folder:

    1. Make sure you navigate into the project folder "Document_Tag_Parser" after cloning, then run the following to create the virtual environment. 
       1. > py -m venv env
    3. To activate use:
       1. > `./env/scripts/activate`
    4. If you're having an error saying that scripts are disabled on your system, you will need to run: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted` in the shell (may require you to run the shell with admin privileges). Once you give access, it should work.  
    5. In powershell, `(env)` should appear on the left in green
    6. Some commands may be different or not work at all. Typing the following will bring you out of the venv
       1. > `deactivate`

2.  After creating your virtual environment follow all the steps below:

    1.  Run the setup file:

        > `python setup.py develop`

    2.  The following command will install all required dependencies:

        > `python -m pip install -r requirements.txt`

    3. One last dependency is needed. Download the poppler Release 22.01.0-0 from here: https://github.com/oschwartz10612/poppler-windows/releases. Unzip it, drag and drop the whole thing into your virtual environment, into the scripts folder in the project: `/projectfolder/env/Scripts`. Make sure what you downloaded is inside the `Release` folder so that the path is now `/projectfolder/env/Scripts/Release-22.01.0-0`. The code will be looking in that specific path for poppler, and if it's not exactly correct an error will result. 
        

    4.  Start has been configured by the setup file, you can run the program using:
        > `my_start`
    5.  The program should open with a console window for debugging.

### **Building an executable**

1. Run the following:
   1. Rename the main `.py` file to extension `.pyw`. This tells windows to run it without the extra console window
   2. Then run:
      1. > `pyinstaller --onefile `document_tag_parser.pyw`
2. Additional notes:
   1. I found initially that using pyinstaller inside the virtual environment was fine, but recently it has caused errors. Try the other if one doesn't work. Further testing is needed.
   2. If you're having issues and need to recompile, you may need to delete the generated `__pycache__`, `dist`, and `build` folders that pyinstaller generates. Sometimes it causes problems.

### **General Troubleshooting**:

1.  If you run `my start` and nothing happens, an error has occurred. I found that the logo path usually causes this. Make sure it, and any code that depends on specific file locations is correct.
2.  Commands not being recognized: some commands in the virtual environment require `python -m` first, such as in step 2.2.
3.  For instances where an error occurs on start up, and the console window flashes for a brief second, open cmd and use:
    1.  > `cmd /k program_name.py`
2.  Even after installing all necessary packages, errors where packages are not found while running the app may occur. If all else fails, reach out to Luke or Dang. 

