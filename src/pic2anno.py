import cv2
import numpy as np


class AnnotationClass:
    """
    A class that contains the parameters of annotation.
    """

    def __init__(self):
        """

        """
        self.__8_bit_char = ['.', ',', '^', '*', '!', '?', '%', '#']
        self.__2_bit_char = [' ', '#']
        self.__bit_mode = '8'
        self.__threshold = 0
        self.__lines = list()
        self.__out_size = [50, 50]

    def convert_pic(self, filename):
        """
        Convert picture into string
        :param filename:
        :return:
        """
        assert self.__bit_mode is '2' or self.__bit_mode is '8'

        # read image as gray scale and resize it to target size
        img = cv2.imread(filename, 0)
        img = cv2.resize(img, tuple(self.__out_size))

        # TODO: need to add noise reduction feature

        if self.__bit_mode is '2':
            if self.__threshold != 0:
                _, img = cv2.threshold(img, self.__threshold, 1, cv2.THRESH_BINARY)
            else:
                # auto-threshold
                _, img = cv2.threshold(img, 0, 1, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            self.__lines = list()
            for l in img:
                self.__lines.append(''.join(list(map(lambda x: self.__2_bit_char[1-x], l))))

        else:
            img = np.round((img - img.min()) / (img.max() - img.min()) * 7).astype(np.uint8)
            self.__lines = list()
            for l in img:
                self.__lines.append(''.join(list(map(lambda x: self.__8_bit_char[7-x], l))))

    def print_lines(self):
        """

        :return:
        """
        for l in self.__lines:
            print(l)


def main():
    anno = AnnotationClass()
    anno.convert_pic('airplane.jpg')
    anno.print_lines()


if __name__ == "__main__":
    main()
