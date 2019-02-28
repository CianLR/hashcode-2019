from read_input import *


def main():
    photos = read_input()
    slides = []
    vert = []
    for p in photos:
        if p.horizontal:
            slides.append((p.i,))
        else:
            vert.append(p)
    for i in range(0, len(vert), 2):
        slides.append((vert[i].i, vert[i+1].i))
    print(len(slides))
    for s in slides:
        print(*s)


if __name__ == '__main__':
    main()


