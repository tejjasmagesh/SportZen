from flask import Flask,redirect,url_for,render_template,request,session,flash
import nltk


from nltk.chat.util import Chat, reflections
import mysql.connector as m
con=m.connect(host='localhost',user='admin',passwd='mag26751!',database='hello')


cursor=con.cursor()


from datetime import timedelta

app = Flask(__name__)
app.secret_key="hello"
app.permanent_session_lifetime = timedelta(minutes=10)




reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Sports-Zen. You can call me BEE!",]
    ],
    [
        r"I would like to book an arena ?",
        ["which arena would you like to book?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Do you need anything else?:)",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Someone created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Bangalore, Karnataka',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2"]
    ],
    ]

#
#
#
#
#
print('a')
home="http://localhost:5000/"
@app.route('/',  methods=["POST","GET"])
def home():

	if request.method=='POST':

	    print("Hi! I am a chatbot created by SportZen for your service")
	    chat = Chat(pairs, reflections)
	    while True:
	        msg = request.form['msg']
	        y=chat.respond(msg)
	        return render_template("index.html",response=y)
	        if msg in 'byeGoodbye':
	            y=chat.respond(msg)
	            return render_template("index.html",response=y)
	            break
	else:
		return render_template("index.html" )

@app.route('/signup/', methods=["POST","GET"])

def signup():
	if request.method == "POST" :
		session.permanent=True
		user1=request.form["username"]
		pas_login=request.form['password']
		dat=request.form['date']
		pas2=request.form['passs']
		mail=request.form['email']
		num=request.form['number']
		nam=request.form['name']
		add=request.form['address']
		cit=request.form['city']
		countr=request.form['country']
		pinc=request.form['pin']
		cursor.execute('select * from creds')
		data=cursor.fetchall()
		for i in data:
			if user1==i[0]:
				msg_used="This username is Already in use!"
				return render_template("signup.html",msg=msg_used)
			elif mail==i[2]:
				msg_use='This email Id is already in use!'
				return render_template("signup.html",msg=msg_use)
			else:
				continue
		if user1=='' or pas_login=='' or pas2=='' or mail=='' or num=='' or nam=='' or dat=='':
			msg1='Please enter all the * marked details!'
			return render_template("signup.html",msg=msg1)
		if pas_login!=pas2:

			msg_wrong='password does not match!'
			return render_template("signup.html",msg=msg_wrong )

		st="insert into creds values('{}', '{}', '{}', '{}','{}','{}','{}','{}','{}','{}','{}')".format(user1,pas_login,mail,num,dat,nam,add,cit,countr,pinc,'')
		cursor.execute(st)

		cursor.execute('create table {}(arena varchar(30),date varchar(30),duration varchar(30),cost varchar(30), links varchar(1000), time varchar(30) )'.format(user1+'mybook',))
		con.commit()
		return redirect(url_for("login"))

	
	if "user" in session : #checks if user is logged in

		return redirect(url_for("user"))	
	return render_template('signup.html')

@app.route('/login/', methods=["POST","GET"])

def login():
	if request.method == "POST" :
		session.permanent=True
		user=request.form["email"]
		pas_login=request.form['password']
		cursor.execute('select * from creds')
		data=cursor.fetchall()
		a=''
		admin=open('auth.txt','w')
		y=admin.write(user)
		admin.close()


		admin1=''
	
		for i in data:
			if i[2]==user and i[1]==pas_login:
				a=True
				session['user']=user

				if i[2]=='admin@sportzen.com' and i[1]=='adminpassword':
					
					session['user']=user
					if session["user"]=='admin@sportzen.com':

						return redirect('/admin')
				elif a:
					user1=session['user']
		
					for y in data :
						if y[2]==user1:
							username=y[0]
							name=y[5]
							dob=y[4]
							ph=y[3]
							mail=y[2]
							add=y[6]
							city=y[7]
							country=y[8]
							pinc=y[9]
							return render_template("user.html",user2=username,name=name,dob=dob,ph=ph,mail=mail,address=add,city=city,country=country,pinc=pinc)
			else:
				continue

		
			



			
		
		
		msg_wrong="Invalid email or password"
		return render_template('login.html',msg=msg_wrong)
		msg_wrong=''



	else:

		if "user" in session : #checks if user is logged in
			flash("Already Logged In")
			return redirect(url_for("user"))	
		return render_template('login.html')
   
