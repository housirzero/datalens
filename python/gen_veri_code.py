import random
# 生成随机验证码，长度=len 
def generate_verification_code(len):
    ''' 随机生成 len 位的验证码 '''
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91): # A-Z
        code_list.append(chr(i))
    for i in range(97, 123): # a-z
        code_list.append(chr(i))
 
    myslice = random.sample(code_list, len)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice) # list to string
    # print code_list
    # print type(myslice)
    return verification_code