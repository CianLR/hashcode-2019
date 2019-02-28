from collections import defaultdict


class Photo:
    def __init__(self, i, orient, tags):
        self.i = i
        self.tags = tags
        self.tag_set = set(tags)
        self.orient = orient
        self.vertical = orient == 'V'
        self.horizontal = not self.vertical


def read_input():
    tag2photo = defaultdict(list)
    N = int(input())
    photos = []
    for i in range(N):
        o, _, *tags = input().split()
        p = Photo(i, o, tags)
        photos.append(p)
        for t in tags:
            tag2photo[t].append(p)
    return photos, tag2photo

