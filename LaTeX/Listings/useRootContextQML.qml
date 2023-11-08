/*
.
.
.
*/
ComboBox{
    // a = front, b = back
    id: setAB
    model: ["a","b"]
    //load actual storage values if 
    //storage location is changed and not empty
    onCurrentValueChanged: {
        if(setLocation.currentValue !==''){
            iC.loadStorage(
                setLocation.currentValue, 
                setAB.currentValue
                )
        }
    }
    Layout.fillHeight: true
    Layout.fillWidth: true
}
/*
.
.
.
*/