import subprocess

cmd = 'pvs'
sp = subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE,stderr = subprocess.PIPE
                      ,universal_newlines = True)
success_code = sp.wait()

out,err = sp.communicate()

if(success_code == 0):
    print(f'List of all Physical Volumes : \n{out}')
    print('\n')
    cmd = 'vgcreate '
    vg_name = input('Enter the name of the volume group you want to create : ')
    cmd = cmd + vg_name + ' '
    n = input('Enter the number of physical volumes you want to include : ')
    for x in range(int(n)):
        pv = input('Enter the name of the physical volume {} (ex. sdb1) : '.format(x+1))
        cmd = cmd + '/dev/' + pv + ' '
    sp = subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE,stderr = subprocess.PIPE
                          ,universal_newlines = True)
    success_code = sp.wait()
    out,err = sp.communicate()

    if(success_code == 0):
        print(f'Result : {out}')
    else:
        print(f'Error......{err}')
else:
    print(f'Error........{err}\nMake sure you are signed in as root')
