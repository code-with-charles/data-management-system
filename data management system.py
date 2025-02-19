import customtkinter
import os
from tkinter import *
import sys
from PIL import Image
import shutil
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme("dark-blue")
window=customtkinter.CTk()
window.geometry("1366x766")

window.title("DATA MANAGEMENT SYSTEM")
            
def resource_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path=os.path.abspath(".")
    return os.path.join(base_path,relative_path)

def get_writable_db_path(db_name):
    #this copies the database to a writeable location
    home_dir=os.path.expanduser("-")
    db_destination=os.path.join(home_dir,db_name)
    
    if not os.path.exists(db_destination):
        shutil.copyfile(resource_path(db_name),db_destination)
    return db_destination
      

dashicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\dash.png')),
                            dark_image=Image.open(resource_path('icons\dash.png')),
                            size=(35,35)
                            )

aiicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\Ai.png')),
                            dark_image=Image.open(resource_path('icons\Ai.png')),
                            size=(30,20)
                            )
backicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\online.png')),
                                dark_image=Image.open(resource_path('icons\online.png')),
                                size=(30,20)
                                )
byteicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\online.png')),
                                dark_image=Image.open(resource_path('icons\online.png')),
                                size=(30,20)
                                )   
cloudicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\cloud database.png')),
                                dark_image=Image.open(resource_path('icons\cloud database.png')),
                                size=(30,20)
                                ) 
databasebicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\online.png')),
                                dark_image=Image.open(resource_path('icons\online.png')),
                                size=(30,20)
                                )
downloadicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\online.png')),
                                dark_image=Image.open(resource_path('icons\online.png')),
                                size=(30,20)
                                ) 
driveicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\drive.png')),
                                dark_image=Image.open(resource_path('icons\drive.png')),
                                size=(30,20)
                                )
homeicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\home.png')),
                                dark_image=Image.open(resource_path('icons\home.png')),
                                size=(30,20)
                                )
workicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\job_work.png')),
                                dark_image=Image.open(resource_path('icons\job_work.png')),
                                size=(30,20)
                                )   
loadingicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\online.png')),
                                dark_image=Image.open(resource_path('icons\online.png')),
                                size=(30,20)
                                ) 
mobileicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\online.png')),
                                dark_image=Image.open(resource_path('icons\online.png')),
                                size=(30,20)
                                )
moneyicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\online.png')),
                                dark_image=Image.open(resource_path('icons\online.png')),
                                size=(30,20)
                                ) 
photoshopicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\photoshop.png')),
                                dark_image=Image.open(resource_path('icons\photoshop.png')),
                                size=(30,20)
                                ) 
premiereicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\premiere.png')),
                                dark_image=Image.open(resource_path('icons\premiere.png')),
                                size=(30,20)
                                ) 
searchicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\photoshop.png')),
                                dark_image=Image.open(resource_path('icons\photoshop.png')),
                                size=(30,20)
                                ) 

settingsicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\settings.png')),
                                            dark_image=Image.open(resource_path('icons\settings.png')),
                                            size=(30,20)
                                            ) 
scheduleicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\online.png')),
                                            dark_image=Image.open(resource_path('icons\online.png')),
                                            size=(30,20)
                                            ) 
notificationicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\Alert.png')),
                                            dark_image=Image.open(resource_path('icons\Alert.png')),
                                            size=(30,20)
                                            ) 
settingsicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\settings.png')),
                                            dark_image=Image.open(resource_path('icons\settings.png')),
                                            size=(30,20)
                                            ) 

databaseicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\online.png')),
                                            dark_image=Image.open(resource_path('icons\online.png')),
                                            size=(30,20)
  
  
                                          )

analyticsicon=customtkinter.CTkImage(light_image=Image.open(resource_path('icons\online.png')),
                                            dark_image=Image.open(resource_path('icons\online.png')),
                                            size=(30,20)
  
  
                                          )
