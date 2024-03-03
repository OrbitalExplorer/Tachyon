import os
import shutil

def prepareExport(basePath):
    def moveConfigFiles(basePath):
        print('Moving files to the yosbr/config folder... ')
        src_dir = os.path.sep.join(basePath) + os.path.sep + 'config' 
        dest_dir = src_dir + os.path.sep + 'yosbr' + os.path.sep + 'config'
        
        for config in os.listdir(src_dir):
            source_file = os.path.join(src_dir, config)
            dest_file = os.path.join(dest_dir, config)
            
            if config != 'yosbr':
                try:
                    shutil.move(source_file, dest_file)
                except IOError as e:
                    print("Fout bij kopiëren:", str(e))

    
    moveConfigFiles(basePath)
    

if __name__ == '__main__':
    prepareExport()