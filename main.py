import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; CREAM=(247,242,231); INK=(20,20,20); RED=(185,28,28); NAVY=(30,58,95); GREY=(90,88,82); LINE=(200,192,175)
SB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; SR="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; SER="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
def F(s,b=False,ser=False):
    try: return ImageFont.truetype(SER if ser else (SB if b else SR),s)
    except Exception: return ImageFont.load_default()
def wrap(d,t,f,mw):
    words=t.split(); lines=[]; cur=""
    for w in words:
        s=(cur+" "+w).strip()
        if d.textlength(s,font=f)<=mw: cur=s
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def txt(d,x,y,s,f,fill=INK):
    d.text((x,y),s,font=f,fill=fill); return d.textlength(s,font=f)
def chip(d,x,y,label,fill):
    f=F(6,True); w=d.textlength(label,font=f)+8; d.rounded_rectangle([x,y,x+w,y+11],radius=2,fill=fill); d.text((x+4,y+1),label,font=f,fill=(255,255,255)); return w+4
def scene(d,b,kind):
    x0,y0,x1,y1=b; sky={"tower":(30,32,68),"gate":(140,30,30),"court":(30,58,95),"drone":(20,24,48),"trophy":(20,90,50),"ship":(25,70,95),"chart":(15,60,45),"server":(120,15,15),"heli":(90,70,40),"market":(140,90,25),"desert":(180,120,40),"strike":(150,60,20),"rocket":(10,15,40),"fire":(160,50,20),"quake":(70,60,90),"court2":(30,58,95)}.get(kind,(40,60,90))
    d.rectangle(b,fill=sky); d.rectangle([x0,y1-14,x1,y1],fill=(35,32,28))
    if kind=="tower":
        d.rectangle([x0+120,y0+18,x0+150,y1-14],fill=(210,200,170)); d.rectangle([x0+155,y0+38,x0+175,y1-14],fill=(170,160,135)); d.polygon([(x0+135,y0+6),(x0+142,y0+18),(x0+128,y0+18)],fill=(230,220,190)); d.ellipse([x0+185,y0+22,x0+215,y0+52],fill=(255,140,40)); d.ellipse([x0+193,y0+30,x0+207,y0+44],fill=(255,200,80)); d.polygon([(x0+60,y0+30),(x0+95,y0+44),(x0+60,y0+44)],fill=(120,120,120)); d.rectangle([x0+88,y0+40,x0+94,y0+44],fill=(60,60,60))
    elif kind=="gate":
        d.rectangle([x0+70,y0+30,x0+250,y1-14],fill=(150,40,35)); d.rectangle([x0+130,y0+48,x0+190,y1-14],fill=(60,20,18)); d.polygon([(x0+70,y0+30),(x0+160,y0+8),(x0+250,y0+30)],fill=(200,60,50)); d.rectangle([x0+150,y0+18,x0+170,y0+30],fill=(230,200,90)); d.rectangle([x0+20,y0+55,x0+60,y1-14],fill=(110,30,28)); d.rectangle([x0+260,y0+55,x0+300,y1-14],fill=(110,30,28))
    elif kind=="court":
        d.rectangle([x0+90,y0+25,x0+230,y1-14],fill=(220,215,200)); d.polygon([(x0+80,y0+25),(x0+160,y0+5),(x0+240,y0+25)],fill=(180,170,150)); d.rectangle([x0+150,y0+35,x0+170,y1-14],fill=(120,110,95)); d.rectangle([x0+110,y0+40,x0+125,y1-14],fill=(120,110,95)); d.rectangle([x0+195,y0+40,x0+210,y1-14],fill=(120,110,95)); d.ellipse([x0+255,y0+30,x0+295,y0+70],fill=(230,200,90)); d.text((x0+258,y0+38),"H",font=F(22,True),fill=(90,70,10))
    elif kind=="drone":
        d.ellipse([x0+40,y0+15,x0+80,y0+55],fill=(255,150,50)); d.rectangle([x0+130,y0+35,x0+210,y1-14],fill=(60,58,60)); d.rectangle([x0+150,y0+50,x0+165,y1-14],fill=(40,40,42)); d.rectangle([x0+180,y0+45,x0+195,y1-14],fill=(40,40,42)); d.polygon([(x0+230,y0+25),(x0+270,y0+38),(x0+230,y0+38)],fill=(150,150,150)); d.rectangle([x0+262,y0+34,x0+270,y0+38],fill=(80,80,80))
    elif kind=="trophy":
        d.ellipse([x0+130,y0+12,x0+190,y0+62],fill=(240,200,60)); d.rectangle([x0+152,y0+58,x0+168,y1-14],fill=(200,160,40)); d.rectangle([x0+135,y0+62,x0+185,y1-14],fill=(180,140,30)); d.rectangle([x0+30,y0+55,x0+90,y1-14],fill=(0,120,70)); d.rectangle([x0+230,y0+55,x0+290,y1-14],fill=(200,40,40))
    elif kind=="ship":
        d.rectangle([x0+60,y0+55,x0+270,y0+75],fill=(200,60,40)); d.rectangle([x0+80,y0+35,x0+130,y0+55],fill=(240,240,240)); d.rectangle([x0+140,y0+42,x0+240,y0+55],fill=(30,90,140)); d.rectangle([x0,y1-22,x1,y1],fill=(25,70,110)); d.ellipse([x0+280,y0+18,x0+305,y0+43],fill=(255,200,90))
    elif kind=="chart":
        d.line([(x0+15,y1-25),(x0+80,y0+55),(x0+150,y0+62),(x0+220,y0+30),(x0+305,y0+12)],fill=(40,200,90),width=4); d.line([(x0+15,y0+22),(x0+305,y0+22)],fill=(255,255,255),width=2); d.rectangle([x0+15,y0+45,x0+35,y1-14],fill=(40,90,140)); d.rectangle([x0+45,y0+55,x0+65,y1-14],fill=(40,90,140)); d.rectangle([x0+75,y0+35,x0+95,y1-14],fill=(40,90,140))
    elif kind=="server":
        d.rectangle([x0+90,y0+20,x0+230,y1-14],fill=(50,50,55)); 
        for i in range(4): d.rectangle([x0+100,y0+24+i*12,x0+220,y0+32+i*12],fill=(90,90,100)); d.ellipse([x0+255,y0+15,x0+300,y0+60],fill=(255,60,50)); d.text((x0+268,y0+28),"!",font=F(22,True),fill=(255,255,255))
    elif kind=="heli":
        d.ellipse([x0+120,y0+30,x0+200,y0+62],fill=(90,100,110)); d.line([(x0+100,y0+32),(x0+220,y0+32)],fill=(200,200,200),width=3); d.rectangle([x0+200,y0+38,x0+280,y0+48],fill=(80,90,100)); d.polygon([(x0+140,y0+62),(x0+170,y0+62),(x0+155,y1-14)],fill=(70,80,90)); d.polygon([(x0+20,y0+60),(x0+90,y0+45),(x0+110,y0+62),(x0+40,y1-14)],fill=(120,100,70))
    elif kind=="market":
        d.rectangle([x0+40,y0+50,x0+280,y1-14],fill=(200,170,120)); d.polygon([(x0+30,y0+50),(x0+160,y0+18),(x0+290,y0+50)],fill=(200,60,50)); d.rectangle([x0+70,y0+62,x0+120,y1-14],fill=(120,80,50)); d.rectangle([x0+200,y0+62,x0+250,y1-14],fill=(120,80,50))
    elif kind=="desert":
        d.ellipse([x0+240,y0+12,x0+285,y0+57],fill=(255,210,100)); d.polygon([(x0,y1-14),(x0+120,y0+55),(x0+240,y1-14)],fill=(210,170,100)); d.polygon([(x0+140,y1-14),(x0+250,y0+65),(x1,y1-14)],fill=(190,150,85)); d.rectangle([x0+60,y0+55,x0+110,y0+70],fill=(80,70,60))
    elif kind=="strike":
        d.ellipse([x0+50,y0+15,x0+100,y0+65],fill=(255,140,40)); d.ellipse([x0+62,y0+27,x0+88,y0+53],fill=(255,200,80)); d.rectangle([x0+150,y0+55,x0+290,y0+72],fill=(90,85,80)); d.rectangle([x0+170,y0+40,x0+210,y0+55],fill=(120,115,110)); d.rectangle([x0+230,y0+45,x0+270,y0+55],fill=(120,115,110))
    elif kind=="rocket":
        d.polygon([(x0+150,y0+8),(x0+170,y0+45),(x0+130,y0+45)],fill=(240,240,240)); d.polygon([(x0+130,y0+45),(x0+115,y0+65),(x0+140,y0+55)],fill=(200,60,50)); d.polygon([(x0+170,y0+45),(x0+185,y0+65),(x0+160,y0+55)],fill=(200,60,50)); d.ellipse([x0+143,y0+22,x0+157,y0+36],fill=(40,90,160)); d.ellipse([x0+250,y0+15,x0+275,y0+40],fill=(255,255,255)); d.ellipse([x0+60,y0+25,x0+75,y0+40],fill=(255,255,255))
    else:
        d.rectangle([x0+40,y0+30,x0+280,y1-14],fill=(60,70,90)); d.ellipse([x0+250,y0+12,x0+295,y0+57],fill=(255,210,100))
