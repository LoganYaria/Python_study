import path_creating
import read_csv
import write_csv

path_import = path_creating.import_path()
file_to_write = read_csv.read_csv_fun(path_import)
path_export = path_creating.export_path()
write_csv.writing_csv(file_to_write,path_export)