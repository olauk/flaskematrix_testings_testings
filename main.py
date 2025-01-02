colorbit_51bit = colorbit.init_color_bit(DigitalPin.P0, BitColorMode.RGB)
colorbit_51bit.set_brightness(255)

def on_forever():
    colorbit_51bit.show_scroll_string_color("God Jul", colorbit.colors(BitColors.RED))
    colorbit_51bit.show_color_icon(ColorIcon.CHRISTMAS_TREE, colorbit.colors(BitColors.GREEN))
    basic.pause(1000)
    colorbit_51bit.show_scroll_string_color("Ho ho ho", colorbit.colors(BitColors.BLUE))
    basic.pause(1000)
    colorbit_51bit.show_scroll_string_color("Vitensenteret", colorbit.colors(BitColors.GREEN))
    basic.pause(1000)
basic.forever(on_forever)