@app.route('/edit/', methods=["POST","GET"])
def edit():
	if "user" in session:# checks if user i logged in , if looged in redirects to usr page
		user1=session["user"]
		if request.method=='POST':
			about2=request.form['about1']
			use1=request.form['user3']
			email=request.form['username']
			name=request.form['name']
			address=request.form['address']
			country=request.form['country']	
			phone=request.form['ph']
			pin=request.form['pin']
			city=request.form['city']


			st="update creds set address='{}' where username='{}'".format(address,use1)
			cursor.execute(st)
			cursor.execute("update creds set phone='{}' where username='{}'".format(phone,use1))
			cursor.execute("update creds set email='{}' where username='{}'".format(email,use1))
			cursor.execute("update creds set name='{}' where username='{}'".format(name,use1))
			cursor.execute("update creds set country='{}' where username='{}'".format(country,use1))
			cursor.execute("update creds set pincode='{}' where username='{}'".format(pin,use1))
			cursor.execute("update creds set city='{}' where username='{}'".format(city,use1))
			cursor.execute("update creds set about='{}' where username='{}'".format(about2,use1))
			con.commit()
			st='select * from creds'
			cursor.execute(st)
			data=cursor.fetchall()		
			for y in data :

				if y[2]==user1:
					username=y[0]
					name=y[5]
					dob=y[4]
					ph=y[3]
					mail=y[2]
					add=y[6]
					city=y[7]
					country=y[8]
					pinc=y[9]
					about1=y[10]
					return render_template("user.html",user2=username,name=name,dob=dob,ph=ph,mail=mail,address=add,city=city,country=country,pinc=pinc,about=about1)						
		st='select * from creds'
		cursor.execute(st)
		data=cursor.fetchall()		
		for y in data :

			if y[2]==user1:
				username=y[0]
				name=y[5]
				dob=y[4]
				ph=y[3]
				mail=y[2]
				add=y[6]
				city=y[7]
				country=y[8]
				pinc=y[9]
				about1=y[10]
				return render_template("edit.html",user2=username,name=name,dob=dob,ph=ph,mail=mail,address=add,city=city,country=country,pinc=pinc,about=about1)

	else:
		flash("you are not logged in")
		return redirect(url_for("login"))		

@app.route('/user/', methods=["POST","GET"])
def user():
	if "user" in session:# checks if user i logged in , if looged in redirects to usr page
		user1=session["user"]
			
		st='select * from creds'
		cursor.execute(st)
		data=cursor.fetchall()		
		for y in data :

			if y[2]==user1:
				username=y[0]
				name=y[5]
				dob=y[4]
				ph=y[3]
				mail=y[2]
				add=y[6]
				city=y[7]
				country=y[8]
				pinc=y[9]
				return render_template("user.html",user2=username,name=name,dob=dob,ph=ph,mail=mail,address=add,city=city,country=country,pinc=pinc)
		


	else:
		flash("you are not logged in")
		return redirect(url_for("login"))

@app.route('/passchange', methods=['POST','GET'])
def passchange():
	if "user" in session:# checks if user i logged in , if looged in redirects to usr page
		user1=session["user"]
		st='select * from creds'
		cursor.execute(st)
		data=cursor.fetchall()
		for y in data :

			if y[2]==user1:
				name=y[5]
		if request.method=='POST':	
			curpas=request.form['curpas']
			conpas=request.form['conpas']
			newpas=request.form['newpas']
			st='select * from creds'
			cursor.execute(st)
			data=cursor.fetchall()
			for y in data :

				if y[2]==user1:
					username=y[5]
					use1=y[0]
					if y[1]!=curpas:
						msg='Please check your Current password'
						return render_template("passchange.html",msg=msg)
					if conpas!=newpas:
						msg='New password and confirm password do not match'
						return render_template("passchange.html",msg=msg)

			cursor.execute("update creds set password='{}' where username='{}'".format(newpas,use1))
			con.commit()
			return redirect(url_for('user'))
		return render_template("passchange.html",name=name)

	else:
		flash("you are not logged in")
		return redirect(url_for("login"))
@app.route('/admin', methods=["POST","GET"])

def admin():
    if "user" in session:
    	if session['user']=='admin@sportzen.com':
    		return render_template("admin.html" )
    	else: 
    		return render_template("404.html" )
    return render_template('404.html')

@app.route('/admin/table')
def table():
    if "user" in session:
    	if session['user']=='admin@sportzen.com':
    		return render_template("tables.html" )
    	else: 
    		return render_template("404.html" )

    return render_template("404.html")
