# -*- coding: utf-8 -*-
import random

from flask import Flask, render_template, session, flash, url_for, redirect
from flask_wtf import Form
from wtforms import IntegerField, SubmitField
from wtforms.validators import Required, NumberRange
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY']='very hard to guess string' #secretkey 干嘛的？
bootstrap = Bootstrap(app) #初始化？发生了什么？


@app.route('/')
def index():
	session["number"]=random.randint(0,10) #session 数据类型是什么？ 
	session['times']= 3 #number，time 变量是什么？看上去像dict 的key
	return render_template('index.html') #render_template 自动去同路径下的templates文件夹找文件？
	
@app.route('/guess/',methods =['GET','POST']) #method=['GET','POST'] 写在需要输入数据的页面。
def guess():
	times = session['times']
	result = session.get("number")
	form = GuessNumberForm() #GuessNumberForm() 函数的用法？
	if form.validate_on_submit(): #.validate_on_submit() 用法？
		times -= 1
		session ['times'] = times
		if times == 0: #为什么在这判断？如果最后一次猜对了呢？
			flash(u'you lose','danger')
			return redirect(url_for('index'))#url_for()函数的参数是.html结尾的文件名吗？
		answer = form.number.data #.number.data() 用法？
		if answer < result:
			flash(u'too small, you have %s times left'%times, 'warning')
		elif answer > result:
			flash(u'too big, you have %s times left'%times, 'warning')
		else:
			flash(u'you win','success')
			return redirect(url_for('index')) #赢了回index。
		return redirect(url_for('guess2')) #输了回guess。	
	return render_template('guess2.html',form = form) #guess()返回一个guess，是空白的表格吗？

@app.errorhandler(404)
def page_not_found(e):
	flash('page not found')
	return render_template('404.html') #render_template 自动去同路径下的templates文件夹找文件？
	
class GuessNumberForm(Form): #定义新的类，继承自Form。 可是这个class该如何使用？为何先使用后定义？
	#用户输入数字？
	number = IntegerField(u'input a number (0~10):',validators=[#IntegerField() 用法？validators 用法？
		Required(u'input a valid number'), NumberRange(0,10,u'input a number between 0~10')])
	#Required(), NumberRange()用法？
	submit = SubmitField(u'submit') #SubmitField() 用法？

if __name__ == '__main__':
	app.run(debug=True)
	