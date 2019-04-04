#Batman Arkham Paint
#Shahriyar Rahman
#This is a Batman themed paint program where the user can use various tools, stamps, and backgrounds to create unique artwork related to or unrelated to Batman
from pygame import *
from random import *
from math import *
from tkinter import *

root = Tk()                                 
root.withdraw()

screen=display.set_mode((1250,770))
col=(0,0,0)     #the colour used for tools when the user left clicks
col2=(255,255,255)  #the colour used for tools when the user right clicks
c=(0,0,0)   #the drawn colour that adjusts when the user left clicks or right clicks
clock=time.Clock()

size=12     #the size of tools used in the program. It is adjustable

font.init()     #initializes fonts for use
timesFont=font.SysFont("Times New Roman",37)
arialFont=font.SysFont("Arial",25)
tools="TOOLS"
colour="COLOURS"
sizedisplay="Size"
paint="P      A      I      N      T"
arkham="A    R    K    H    A    M"
stamps="Stamps/Backgrounds"
tooltxt=timesFont.render((tools),True,(174,18,18))
colourtxt=timesFont.render((colour),True,(174,18,18))
sizetxt=timesFont.render((sizedisplay),True,(174,18,18))
painttxt=arialFont.render((paint),True,(0,0,0))
arkhamtxt=arialFont.render((arkham),True,(0,0,0))
stampstxt=timesFont.render((stamps),True,(174,18,18))

#these lines load background images 
back=image.load("arkhamcity_opt.jpg")
logo=image.load("batmanlogo.png")
colours=image.load("colours.png")
gravestone=image.load("gravestone_opt.png")

#these lines load the icons for when basic tools are not selected and define shapes used for their tool icons
pencil=image.load("pencil_opt.png")
eraser=image.load("erasericon_opt.png")
marker=image.load("marker_opt.png")
paintbrush=image.load("paintbrushicon_opt.png")
spray=image.load("spray_opt.png")
fill=image.load("fill_opt.png")
rect=Rect(87,360,40,30)
fullrect=Rect(142,360,40,30)
ellipsebutton=Rect(197,360,40,30)
fullellipsebutton=Rect(252,360,40,30)
dropper=image.load("dropper_opt.png")
airbrush=image.load("airbrush_opt.png")

#these lines load icons for when the user is hovering over particular tools
pencilhover=image.load("pencilhover.png")
eraserhover=image.load("eraserhover.png")
markerhover=image.load("markerhover.png")
painthover=image.load("painthover.png")
sprayhover=image.load("sprayhover.png")
fillhover=image.load("fillhover.png")
dropperhover=image.load("dropperhover.png")
airbrushhover=image.load("airbrushhover.png")

#these lines load icons for when tools are selected
pencilselect=image.load("pencilselected.png")
eraserselect=image.load("eraserselected.png")
markerselect=image.load("markerselected.png")
paintselect=image.load("paintselected.png")
sprayselect=image.load("sprayselected.png")
fillselect=image.load("fillselected.png")
dropperselect=image.load("dropperselected.png")
airbrushselect=image.load("airbrushselected.png")

#these lines load the stamps used on the canvas
batman=image.load("batman_opt.png")
batman2=image.load("batman2_opt.png")
joker=image.load("joker1_opt.png")
batgirl=image.load("batgirl_opt.png")
catwoman=image.load("catwoman_opt.png")
robin=image.load("robin_opt.png")
knight=image.load("knight_opt.png")
harley=image.load("harley_opt.png")
mobile=image.load("batmobile1_opt.png")

#these lines load the stamp buttons for when they are not used, when they're being hovered over by the user, and when they are selected
batmanbutton=image.load("batmanbutton2.png")
batmanbuttonhover=image.load("batmanbutton.png")
batman2button=image.load("batman2button2.png")
batman2buttonhover=image.load("batman2button.png")
jokerbutton=image.load("joker1button2.png")
jokerbuttonhover=image.load("joker1button.png")
batgirlbutton=image.load("batgirlbutton2.png")
batgirlbuttonhover=image.load("batgirlbutton.png")
catwomanbutton=image.load("catwomanbutton2.png")
catwomanbuttonhover=image.load("catwomanbutton.png")
robinbutton=image.load("robinbutton2.png")
robinbuttonhover=image.load("robinbutton.png")
knightbutton=image.load("knightbutton2.png")
knightbuttonhover=image.load("knightbutton.png")
harleybutton=image.load("harleybutton2.png")
harleybuttonhover=image.load("harleybutton.png")
mobilebutton=image.load("batmobilebutton2.png")
mobilebuttonhover=image.load("batmobilebutton.png")