@app.route('/admin/charts')
def chart():
    if "user" in session:
    	if session['user']=='admin@sportzen.com':
    		return render_template("charts.html" )
    	else: 
    		return render_template("404.html" )

    return render_template("404.html")
@app.route('/forgot', methods=["POST","GET"])

def forgot_password():
	if request.method == "POST" :
		session.permanent=True
		user1=request.form["email"]
		ph=request.form['phone']
		
		pas2=request.form['pass']
		pas1=request.form['pass1']
		if user1=='' or pas1=='' or pas2=='' or ph=='' :

			msg1='Please enter all the * marked details!'
			return render_template("forgot-password.html",msg=msg1)
		if pas1!=pas2:
			msg_wrong='password does not match!'
			return render_template("forgot-password.html",msg=msg_wrong )
		cursor.execute('select * from creds')
		data=cursor.fetchall()
		check=0
		y=len(data)
		for i in data :
			if i[2]==user1 :
				continue
			elif i[2]!=user1:
				check+=1
			else:
				continue
			if check==y-1:
				continue
			else:
				msg='User/Email does not exist'
				return render_template("forgot-password.html",msg=msg)
		for i in data:
			if i[2]==user1 and i[3]==ph:
				st="update creds set password='{}' where email='{}' and phone='{}'"  .format(pas1,user1,ph)
				cursor.execute(st)
				con.commit()
				check
				return render_template("login.html" )	
			else:
				continue

		

	return render_template("forgot-password.html" )
@app.route('/logout/')
def logout():
	session.pop("user","info")

	
	return redirect(url_for("login"))
@app.route('/admin/delete', methods=["POST","GET"])
def delete(): 
    if "user" in session:
    	if session['user']=='admin@sportzen.com':
    		st='select * from creds'
    		cursor.execute(st)
    		data=cursor.fetchall()

    		if request.method == "POST" :
    			session.permanent=True
    			option=request.form.getlist('options')
    			for i in option:
    				st1='delete from creds where username="{}"'.format(i)
    				cursor.execute(st1)
    				cursor.execute('drop table {}'.format(i+'mybook'))
    				con.commit()
    				msg="User(s) Succesfully Deleted!"

    				#______________________________________________________
		    		st='select * from creds'
		    		cursor.execute(st)
		    		data=cursor.fetchall()

    				return render_template("delete1.html",value=data,msg=msg)
    		return render_template("delete1.html",value=data)
    else:
    	return render_template("404.html")

@app.route('/test', methods=["POST","GET"])
def chat():
	if request.method=='POST':

	    print("Hi! I am a chatbot created by SportZen for your service")
	    chat = Chat(pairs, reflections)
	    while True:
	        msg = request.form['mess']
	        y=chat.respond(msg)
	        return render_template("chatbot.html",msg=y)
	        if msg in 'byeGoodbye':
	            y=chat.respond(msg)
	            return render_template("chatbot.html",msg=y)
	            break
	else:
		return render_template("chatbot.html")


@app.route('/404')
def u():
	return render_template("404.html")

@app.route('/book',  methods=["POST","GET"])
def book():
    if "user" in session:
    	y='select * from creds'
    	cursor.execute(y)
    	data=cursor.fetchall()
    	for i in data:
    		if i[2]==session['user']:
    			temp=i[0]
    	user10=temp.strip('"')
    	try:
    		cursor.execute('drop table {}'.format(user10,))
    		con.commit()
    	except:
    		print('a')
    	if request.method=='POST':
    		cursor.execute('select * from creds')
    		data=cursor.fetchall()
    		for i in data:
    			if i[2]==session['user']:
    				temp=i[0]
    		user10=temp.strip('"')
    		area=request.form['location']
    		date=request.form['date']
    		time=request.form['time']
    		duration=request.form['hours']

    		try:
    			cursor.execute('create table {} (location varchar(20), date varchar(20), duration varchar(20),time varchar(20))'.format(user10,))
    			con.commit()
    		except:
    			print('a')

    		cursor.execute("insert into {} values('{}','{}','{}','{}')".format(user10,area,date,duration,time))
    		con.commit()

    		if area=='' or date=='' or time=='' or duration=='':
    			msg='please enter all the details'
    			return render_template('book.html',msg=msg)
    		if duration=='0':
    			msg='Duration Cannot be 0 hrs'
    			return render_template('book.html',msg=msg)
    		return redirect(url_for('booking'))
    	
    	return render_template('book.html')
    else:
    	return redirect(url_for("login"))
