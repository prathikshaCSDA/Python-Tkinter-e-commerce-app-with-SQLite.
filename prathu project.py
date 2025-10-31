from tkinter import*
import random
import smtplib
import sqlite3
from tkinter import messagebox
from tkinter import filedialog,PhotoImage
from tkinter import ttk

con=sqlite3.connect("prathu.db")
cur=con.cursor()
qur1="create table if not exists t1(email text,password text,phone_no text)"
qur2="create table if not exists t2(email text,password text)"
qur3="create table if not exists t3( user_email text,new_password text)"
qur4="create table if not exists t4(product_id text,product_name text,product_price text,qty text,product_img blob,likes integer default 0,dislikes integer default 0,comment text default text "")"
qur5="create table if not exists t5(product_id text,buyer_name text,address text,mobile_no text)"
cur.execute(qur5)
cur.execute(qur1)
cur.execute(qur2)
cur.execute(qur3)
cur.execute(qur4)
sender_email="prathiharith@gmail.com"
sender_password="fmpy guuh lseo grct"
a=Tk()
im=[]
pp=[]
zz=[]
file_path=None
def signup(eee1,eee2):
      e.get()=="username",e1.get()=="password"
      x=Tk()
      otp_time=0
      def send_otp():
            global otp
            email=e2.get()
            otp=str(random.randint(100000,999999))
            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(sender_email,sender_password)
            msg="your opt is{}".format(otp)
            server.sendmail(sender_email,email,msg)
            server.quit()
            print ("otp send to", email)
            print(otp)
            
      def verify_otp():
           global otp
           if e5.get()==otp:

                   cur.execute('select email from t1 ')
                   drt=cur.fetchall()
                   print(drt)
                   if  e.get() in drt:
                         messagebox.showerror('error','user already exist')
                   else:
                         
                         ins="insert into t1( email,password,phone_no)values(?,?,?)"
                         z=(e2.get(),e3.get(),e4.get())
                         cur.execute(ins,z)
                         con.commit()
                         messagebox.showinfo("success","saved successfuly")
                   
           else:
                  print("invalid OTP")
                              
      x.geometry('600x500')
      x.title("otp verification")
      l=Label(x,text="email",font=10)
      l.grid(row=0,column=0)
      l1=Label(x,text="password",font=10)
      l1.grid(row=1,column=0)
      l2=Label(x,text="phone no",font=10)
      l2.grid(row=2,column=0)
      e2=Entry(x)
      e2.grid(row=0,column=1)
      e3=Entry(x)
      e3.grid(row=1,column=1)
      e4=Entry(x)
      e4.grid(row=2,column=1)
      b=Button(x,text="send otp",command=send_otp)
      b.grid(row=3,column=3)
      l3=Label(x,text="otp")
      l3.grid(row=5,column=0)
      e5=Entry(x)

      e5.grid(row=5,column=1)
      b1=Button(x,text="verify otp",command=verify_otp)
      b1.grid(row=6,column=6)