def home_page():
    home_frame=customtkinter.CTkFrame(window,width=1365,height=765,border_width=7,border_color='green')
    home_frame.place(relx=0.0)
    display_frame=customtkinter.CTkFrame(home_frame,height=710,width=1300)
    display_frame.place(relx=0.045,rely=0.068)
    
    #top labe1
    global current_image_index
    def update_image():
        global current_image_index
        
        img=images[current_image_index]
        ctk_img=customtkinter.CTkImage(light_image=img,
                                    dark_image=img,
                                    size=(1290,690))
        image_label.configure(image=ctk_img)
        current_image_index +=1
        
        if current_image_index >=len(images):
            current_image_index=0
        display_frame.after(3000,update_image)
        
        
    image_files=[

"pics\image.jpg",
"pics/image1.png",
"pics/image2.png",
"pics/image3.jpg",
"pics/image4.webp",
"pics/image5.png",
"pics/image6.jpg",
"pics/Energy_Dashboard_2x.jpg.png",

   
    

     
    ]
        
    images=[Image.open(resource_path(img_file)) for img_file in image_files]
    image_label=customtkinter.CTkLabel(display_frame,text=".")
    image_label.place(relwidth=1,relheight=1,x=0,y=0)
    current_image_index=0
    update_image()
    top_frame=customtkinter.CTkFrame(home_frame,width=1362,height=50,fg_color='#152238')
    top_frame.place(relx=0.)
    side_frame=customtkinter.CTkFrame(home_frame,fg_color='black',width=60,height=762)
    side_frame.place(relx=0.0,rely=0.0)
    
    
    dash=customtkinter.CTkButton(side_frame,image=dashicon,text="",fg_color="black",corner_radius=100,width=0)
    dash.place(relx=0.0,rely=0.0)

    home=customtkinter.CTkButton(side_frame,image=homeicon,text="",fg_color="black",corner_radius=30,width=0)
    home.place(relx=0.001,rely=0.08)

    premier=customtkinter.CTkButton(side_frame,image=premiereicon,text="",fg_color="black",corner_radius=30,width=0)
    premier.place(relx=0.001,rely=0.14)
    photo=customtkinter.CTkButton(side_frame,image=photoshopicon,text="",fg_color="black",corner_radius=30,width=0)
    photo.place(relx=0.001,rely=0.20)
    scheduler=customtkinter.CTkButton(side_frame,image=scheduleicon,text="",fg_color="black",corner_radius=30,width=0)
    scheduler.place(relx=0.001,rely=0.26)
    money=customtkinter.CTkButton(side_frame,image=moneyicon,text="",fg_color="white",corner_radius=30,width=0)
    money.place(relx=0.001,rely=0.32)
    drive=customtkinter.CTkButton(side_frame,image=driveicon,text="",fg_color="black",corner_radius=30,width=0)
    drive.place(relx=0.001,rely=0.73)
    notification=customtkinter.CTkButton(side_frame,image=notificationicon,text="",fg_color="black",corner_radius=30,width=0)
    notification.place(relx=0.001,rely=0.85)
    settings=customtkinter.CTkButton(side_frame,image=settingsicon,text="",fg_color="black",corner_radius=30,width=0)
    settings.place(relx=0.001,rely=0.90)
    back=customtkinter.CTkButton(side_frame,image=backicon,text="",fg_color="black",corner_radius=30,width=0)
    back.place(relx=0.001,rely=0.79)
 ################################################################################################################################
    ai=customtkinter.CTkButton(top_frame,image=aiicon,text="",fg_color="#152238",corner_radius=30,width=0)
    ai.place(relx=0.30,rely=0.28)
    analytics=customtkinter.CTkButton(top_frame,image=analyticsicon,text="",fg_color="#152238",corner_radius=30,width=0)
    analytics.place(relx=0.34,rely=0.28)
    database=customtkinter.CTkButton(top_frame,image=databasebicon,text="",fg_color="#152238",corner_radius=30,width=0)
    database.place(relx=0.38,rely=0.28)
    task=customtkinter.CTkButton(top_frame,image=workicon,text="",fg_color="#152238",corner_radius=30,width=0)
    task.place(relx=0.42,rely=0.28)
    cloud=customtkinter.CTkButton(top_frame,image=cloudicon,text="",fg_color="#152238",corner_radius=30,width=0)
    cloud.place(relx=0.46,rely=0.28)
    segment=customtkinter.CTkButton(top_frame,image=databaseicon,text="",fg_color="#152238",corner_radius=30,width=0)
    segment.place(relx=0.50,rely=0.28)
    search=customtkinter.CTkButton(top_frame,image=searchicon,text="",fg_color="#152238",corner_radius=30,width=0)
    search.place(relx=0.54,rely=0.28)



home_page()

window.mainloop()
