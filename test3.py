from win32api import *
  
def get_version_number(file_path):
  
    File_information = GetFileVersionInfo(file_path, "\\")
  
    ms_file_version = File_information['FileVersionMS']
    ls_file_version = File_information['FileVersionLS']
  
    return [str(HIWORD(ms_file_version))]
  
file_path = r'C:\Program Files\Fortinet\FortiClient\FortiClient.exe'
  
version = ".".join(get_version_number(file_path))
  
print(version)
version2 = int(version)

if version2 < 9:
    print("Es menor")

if version2 > 6:
    print("Es Mayor")