#these lines load the canvas backgrounds
gothamroad=image.load("gothamroad.jpg")
gothamalley=image.load("gothamalley.jpg")
gothamstreet=image.load("gothamstreet.jpg")
gothamprison=image.load("gothamprison.jpg")

#these lines load the images used in the background buttons
gothamroadbutton=image.load("gothamroadbutton.jpg")
gothamalleybutton=image.load("gothamalleybutton.jpg")
gothamstreetbutton=image.load("gothamstreetbutton.jpg")
gothamprisonbutton=image.load("gothamprisonbutton.jpg")

#these lines load the images for the top function bar
clear=image.load("clear_opt.png")
load=image.load("load_opt.png")
save=image.load("save_opt.png")
undo=image.load("undo_opt.png")
redo=image.load("redo_opt.png")

#these lines blit the central images and texts
screen.blit(back,(0,0))
screen.blit(logo,(375,10))
screen.blit(gravestone,(15,250))
screen.blit(colours,(20,561))
screen.blit(tooltxt,(102,252))
screen.blit(colourtxt,(33,515))
screen.blit(painttxt,(655,200))
screen.blit(arkhamtxt,(385,200))
screen.blit(stampstxt,(892,0))

coloursRect=Rect(20,561,285,184)    #the space where the colour selector is located

colourRect=Rect(220,516,40,40)  #the space where the first colour is shown
colour2Rect=Rect(265,516,40,40)     #the space where the second colour is shown
canvasRect=Rect(325,250,900,500)    #the space for the canvas
draw.rect(screen,(255,255,255),canvasRect)

#these lines define the rectangles for tool selection
pencilRect=Rect(27,295,50,50)
eraserRect=Rect(82,295,50,50)
markerRect=Rect(137,295,50,50)
paintRect=Rect(192,295,50,50)
sprayRect=Rect(247,295,50,50)
fillRect=Rect(27,350,50,50)
rectRect=Rect(82,350,50,50)
fullrectRect=Rect(137,350,50,50)
ellipseRect=Rect(192,350,50,50)
fullellipseRect=Rect(247,350,50,50)
lineRect=Rect(55,405,50,50)
dropperRect=Rect(110,405,50,50)
airbrushRect=Rect(165,405,50,50)
polygonRect=Rect(220,405,50,50)

#these lines define the rectangles for stamp selection
batRect=Rect(880,45,65,55)
bat2Rect=Rect(950,45,65,55)
jokerRect=Rect(1020,45,65,55)
batgirlRect=Rect(1090,45,65,55)
catwomanRect=Rect(1160,45,65,55)
robinRect=Rect(915,105,65,55)
knightRect=Rect(985,105,65,55)
harleyRect=Rect(1055,105,65,55)
mobileRect=Rect(1125,105,65,55)

#these lines define the rectangles for background selection
gothamroadRect=Rect(880,170,80,55)
gothamalleyRect=Rect(968,170,80,55)
gothamstreetRect=Rect(1056,170,80,55)
gothamprisonRect=Rect(1144,170,80,55)

#these lines blit the background button images
screen.blit(gothamroadbutton,(880,170))
screen.blit(gothamalleybutton,(968,170))
screen.blit(gothamstreetbutton,(1056,170))
screen.blit(gothamprisonbutton,(1144,170))

#these lines define the spaces for the top function buttons
clearRect=Rect(0,0,40,40)
loadRect=Rect(40,0,40,40)
saveRect=Rect(80,0,40,40)
undoRect=Rect(120,0,40,40)
redoRect=Rect(160,0,40,40)
toolbarRect=Rect(0,0,200,40)

toolRect=Rect(27,295,272,221)   #background for tools
tools=screen.subsurface(toolRect).copy()

draw.rect(screen,(174,18,18),toolbarRect)

