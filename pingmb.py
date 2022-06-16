import subprocess,sys,re

#Archivo de tamano 1024kb
MB="."*(1024*1024)

def pingmb(MBs,ip,verbose=False):
    #multiplicador de archivo dinamico * el tamano recibido en el input
    with open('tmp','w') as t:
        for i in range(0,int(MBs)):
            t.write(MB)
        t.close()
    r=subprocess.run(f"time scp tmp {ip}", shell=True, check=True,capture_output=True)
    out=r.stderr.decode("ASCII")
    time_s=re.match(".*system.([\d:\.]+)",out.strip()).group(1)
    tlist=time_s.replace(".",":").split(":")
    time=int(tlist[0])*60+int(tlist[1])+int(tlist[2])*.01
    try:
        subprocess.run(f"rm {ip}",shell=True,check=True)
    except:
        pass
    subprocess.run(f"rm tmp",shell=True,check=True)
    if(verbose):
        print(time, "s") 
    return time
    
if(__name__=="__main__"):
    if(len(sys.argv)!=3):
        print("python3 pingmb.py MB_size, IP")
    else:
        try:
            pingmb(sys.argv[1],sys.argv[2],verbose=True)
        except:
            print("Nop, vuelve a ingresar los parametros correctamente")
