import graphics as k
from tkinter.filedialog import asksaveasfilename as a


def openImage(image):
    img = k.Image(k.Point(0, 45), image)
    width = img.getWidth()
    height = img.getHeight() + 90
    img.move(width // 2, height // 2)
    win = k.GraphWin(image, width, height)
    win.setBackground('snow3')
    x = width//13
    y = height//18
    x2 = x + width//8
    y2 = y + height//18
    button1 = k.Rectangle(k.Point(x, y), k.Point(x2, y2))
    button1.draw(win).setFill("snow2")

    button2 = button1.clone()
    button2.move(width//6, 0)
    button2.draw(win)
    button3 = button2.clone()
    button3.move(width//6, 0)
    button3.draw(win)
    button4 = button3.clone()
    button4.move(width//6, 0)
    button4.draw(win)
    button5 = button4.clone()
    button5.move(width//6, 0)
    button5.draw(win)


    k.Text(button1.getCenter(), "Statistics").draw(win)

    k.Text(button2.getCenter(), "Black and White").draw(win)

    k.Text(button3.getCenter(), "Invert Color").draw(win)

    k.Text(button4.getCenter(), "Save Image").draw(win)

    k.Text(button5.getCenter(), "Quit").draw(win)


    img.draw(win)

    return img, win


def convertToNegative(img):
    print("Inverting color...")
    for col in range(img.getHeight()):
        for row in range(img.getWidth()):
            r, g, b = img.getPixel(row, col)
            img.setPixel(row, col, k.color_rgb(255 - r, 255 - g, 255 - b))
        k.update()
    print("  ...Done.")


def grayscale(img):
    # print the intro for the gray scale
     print("Converting to black and white...")
    # get every pixel
     for col in range(img.getHeight()):
        for row in range(img.getWidth()):
            (r, g, b) = img.getPixel(row, col)
            # make a calculations to change in to grayscale.
            gray = int(round(0.299*r + 0.587*g + 0.114*b))
            img.setPixel(row, col,k.color_rgb(gray,gray,gray))
            # update the picture for the gray scale.
        k.update()
     print("   ...Done.")

    # create a stats function
def stats(image):
    print("stats button has been pressed")

    print("image stats....")
    print("calculating image histogram")

    # create a list for the histogram

    nred = []
    ngreen = []
    nblue = []

    # initialize variables and create some lists

    count = 0
    sumred=0
    sumblue=0
    sumgreen=0
    # Create a histogram that contains 256 0's  for the 3 color
    for col in range(256):
        nred.append(0)
        nblue.append(0)
        ngreen.append(0)

        # gets every pixels
    for col in range(image.getHeight()):
        for row in range(image.getWidth()):
            r, g, b = image.getPixel(row, col)
            # count the number of red, blue and green bars in each pixel based on the brightness level.

            nred[r] += 1
            ngreen[g] += 1
            nblue[b] += 1
            count += 1

    print("\nCOUNT|", " " * 3, "RED |", " " * 2, "GREEN|", "BLUE\n" + "-----|---------|---------|-----")

    # print the histogram
    for i in range(256):
        print("{0:<5}{1:<6}{2:<4}{3:<5}{4:<5}{5:<3}{6:0}".format(i, "|", nred[i], "|", ngreen[i], "|", nblue[i]))
        sumred= sumred + nred[i]*i
        sumblue = sumblue + nblue[i] * i
        sumgreen = sumgreen + ngreen[i] * i

       
       # Calulate the mean of the rgb values.

    print("\nMean Red: ", sumred / count)
    print("Mean Green: ", sumgreen / count)
    print("Mean Blue: ", sumblue / count)
    print("Number of pixels in image: ", count)


def m(cat, image, win):
    x = cat.getX()
    y = cat.getY()
    width = image.getWidth()
    height = image.getHeight() + 90
    x1 = width//13

    y1 = height//18
    y2 = y1 + height//18

    xx = [x1]

    for i in range(9):

        if i % 2 == 0:
            e = width // 8
        else:
            e = width // 23

        xx.append(xx[i] + e)
    if xx[0] <= x <= xx[1] and y1 <= y <= y2:
        stats(image)
    elif xx[2] <= x <= xx[3] and y1 <= y <= y2:
        grayscale(image)
    elif xx[4] <= x <= xx[5] and y1 <= y <= y2:
        convertToNegative(image)
    elif xx[6] <= x <= xx[7] and y1 <= y <= y2:
        t = a()
        image.save(t + ".png")
        print("your image is saved")
    elif xx[8] <= x <= xx[9] and y1 <= y <= y2:
        win.close()


def main():
    try:

        inFile = input("\nEnter the name and extension of a GIF or PNG file to convert: ")
        image, win = openImage(inFile)
        while True:
            click = win.checkMouse()
            if click:
                m(click, image, win)
    except k.GraphicsError:
        print("\nclosed")
    except:
       print('Be sure to put in the correct file name')


main()
