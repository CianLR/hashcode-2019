
class Photo:
    def __init__(self, orient, tags):
        self.tags = tags
        self.tag_set = set(tags)
        self.orient = orient
        self.vertical = orient == 'V'
        self.horizontal = not self.vertical


def read_input():
    N = int(input())
    photos = []
    for _ in range(N):
        o, _, *tags = input().split()
        photos.append(Photo(o, tags))
    return photos