def mini(d,b,kind):
    x0,y0,x1,y1=b; sky={"drone":(20,24,48),"trophy":(20,90,50),"ship":(25,70,95),"chart":(15,60,45),"server":(120,15,15),"heli":(90,70,40),"market":(140,90,25),"desert":(180,120,40),"strike":(150,60,20),"rocket":(10,15,40)}.get(kind,(40,60,90)); d.rectangle(b,fill=sky)
    if kind=="drone": d.ellipse([x0+20,y0+5,x0+45,y0+28],fill=(255,150,50)); d.rectangle([x0+90,y0+14,x0+160,y0+26],fill=(60,58,60))
    elif kind=="trophy": d.ellipse([x0+85,y0+3,x0+110,y0+26],fill=(240,200,60)); d.rectangle([x0+94,y0+24,x0+101,y1],fill=(200,160,40))
    elif kind=="ship": d.rectangle([x0+40,y0+16,x0+160,y0+26],fill=(200,60,40)); d.rectangle([x0+55,y0+7,x0+80,y0+16],fill=(240,240,240))
    elif kind=="chart": d.line([(x0+10,y1-6),(x0+60,y0+16),(x0+110,y0+20),(x0+160,y0+8)],fill=(40,200,90),width=3)
    elif kind=="server": d.rectangle([x0+60,y0+6,x0+130,y1-4],fill=(50,50,55)); d.ellipse([x0+145,y0+5,x0+168,y0+28],fill=(255,60,50)); d.text((x0+153,y0+10),"!",font=F(12,True),fill=(255,255,255))
    elif kind=="heli": d.ellipse([x0+80,y0+8,x0+120,y0+26],fill=(90,100,110)); d.line([(x0+60,y0+12),(x0+140,y0+12)],fill=(200,200,200),width=2); d.rectangle([x0+120,y0+15,x0+170,y0+22],fill=(80,90,100))
    elif kind=="market": d.rectangle([x0+30,y0+15,x0+165,y1],fill=(200,170,120)); d.polygon([(x0+25,y0+15),(x0+98,y0+3),(x0+170,y0+15)],fill=(200,60,50))
    elif kind=="desert": d.ellipse([x0+150,y0+4,x0+172,y0+26],fill=(255,210,100)); d.polygon([(x0,y1),(x0+80,y0+14),(x0+160,y1)],fill=(210,170,100))
    elif kind=="strike": d.ellipse([x0+30,y0+4,x0+58,y0+30],fill=(255,140,40)); d.rectangle([x0+95,y0+18,x0+175,y0+27],fill=(90,85,80))
    elif kind=="rocket": d.polygon([(x0+90,y0+2),(x0+102,y0+22),(x0+78,y0+22)],fill=(240,240,240)); d.ellipse([x0+150,y0+5,x0+165,y0+20],fill=(255,255,255))
    else: d.rectangle([x0+30,y0+10,x0+165,y1-4],fill=(60,70,90))
