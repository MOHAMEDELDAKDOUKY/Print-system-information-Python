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
    

    
    
# you need the module dbus-python
def get_graphic_card_properties():
    import dbus
    bus = dbus.SystemBus()
    hal_manager_object = bus.get_object('org.freedesktop.Hal', '/org/freedesktop/Hal/Manager')
    prop = 'pci.device_class'
    for device in hal_manager_object.get_dbus_method('GetAllDevices', 'org.freedesktop.Hal.Manager')():
        dev = bus.get_object('org.freedesktop.Hal', device)
        interface = dbus.Interface(dev, dbus_interface='org.freedesktop.Hal.Device')
        if interface.PropertyExists(prop):
            if interface.GetProperty(prop) == 3:
                # we return the properties of the first device in the list
                # with a pci.device_class == 3 (should check if several such devs...
                return interface.GetAllProperties()
dic = get_graphic_card_properties()
for key, value in dic.iteritems():
    print("%s : %s" %(key, value))
