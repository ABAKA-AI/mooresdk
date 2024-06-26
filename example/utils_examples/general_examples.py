# -*-coding:utf-8 -*-
import moore


def test_str2dict():
    dict_string = '{"k1": "v1", "k2": "v2", "k3": "v3"}'
    test_dict = moore.str2dict(dict_string)
    print(test_dict)
    print(type(test_dict))


def test_getkey():
    test_dict = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    key = moore.get_key(test_dict, 'v1')
    print(key)


def test_chunks():
    points = [1,2,3,4,5,6,7,8,9,10,11,12]
    test_points1 = moore.chunks(points, 2)
    test_points2 = moore.chunks(points, 3)
    print(test_points1)
    print(test_points2)


def test_find_nth():
    test_string = 'aaabcdefghiiijk'
    index = moore.find_nth(test_string, 'l', 2)
    print(index)


def test_find_last():
    test_string = 'aaabcdefghiiijk'
    index = moore.find_last(test_string, 'l')
    print(index)


def test_to_bytes():
    test_string = 'aaabcdefghiiijk'
    byte = moore.s2bytes(test_string)
    print(byte)


def test_to_string():
    test_string = b'aaabcdefghiiijk'
    string = moore.b2string(test_string)
    print(string)


def test_cal_distance():
    point_a = [12, 45]
    point_b = [104, 84]
    dis = moore.cal_distance(point_a, point_b)
    print(dis)


def test_cal_angle():
    point_a = [0, 0]
    point_b = [-2, -2]
    angle = moore.cal_angle(point_a, point_b)
    print(angle)


def test_cutFrames():
    infile_name = '../example_file/videos/test.mp4'
    outfile_name = '../example_file/images/cutframes'
    moore.cutFrames(infile_name, outfile_name, 10)


if __name__ == '__main__':
    test_chunks()