#these lines blit the images for the toolbar tools
screen.blit(clear,(0,0))
screen.blit(load,(40,0))
screen.blit(save,(80,0))
screen.blit(undo,(120,0))
screen.blit(redo,(160,0))

redolist=[]     #the list of images attainable by clicking the redo button
undolist=[]     #the list of images attainable by clicking the undo button
undolist.append(screen.subsurface(325,250,900,500).copy())
drawing=False   #decides if the the user is drawing something or not

ddmx,ddmy=0,0   #used for the pencil tool to connect the dots 
tool="pencil" #default tool
click=False     #decides if the mouse is being right or left clicked
leftclick=False     #decides if the mouse is being right-clicked
rightclick=False    #decides if the mouse is being left-clicked
polyactive=False    #decides if a polygon is being drawn or not
running =True
while running:
    click=False
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            if e.button in [1,3] and canvasRect.collidepoint(mx,my):
                if polyactive==False:
                    startx,starty=e.pos #for the start of the polygon drawing
                    polyactive=True
            if e.button in [1,3]:
                click=True #the mouse is being clicked
                mx1,my1=e.pos   #the location of the click
                canvas=screen.subsurface(canvasRect).copy() #a copy of the canvas made each time the mouse is clicked
            if e.button==1:
                leftclick=True
            if e.button==3:
                rightclick=True
            if e.button==4 and size<28:
                size+=2     #increases size by scrolling up 
            if e.button==5 and size>2:
                size-=2     #decreases size by scrolling down
        if e.type==MOUSEBUTTONUP:
            if e.button in [1,3]:
                if polyactive==True and canvasRect.collidepoint(mx,my):
                    startx,starty=e.pos     #the next point to be drawn from in the polygon 
            if drawing==True:
                undolist.append(screen.subsurface(325,250,900,500).copy()) #adds image to undo list for future use
                drawing=False
    #----------------------------------------------------------------------
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
        drawing=True
    
    brushHead=Surface((size*2,size*2),SRCALPHA)  #draw using alpha     
    draw.circle(brushHead,(c[0],c[1],c[2],5),(size,size),size) #size and colour adjustable alpha circle for airbrush tool
    
    if coloursRect.collidepoint(mx,my):
        if mb[0]==1:
            col=screen.get_at((mx,my)) #changes colour 1
        if mb[2]==1:
            col2=screen.get_at((mx,my)) #changes colour 2
    draw.rect(screen,col,colourRect) #visual aid showing colour 1
    draw.rect(screen,(255,255,255),colourRect,2)
    draw.rect(screen,col2,colour2Rect) #visual aid showing colour 2
    draw.rect(screen,(255,255,255),colour2Rect,2)

    if mb[0]==1:
        c=col #universal colour will be first colour
    if mb[2]==1:
        c=col2 #universal colour will be second colour
    
    screen.blit(tools,(27,295)) #blits tool area to avoid overlapping of translucent pixels in png images for buttons
    screen.blit(pencil,(27,295)) #blits stamps and draws unselected shapes constantly when not being used or hovered over
    screen.blit(eraser,(87,300))
    screen.blit(marker,(140,298))
    screen.blit(paintbrush,(195,300))
    screen.blit(spray,(264,298))
    screen.blit(fill,(32,355))
    draw.rect(screen,(0,0,0),rect,2)
    draw.rect(screen,(0,0,0),fullrect)
    draw.ellipse(screen,(0,0,0),ellipsebutton,2)
    draw.ellipse(screen,(0,0,0),fullellipsebutton)
    draw.line(screen,(0,0,0),(60,450),(100,410),3)
    screen.blit(dropper,(115,410))
    screen.blit(airbrush,(168,408))
    draw.polygon(screen,(0,0,0),[(245,410),(225,430),(235,450),(255,450),(265,430)],3)

    screen.blit(sizetxt,(97,465)) #text next to size indicator
    draw.circle(screen,(0,0,0),(195,485),size) #circle indicating size tools are using

    #drawn to avoid distorted stamp button images due to translucent pixels being drawn over
    draw.rect(screen,(255,255,255),batRect)
    draw.rect(screen,(255,255,255),bat2Rect)
    draw.rect(screen,(255,255,255),jokerRect)
    draw.rect(screen,(255,255,255),mobileRect)
    draw.rect(screen,(255,255,255),batgirlRect)
    draw.rect(screen,(255,255,255),catwomanRect)
    draw.rect(screen,(255,255,255),robinRect)
    draw.rect(screen,(255,255,255),knightRect)
    draw.rect(screen,(255,255,255),harleyRect)

    #blits button images constantly when other if statements are not active (tool selection, tool hover)
    screen.blit(batmanbutton,(880,45))
    screen.blit(batman2button,(950,45))
    screen.blit(jokerbutton,(1020,45))
    screen.blit(batgirlbutton,(1090,45))
    screen.blit(catwomanbutton,(1160,45))
    screen.blit(robinbutton,(915,105))
    screen.blit(knightbutton,(985,105))
    screen.blit(harleybutton,(1055,105))
    screen.blit(mobilebutton,(1125,105))

    #draws borders around stamp and background buttons when not selected or hovered over
    draw.rect(screen,(128,128,128),batRect,2)
    draw.rect(screen,(128,128,128),bat2Rect,2)
    draw.rect(screen,(128,128,128),jokerRect,2)
    draw.rect(screen,(128,128,128),mobileRect,2)
    draw.rect(screen,(128,128,128),batgirlRect,2)
    draw.rect(screen,(128,128,128),catwomanRect,2)
    draw.rect(screen,(128,128,128),robinRect,2)
    draw.rect(screen,(128,128,128),knightRect,2)
    draw.rect(screen,(128,128,128),harleyRect,2)

    draw.rect(screen,(0,0,0),gothamroadRect,2)
    draw.rect(screen,(0,0,0),gothamalleyRect,2)
    draw.rect(screen,(0,0,0),gothamstreetRect,2)
    draw.rect(screen,(0,0,0),gothamprisonRect,2)

    if undoRect.collidepoint(mx,my) and click==True: #to select any button (tools, stamps, backgrounds) the button must be clicked on, not dragged on by a used mouse
        polyactive=False
        length=len(undolist)
        if length>1:
            if length>=1:
                redolist.append(undolist.pop()) #removes image and inserts image into redo list 
            screen.blit(undolist[-1],(325,250))
    if redoRect.collidepoint(mx,my) and click==True:
        polyactive=False
        length=len(redolist)
        if length>0:
            lastpic=redolist[-1]
            screen.blit(lastpic,(325,250))
            undolist.append(redolist.pop()) #removes image from redo list and inserts into undo list
    if drawing==True:
        redolist=[] #makes list so what is being drawn has nothing after it in the list to go to when redo button is clicked

    if saveRect.collidepoint(mx,my) and click==True:
        filename=filedialog.asksaveasfilename(defaultextension=".png") #asks to enter filename for saving
        if filename!="":    #will not crash if nothing is entered
            image.save(canvas,filename)
    if loadRect.collidepoint(mx,my) and click==True:
        filename=filedialog.askopenfilename(filetypes=[("Images","*.jpg;*.png;*.jpeg;*.bmp")]) #asks for filename to open
        if filename!="":
            pic=image.load(filename)
            screen.blit(pic,(325,250))
    if clearRect.collidepoint(mx,my) and click==True:
        draw.rect(screen,(255,255,255),canvasRect) #draws white canvas to clear
    
    if pencilRect.collidepoint(mx,my):
        screen.blit(pencilhover,(27,295)) #blits special hover image (used for other tools below)
        if click==True:     #selects tool
            tool="pencil"
    if eraserRect.collidepoint(mx,my):
        screen.blit(eraserhover,(87,300))
        if click==True:
            tool="eraser"
    if markerRect.collidepoint(mx,my):
        screen.blit(markerhover,(140,298))
        if click==True:
            tool="marker"
    if paintRect.collidepoint(mx,my):
        screen.blit(painthover,(195,300))
        if click==True:
            tool="paint"
    if sprayRect.collidepoint(mx,my):
        screen.blit(sprayhover,(264,298))
        if click==True:
            tool="spray"
    if fillRect.collidepoint(mx,my):
        screen.blit(fillhover,(32,355))
        if click==True:
            tool="fill"
    if rectRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,255),rect,2)
        if click==True:
            tool="rect"
    if fullrectRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,255),fullrect)
        if click==True:
            tool="fullrect"
    if ellipseRect.collidepoint(mx,my):
        draw.ellipse(screen,(255,255,255),ellipsebutton,2)
        if click==True:
            tool="ellipse"
    if fullellipseRect.collidepoint(mx,my):
        draw.ellipse(screen,(255,255,255),fullellipsebutton)
        if click==True:
            tool="fullellipse"
    if lineRect.collidepoint(mx,my):
        draw.line(screen,(255,255,255),(60,450),(100,410),3)
        if click==True:
            tool="line"
    if dropperRect.collidepoint(mx,my):
        screen.blit(dropperhover,(115,410))
        if click==True:
            tool="dropper"
    if airbrushRect.collidepoint(mx,my):
        screen.blit(airbrushhover,(168,408))
        if click==True:
            tool="airbrush"
    if polygonRect.collidepoint(mx,my):
        draw.polygon(screen,(255,255,255),[(245,410),(225,430),(235,450),(255,450),(265,430)],3)
        if click==True:
            tool="polygon"
            polyactive=False #resets starting point for polygon

    if batRect.collidepoint(mx,my):
        screen.blit(batmanbuttonhover,(880,45))     #blits special hover button and special hover border (used for other stamps and backgrounds below)
        draw.rect(screen,(0,0,0),batRect,2)
        if click==True:
            tool="batman"
    if bat2Rect.collidepoint(mx,my):
        screen.blit(batman2buttonhover,(950,45))
        draw.rect(screen,(0,0,0),bat2Rect,2)
        if click==True:
            tool="batman2"
    if jokerRect.collidepoint(mx,my):
        screen.blit(jokerbuttonhover,(1020,45))
        draw.rect(screen,(0,0,0),jokerRect,2)
        if click==True:
            tool="joker"
    if batgirlRect.collidepoint(mx,my):
        screen.blit(batgirlbuttonhover,(1090,45))
        draw.rect(screen,(0,0,0),batgirlRect,2)
        if click==True:
            tool="batgirl"
    if catwomanRect.collidepoint(mx,my):
        screen.blit(catwomanbuttonhover,(1160,45))
        draw.rect(screen,(0,0,0),catwomanRect,2)
        if click==True:
            tool="catwoman"
    if robinRect.collidepoint(mx,my):
        screen.blit(robinbuttonhover,(915,105))
        draw.rect(screen,(0,0,0),robinRect,2)
        if click==True:
            tool="robin"
    if knightRect.collidepoint(mx,my):
        screen.blit(knightbuttonhover,(985,105))
        draw.rect(screen,(0,0,0),knightRect,2)
        if click==True:
            tool="knight"
    if harleyRect.collidepoint(mx,my):
        screen.blit(harleybuttonhover,(1055,105))
        draw.rect(screen,(0,0,0),harleyRect,2)
        if click==True:
            tool="harley"
    if mobileRect.collidepoint(mx,my):
        screen.blit(mobilebuttonhover,(1125,105))
        draw.rect(screen,(0,0,0),mobileRect,2)
        if click==True:
            tool="batmobile"
    
    if gothamroadRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,255),gothamroadRect,2)
        if click==True: 
            screen.blit(gothamroad,(325,250)) #blits background onto canvas
            undolist.append(screen.subsurface(325,250,900,500).copy()) #adds image to undo list for use
    if gothamalleyRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,255),gothamalleyRect,2)
        if click==True:
            screen.blit(gothamalley,(325,250))
            undolist.append(screen.subsurface(325,250,900,500).copy())
    if gothamstreetRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,255),gothamstreetRect,2)
        if click==True:
            screen.blit(gothamstreet,(325,250))
            undolist.append(screen.subsurface(325,250,900,500).copy())
    if gothamprisonRect.collidepoint(mx,my):
        draw.rect(screen,(255,255,255),gothamprisonRect,2)
        if click==True:
            screen.blit(gothamprison,(325,250))
            undolist.append(screen.subsurface(325,250,900,500).copy())
    
            
    if tool=="pencil":
        screen.blit(pencilselect,(27,295))
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)     #makes it so nothing is drawn outside of the canvas
            draw.line(screen,c,(mx,my),(ddmx,ddmy),2)
            screen.set_clip(None)   #makes features outside the canvas accessible
        ddmx,ddmy=mx,my #new points for the line and dot connections
    if tool=="eraser":
        screen.blit(eraserselect,(87,300))
        dist=hypot(mx-dmx,my-dmy) #distance formula used throughout the program to cover all pixels where shapes are not drawn, and make a smooth finish. Used for other tools as well
        dist=max(1,dist)
        sx=(mx-dmx)/dist
        sy=(my-dmy)/dist
        times=int(dist)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            for i in range(times):  #covers each pixel
                draw.circle(screen,(255,255,255),(int(dmx+sx*i),int(dmy+sy*i)),size)
            screen.set_clip(None)   
    if tool=="marker":
        screen.blit(markerselect,(140,298))
        dist=hypot(mx-dmx,my-dmy)
        dist=max(1,dist)
        sx=(mx-dmx)/dist
        sy=(my-dmy)/dist
        times=int(dist)
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            for i in range(times):
                draw.line(screen,c,(dmx+sx*i-size,dmy+sy*i-size),(dmx+sx*i+size,dmy+sy*i+size),5)
            screen.set_clip(None)
    if tool=="paint":
        screen.blit(paintselect,(195,300))
        dist=hypot(mx-dmx,my-dmy)
        dist=max(1,dist)
        sx=(mx-dmx)/dist
        sy=(my-dmy)/dist
        times=int(dist)
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            for i in range(times):
                draw.circle(screen,c,(int(dmx+sx*i),int(dmy+sy*i)),size)
            screen.set_clip(None)
    if tool=="spray":
        screen.blit(sprayselect,(264,298))
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            for i in range(size*2):   #does calculations faster
                h=randint(0-size,size) #chooses random number within radius of spray area for height
                w=randint(0-size,size) #chooses random number within radius of spray area for width
                dist=hypot(h,w)
                if dist<=size:  #the size is the radius of the circular spray area. The distance must be smaller than the radius to create a circular area
                    draw.circle(screen,c,(mx+h,my+w),0)
            screen.set_clip(None)
    if tool=="fill":
        screen.blit(fillselect,(32,355))
        if leftclick==True and canvasRect.collidepoint(mx,my) or rightclick==True and canvasRect.collidepoint(mx,my):
            replace=screen.get_at((mx,my))  #the colour being replaced
            if replace!=c:
                pixels=[(mx1,my1)]  #start point for pixels to be covered
                while pixels!=[]:
                    omx,omy=pixels.pop()
                    if screen.get_at((omx,omy))==replace and canvasRect.collidepoint(omx,omy):
                        screen.set_at((omx,omy),c)  #changes colour
                        pixels+=[(omx+1,omy),(omx-1,omy),(omx,omy+1),(omx,omy-1)]   #goes to other pixels for checking
    if tool=="rect":
        draw.rect(screen,(174,18,18),rect,2)
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250)) #keeps shape from leaving mark everywhere it hovers over
            draw.rect(screen,c,(mx1,my1,mx-mx1,my-my1),size) #draws rectangle from click point to where the mouse is dragged to and released
            screen.set_clip(None)
    if tool=="fullrect":
        draw.rect(screen,(174,18,18),fullrect)
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            draw.rect(screen,c,(mx1,my1,mx-mx1,my-my1))
            screen.set_clip(None)
    if tool=="ellipse":
        draw.ellipse(screen,(174,18,18),ellipsebutton,2)
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            ellipse=Rect(mx1,my1,(mx-mx1),(my-my1)) #ellipse is to be drawn from click point to where the mouse is dragged and released
            ellipse.normalize()     
            if size*2>ellipse.height or size*2>ellipse.width:
                draw.ellipse(screen,c,ellipse) #draws filled ellipse if radius of the ellipse is greater than the thickness of the ellipse, which would make it crash
            else:
                draw.ellipse(screen,c,(ellipse),size) #draws unfilled ellipse in other cases
            screen.set_clip(None)
    if tool=="fullellipse":
        draw.ellipse(screen,(174,18,18),fullellipsebutton)
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            ellipse=Rect(mx1,my1,(mx-mx1),(my-my1))
            ellipse.normalize()
            draw.ellipse(screen,c,ellipse)
            screen.set_clip(None)
    if tool=="line":
        draw.line(screen,(174,18,18),(60,450),(100,410),3)
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250)) #keeps line from being seen everywhere it hovers over
            draw.line(screen,c,(mx1,my1),(mx,my),size)
            screen.set_clip(None)
    if tool=="dropper":
        screen.blit(dropperselect,(115,410))
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            col=screen.get_at((mx,my)) #changes colour 1
        if mb[2]==1 and canvasRect.collidepoint(mx,my):
            col2=screen.get_at((mx,my)) #changes colour 2
    if tool=="airbrush":
        screen.blit(airbrushselect,(168,408))
        dist=hypot(mx-dmx,my-dmy)
        dist=max(1,dist)
        sx=(mx-dmx)/dist
        sy=(my-dmy)/dist
        times=int(dist)
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            for i in range(times):
                screen.blit(brushHead,(dmx+sx*i-size,dmy+sy*i-size)) #blits adjusted circle in every possible space around every center(dmx+sx*i)
            screen.set_clip(None)
    if tool=="polygon":
        draw.polygon(screen,(174,18,18),[(245,410),(225,430),(235,450),(255,450),(265,430)],3) #highlight to show tool is selected
        if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))   #keeps lines from marking everywhere they hover over
            draw.line(screen,c,(startx,starty),(mx,my),size) #draws line from last point in polygon
            screen.set_clip(None)
    dmx,dmy=mx,my   #the point where pixels in between it and mx,my must be covered for various tools
    
    if tool=="batman":
        screen.blit(batmanbuttonhover,(880,45)) #indicates the tool is selected (used for other stamps below)
        draw.rect(screen,(174,18,18),batRect,2) #indicates tool is selected (highlight method used for other stamps below)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250)) #keeps blitting the canvas image to prevent image from blitting everywhere it goes, but only where the mouse is released (used for other stamps below)
            screen.blit(batman,(mx-72,my-112)) #blits image to look like the mouse is in the center (dimensions are different for each stamp
            screen.set_clip(None)
    if tool=="batman2":
        screen.blit(batman2buttonhover,(950,45))
        draw.rect(screen,(174,18,18),bat2Rect,2)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            screen.blit(batman2,(mx-162,my-75))
            screen.set_clip(None)
    if tool=="joker":
        screen.blit(jokerbuttonhover,(1020,45))
        draw.rect(screen,(174,18,18),jokerRect,2)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            screen.blit(joker,(mx-34,my-100))
            screen.set_clip(None)
    if tool=="batgirl":
        screen.blit(batgirlbuttonhover,(1090,45))
        draw.rect(screen,(174,18,18),batgirlRect,2)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            screen.blit(batgirl,(mx-69,my-100))
            screen.set_clip(None)
    if tool=="catwoman":
        screen.blit(catwomanbuttonhover,(1160,45))
        draw.rect(screen,(174,18,18),catwomanRect,2)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            screen.blit(catwoman,(mx-40,my-100))
            screen.set_clip(None)
    if tool=="robin":
        screen.blit(robinbuttonhover,(915,105))
        draw.rect(screen,(174,18,18),robinRect,2)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            screen.blit(robin,(mx-80,my-105))
            screen.set_clip(None)
    if tool=="knight":
        screen.blit(knightbuttonhover,(985,105))
        draw.rect(screen,(174,18,18),knightRect,2)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            screen.blit(knight,(mx-45,my-105))
            screen.set_clip(None)
    if tool=="harley":
        screen.blit(harleybuttonhover,(1055,105))
        draw.rect(screen,(174,18,18),harleyRect,2)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            screen.blit(harley,(mx-49,my-100))
            screen.set_clip(None)
    if tool=="batmobile":
        screen.blit(mobilebuttonhover,(1125,105))
        draw.rect(screen,(174,18,18),mobileRect,2)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(canvas,(325,250))
            screen.blit(mobile,(mx-200,my-108))
            screen.set_clip(None)
    #----------------------------------------------------------------------
    display.flip()
    clock.tick(60)

quit()
