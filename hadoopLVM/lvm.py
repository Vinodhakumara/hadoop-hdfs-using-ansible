from os import system
from subprocess import getoutput
def create(crtDisk1,crtDisk2,crtVG="g1",crtLV="lv1",crtSize=0,crtDir="/testDir"):
    #system(f"pvcreate {crtDisk1}")
    #system(f"pvcreate {crtDisk2}")
    #system(f"vgcreate {crtVG} {crtDisk1} {crtDisk2}")
    #system(f"lvcreate --size {crtSize}G --name {crtLV} {crtVG}")
    #system(f"mkfs.ext4 /dev/mapper/{crtVG}-{crtLV}")
    try:
        system(f"mkdir {crtDir}")
    finally:
        system(f"mount /dev/mapper/{crtVG}-{crtLV} {crtDir}")
        system(f"df -Th")

def increase(incVG="g1",incLV="lv1",incSize=0):
    system(f"lvextend --size +{incSize}G /dev/mapper/{incVG}-{incLV}")
    system(f"resize2fs /dev/mapper/{incVG}-{incLV}")
    system(f"df -Th")



def decrease(decVG,decLV,decSize,decDir):
    system(f"umount {decDir}")
    system(f"e2fsck -f /dev/mapper/{decVG}-{decLV}")
    system(f"resize2fs /dev/mapper/{decVG}-{decLV} {decSize}G")
    system(f"lvreduce -L {decSize}G /dev/mapper/{decVG}-{decLV}")
    system(f"mount /dev/mapper/{decVG}-{decLV} {decDir}")
    system(f"df -Th")
