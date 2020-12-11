# https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
def addBorder(picture):
    bord = '*' * (len(picture[0])+2)
    for i,text in enumerate(picture):
        picture[i] = '*' + text + '*'
    picture.insert(0,bord)
    picture.append(bord)
    return picture
