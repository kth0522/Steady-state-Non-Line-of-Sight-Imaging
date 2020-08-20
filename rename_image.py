import os
import shutil

src_path = "/home/taehokim/workspace/project/NLOSRender/mnist_png"
dataset_path = "/home/taehokim/workspace/project/NLOSRender/mnist_dataset/"

for (path, dir, files) in os.walk(src_path):
	for filename in files:
		ext = os.path.splitext(filename)[-1]
		if ext == '.png':
			src_full_path = "{}/{}".format(path, filename)
			file_number = filename.split('.')[0]
			new_filename = "im%05d.png" % int(file_number)
			print(new_filename)			
			shutil.move(src_full_path, dataset_path+new_filename)
			
