import subprocess,sys,re

MB="A"*(1024*1024)

def pingmb(ip,MBs,verbose=False):
    #subprocess.run("echo \"LIIINUUUUX\" > tmp", shell=True)
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
        print("Usage: pingmb.py IP MB_size")
    else:
        try:
            pingmb(sys.argv[1],sys.argv[2],verbose=True)
        except:
            print("Malformatted input or server declined upload.")
