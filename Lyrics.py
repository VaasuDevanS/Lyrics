# Module for Database
import shelve

# Module for GUI Creation
from Tkinter import *
from Tkinter import StringVar as Str
import tkMessageBox as msgbox

# Module for String Processing
import re

# Module for Downlading Lyrics from the Internet
import requests    

# My Database
import os
try:
    os.chdir("D:\\")
    a="D:\\"
except:
    os.chdir("E:\\")
    a="E:\\"
if not os.path.exists("Lyrics"):
    os.mkdir("Lyrics")
    os.chdir(a+"Lyrics")
    database_songs=shelve.open("Lyrics_database")
    arg=open("About","w")
    arg.write("Dont delete this folder..Deleting this folder will delete all the offline Lyrics..")
    arg.close()
    config['bg']="white"
    config['fg']="black"    
    config['name']="User"

os.chdir(a+"Lyrics")
database_songs=shelve.open("Lyrics_database")
config=shelve.open("Config_data")

def main():
    
    #Creating The GUI Window
    app=Tk()
    app.title("Lyrics--"+config['name'])
    app.geometry("300x586+800+30")
    app.iconbitmap(default="D:\\Program_files\Python\Lyrics\\foo.ico")
    app.resizable(0,0)
    
    frame=Frame(app)
    frame.pack()
    
    f=Frame(app,padx=10)
    a=Frame(app)
    g=Frame(app)
    
    menubar=Menu(app)

    def aboutapp():
        msgbox.showinfo("About",message="Save your Favourite Lyrics in a better way..! \nDeveloped using Python2.7")
        
    def aboutdev():
        result=msgbox.askyesno("About",message="Developed by vaasu devan S\nMail-id: vaasuceg.96@gmail.com\nDo you want to see his GitHub Profile?")
        
        if result:
            import webbrowser          #For opening The default Browser
            webbrowser.open("https://github.com/VaasuDevanS/")
            
    def settings():
        
        def v(t):
            
            try:
                colo=d.get(ACTIVE)
                msgbox.showinfo("Background Color",message="Background Color changed successfully..")
                del config['bg']
                config['bg']=colo[1:]
            except:
                msgbox.showerror("Background Color",message="Select the correct Color")
            
        def va(t):
            try:
                colo=e.get(ACTIVE)
                msgbox.showinfo("Text Color",message="Text Color changed successfully..")
                del config['fg']
                config['fg']=colo[1:]
            except:
                msgbox.showerror("Background Color",message="Select the correct Color")

        sett=Tk()
        sett.title("      Settings")
        sett.geometry("225x300+550+30")
        
        se=Frame(sett)
        
        see=Frame(sett)
        
        ra=Label(see,text="Background")
        ra.pack(side=LEFT)
        
        sett.resizable(0,0)

        d=Listbox(se,width=13)
        
        d.insert(END," red")
        d.insert(END," brown")
        d.insert(END," black")
        d.insert(END," blue")
        d.insert(END," green")
        d.insert(END," orange")
        d.insert(END," cyan")
        d.insert(END," magenta")
        d.insert(END," white")

        d.bind('<Double-Button-1>',v)
        
        raa=Label(see,text="          Foreground")
        raa.pack(side=RIGHT)        
        
        d.pack(side=LEFT)
        
        e=Listbox(se,width=15)
        e.pack(side=RIGHT,padx=15)
        
        e.insert(END," red")
        e.insert(END," brown")
        e.insert(END," black")
        e.insert(END," blue")
        e.insert(END," green")
        e.insert(END," orange")
        e.insert(END," cyan")
        e.insert(END," magenta")
        e.insert(END," white")

        e.bind('<Double-Button-1>',va)    
            
        sea=Frame(sett)    
        name=Label(sea,text="Change your name")
        name.pack()
        
        okay=Entry(sea)
        okay.pack()
        
        def okayy():
            del config['name']
            config['name']=okay.get()
            msgbox.showinfo("Name",message="Name changed Successfully..Restart to see the change..")
            
        
        okie=Button(sea,text="Ok",command=okayy)
        okie.pack(ipadx=5)
        
        see.pack()
        se.pack()
        sea.pack()
        sett.focus_force()
        sett.mainloop()
        
    app.config(menu=menubar)  
    
    filemenu=Menu(menubar,tearoff=0,foreground="red")
    filemenu.add_command(label="About the app",command=aboutapp)
    filemenu.add_command(label="About the Developer",command=aboutdev)
    
    file_=Menu(menubar,tearoff=0,foreground="red")
    file_.add_command(label="Settings",command=settings)
    
    menubar.add_cascade(label="App",menu=filemenu,underline=0) 
    menubar.add_cascade(label="Tools",menu=file_,underline=0)

    def Resources():
        
        g.pack_forget()

        resources.config(state="disable")
        database.config(state="normal")  
        
        def clear():

            text_box.delete(0,END)  
            my_list.delete(0,END)   
            Search.config(state="normal")
            Clear.config(state="normal")           
        
        def search():   

            def vaasu(ch):
                
                value=my_list.get(ACTIVE)
                try:
                    
                    def save():
                        L=view.get("1.0",END)
                        a=[database_links[choi][0],database_links[choi][1],L]
                        b=sorted(map(int,database_songs.keys()))
                        try:
                            database_songs[`b[-1]+1`]=a
                        except:
                            database_songs[`1`]=a
                            
                        msgbox.showinfo("Confirmation",message="Saved to the database..")
                    
                    value=value.split()
                    choi=int(value[0])
                    song_raw_data=requests.get(database_links[choi][1])
                    song=re.findall('''<p id="songLyricsDiv"  class="songLyricsV14 iComment-text">(.*?)</p>''',`song_raw_data.text`)
                    A=re.sub('<(.*?)>','_',song[0])
                    B=A.split('_')
                    for i in B:
                        i=i.split("\\")
                        j="".join(i)
                        if j.startswith('n'):
                            Ly.append(j[1:])
                        elif j.startswith('rn'):
                            Ly.append(j[2:])
                        else:
                            Ly.append(j)
                        
                    G=Tk()
                    G.title("SongLyrics.com")
                    G.geometry("300x600+485+30")
                    G.resizable(0,0)
                    
                    view=Text(G,wrap=WORD,height=30)
                    view.focus_force()
                    for i in Ly:
                        view.insert(END,i)
                        view.insert(END,"\n")
                    view.pack(pady=20)
                    
                    ok=Button(G,text="Save",command=save)
                    ok.pack()
                    
                    G["bg"]=config["bg"]
                    view.config(foreground=config['fg'])
                    G.focus_force()
                    G.mainloop()           
                    
                except:
                    msgbox.showerror("Lyrics",message="Select correct song :)")
            
            Search.config(state="disable")
        
            descriptions,links,Ly=[],[],[]
            key_word=text_box.get()
            website="http://www.songlyrics.com/index.php?section=search&searchW="+key_word+"&submit=Search"
            data=requests.get(website)
            total_results=re.findall('''<div class="search-results">(.*?)</div>''',`data.text`)
            total_no=int(re.sub("\D","",total_results[0]))
            page_nos=re.findall('''<ul class="pagination">(.*?)</ul>''',`data.text`)
            
            if total_no<=10:
                results=re.findall('''<div class="serpresult">(.*?)</div>''',`data.text`)
            else:
                page_nos_only=max(map(int,re.sub("\D"," ",page_nos[0]).split()))
                results=re.findall('''<div class="serpresult">(.*?)</div>''',`data.text`)
                for page_num in xrange(2,7):
                    search_web="http://www.songlyrics.com/index.php?section=search&searchIn1=artist&searchIn2=album&searchIn3=song&searchIn4=lyrics&searchW="+key_word+"&pageNo="+`page_num`
                    data=requests.get(search_web)
                    flag=re.findall('''<div class="serpresult">(.*?)</div>''',`data.text`)
                    for i in flag:
                        results.append(i)
            if len(results)==0:
                msgbox.showinfo("No Results",message="Try with a different keyword..")
                text_box.delete(0,END) 
                
            for i in results:
                m=re.sub('''<(.*?)>''',"",i)
                m=m.split("\\")
                while 't' in m:m.remove('t')
                while 'n' in m:m.remove('n')
                for flag in m:
                    if flag.startswith('tby') or flag.startswith('by'):
                        descriptions.append((m[1][1:],flag[1:]))
                n=re.findall('''<(.*?)>''',i)
                for i in n:
                    if i.startswith("a href="):
                        link=re.findall('''"(.*?)"''',i)
                        if link not in links:
                            if len(link)==2:
                                sam=link[0]
                                if sam not in links:
                                    links.append(sam)
            database_links={i:j for i,j in enumerate(zip(descriptions,links),start=1)}    
            
            my_list.insert(END,"")
            
            for i in database_links:
                song_name=`i`+"  "+database_links[i][0][0]+"  "+database_links[i][0][1]
                my_list.insert(END,song_name)
                my_list.insert(END," ")
              
            my_list.bind('<Double-Button-1>',vaasu)  
            
            Clear.config(state="normal")
            scroll.config(command=my_list.yview)
            scrol.config(command=my_list.xview)
            
        def Butt():
            
            website="https://www.freecodecamp.com/the-fastest-web-page-on-the-internet"
            try:
                
                data=requests.get(website)
                connection="Connected"
                color="green"
                conn.configure(foreground="green")
                disp.set(connection) 
            except:
                
                connection="Not connected"
                color="red" 
                conn.configure(foreground="red")
                disp.set(connection)    
                
            if not connection=="Connected":
                Search.config(state="disable")
                Clear.config(state="disable")
                
            else:
                Search.config(state="normal")
                Clear.config(state="normal")  
                
        disp=Str()
        disp.set("")        
                
        Search=Button(f,text="Search",command=search)  
        
        Clear=Button(f,text="Clear",command=clear) 
        Disp=Button(f,text="Status:",command=Butt)   
        conn=Label(f,textvariable=disp)         

        website="https://www.freecodecamp.com/the-fastest-web-page-on-the-internet"
        try:
            data=requests.get(website)
            connection="Connected"
            conn.configure(foreground="green")
            disp.set(connection)
            
        except:
            connection="Not connected"
            color="red"       
            conn.configure(foreground="red")
            disp.set(connection)
            Search.config(state="disable")
            Clear.config(state="disable")      

        a.pack()
               
        Disp.pack()
        
        conn.pack()

        display=Str()
        display.set("Enter the song / artist / album name..")
        Display=Label(f,textvariable=display)
        Display.pack()
        
        text_box=Entry(f,width=30,textvariable=Str())
        text_box.pack(pady=10)
        text_box.focus_force()

        Search.pack()
        Clear.pack(ipadx=10)
        
        scroll=Scrollbar(f,orient=VERTICAL)
        scrol=Scrollbar(f,orient=HORIZONTAL)
        
        my_list=Listbox(f,yscrollcommand=scroll.set,xscrollcommand=scrol.set,width=40,height=30) 
        
        f.pack() 
        
        scroll.pack(side=RIGHT,fill=Y)  
        scrol.pack(side=BOTTOM,fill=X)
        my_list.pack(pady=30,fill=BOTH,expand=TRUE)   
        
    def Database():
        g.pack()

        def Refresh():
            
            data.delete(0,END)
                    
            for i in sorted(map(int,database_songs.keys())):
                song_name=`i`+"  "+str(database_songs[`i`][0][0])+" "+str(database_songs[`i`][0][1])
                data.insert(END,song_name)
                data.insert(END,"  ")            

        refresh=Button(g,text="Refresh",command=Refresh)
        
        
        def vaas(p):
            
            try:
                value=data.get(ACTIVE)
                value=value.split()
                choice=value[0]
                Ly=database_songs[choice][2]
                
                K=Tk()
                view=Text(K,wrap=WORD,height=30)
                view.focus_force()
                view.insert(END,Ly)
                view.pack(pady=20)

                def delete():
                    res=msgbox.askyesno("Deletion",message="Are you sure You want to delete from the database?\nThis cant be undone.")
                    if res:
                        nos=['.']+sorted(map(int,database_songs.keys()))
                        choi=int(choice)
                        nos=nos[choi+1:]
                        if len(nos)!=0:
                            no=map(lambda i:i-1,nos)
                            for i,j in zip(nos,no):
                                temp=database_songs[`i`]
                                del database_songs[`i`]
                                database_songs[`j`]=temp
                            K.destroy()
                            Refresh()
                        elif len(nos)==0:
                            del database_songs[`choi`]
                            K.destroy()
                            Refresh()
                        
                def update():
                    song_edited=view.get("1.0",END)
                    a=[database_songs[choice][0],database_songs[choice][1],song_edited]
                    del database_songs[choice]
                    database_songs[choice]=a
                    msgbox.showinfo("Update",message="Song updated Successfully")
                    Refresh()
                    K.destroy()

                su=Frame(K)
                updat=Button(su,text="Update",command=update)
                updat.pack(side=LEFT)
                dele=Button(su,text="Delete",command=delete)
                dele.pack(side=RIGHT)
                su.pack()

                K.title("Database")
                K.geometry("300x600+485+30")
                K.resizable(0,0)                
                K["bg"]=config["bg"]
                view.config(foreground=config['fg'])
                K.focus_force()
                K.mainloop()    
                
            except:
                msgbox.showerror("Lyrics",message="Select correct song :)")

        database.config(state="disable")        
        f.pack_forget()
        a.pack_forget()
        frame.pack()
        resources.config(state="normal")   
        
        scrll=Scrollbar(g,orient=VERTICAL)
        scrl=Scrollbar(g,orient=HORIZONTAL)        
        data=Listbox(g,yscrollcommand=scrll.set,xscrollcommand=scrl.set,width=40,height=33) 
        
        for i in sorted(map(int,database_songs.keys())):
            song_name=`i`+"  "+str(database_songs[`i`][0][0])+" "+str(database_songs[`i`][0][1])
            data.insert(END,song_name)
            data.insert(END,"  ")

        data.bind('<Double-Button-1>',vaas)
        Refresh()
        

        scrll.config(command=data.yview)
        scrl.config(command=data.xview) 
        refresh.pack()
        scrll.pack(side=RIGHT,fill=Y)
        scrl.pack(side=BOTTOM,fill=X)
        data.pack()
        

    database=Button(frame,text="Database",fg="brown",command=Database)
    database.pack(side=LEFT,pady=10)
    
    resources=Button(frame,text="Resources",fg="blue",command=Resources)
    resources.pack(side=RIGHT)
    
    databse_links={}
    for_data=[]
    
    g.pack()
 
    #Running the Window
    app.focus_force()
    app.mainloop()

if __name__=='__main__':
    main()
    
database_songs.close()
config.close()