CONT=[[( -168,66),(-140,70),(-125,72),(-110,73),(-95,80),(-80,73),(-65,60),(-55,47),(-60,45),(-75,35),(-80,25),(-90,21),(-97,16),(-105,20),(-115,28),(-125,40),(-125,48),(-140,60),(-155,58),(-165,60)],[(-80,10),(-75,5),(-60,5),(-50,0),(-40,-5),(-35,-8),(-40,-20),(-48,-28),(-58,-35),(-65,-40),(-70,-50),(-73,-55),(-70,-40),(-73,-20),(-80,-5)],[(-10,36),(-9,43),(-2,48),(-5,50),(0,51),(5,53),(8,57),(10,59),(18,56),(21,55),(24,59),(28,60),(30,62),(25,65),(20,70),(15,70),(5,60),(5,58),(0,55),(-5,50),(-10,43)],[(-17,15),(-10,30),(0,36),(10,37),(20,32),(30,31),(35,28),(40,15),(43,11),(48,11),(51,10),(44,0),(40,-10),(35,-18),(32,-26),(28,-33),(20,-35),(16,-28),(12,-18),(12,-5),(9,4),(-8,5) ],[(30,36),(35,36),(40,38),(45,40),(50,40),(55,45),(60,50),(65,55),(70,60),(75,68),(80,70),(90,75),(100,76),(110,74),(120,73),(130,72),(140,72),(150,70),(160,65),(162,60),(158,52),(142,50),(140,40),(135,35),(130,32),(127,35),(122,30),(120,25),(110,20),(108,12),(105,8),(100,6),(98,10),(95,15),(90,22),(85,20),(80,15),(77,8),(75,12),(70,20),(65,25),(60,25),(55,26),(52,28),(48,30),(43,35),(40,36)],[(113,-22),(114,-30),(115,-35),(120,-34),(129,-32),(137,-35),(140,-38),(145,-38),(150,-37),(153,-32),(153,-27),(150,-22),(146,-19),(142,-11),(136,-12),(132,-11),(126,-14),(122,-17),(118,-20)],[(-45,60),(-40,65),(-30,68),(-22,70),(-25,76),(-35,80),(-50,78),(-58,72),(-55,65)]]
PINS=[(24.7,46.7),(31.2,121.5),(40.7,-74.0),(47.8,35.2),(14.7,-17.4),(26.5,56.2),(40.9,-73.0),(47.7,-122.1),(39.8,30.5),(10.4,-75.5),(12.8,45.0),(13.0,44.9),(39.7,98.5)]
def draw():
    im=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(im); M=16
    d.text((M,4),"THE WORLD ON ONE DAY",font=F(9,True),fill=RED); _k="38 STORIES  ·  7 REGIONS  ·  14 FIELDS  ·  TUESDAY 24 NOVEMBER 2026"; d.text((W-M-d.textlength(_k,font=F(8,True)),4),_k,font=F(8,True),fill=NAVY)
    d.line([(M,20),(W-M,20)],fill=LINE,width=1); d.text((M,24),"Tuesday 24 November 2026",font=F(30,True,True),fill=INK); d.text((W-190,34),"ONE DAY. ONE PAGE.",font=F(10,True),fill=RED)
    d.text((M,58),"Riyadh tower hit again  ·  Shanghai party chief probed  ·  Huawei guilty on 10 of 12 counts",font=F(10,False,True),fill=RED)
    regs=[("Europe",7,(30,58,95)),("Middle East",8,(185,28,28)),("Asia",9,(180,120,20)),("Africa",5,(20,110,60)),("Americas",5,(110,60,140)),("Oceania",0,(90,88,82)),("World / Space",4,(10,90,110))]
    x=M; y=76
    for name,n,c in regs:
        w=138; d.rectangle([x,y,x+w-4,y+15],fill=c); d.text((x+6,y+2),f"{name} {n}",font=F(8,True),fill=(255,255,255)); x+=w
    d.text((M,96),"THE DAY IN UTC",font=F(8,True),fill=RED); utc=[("02:15","NATO vows space defence"),("08:16","Hanoi hot-pot blast"),("10:42","Saudi strikes Yemen"),("14:27","Riyadh tower hit"),("16:51","Houthis 60 km from Aden"),("18:58","Hormuz ship attack"),("20:41","Huawei guilty")]
    x=M
    for t,e in utc:
        d.text((x,106),t,font=F(9,True),fill=NAVY); d.text((x,117),e,font=F(7),fill=INK); x+=143
    d.text((M,134),"THE DAY IN NUMBERS",font=F(8,True),fill=RED); nums=[("11","hurt in Riyadh"),("9","killed in Ukraine"),("50,018","Dow, first over 50k"),("+8.99%","Taiex, record high"),("25","killed / missing, Yemen"),("26","Cikande fire toll"),("10 / 12","Huawei guilty counts"),("96 / 73","drones fired / downed")]
    x=M
    for v,l in nums:
        d.text((x,143),v,font=F(15,True),fill=RED); d.text((x,162),l,font=F(7),fill=INK); x+=123
    d.line([(M,176),(W-M,176)],fill=LINE,width=1)
    heroes=[(1,"RIYADH · MIDDLE EAST","CONFIRMED","Saudi officials · AP","Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone strikes the PIF tower — the tallest in Riyadh — for the 2nd time in a week. 11 hurt: 2 Saudi, 2 Indian, 3 Nepali, 4 Egyptian.","tower"),(2,"SHANGHAI · ASIA","OFFICIAL","CCDI · Reuters","China probes Shanghai party chief Chen Jining","Chen Jining, 62, is probed for 'serious violations' — the 4th Politburo member to fall in a graft inquiry, the year's biggest elite shock.","gate"),(3,"NEW YORK · US / TECH","CONFIRMED","US federal court · AP","Huawei guilty on 10 of 12 counts","A US jury finds Huawei guilty on 10 of 12 counts — trade-secret theft and bank fraud. Cleared of racketeering. Sentencing Sep 2027; Huawei to appeal.","court")]
    hx=M; hy=182; hw=322; hh=168
    for n,kick,cf,src,head,deck,kind in heroes:
        d.rectangle([hx,hy,hx+hw,hy+hh],outline=LINE,width=1,fill=(255,255,255)); scene(d,(hx+1,hy+1,hx+hw-1,hy+82),kind); d.text((hx+6,hy+86),f"{n}  {kick}",font=F(7,True),fill=RED); cx=hx+6; cy=hy+99; cx+=chip(d,cx,cy,cf,(20,140,60) if cf=="CONFIRMED" else (30,58,95)); d.text((cx,cy+1),src,font=F(6),fill=GREY)
        yy=hy+112
        for ln in wrap(d,head,F(10,True),hw-12): d.text((hx+6,yy),ln,font=F(10,True),fill=INK); yy+=12
        for ln in wrap(d,deck,F(7),hw-12): d.text((hx+6,yy),ln,font=F(7),fill=INK); yy+=9
        hx+=hw+7
    cards=[(4,"ZAPORIZHZHIA · EUROPE / WAR","REPORTED","Ukrainian officials","Russian attacks kill 9 across Ukraine in a day","9 killed, 81 hurt in a day. 96 drones fired; 73 shot down or jammed over Kyiv.","drone"),(5,"CAS · AFRICA / SPORT","OFFICIAL","CAS","CAS hands Senegal back the AFCON title","Morocco forfeit 3–0, so Senegal win 1–0 and take the Africa Cup back.","trophy"),(6,"HORMUZ · MIDDLE EAST","REPORTED","UKMTO","IRGC attacks container ship in Hormuz","Ship attacked 18:58 UTC; navigation cut, exclusion zone north of Khasab, Oman.","ship"),(7,"NEW YORK · WORLD / MARKETS","CONFIRMED","Market close","Dow closes above 50,000 for the first time","Dow 50,018. Nasdaq −1.5% on chip slide; Taiex +8.99% record 40,122.","chart"),(8,"REDMOND · WORLD / TECH","REPORTED","Reuters","Microsoft declares 'Code Red' after historic outage","After a 24-hour outage, the worst in Exchange Online history: 1-hour recovery target, 5 workstreams.","server"),(9,"ESKISEHIR · EUROPE","REPORTED","Turkish officials","Turkish military helicopter crash kills 5","AS-532 helicopter crashes in Eskisehir; 5 killed. 19:52 UTC.","heli"),(10,"CARTAGENA · AMERICAS","REPORTED","Colombian officials","Supermarket hostages: 25 held in Cartagena","25 hostages in a Cartagena supermarket; 5 elderly women freed; landings halted ~45 min.","market"),(11,"ADEN · MIDDLE EAST","REPORTED","Wires","Houthis advance within 60 km of Aden","Houthi forces advance to within 60 km of Aden, Yemen. 16:51 UTC.","desert"),(12,"LAHJ · MIDDLE EAST","REPORTED","Yemeni officials","Saudi strikes kill 25, wound 6 in Yemen","Strikes on a bus and truck in Wadi Maabaq, Lahj: 25 killed or missing, 6 wounded.","strike"),(13,"JIUQUAN · WORLD / SPACE","OFFICIAL","CMSA","China names first foreign astronaut for Tiangong","Shenzhou-24 crew: Tang Hongbo, Wu Yi and Muhammad Zeeshan Ali of Pakistan — first foreigner on Tiangong.","rocket")]
    cw=193; ch=136; cy0=356
    for i,(n,kick,cf,src,head,deck,kind) in enumerate(cards):
        cx=M+(i%5)*(cw+6); cy=cy0+(i//5)*(ch+6); d.rectangle([cx,cy,cx+cw,cy+ch],outline=LINE,width=1,fill=(255,255,255)); mini(d,(cx+1,cy+1,cx+cw-1,cy+34),kind); d.text((cx+5,cy+37),f"{n}  {kick}",font=F(6,True),fill=RED); yy=cy+48
        for ln in wrap(d,head,F(8,True),cw-10): d.text((cx+5,yy),ln,font=F(8,True),fill=INK); yy+=10
        for ln in wrap(d,deck,F(7),cw-10)[:3]: d.text((cx+5,yy),ln,font=F(7),fill=INK); yy+=9
        chip(d,cx+5,cy+ch-14,cf,(20,140,60) if cf in ("CONFIRMED","OFFICIAL") else (90,88,82)); d.text((cx+52,cy+ch-13),src,font=F(6),fill=GREY)
    my=640; d.text((M,my),"WORLD MAP — PINS 1–13",font=F(8,True),fill=RED); mx,my0,mw,mh=M,my+14,384,150; d.rectangle([mx,my0,mx+mw,my0+mh],fill=(190,215,235),outline=LINE)
    def ll(lat,lon): return mx+(lon+180)/360*mw, my0+(84-lat)/142*mh
    for poly in CONT:
        pts=[ll(lat,lon) for lon,lat in poly]; d.polygon(pts,fill=(168,178,128),outline=(110,120,80))
    for i,(lat,lon) in enumerate(PINS,1):
        px,py=ll(lat,lon); d.ellipse([px-8,py-8,px+8,py+8],fill=RED,outline=(255,255,255)); d.text((px-3,py-6),str(i),font=F(7,True),fill=(255,255,255))
    d.text((mx,my0+mh+4),"Red pins = stories 1–13.  Riyadh 1 · Shanghai 2 · New York 3, 7 · Zaporizhzhia 4",font=F(6),fill=GREY); d.text((mx,my0+mh+14),"Senegal 5 · Hormuz 6 · Redmond 8 · Eskisehir 9 · Cartagena 10 · Aden 11 · Lahj 12 · Jiuquan 13",font=F(6),fill=GREY)
    ax=412; d.text((ax,my),"ALSO ON TUESDAY — 25 MORE STORIES",font=F(8,True),fill=RED)
    also=["14 Ankara: Haftar visits Turkey for the first time","15 London: UK sanctions Houthis + 4 officials","16 Villavicencio: Car bomb injures 23","17 Gaza: Israel kills Hamas security chief + 6","18 Baghdad: Iraq orders federal control of Kurdish oilfields","19 Gaza: Meningitis alert — 272 cases in Oct, 15 dead in 2026","20 DR Congo: Missing Cessna 208, rebels claim shootdown","21 Hanoi: Hot-pot blast kills ≥6, ≥10 hurt","22 Gulf of Finland: Ukraine hits ship Sparta II, 16 evacuated","23 Kuala Lumpur: Malaysia to return migrants to Myanmar","24 Ulleungdo: S. Korea shelter order, Russian jets in ADIZ","25 Dhaka: Hasina plans return 16 Dec","26 The Hague: 14 nations endorse ICJ Myanmar ruling (9–6)","27 Jakarta: Indonesia nominates 2 VP candidates","28 Beijing: China sentences official Ma to death for spying","29 Brussels: NATO vows defence against space threat","30 Mexico City: US drone aided El Chapo Isidro capture","31 San Salvador: Bukele names 3 soldiers killed in Haiti","32 Ottawa: Pentagon rebukes Canada — 41.9% air fleet ready","33 Washington: US adds Megaspeed to trade blacklist","34 Kyiv: Zelensky urges Ukraine / Russia / US / Europe talks","35 Ras Al Khaimah: Bus-truck crash kills 13, 14 hurt","36 London: England record 5,258 heat deaths, summer 2026","37 Kourou: Ariane 6 lofts 36 Amazon satellites","38 Cikande: Factory-fire toll rises to 26"]
    for i,s in enumerate(also):
        col=i//13; row=i%13; xx=ax+col*300; yy=my+16+row*13; d.text((xx,yy),s,font=F(7),fill=INK)
    dy=848; d.rectangle([M,dy,W-M,dy+104],outline=RED,width=2,fill=(255,240,240)); d.text((M+8,dy+5),"DATE CHECK",font=F(9,True),fill=RED)
    dc=["Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.","LEFT OUT (not 24 Nov): Hormuz mine claims, 4 tankers (Mon 23 Nov) · Huang returns as Nvidia CEO, shares +31% (Mon 23 Nov) · EU sanctions package 22 (Mon 23 Nov) · COP31 ends with no deal (Sun 22 Nov) · Corvette Merkury sunk (Sat 22 Nov) · El Chapo Isidro captured (Fri 20 Nov) · Cikande factory fire started (Sat 21 Nov) · ATP Finals (Sun 22 Nov) · F1 Las Vegas GP (Sat 21 Nov) · ICJ Myanmar ruling (last week).","NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) · MPR session to pick VP (11 Dec) · Huawei sentencing (Sep 2027) · Hasina return to Bangladesh (16 Dec)."]
    yy=dy+18
    for s in dc:
        for ln in wrap(d,s,F(7),W-2*M-16): d.text((M+8,yy),ln,font=F(7),fill=INK); yy+=10
    fy=958; d.line([(M,fy),(W-M,fy)],fill=LINE,width=1); d.text((M,fy+5),"Sources: dailysummaryof.com/world/2026-11-24 · Reuters · AP · CCDI · CAS · UKMTO · CMSA · UKHSA · wires.",font=F(7),fill=GREY)
    d.text((M,fy+17),"Chips: CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side's claim.",font=F(7),fill=GREY); d.text((M,fy+29),"Scenes are drawn illustrations, not photographs. All figures as reported 24 Nov 2026.",font=F(7),fill=GREY); d.text((W-260,fy+29),"THE WORLD ON ONE DAY · 24 NOV 2026",font=F(7,True),fill=NAVY)
    return im,d
if __name__=="__main__":
    im,_=draw(); out=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png"); os.makedirs(os.path.dirname(out) or ".",exist_ok=True); im.save(out,optimize=True)
