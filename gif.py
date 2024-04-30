import imageio.v2 as imageio
filenames=["flosketch.jpeg","floweroriginal.jpeg"]
images=[]
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('anim.gif',images,'GIF',duration=4)
