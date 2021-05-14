def temperature_converter(temp, unit, unit1):
    if unit == "Celsius" and unit1 == "Fahrenheit":
        conv_ans = temp * 1.8 + 32
        return conv_ans
    elif unit == "Fahrenheit" and unit1 == "Celsius":
        conv_ans = (temp-32) / 1.8
        return conv_ans
    elif unit == "Celsius" and unit1 == "Celsius":
        return temp
    elif unit == "Fahrenheit" and unit1 == "Fahrenheit":
        return temp
    else:
        pass
