import os
import shutil

for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		print(os.path.join(root, name))
		src_file = "shark.png"
		dst_file = os.path.join(root, name)
		if os.path.samefile(src_file, dst_file) or dst_file.find("copy.py") > -1:
			continue
		shutil.copy(src_file, dst_file)