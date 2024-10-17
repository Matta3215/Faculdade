def celsius_para_fahrenheit(tc):
    tf = ((9 * tc) / 5) + 32
    return tf

def fahrenheit_para_celsius(tf):
    tc = ((tf - 32) * 5) / 9
    return tc


temperatura = input("Digite celsius para converter de °C para °F ou fahrentheit para converter de °F para °C: ").lower()


if (temperatura == "celsius"):
    tc = int(input("Digite a temperatura em °C: "))
    
    print(f"{tc}°C é igual a {celsius_para_fahrenheit(tc):.2f}°F")

elif (temperatura == "fahrenheit"):
    tf = int(input("Digite a temperatura em °F: "))
    
    print(f"{tf}°F é igual a {fahrenheit_para_celsius(tf):.2f}°C")
