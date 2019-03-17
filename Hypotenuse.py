import math

def cal_hypotenuse(leg1,leg2):
    sqr_leg1 = leg1**2
    sqr_leg2 = leg2 ** 2
    hyptonuse = math.sqrt(sqr_leg1+sqr_leg2)
    # print("Squared leg1 is:%d and Squared leg2 is:%d \n and Hypotenuse is : %f" % (sqr_leg1,sqr_leg2,hyptonuse))
    return hyptonuse

print('%.2f'%(cal_hypotenuse(2,3)))