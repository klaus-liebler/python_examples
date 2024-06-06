import logging
logging.basicConfig(
    filename="log.txt",
    filemode="w", 
    level=logging.WARNING, 
    encoding="UTF-8",
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug("Debug für Details, die man nur braucht, wenn das Programm nicht funktioniert")
logging.info("Info für Details, die man in besonderen Betriebsphasen benötigt")
logging.warning("Warn, wenn das System zwar weiterlaufen kann, aber ein Nutzereingriff notwendig ist")
logging.error("Error, wenn das System nicht weiterlaufen kann")