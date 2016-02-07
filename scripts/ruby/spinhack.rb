
# Simple spin hack script written for Osu! back when I was bad at spinners and wanted to test the limits.
require 'Win32API' # Require the Win32API so we can alter the mouse pointer.

# 	Oh no! You are using global variables! Hold your horses. The reason we do this is because we're running
# 	a simple script where we don't have to pay attention to our variable scope. Sure, we could have wrapped this
# 	all in a neat little class and felt really good about ourselves but that would just clutter further code
# 	and make it less nice to read in the end. Why would you want multiple instances of this script anyway?
# 	With that said, calm down and just run the damn thing. No need in getting upset. It's all good.

# These values need to be modified to work with your given setup.
$screen_width = 1920
$screen_height = 1080 # Screen size settings.
$spin_radius = 250 # Distance to the center of the screen.
$spin_direction = -1 # Sets the spin direction.
$spin_key = 65 # The keycode used to activate the script.
$showKeycodes = false # Optionally show pressed keycodes.

# These values are handled by the script and should not be edited.
$frames_elapsed = 0 # Stores spin time required by the calculation.
$spin_active = false # Enables the spin movement depending on the given boolean state.

# Create handles for the given system functions.
set_cursor_pos = Win32API.new('user32', 'SetCursorPos', %w(I I), 'V')
key_press = Win32API.new('user32', 'GetAsyncKeyState', ['i'], 'i')

def handle_press(keycode)
  if keycode == $spin_key
    if $spin_active == true
      puts "Spinning disabled\n"
      $spin_active = false

    else
      puts "Spinning enabled\n"
      $spin_active = true
    end
  end
end

loop do # Main program loop.
  # Catch numbers.
  (0x30..0x39).each do |keycode|
    next unless key_press.call(keycode) & 0x01 == 1
    if $showKeycodes
      puts keycode # Show the keycodes for numbers.
    end

    handle_press(keycode)
  end

  # Catch letters.
  (0x41..0x5A).each do |keycode|
    next unless key_press.call(keycode) & 0x01 == 1
    if $showKeycodes
      puts keycode # Show the keycodes for characters.
    end

    handle_press(keycode)
  end

  # If the spin is active calculate the cursor position.
  if $spin_active == true
    $frames_elapsed += 1
    set_cursor_pos.Call(
      ($screen_width / 2) + (Math.cos($frames_elapsed * $spin_direction) * $spin_radius),
      ($screen_height / 2) + (Math.sin($frames_elapsed * $spin_direction) * $spin_radius)
    )
  end

  # Sleep for a moment so that we don't lock anything up.
  sleep(0.01)
end
