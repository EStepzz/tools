from tools.logger import Log
from flask import render_template,session, request, redirect,url_for,Blueprint,Response,abort
from tools.back_do import *
from tools.models import User
import time
from tools import db
from functools import wraps
tool_app = Blueprint('tool_app',__name__,template_folder='templates')

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not 'user' in session:
            abort(401)
        return func(*args, **kwargs)

    return decorated_function
@tool_app.route('/register',methods=['GET','POST'])
def registe_user():
    if request.method=='GET':
        return render_template('register.html')
    elif request.method=='POST':
        paras = request.form
        name = paras['name']
        passwd = paras['passwd']
        email = paras['email']

        result = User.query.filter_by(username = name).first()
        print(result)
        data = User(username=name,email=email,time=time.time())
        data.hash_password(passwd)
        if result == None:
            db.session.add(data)
            db.session.commit()
            Log.debug("注册成功")

            return redirect(url_for('tool_app.login'))

        else:
            return "用户已注册"
@tool_app.route('/',methods=["GET","POST"])
@tool_app.route('/index',methods=["GET","POST"])
@tool_app.route('/login',methods=["GET",'POST'])
def login():
    '''登录，创建用户'''
    if request.method=="GET":
        name =  request.cookies.get('name')
        if name == session['name']:
            return redirect(url_for('tools_app.license'))
        else:
            return render_template('login.html')
    elif request.method=="POST":
        paras = request.form
        username = paras['name']
        passwd = paras['passwd']
        #调用查询命令
        result  = User.query.filter_by(username=username).first()

        if not result:
            return "未注册该用户"
        if result.verify_password(passwd):
            res = Response('add cookies')
            res.set_cookie('name',value=username,expires=time.time()+6*60)
            return redirect(url_for('tool_app.licenseInfo'))
        else:
            return "用户名或密码不正确"


@tool_app.route('/license',methods=["POST"])
@login_required
def licenseInfo():
    print("******")
    postParams = request.form
    for i in postParams:
        if postParams[i] == None:
            postParams[i] = 0
        else:
            continue
    content = '-N '+postParams['dns']+'-A'+postParams['gslb']+ '-H '+\
              postParams['dhcp']+'-R '+postParams['reg']+postParams['stime']+\
              postParams['days']+postParams['auth']+postParams['root_change_password']+ \
              postParams['usr_license']+postParams['control_node_num']+postParams['T']+postParams['V']+\
              '-U '+postParams['user_name']+'-t '+postParams['t']+'-M '+postParams['device_type']
    print (content)
    return "<p>提交成功</p>"

@login_required
@tool_app.route('/getlicense',methods=['GET','POST'])
def rootpassword():
    if request.method =="GET":
        return render_template('base.html')
    else:
        params = request.form
        rootpw = params['rootpw']
        result = tools.rootpw_decode(rootpw)
        return "<h3>{}</h3>".format(result)



