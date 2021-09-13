bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    basic.showIcon(IconNames.Happy)
})
bluetooth.onBluetoothDisconnected(function on_bluetooth_disconnected() {
    basic.showIcon(IconNames.Sad)
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function on_uart_data_received() {
    
    uartCmd = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    if (uartCmd == "f") {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 84)
    } else if (uartCmd == "s") {
        maqueen.motorStop(maqueen.Motors.All)
    } else if (uartCmd == "b") {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 84)
    } else if (uartCmd == "r") {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 84)
    } else if (uartCmd == "l") {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 84)
    }
    
})
let uartCmd = ""
bluetooth.startUartService()
basic.showString("Uart On")
basic.showIcon(IconNames.Heart)
