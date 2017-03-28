import sys

from matplotlib_venn import venn2
from matplotlib import pyplot as plt

def get_unique_entry(file_object):
    l=[]
    for line in file_object:
        l.append(line.strip())
    
    return set(l)

# you can leave it empty if you don't want a figure title
figure_title=""

# Don't forget to change this file name when you create a new figure, otherwise it will overwrite.
savefile_name="genome cosmic overlap.pdf"

# leave set name empty if you prefer not to have
set1_name='genome'
set2_name='Cosmic'

set1 = get_unique_entry(open(sys.argv[1],"r"))
set2 = get_unique_entry(open(sys.argv[2],"r"))

print len(set1),len(set2)

# calculate intersections between sets

n10=set1 - set2
n11=set1 & set2
n01=set2 - set1

v = venn2([set1,set2], set_labels = ('A', 'B'))
v.get_patch_by_id('10').set_alpha(0.5)
v.get_patch_by_id('10').set_color('orange')
v.get_patch_by_id('01').set_alpha(0.5)
v.get_patch_by_id('01').set_color('orange')
v.get_patch_by_id('11').set_alpha(0.5)
v.get_patch_by_id('11').set_color('red')
v.get_label_by_id('10').set_text(str(n10))
v.get_label_by_id('11').set_text(str(n11))
v.get_label_by_id('01').set_text(str(n01))
v.get_label_by_id('A').set_text('')
v.get_label_by_id('B').set_text('')
v.get_label_by_id('A').set_size(20)
v.get_label_by_id('B').set_size(20)

plt.annotate(set1_name, xy = v.get_label_by_id('10').get_position(), xytext = (-30,-70), size = 'xx-large',
             ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.5', fc = 'lime', alpha = 0.3))

plt.annotate(set2_name, xy = v.get_label_by_id('01').get_position(), xytext = (30,-70), size = 'xx-large',
             ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.5', fc = 'lime', alpha = 0.3))
plt.title(figure_title,fontsize=24)
#plt.show()
plt.savefig(savefile_name)