def admin_panel():
      k=Toplevel()
      def save():
            
            
            ins="insert into t4( product_id,product_name,product_price,qty,product_img)values(?,?,?,?,?)"
            z=(e5.get(),e6.get(),e7.get(),e8.get(),file_path)
            print(z)
            if not e5.get() :
                  messagebox.showerror('error',"enter the all required  details")
            
            
            else:
                  cur.execute('select product_id from t4 where product_id=?',(e5.get(),))
                  pid_check=cur.fetchone()
                  if pid_check:
                        messagebox.showerror('error','product id already exists')
                  else:
                                                  
                        cur.execute(ins,z)
                        con.commit()
                        messagebox.showinfo('success',' uploaded successfully')
      
                          
      def upl_img():
            global file_path
            file_path=filedialog.askopenfilename(title='upload only png files',filetype=[('png','*.png')])
            if file_path:
                  img=PhotoImage(file=file_path)
                  increace_size=img.subsample(1,1)
                  im.append(increace_size)
                  img1_label=Label(k,image=increace_size)
                  img1_label.place(x=450,y=230)
                  
           
      def order_details():
          
            cur.execute('select * from t5')
            orders=cur.fetchall()
            print(orders)
            tk_frame=Frame(k)
            tk_frame.grid(row=8,column=6)
            
            tr2=ttk.Treeview(tk_frame)
            tr2['columns']=["product_id","buyer_name","address","mobile_no"]
            tr2.column('#00',anchor='center',width=0,stretch=NO)
            tr2.column('#01',anchor='center')
            tr2.column('#02',anchor='center')
            tr2.column('#03',anchor='center')
            tr2.column('#04',anchor='center')
            tr2.heading('#00',text='')
            tr2.heading('#01',text='product_id')
            tr2.heading('#02',text='buyer_name')
            tr2.heading('#03',text='address')
            tr2.heading('#04',text='mobile_no')
            #orders=[("product_id","buyer_name","address","mobile_no")]
            for j in orders:
                        tr2.insert("",END,values=j)
            tr2.pack(fill=X)
            
           
      k.geometry("800x600")
      k.title("product details")
      product_id=Label(k,text="product id",font=10)
      product_id.grid(row=0,column=2)
      product_name=Label(k,text="product name",font=10)
      product_name.grid(row=1,column=2)
      product_price=Label(k,text="product price",font=10)
      product_price.grid(row=2,column=2)
      product_qty=Label(k,text="qty",font=10)
      product_qty.grid(row=3,column=2)
      product_img=Label(k,text="product img")
      product_img.grid(row=4,column=2)
      e5=Entry(k)
      e5.grid(row=0,column=5)
      e6=Entry(k)
      e6.grid(row=1,column=5)
      e7=Entry(k)
      e7.grid(row=2,column=5)
      e8=Entry(k)
      e8.grid(row=3,column=5)
      b3=Button(k,text="save",command=save)
      b3.grid(row=6,column=5)
      b4=Button(k,text="upload image",command=upl_img)
      b4.grid(row=4,column=5)
      b5=Button(k,text="order details",command=order_details)
      b5.grid(row=6,column=9)
      
def userdashboard():
      p=Toplevel()
      cur.execute('select * from t4')
      datas=cur.fetchall()
      print(datas)
      def like_countfun(pid,lbt):
            print(pid)
            cur.execute('update  t4 set likes=likes+1 where product_id=?',(pid,))
            con.commit()
            lbt.config(bg='grey',state=DISABLED)
      def dislike_countfun(pid,lbt):
            cur.execute('update  t4 set dislikes=dislikes+1 where product_id=?',(pid,))
            con.commit()
            lbt.config(bg='grey',state=DISABLED)
      def comment_fun(pid,frame,cm,prevcommnt=None):
            def submit_cmt():
                  new_cm=newcmt_entry.get("1.0","end-1c")
                  cur.execute('update  t4 set comment=? where product_id=?',(new_cm,pid,))
                  con.commit()
                  if cm:
                       print(cm)
                       prevcmt_label=Label(frame,text=cm)
                       prevcmt_label.pack()
                       newcmt_entry=Text(frame,height=5,font=('arial',8))
                       newcmt_entry.pack(fill=X)
                       sub_button=Button(frame,text='submit',command=submit_cmt)
                       sub_button.pack()
      for pid,product_name,price,qty,file_path,like_count,dislike_count,comnt in datas:
            
            fr=Frame(p,highlightthickness=4,highlightbackground='red',bg='white')
            fr.pack(fill='both',pady=4)
            if file_path:
                  global pp
                  ph=PhotoImage(file=file_path)
                  print('hhhhhhhhhhhhhhhh')
                  reduce_size=ph.zoom(1).subsample(4)
                  print(file_path)
                  pp.append(reduce_size)
                  
                  plbl=Label(fr,image=reduce_size)
                                   
                  plbl.image=ph
                                   
                  plbl.pack()
            def buy_now():
                  global bb
                  d=Toplevel()
                  def order_save():
                        if not aa.get() and not bb.get() and  not cc.get():
                              messagebox.showerror('error','please fill all the details')
                        else:
                              ins="insert into t5( product_id,buyer_name,address,mobile_no)values(?,?,?,?)"
                              y=(aa.get(),bb.get(),cc.get(),ee.get())
                              cur.execute(ins,y)
                              con.commit()
                              print(y)
                         
                  d.geometry("800x600")
                  d.title("details")
                  product_id=Label(d,text="product_id:",font=10)
                  product_id.grid(row=0,column=0)
                  buyer_name=Label(d,text="buyername:",font=10)
                  buyer_name.grid(row=1,column=0)
                  mobile_no=Label(d,text="mobileno:",font=10)
                  mobile_no.grid(row=2,column=0)
                  delivery_address=Label(d,text="address:",font=10)
                  delivery_address.grid(row=3,column=0)
                  aa=Entry(d)
                  aa.grid(row=0,column=2)
                  bb=Entry(d)
                  bb.grid(row=1,column=2)
                  cc=Entry(d)
                  cc.grid(row=2,column=2)
                  ee=Entry(d)
                  ee.grid(row=3,column=2)
            
                  pht=PhotoImage(file="qrcode.png")
                  zz.append(pht)
                  qr_lbl=Label(d,image=pht)
                  qr_lbl.grid(row=5,column=5)
                  order_save=Button(d,text="confirm order",command=order_save)
                  order_save.grid(row=9,column=9)
                 
            txt_lbl=Label(fr,text=product_name) 
            txt_lbl.pack(fill='both',pady=5)
            like_button=Button(fr,text="\U0001F44D",bg='green',fg='white')
            like_button.pack(side=LEFT,padx=5)
            lcl_label=Label(fr,text=like_count)
            lcl_label.pack(side=LEFT)
            like_button.config(command=lambda lbt=like_button, id=pid:like_countfun(id,lbt))
            dislike_button=Button(fr,text="\U0001F44E",bg='red',fg='white')
            dislike_button.pack(side=LEFT,padx=5)
            dislike_label=Label(fr,text=dislike_count)
            dislike_label.pack(side=LEFT,padx=5)
            dislike_button.config(command=lambda id=pid,disb=dislike_button:dislike_countfun(id,disb))
            cmnt_button=Button(fr,text="\U0001F5E8")
            cmnt_button.pack(side=LEFT,padx=5)
            price_ll=Label(fr,bg='pink',fg='white',text="price: ",font=('arial',20))
            price_ll.pack(side=LEFT,padx=5)
            
            price_lbl=Label(fr,bg='blue',fg='white',text=price,font=('arial',20))
            price_lbl.pack(side=LEFT,padx=5)
            cmnt_button.config(command=lambda id=pid,f=fr,com=comnt:comment_fun(id,f,com))
            b4=Button(fr,text="buynow",command=buy_now)
            b4.pack(side=RIGHT,pady=5)
      
      
