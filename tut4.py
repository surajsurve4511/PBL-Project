elif 'shutdown' is order or 'turn off' in order :
     speak('Hold on a second sir! Your system is on itsa way to shutdown')
     speak('MAke sure all of your applications are closed')
     time.sleep(5)
     subprocess.call(['shudown','/s'])
