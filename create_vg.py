import subprocess

pv = 'sda4'
cmd = 'pvcreate /dev/' + pv

sp = subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE,stderr = subprocess.PIPE
                      ,universal_newlines = True)
success_code = sp.wait()
out,err = sp.communicate()

if(success_code == 0):
    print(f'...\n{out}\n...')
    vg = 'myvg1'
    cmd = 'vgcreate ' + vg + ' /dev/' + pv
    sp = subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE,stderr = subprocess.PIPE
                          ,universal_newlines = True)
    success_code = sp.wait()
    out,err = sp.communicate()

    if(success_code == 0):
        print(f'Result : \n{out}')
    else:
        print(f'Error creating volume group....\n{err}')
else:
    print(f'Error creating phhysical volumne....\n{err}')
