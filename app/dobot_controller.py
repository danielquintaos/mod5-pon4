from pydobot import Dobot
import serial.tools.list_ports
import time

def get_dobot_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if 'Dobot' in port.description:
            return port.device
    return None

def is_dobot_connected():
    port = get_dobot_port()
    return port is not None

#def is_dobot_connected():
    """Mock the Dobot connection status for testing."""
    return True

def send_command_to_dobot(command):
    port = get_dobot_port()
    if port is None:
        print("Dobot not connected.")
        return False

    device = Dobot(port=port)
    try:
        if command.startswith("move"):
            # Expected command format: "move,x,y,z,r"
            _, x, y, z, r = command.split(',')
            device.move_to(float(x), float(y), float(z), float(r), wait=True)
        elif command == "home":
            device.go_home()
        elif command.startswith("gripper"):
            # Expected command format: "gripper,on" or "gripper,off"
            _, state = command.split(',')
            if state == "on":
                device.grip(True)
            elif state == "off":
                device.grip(False)
        elif command.startswith("speed"):
            # Expected command format: "speed,velocity,acceleration"
            _, velocity, acceleration = command.split(',')
            device.set_speed(float(velocity), float(acceleration))
        else:
            print(f"Unknown command: {command}")
            return False
        print(f"Executed command: {command}")
    finally:
        device.close()

    return True
