from PIL import Image,ImageFilter

img = Image.open('akash.jpg')

#img.thumbnail( (200,200) )

#img.filter( ImageFilter.BLUR ).show()

img_resize = img.resize( (100,100) )
img_resize.save( 'akash_resize.jpg' )
#img.show()

#img.show()
#print( img.size )



