from read_input import *
from random import shuffle

def gen_vert(vert):
    tags = sorted([(len(v.tag_set)," ".join(sorted(v.tag_set)), v.i) for v in vert])
    new_vert = []
    for i in range((len(tags) // 2) - 1):
        new_vert.append((tags[i][2], tags[-i - 1][2]))
    return new_vert


def main():
    photos = read_input()
    slides = []
    vert = []
    for p in photos:
        if p.horizontal:
            slides.append((p.i,))
        else:
            vert.append(p)
    all_tags = set([])
    for v in vert:
        all_tags = all_tags.union(v.tag_set)
    #print(len(all_tags))
    slides += gen_vert(vert)

    #print(len(vert))
    #for i in range(0, len(vert), 2):
    #    slides.append((vert[i].i, vert[i+1].i))
    shuffle(slides)
    print(len(slides))
    for s in slides:
        print(*s)


if __name__ == '__main__':
    main()


