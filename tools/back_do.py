#后台执行相关命令
import paramiko
import os
import sqlite3
import sqlalchemy
class tools():
    def __init__(self):
        self.username = 'root'
        self.password = 'zdns@knet.cn'
        self.path = 'licenses'
        self.ip = '127.0.0.1'
        self.machineInfoPath = ''

    def sftp(self,machine_info_path, license_path,username='root',password='zdns@knet.cn' ):
        '''
        @采用scp方式复制machine.info 到本地然后制作好license再scp到目的IP服务器
        :param username: 用户名称
        :param password: 用户密码
        :param machine_info_path: machine info 地址
        :param license_path: 生成license 文件地址
        :return:
        '''
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip,22,username,password)
        sftp = ssh.open_sftp()
        sftp.get(machine_info_path)
        self.make_license()
        sftp.put(license_path)

        ssh.close()
        return "success to gen license"

    def checkout(self,name,machineFilePath):
        '''
        @检查文件路径
        name:用户名称
        machineFilePath like this: /etc/file
        '''
        #是否license文件路径存在

        dir = os.popen('ls /')
        if 'license' not in dir:
            os.popen('mkdir license')
        else:
            return "already exist"

    def make_license(self,orders):
        '''
        :param cmd:@
        :return:
        '''
        projectname = orders['projectname']
        dns = orders['dns']
        gslb = orders['gslb']
        dhcp = orders['dhcp']
        gslb = orders['gslb']
        stime = orders['stime']
        days = orders['days']
        remote_auth = orders['remote_auth']
        usr_license = orders['usr_license']
        control_node_num = orders['control_node_num']
        V = orders['V']
        user_name = orders['user_name']
        user_name = orders['user_name']
        device_type = orders['device_type']
        cmd1 = 'publisher -c license -p /etc/pub.key -q /etc/pri.key -i'
        order =''#已经组装好的其他参数

        cmd = cmd1 +order
        res = os.popen(cmd).readline()
        if res =="Don't use remote server to auth":
            return "success"
        else:
            return res

    def register(self):
        '''
        注册功能
        :param name: @type string用户名
        :param passwd @type string:
        :param email@type string :
        :return:
        '''
        if name==None:
            return "用户名是空的，请重新提交"
        elif passwd == None:
            return "密码是空的，请重新提交"
        elif email == None:
            return "需要输入邮箱账号！"
        else:
            #写入数据库
            pass
        pass
    def getUserFromDb(self):
        pass

    def licenseInfoToDB(self,orders):
        '''

        :param projectname: 项目名称，string
        :param dns: dns 权限
        :param gslb: gslb 权限
        :param dhcp:  dhcp 权限
        :param reg:
        :param stime:  开始时间
        :param days:  使用时间
        :param remote_auth: 远端鉴权
        :param usr_license:
        :param control_node_num:
        :param V:
        :param user_name:
        :param device_type:
        :return:
        '''
        #传入form 表单字典再处理
        projectname = orders['projectname']
        dns = orders['dns']
        gslb = orders['gslb']
        dhcp = orders['dhcp']
        gslb = orders['gslb']
        stime = orders['stime']
        days = orders['days']
        remote_auth = orders['remote_auth']
        usr_license = orders['usr_license']
        control_node_num = orders['control_node_num']
        V = orders['V']
        user_name = orders['user_name']
        user_name = orders['user_name']
        device_type = orders['device_type']
        pass

    def rootpw_decode(self,rootpw_encode):
        #去空格
        rootpw = rootpw_encode.strip()
        #调用命令解密
        cmd = '/usr/bin/root_password_change_priv' + ' '+rootpw
        res = os.popen(cmd).readline()
        #结果处理回传
        res = res.strip()
        return res

if __name__=="__main__":
    pass