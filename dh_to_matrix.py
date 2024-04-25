import numpy as np # maths package


# create a transformation matrix from a dh table
# returns a function that takes an angle as a variable to calculate forward kinematics
def dh_to_matrix(d, alpha, r, offset=0):
    alpha = np.radians(alpha)
    offset = np.radians(offset)

    # the function that will be used for our forward kinematics
    def test(theta):
        theta = np.radians(theta)+offset
        return np.array([
            [np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), r * np.cos(theta)],
            [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), r * np.sin(theta)],
            [0, np.sin(alpha), np.cos(alpha), d],
            [0, 0, 0, 1]
        ])

    return test


def full_arm(t1, t2, t3, t4, t5, t6):
    dh_0_1 = dh_to_matrix(128.3 + 115, 90, 0)
    dh_1_2 = dh_to_matrix(30, 180, 280, 90)
    dh_2_3 = dh_to_matrix(20, 90, 0, 90)
    dh_3_4 = dh_to_matrix(140 + 105, 90, 0, 90)
    dh_4_5 = dh_to_matrix(28.5 + 28.5, 90, 0, 180)
    dh_5_6 = dh_to_matrix(105 + 130, 90, 0, 90)
    return dh_0_1(t1) @ dh_1_2(t2) @ dh_2_3(t3) @ dh_3_4(t4) @ dh_4_5(t5) @ dh_5_6(t6)

def get_euler_angles(dh):
    rotation = dh[:3,:3]
    return 0


if __name__ == '__main__':
    transform = full_arm(3.234, 9.099, 107.08, 211.91, 281.391,292.76)
    print(transform)
    print(transform[:3,:3])
