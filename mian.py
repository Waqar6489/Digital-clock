from tkinter import *
import datetime
def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    mi=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')

    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sce.config(text=sec)
    lab_am_pm.config(text=am)

    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    
    lab_hr.after(200,date_time)
    
clock=Tk()
clock.title('     Time Master')
clock.geometry('1200x600')
clock.config(bg='black')

# time code
tittle=Label(clock,text="Digital Clock",font=("Arial",50,"bold"),fg='#0FFF50',bg='black')
tittle.place(x=400,y=40,height=80,width=400)

lab_hr=Label(clock,text="00",font=("Time New Roman",60,"bold"),fg='#0FFF50',bg='black')
lab_hr.place(x=150,y=150,height=110,width=100)

lab_min=Label(clock,text="00",font=("Time New Roman",60,"bold"),fg='#0FFF50',bg='black')
lab_min.place(x=400,y=150,height=110,width=100)

lab_sce=Label(clock,text="00",font=("Time New Roman",60,"bold"),fg='#0FFF50',bg='black')
lab_sce.place(x=650,y=150,height=110,width=100)

lab_am_pm=Label(clock,text="00",font=("Time New Roman",60,"bold"),fg='#0FFF50',bg='black')
lab_am_pm.place(x=905,y=150,height=110,width=130)

lab_hr_txt=Label(clock,text="Hour",font=("Time New Roman",30,"bold"),fg='#0FFF50',bg='black')
lab_hr_txt.place(x=150,y=250,height=110,width=100)

lab_min_txt=Label(clock,text="Min",font=("Time New Roman",30,"bold"),fg='#0FFF50',bg='black')
lab_min_txt.place(x=400,y=250,height=110,width=100)

lab_sce_txt=Label(clock,text="Sec",font=("Time New Roman",30,"bold"),fg='#0FFF50',bg='black')
lab_sce_txt.place(x=650,y=250,height=110,width=100)

lab_am_txt=Label(clock,text="Am/Pm",font=("Time New Roman",30,"bold"),fg='#0FFF50',bg='black')
lab_am_txt.place(x=900,y=250,height=110,width=150)

#date code
lab_date=Label(clock,text="00",font=("Time New Roman",60,"bold"),fg='#0FFF50',bg='black')
lab_date.place(x=150,y=350,height=110,width=100)

lab_date_txt=Label(clock,text="Date",font=("Time New Roman",30,"bold"),fg='#0FFF50',bg='black')
lab_date_txt.place(x=150,y=450,height=110,width=100)

lab_month=Label(clock,text="00",font=("Time New Roman",60,"bold"),fg='#0FFF50',bg='black')
lab_month.place(x=400,y=350,height=110,width=100)

lab_month_txt=Label(clock,text="Month",font=("Time New Roman",30,"bold"),fg='#0FFF50',bg='black')
lab_month_txt.place(x=390,y=450,height=110,width=130)

lab_year=Label(clock,text="00",font=("Time New Roman",60,"bold"),fg='#0FFF50',bg='black')
lab_year.place(x=650,y=350,height=110,width=100)

lab_year_txt=Label(clock,text="Year",font=("Time New Roman",30,"bold"),fg='#0FFF50',bg='black')
lab_year_txt.place(x=650,y=450,height=110,width=110)

lab_day=Label(clock,text="00",font=("Time New Roman",60,"bold"),fg='#0FFF50',bg='black')
lab_day.place(x=900,y=350,height=110,width=150)

lab_day_txt=Label(clock,text="Day",font=("Time New Roman",30,"bold"),fg='#0FFF50',bg='black')
lab_day_txt.place(x=910,y=450,height=110,width=100)



# function call
date_time()

clock.mainloop()