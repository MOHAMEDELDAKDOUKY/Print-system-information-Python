import wmi
lspci -v -s `lspci | awk '/VGA/{print $1}'`
computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

print('OS Name: {0}'.format(os_name))
print('OS Version: {0}'.format(os_version))
print('CPU: {0}'.format(proc_info.Name))
print('RAM: {0} GB'.format(system_ram))
for i in range (len(computer.Win32_VideoController())):
    print('Graphics Card %d : {}'.format(gpu_info[i].Name) %(i))
    
