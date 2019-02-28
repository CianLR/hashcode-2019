
class Photo:
    def __init__(self, i, orient, tags):
        self.i = i
        self.tags = tags
        self.tag_set = set(tags)
        self.orient = orient
        self.vertical = orient == 'V'
        self.horizontal = not self.vertical


def read_input():
    N = int(input())
    photos = []
    for i in range(N):
        o, _, *tags = input().split()
        photos.append(Photo(i, o, tags))
    return photos

