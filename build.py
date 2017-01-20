dirroot = 'D:\\www\\github\\build'
sitetitle='Unknown'
publishdir = 'D:\\www\\github\\build\\publish'
siteroot='http://localhost/github/bokhua.github.io'
publishdir = 'D:\\www\\github\\bokhua.github.io'
#siteroot='https://bokhua.github.io'
templatename = 'default'

#######################################################

import sys
import os
import shutil
template = ''
content = ''
footer = ''

#cmd = sys.argv[1]
contentdir = dirroot + '\\content'
templatedir = dirroot + '\\template\\' + templatename
#publishdir = dirroot + '\\publish'
def init():
    print('init directory')

def buildtemplate():

	templatefile = templatedir + '\\' + 'template.html'
	global template
	with open(templatefile, 'r') as ofile:
		template = ofile.read()  
	template = template.replace('{{sitetitle}}', sitetitle).replace('{{siteroot}}', siteroot).replace('{{footer}}', footer)

	buildtemplatefiles('css')
	buildtemplatefiles('js')
	buildtemplatefiles('fonts')

def buildtemplatefiles(subdir):
	path = templatedir + '\\' + subdir
	newpath = publishdir + '\\' + subdir
	if not os.path.exists(newpath):
		os.mkdir(newpath)
	for x in os.listdir(path):
		shutil.copy2(path + '\\' + x, newpath + '\\' + x)


def build():
	# clearfolder(publishdir)
	buildtemplate()
	buildcontentfiles(contentdir)

def buildcontentfiles(dir):
	dirlist = os.listdir(dir)
	for x in dirlist:
		path = dir + '\\' + x
		buildcontentfile(path)
		if os.path.isdir(path) == True:
			buildcontentfiles(path)

def buildcontentfile(path):
	if path == os.path.realpath(__file__):
		return
	
	newpath = publishdir + path.replace(contentdir, '')

	if os.path.isdir(path):
		if not os.path.exists(newpath):
			os.mkdir(newpath)
			return 
	else:
		ext = os.path.splitext(path)[1]
		if ext == '.html':
			content = ''
			with open(path, 'r') as ofile:
				content = ofile.read()

			html = template.replace('{{content}}', content)
			with open(newpath, 'w') as ofile:
				ofile.write(html)
		else:
			shutil.copy2(path, newpath)

def clearfolder(dir):
	if os.path.exists(dir):
		shutil.rmtree(dir)
	if not os.path.exists(dir):
		os.mkdir(dir)

build()
# if(cmd == 'init'):
#     init()
# elif(cmd == 'build'):
# 	build()