@app.route('/booking',  methods=["POST","GET"])
def booking():
    if "user" in session:
    	cursor.execute('select * from creds')
    	data=cursor.fetchall()
    	for i in data:
    		if i[2]==session['user']:
    			temp=i[0]
    			usename=i[5]
    			email=i[2]

    	user10=temp.strip('"')
    	try :
    		use=user10+'book'
    		cursor.execute("drop table {}".format(use,))
    		con.commit()
    	except:
    		print('a')
    	cursor.execute('show tables')
    	y=cursor.fetchall()
    	for i in y:
    		for j in i:
    			if user10==j:
			    	cursor.execute('select * from {}'.format(user10,))

			    	dat=cursor.fetchall()    	
			    	area=dat[0][0]
			    	date=dat[0][1]
			    	duration=dat[0][2]
			    	time=dat[0][3]
						

			    	if request.method=='POST':
			    		book=request.form['book']
			    		if book=='book1':
			    			url='https://i.ytimg.com/vi/Ui9OGlDX8-A/maxresdefault.jpg'
			    			url2='https://media-cdn.tripadvisor.com/media/photo-s/0f/96/15/39/dining-area.jpg'
			    			url3='https://5.imimg.com/data5/SELLER/Default/2021/4/OI/LX/VY/40039373/badminton-court-wooden-flooring-500x500.jpg'
			    			name='Palm Meadows Badminton Centre'
			    			cost=500*int(duration)
			    			service=cost*5/100
			    			tax=cost*18/100
			    			total=cost+tax+service
			    			y=time.split(':')
			    			o=int(y[0])+int(duration)
			    			tim=str(o)+':'+y[1]
			    			use=user10+'book'
			    			co=str(cost)
			    			st='create table {} (name varchar(30),time varchar(30),tim varchar(30),cost varchar(30),date varchar(30) )'.format(use,)
			    			try:
			    				cursor.execute(st)
			    				con.commit()
			    			except:
			    				print('')
			    			tot=str(total)
			    			cursor.execute("insert into {} values('{}','{}','{}','{}','{}','{}')".format(user10+'mybook',name,date,duration,tot,url,time))
			    			st1="insert into {} values('{}','{}','{}','{}','{}') ".format(use,name,time,tim,co,date)
			    			cursor.execute(st1)
			    			con.commit()

			    			return render_template('payment.html',name=name,url=url,cost=cost,usename=usename,email=email,service=service,tax=tax,total=total,url2=url2,url3=url3,date=date,time=time,duration=duration,time_to=tim)

		    			if book=='book2':
			    			url='https://5.imimg.com/data5/PT/RK/MY-14059388/football-flooring-service-500x500.jpg'
			    			url2='https://imgstaticcontent.lbb.in/lbbnew/wp-content/uploads/sites/2/2017/04/09204239/RooftTopFootball1-600x400.jpg'
			    			url3='https://media-cdn.tripadvisor.com/media/photo-s/0f/96/15/39/dining-area.jpg'
			    			name='Nova Football Centre'
			    			cost=900*int(duration)
			    			service=cost*5/100
			    			tax=cost*18/100
			    			total=cost+tax+service
			    			y=time.split(':')
			    			o=int(y[0])+int(duration)
			    			tim=str(o)+':'+y[1]
			    			use=user10+'book'
			    			co=str(cost)
			    			st='create table {} (name varchar(30),time varchar(30),tim varchar(30),cost varchar(30),date varchar(30) )'.format(use,)
			    			try:
			    				cursor.execute(st)
			    				con.commit()
			    			except:
			    				print('')
			    			tot=str(total)
			    			cursor.execute("insert into {} values('{}','{}','{}','{}','{}','{}')".format(user10+'mybook',name,date,duration,tot,url,time))
			    			st1="insert into {} values('{}','{}','{}','{}','{}') ".format(use,name,time,tim,co,date)
			    			cursor.execute(st1)
			    			con.commit()

			    			return render_template('payment.html',name=name,url=url,cost=cost,usename=usename,email=email,service=service,tax=tax,total=total,url2=url2,url3=url3,date=date,time=time,duration=duration,time_to=tim)
		    			if book=='book3':
			    			url='https://www.stevens.edu/sites/stevens_edu/files/styles/news_detail/public/0085%2024847.jpg?itok=oGRRJUwH'
			    			url2='https://www.pleasantonweekly.com/news/photos/2021/may/26/23911_col.jpg'
			    			url3='https://media-cdn.tripadvisor.com/media/photo-s/0f/96/15/39/dining-area.jpg'
			    			name='Fortune Sports Academy'
			    			cost=1500*int(duration)
			    			service=cost*5/100
			    			tax=cost*18/100
			    			total=cost+tax+service
			    			y=time.split(':')
			    			o=int(y[0])+int(duration)
			    			tim=str(o)+':'+y[1]
			    			use=user10+'book'
			    			co=str(cost)
			    			st='create table {} (name varchar(30),time varchar(30),tim varchar(30),cost varchar(30),date varchar(30) )'.format(use,)
			    			try:
			    				cursor.execute(st)
			    				con.commit()
			    			except:
			    				print('')
			    			tot=str(total)
			    			cursor.execute("insert into {} values('{}','{}','{}','{}','{}','{}')".format(user10+'mybook',name,date,duration,tot,url,time))
			    			st1="insert into {} values('{}','{}','{}','{}','{}') ".format(use,name,time,tim,co,date)
			    			cursor.execute(st1)
			    			con.commit()

			    			return render_template('payment.html',name=name,url=url,cost=cost,usename=usename,email=email,service=service,tax=tax,total=total,url2=url2,url3=url3,date=date,time=time,duration=duration,time_to=tim)


			    		return render_template('booking.html',location=area,date=date,time=time,duration=duration)
			    	return render_template('booking.html',location=area,date=date,time=time,duration=duration)

    				break
    			else:
    				
    				continue

    	return redirect(url_for('book'))



    	#return redirect(url_for('book'))

    	cursor.execute('select * from {}'.format(user10,))

    	dat=cursor.fetchall()    	
    	area=dat[0][0]
    	date=dat[0][1]
    	duration=dat[0][2]
    	time=dat[0][3]
			

    	if request.method=='POST':

    		return render_template('booking.html',location=area,date=date,time=time,duration=duration)
    	return render_template('booking.html',location=area,date=date,time=time,duration=duration)
    else:
    	return redirect(url_for("login"))




