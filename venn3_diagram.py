import sys
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt


def get_unique_entry(file_object):
    l=[]
    for line in file_object:
        l.append(line.strip())
    
    file_object.close()
    return set(l)

# you can leave it empty if you don't want a figure title
figure_title="Tryptic peptide (0miss) overlap"

# Don't forget to change this file name when you create a new figure, otherwise it will overwrite.
savefile_name="trypticpep_pepAtlas_HiRIEF2_UUset_2017Feb.pdf"

# leave set name empty if you prefer not to have
set1_name='PeptideAtlas'
set2_name='A431 dataset'
set3_name='Tissues dataset'

set1 = get_unique_entry(open(sys.argv[1],"r"))
set2 = get_unique_entry(open(sys.argv[2],"r"))
set3 = get_unique_entry(open(sys.argv[3],"r"))

print len(set1),len(set2),len(set3)

v = venn3([set1,set2,set3],set_labels = ('A', 'B','C'))


# calculate intersections between sets
n100= set1 - (set2|set3)
n010= set2 - (set1|set3)
n001= set3 - (set1|set2)

n110= set1 & set2 - set3
n101= set1 & set3 - set2
n011= set2 & set3 - set1
n111= set1 & set2 & set3

print len(n100),len(n010),len(n001)
print len(n110),len(n101),len(n011),len(n111)
# Subset labels
v.get_label_by_id('100').set_text(str(len(n100)))
v.get_label_by_id('010').set_text(str(len(n010)))
v.get_label_by_id('001').set_text(str(len(n001)))

v.get_label_by_id('110').set_text(str(len(n110)))
v.get_label_by_id('101').set_text(str(len(n101)))
v.get_label_by_id('011').set_text(str(len(n011)))
v.get_label_by_id('111').set_text(str(len(n111)))

v.get_label_by_id('A').set_text(set1_name)
v.get_label_by_id('B').set_text(set2_name)
v.get_label_by_id('C').set_text(set3_name)

# Subset colors
v.get_patch_by_id('100').set_color('orange')
v.get_patch_by_id('010').set_color('red')
v.get_patch_by_id('110').set_color('blue')


# Subset alphas
v.get_patch_by_id('101').set_alpha(0.4)
v.get_patch_by_id('011').set_alpha(1.0)
v.get_patch_by_id('111').set_alpha(0.7)



# annotate sets
'''
plt.annotate(set1_name, xy = v.get_label_by_id('100').get_position(), xytext = (-30,-70), size = 'xx-large',
             ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.5', fc = 'lime', alpha = 0.3))

plt.annotate(set2_name, xy = v.get_label_by_id('010').get_position(), xytext = (30,-70), size = 'xx-large',
             ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.5', fc = 'lime', alpha = 0.3))

plt.annotate(set3_name, xy = v.get_label_by_id('001').get_position(), xytext = (-30,-70), size = 'xx-large',
             ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.5', fc = 'lime', alpha = 0.3))
'''

plt.title(figure_title,fontsize=24)
#plt.show()
plt.savefig(savefile_name)
