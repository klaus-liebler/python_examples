import locale
locale.setlocale(locale.LC_ALL, "")
name = "A1"
value = 14543.656
value_string = locale.format_string("%12.2f", value)
print(f"Der Messwert {name} liegt bei {value_string}.")