@app.route('/confirmed',  methods=["POST","GET"])
def confirmedd():

    if "user" in session:
    	cursor.execute('select * from creds')
    	data=cursor.fetchall()
    	for i in data:
    		if i[2]==session['user']:
    			temp=i[0]
    			usename=i[5]
    			email=i[2]

    	user10=temp.strip('"')

    	cursor.execute('show tables')
    	y=cursor.fetchall()
    	for i in y:
    		for j in i:
    			if user10+'book'==j:
			    	cursor.execute('select * from {}'.format(user10+'book',))

			    	dat=cursor.fetchall()    	
			    	name=dat[0][0]
			    	time=dat[0][1]
			    	tim=dat[0][2]
			    	co=dat[0][3]
			    	cost=int(co)
	    			service=cost*5/100
	    			tax=cost*18/100
	    			total=cost+tax+service						
	    			date=dat[0][4]

	    			cursor.execute('drop table {} '.format(user10+'book'))
	    			cursor.execute('drop table {}'.format(user10))

			    	return render_template('confirmed.html',name=name,time=time,tim=tim,cost=cost,service=service,tax=tax,total=total,date=date)

    				break
    			else:
    				
    				continue

    	return redirect(url_for('booking'))



    else:
    	return redirect(url_for("booking"))

@app.route('/mybookings/', methods=["POST","GET"])
def mybook():
	if "user" in session:# checks if user i logged in , if looged in redirects to usr page
		user1=session["user"]
			
		st='select * from creds'
		cursor.execute(st)
		data=cursor.fetchall()
		for y in data :
			if y[2]==user1:
				username=y[0]
		st='select * from {}'.format(username+'mybook')
		cursor.execute(st)
		dat=cursor.fetchall()
		if len(dat)==0:
			msgnone="You currently Don't have any Bookings."
			return render_template('mybookings.html',msgnone=msgnone)
		if request.method=='POST':
			time=request.form['book']
			st='select * from {}'.format(username+'mybook')
			cursor.execute(st)
			dat=cursor.fetchall()
			st='delete from {} where time="{}"'.format(username+'mybook',time)
			cursor.execute(st)
			con.commit()
			return render_template("mybookings.html",data=dat)
		st='select * from {}'.format(username+'mybook')
		cursor.execute(st)
		dat=cursor.fetchall()
		return render_template("mybookings.html",data=dat)
	else:
		return redirect(url_for('login'))

@app.errorhandler(404)
  
# inbuilt function which takes error as parameter
def not_found(e):
  
# defining function
  return render_template("404.html")

if __name__=="__main__":
	app.run(debug=True,host='0,0,0,0')
	chat() 
