from pasco import CodeNodeDevice, Icons

# Create an object for the //code.Node
code_node_device = CodeNodeDevice()
code_node_device.connect_by_id('380-931')  # Replace '481-782' with your device's ID

# Check the temperature continuously
while True:
    # Read the temperature from the //code.Node sensor
    temp_value = code_node_device.read_data('Temperature')
    code_node_device.set_sound_frequency(440)  # Adjust the frequency value as desired

    # If temperature is over 85 F or under 60 F, sound an alarm and show a sad face on the LED screen
    if temp_value > 29.5 or temp_value < 15.6:
        # Set a louder speaker frequency for the alarm sound
        code_node_device.set_sound_frequency(440)  # Adjust the frequency value as desired

        # Show a sad face on the LED screen
        code_node_device.show_image_in_array(Icons().sad)
        
        print(f"Alarm! Temperature is {temp_value} F")
    else:
        # If the temperature is within the normal range, turn off the alarm and display a happy face
        code_node_device.set_sound_frequency(0)
        code_node_device.show_image_in_array(Icons().smile)

        print(f"Temperature is OK: {temp_value} F")
