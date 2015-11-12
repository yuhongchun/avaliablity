# -*- encoding: utf8 -*-
import os
import sys
import ftplib

class FTPSync(object):
    def __init__(self):
        self.conn = ftplib.FTP('121.40.x.x', 'yhc', 'yhc101')
        self.conn.nlst()              # 远端FTP目录，可以拉取或备份我们最近一天的数据
        os.chdir('c:/data/')          # 本地下载目录，建议在本地C盘或D盘建立data目录

    def get_dirs_files(self):
        ''' 得到当前目录和文件, 放入dir_res列表 '''
        dir_res = []
        self.conn.dir('.', dir_res.append)
        files = [f.split(None, 8)[-1] for f in dir_res if f.startswith('-')]
        dirs =  [f.split(None, 8)[-1] for f in dir_res if f.startswith('d')]
        return (files, dirs)

    def walk(self, next_dir):
        print 'Walking to', next_dir
        self.conn.cwd(next_dir)
        try:
            os.mkdir(next_dir)
        except OSError:
            pass
        os.chdir(next_dir)

        ftp_curr_dir = self.conn.pwd()
        local_curr_dir = os.getcwd()

        files, dirs = self.get_dirs_files()
        print "FILES: ", files
        print "DIRS: ", dirs
        for f in files:
            print next_dir, ':', f
            outf = open(f, 'wb')
            try:
                self.conn.retrbinary('RETR %s' % f, outf.write)
            finally:
                outf.close()
        for d in dirs:
            os.chdir(local_curr_dir)
            self.conn.cwd(ftp_curr_dir)
            if d in dirs[-1]:
                self.walk(d)
            '''
            我们的服务器保存了最近30天的数据，这个没必要全部进行下载，只需要下载最近刚建立
            的数据就行了，所以用到了dirs[-1],如果需要下载全部数据，则去掉if这两行代码。
            '''

    def run(self):
        self.walk('.')

def main():
    f = FTPSync()
    f.run()

if __name__ == '__main__':
    main()