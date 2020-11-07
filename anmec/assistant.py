import os
import time

time_delay = 1
project_path = "D:\\google_drive\\MIPT_AI\\draw_KD_v2\\pdf\\w1"
files = os.listdir(project_path) #+"figures")
files = [f for f in files if f[-3:] == "svg"]

# command = 'D:\\Apps\\Inkscape\\bin\\inkscape --export-type="pdf" --export-latex {}figures\\{}'
command = 'D:\\Apps\\Inkscape\\bin\\inkscape --export-type="pdf" --export-latex {}\\{}'

while True:
    if len(files[0]) > 1:
        start = time.time()
        for file in files:
            os.system(command.format(project_path, file))
            print("Updated {} files".format(file))
        tmp_dt = time.time() - start
        print("Time spent:\t{:.1f}s".format(tmp_dt))
        if tmp_dt > time_delay:
            time_delay = tmp_dt
    else:
        file = files
        os.system(command.format(project_path, file))
    print(".svg files updated")
    time.sleep(time_delay)
    break
