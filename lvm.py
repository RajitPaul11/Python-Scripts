import os
print("      Welcome ~")
print("*********************")
def lvCreation(dev_name, vg_name, lv_name, size, dir_name):
  os.system(f'pvcreate {dev_name}')
  os.system(f'vgcreate {vg_name} {dev_name}')
  os.system(f'vgdisplay {vg_name}')
  os.system(f'lvcreate --size {size}G --name {lv_name} {vg_name}')
  os.system(f'mkfs.ext4 /dev/{vg_name}/{lv_name}')
  os.system(f'mount /dev/{vg_name}/{lv_name} {dir_name}')

def lvExtend( exdev_name, exvg_name, exsize, exlv_name):
  os.system(f'pvcreate /dev/{exdev_name}')
  os.system(f'vgextend {exvg_name} /dev/{exdev_name}')
  os.system(f'lvextend --size +{exsize}G /dev/{exvg_name}/{exlv_name}') 
  os.system(f'resize2fs /dev/{exvg_name}/{exlv_name}')
  os.system('df -h')
  
def lvReduce(reddir_name, redvg_name, redlv_name, redsize):
  os.system(f'umount {reddir_name}')
  os.system(f'e2fsck -f /dev/mapper/{redvg_name}-{redlv_name}')
  os.system(f'resize2fs /dev/mapper/{redvg_name}-{redlv_nmae} {redsize}G')
  os.system(f'lvreduce -L {redsize}G /dev/mapper/{redvg_name}-{redlv_name} -y')
  os.system(f'mount /dev/mapper/{redvg_name}-{redlv_name} /{reddir_name}')
  os.system('df -h')
  

while True:
  print("What do you want to go for?")
  user_Choice = input("Press 1 for LV Creation \nPress 2 for LV Extend \nPress 3 for LV Reduce \nPress e for exit")  
  if int(user_Choice) == 1:
    dev_name = input("Please enter the device name - ")
    vg_name = input("Please enter your VG name - ")
    lv_name = input("Please enter your LV name - ")
    size = input("Please enter the size of LV - ")
    dir_name = input('Please enter the directory you want to mount the LV to -')
    lvCreation(dev_name, vg_name, lv_name, size,  dir_name)
    os.system('sleep 4')
    os.system('clear')
  elif int(user_Choice) == 2:
    exdev_name = input("Please enter the new device name")
    exvg_name = input("Please enter the vg you want to extend")
    exlv_name = input("Please enter the lv you want to extend")
    exsize = input("Please enter the size you want to extend")  
    lvExtend(exdev_name, exvg_name, exsize, exlv_name)
    os.system('sleep 4')
    os.systyem('clear')
  elif int(user_Choice) == 3:
    reddir_name = input("Please enter the mounted dir")
    redvg_name  = input("Please enter the VG name you want to reduce")
    redlv_name = input("Please enter the LV name you want to reduce")
    redsize = input("Please enter the size you want to reduce")
    lvReduce(reddir_name, redvg_name, redlv_name, redsize)
    os.system('sleep 4')
    os.system('clear')
  elif user_Choice == "e":
    os.system(exit)
  else:
    print("Invalid Input! Please Try Again :D")
        