def login(eee1,eee2):
      
      res=(eee1,eee2)
      if e.get()=="admin@gmail.com" and e1.get()=="12345":
            admin_panel()
      else:
                  
            cur.execute('select * from t1 where email=? and password=?',(res))
            data=cur.fetchone()
            if data is None:
                  messagebox.showerror('error','user not found')
            else:
                 userdashboard()
def frg(eee1,eee2):
     v=Tk()
 
     
     def sav():
            e6.get()=="useremail",e7.get()=="newpassword"
            ins="insert into t3( useremail,newpassword)values(?,?)"
            c=(e6.get(),e7.get())
            usrpwd=(e6.get(),e7.get())
            cur.execute('update t1 set password=? where email=?',(usrpwd))
            con.commit()
            messagebox.showinfo("success"," password updated successfuly")
     l=Label(v,text="useremail",font=10)
     l.grid(row=0,column=0)
     l1=Label(v,text="newpassword",font=10)
     l1.grid(row=1,column=0)
     e6=Entry(v)
     e6.grid(row=0,column=2)
     e7=Entry(v)
     e7.grid(row=1,column=2)
     b1=Button(v,text="save",command=sav)
     b1.grid(row=3,column=5)
a.geometry('600x500')
a.title("email verification")
l=Label(a,text="username",font=10)
l.grid(row=0,column=0)
l1=Label(a,text="password",font=10)
l1.grid(row=1,column=0)
e=Entry(a)
e.grid(row=0,column=2)
e1=Entry(a)
e1.grid(row=1,column=2)
b=Button(a,text="login",command=lambda:login(e.get(),e1.get()))
b.grid(row=3,column=3)
b1=Button(a,text="signup",command=lambda:signup(e.get(),e1.get()))
b1.grid(row=3,column=5)
b2=Button(a,text="forgetpassword",command=lambda:frg(e.get(),e1.get()))
b2.grid(row=3,column=7)             

