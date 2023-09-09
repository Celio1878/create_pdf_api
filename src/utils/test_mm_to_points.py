from mm_to_points import mm_to_points

pdf_max_height = 793.7025372969326


def test_mm_to_point():
    assert mm_to_points(1) == 2.8346519189176163
    assert mm_to_points(2) == 5.6693038378352325
    assert mm_to_points(3) == 8.50395575675285
    assert mm_to_points(4) == 11.338607675670465
    assert mm_to_points(5) == 14.173259594588082
    assert mm_to_points(280) == pdf_max_height
