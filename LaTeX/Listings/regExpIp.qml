TextField{
    id: readerIpAdressField
    text: "0.0.0.0"
    width: parent.width - 120
    height:  30
    validator: RegularExpressionValidator {
        regularExpression: /^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$/
        // / ^ means string must start at the beginning
        // {1,3} means 1 to 3 digits
        // \ . means a dot, [0-9] means a digit
        // so /^(?:[0-9]{1,3}\.){3} means 1 to 3 digits 
        // followed by a dot, repeated 3 times
        // followed by 1 to 3 digits
    }
    onEditingFinished: {
        saveButton.enabled = true
    }
    enabled: !locked
    Component.onCompleted: {
        readerIpAdressField.text = readerIpAdress
    }
}