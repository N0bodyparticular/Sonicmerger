current_repo = "R:/web/fusion"             # repo to copy into the htdocs folder.
htdocs_folder = "R:/XAMPP/htdocs"          # location of the htdocs folder.
update_interval = 15                       # update/check interval

import os, shutil, time

def check_files():
    global tree
    sourcetree = os.listdir(current_repo)
    targettree = os.listdir(htdocs_folder)

    for path in sourcetree:
            if os.path.isfile(current_repo + "/" + path):
                    # working on a file
                    if os.path.exists(htdocs_folder + "/" + path):
                            # file does exist.
                            targettime = os.path.getmtime(current_repo + "/" + path)
                            sourcetime = os.path.getmtime(htdocs_folder + "/" + path)

                            if targettime > sourcetime: # target was created before source - source is newer.
                                print("Updated " + htdocs_folder + "/" + path + ".")
                                shutil.copy(current_repo + "/" + path, htdocs_folder + "/" + path)
                                
                    else:
                        print("Created " + htdocs_folder + "/" + path + ".")
                        shutil.copy(current_repo + "/" + path, htdocs_folder + "/" + path)
                        
            else: # working on directory
                    if not os.path.exists(htdocs_folder + "/" + path):
                            os.mkdir(htdocs_folder + "/" + path)
                            print("Created " + htdocs_folder + "/" + path + ".")

    for path in targettree:
            if os.path.isfile(htdocs_folder + "/" + path):
                    if not os.path.exists(current_repo + "/" + path):
                            print("Removing stray file " + htdocs_folder + "/" + path + ".")
                            os.remove(htdocs_folder + "/" + path)
            else:
                    if not os.path.exists(current_repo + "/" + path):
                            print("Removing stray folder " + htdocs_folder + "/" + path + ".")
                            os.rmdir(htdocs_folder + "/" + path)
                    
                            

while 1:
                check_files()
                time.sleep(update_interval)
