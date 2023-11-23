from PIL import Image
from resizeimage import resizeimage

def resize_img(in_file, w_size):
    print(in_file)
    imgEdit  = Image.open(in_file)
    imgEdit = resizeimage.resize_width(imgEdit, w_size)
    imgGirada = imgEdit.transpose(Image.ROTATE_270)
    imgGirada.save(in_file, imgEdit.format)

    return imgGirada

# resize_img('media\images\989562828823.jpg', 300)