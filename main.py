def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SAD)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_uart_data_received():
    global uartCmd
    uartCmd = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    if uartCmd == "f":
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 84)
    elif uartCmd == "s":
        maqueen.motor_stop(maqueen.Motors.ALL)
    elif uartCmd == "b":
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 84)
    elif uartCmd == "r":
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 84)
    elif uartCmd == "l":
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 84)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

uartCmd = ""
bluetooth.start_uart_service()
basic.show_string("Uart On")
basic.show_icon(IconNames.HEART)