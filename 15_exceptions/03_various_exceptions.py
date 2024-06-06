try:
    print("Jetzt passiert schlimme Dinge")
    a=3/0
    foo="Klaus"+3
    f=open("sdföl")
except ValueError:
    print("Es gab einen ValueError")
except (TypeError, ZeroDivisionError):
    print("Es gab einen TE oder eien ZDE")
except:
    print("Es gab einen anderen Fehler")