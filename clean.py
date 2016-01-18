#-*- coding: utf-8 -*-
import os,shutil,getopt,sys
""" 编译器清理工具，开发辅助，用于 Visual Studio 编译产生的垃圾的清理。
支持命令行。
不同的需求自行修改全局设置 LDIR,LIGN,LEXT """
#软件版本
version=0.2
#待删除目录
LDIR=['debug','release','releaseu','debugu','ipch','_UpgradeReport_Files','DebugU','ReleaseU']
#忽略扫描的目录
LIGN=['.git','.svn']
#待删除的文件扩展名
LEXT=['ilk','iobj','ipdb','obj','log','pdb','properties','sdf','exp','user','aps']

#处理目录
#@d 处理的根目录
#@dm diplay message ? 
def _clean(d,dm=True):
    """Clean directory d, dependencied on global varible LDIR,LEXT,VERBOSE."""
    if not os.path.isdir(d):
        print d+" is not a directory,quit processing"
        return;
    d=os.path.abspath(d)
    if(dm):
        print "Preparing clean "+d
    sub=os.listdir(d);
    for f in sub:
        ff=os.path.join(d,f)
        # Delete folder 'Debug' and 'Release'
        if os.path.isdir(ff):
            if f.lower() in LIGN:
                if(dm):
                    print "Ignore directory "+ff
                continue
            if f.lower() in LDIR:
                shutil.rmtree(ff)
                if(dm):
                    print "Removed directory "+ff
            else:_clean(ff,dm)
        if os.path.isfile(ff):
            (name,ext)=os.path.splitext(f)
            if ext[1:].lower() in LEXT:
                os.remove(ff)
                if(dm):
                    print "Removed file "+ff
#显示命令帮助
def usage():
    """Display help text message"""
    print "    This is a developer utility for removing Visual Studio temporary files."
    print "Usage:"
    print "    python clean.py [-h -v] dir1 dir2..."
    print "Options:"
    print "    -h display this text."
    print "    -v display execution vebose message."
    print "Example:"
    print "    python clean.py -v d:\\exam e:\\code"
#主函数
def clean():
    verbose = False
    opts,args=getopt.getopt(sys.argv[1:],"hvVe:d:")
    for o,v in opts:
        if o == "-V":
            verbose=True
        elif o == "-h":
            usage()
            sys.exit(0)
        elif o == "-v":
            print version
            sys.exit(0)
    if 0==len(args):
        args.append(os.path.curdir)
    for a in args:
        _clean(a,verbose)
    print "Done."

if __name__ == "__main__":
    clean()
    
        
    
