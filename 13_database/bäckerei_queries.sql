SELECT P.name, P.preis_ct, LI.menge, F.ort 
FROM produktstammdaten P
JOIN lagerbestand_ist LI ON LI.produkt_id=P.id
JOIN filialstammdaten F ON LI.filiale_id = F.id
WHERE F.ort="New York" and LI.menge>0