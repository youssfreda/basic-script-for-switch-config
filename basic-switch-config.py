from netmiko import ConnectHandler

# Define the device details
cisco_switch = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',  # Replace with the IP address of your switch
    'username': 'admin',    # Replace with your username
    'password': 'password', # Replace with your password
    'secret': 'secret',     # Replace with your enable secret
    'port': 22,             # Optional, default is 22
    'verbose': True,        # Optional, for detailed logs
}

# Configuration commands
config_commands = [
    'hostname Switch2850',
    'interface FastEthernet0/1',
    'switchport mode access',
    'switchport access vlan 10',
    'no shutdown',
    'exit',
    'interface FastEthernet0/2',
    'switchport mode trunk',
    'switchport trunk allowed vlan 10,20,30',
    'no shutdown',
    'exit',
    'vlan 10',
    'name Sales',
    'exit',
    'vlan 20',
    'name Engineering',
    'exit',
    'vlan 30',
    'name HR',
    'exit',
    'ip default-gateway 192.168.1.254',
    'line vty 0 4',
    'password vtypassword',
    'login',
    'exit',
]

def configure_switch():
    # Connect to the device
    net_connect = ConnectHandler(**cisco_switch)
    
    # Enter enable mode
    net_connect.enable()

    # Send configuration commands
    output = net_connect.send_config_set(config_commands)
    print(output)

    # Save configuration
    output = net_connect.save_config()
    print(output)

    # Disconnect from the device
    net_connect.disconnect()

if __name__ == '__main__':
    configure_switch()
