# 练习 1：编写一个程序来读取文件并以大写形式（逐行）打印文件内容。执行该程序将如下所示：
# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#      BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#      SAT, 05 JAN 2008 09:14:16 -0500
# 您可以从 www.py4e.com/code3/mbox-short.txt 下载该文件

fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print(lx.upper())