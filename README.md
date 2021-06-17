# SABIO_backend
SABIO webapp code for sharing between server and local machine



## Process

### NMvW Data:

 - have full dumps of tables *whose rows do not need to match w. Objects*:
   - Classifications 
   - TextTypes 
   - ThesXrefTypes
   - ClassificationNotations
   - TermTypes 
   - ThesXrefs 
   - ObjTitles 
   - TextEntries 
   - Terms 
   - TitleTypes
 - other tables


# TODO 

 - configure:
   - Nginx
   - Gunicorn
   - iptables
   - CORS
   - HTTPS & certbot



# Frontend

### Questions: 

 - could we make dataset IDs and engine IDs integers (currently strings, sometimes integers)? 
   they'll always be integer in my back-end (indices or hash values, haven't fully decided yet, 
   but either way ints), so that could save me some casting/checking
 - could we split the /search endpoint into /search and /score?
 - what if the description of an object is very long? 
   what if it doesn't exist (empty value)? same question for the object's name (=title)


    
