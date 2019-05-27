class PasswordTool: # 密码工具类
    def __init__(self, password):
    # 类的属性       
        self.password = password
        self.strength_level = 0

    # 类的方法
    def process_password(self):
    # 规则1：密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位！')

    # 规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')

    # 规则3：包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母！')
   
    def check_number_exist(self):
    # 判断字符串中是否含有数字
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
    # 判断字符串中是否含有字母
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

class FileTools:
    def __init__(self, filename, filepath):
        self.filename=filename
        self.filepath=filepath
    
    def myread(self) -> str:
        myfile = open(self.filepath+self.filename,'r')
        mystr = myfile.read()
        myfile.close()
        return mystr

    def mywrite(self,str_to_write:str):
        myfile = open(self.filepath+self.filename,'a')
        myfile.write(str_to_write)
        myfile.close()


def main():
    try_times = 5
    while try_times > 0:
        password = input('请输入密码：')
        # 实例化密码工具对象
        password_tool = PasswordTool(password)

        password_tool.process_password()

        f = open('password_5.0.txt', 'a',encoding='utf-8')
        f.write('密码：{}, 强度：{}\n'.format(password, \
                                        password_tool.strength_level))
        f.close()

        if password_tool.strength_level == 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_times -= 1
            print()
        if try_times <= 0:
            print('尝试次数过多，密码设置失败！')

if __name__ == '__main__':
     main()


