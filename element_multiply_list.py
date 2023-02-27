def ele_multipy_list(l):
  """This fun return multiplication of numberic value in list"""
    mlt = 1
    for i in l :
        if type(i) == int or type(i) ==float:
            mlt = mlt*i
    return mlt

l = [25,4,4.5,4.21,"asd","affa", 4+5j]
ele_list(l)
