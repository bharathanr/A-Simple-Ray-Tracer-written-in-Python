import Image

def save_bmpOrtho(name, buf, image_size):
    image = Image.new("RGB", image_size)
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            image.putpixel((i,j), buf[i * image_size[1] + j])
    image.save(name + ".bmp")

def save_bmp(name, buf, image_size):
    image = Image.new("RGB", image_size)
    for i in xrange(image_size[0]):
        for j in range(image_size[1]):
            image.putpixel((i , 767 - j), buf[i * image_size[1] + j])
    image.save(name + ".bmp")

if __name__ == "__main__":
    #Test code
    buf = []
    i = 0
        
    while (i < 1024*768):
        buf.append((0, 255, 0))
        i += 1
    
    save_bmp("test", buf)
