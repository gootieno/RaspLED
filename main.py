from rpi_ws281x import PixelStrip, Color
import time

# LED strip configuration:
LED_COUNT = 60        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800kHz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0

# Create PixelStrip object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Initialize the library (must be called once before other functions).
strip.begin()

def color_wipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

try:
    while True:
        # Red wipe
        color_wipe(strip, Color(255, 0, 0))
        time.sleep(1)
        # Green wipe
        color_wipe(strip, Color(0, 255, 0))
        time.sleep(1)
        # Blue wipe
        color_wipe(strip, Color(0, 0, 255))
        time.sleep(1)
        # Clear wipe (turn off)
        color_wipe(strip, Color(0, 0, 0))
        time.sleep(1)

except KeyboardInterrupt:
    color_wipe(strip, Color(0, 0, 0))
