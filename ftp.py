from ftplib import FTP, error_perm

# Eingabe des FTP-Servers und Passworts
ftp_server = input("FTP Server: ")
username = input("Benutzername: ")
password = input("Passwort: ")

try:
    # Verbindung zum FTP-Server herstellen
    ftp = FTP(ftp_server)
    ftp.login(user=username, passwd=password)
    
    # Verzeichnisinhalt anzeigen
    print("Verzeichnisinhalt:")
    ftp.retrlines('LIST')

except error_perm as e:
    print(f"FTP-Fehler: {e}")
except Exception as e:
    print(f"Fehler: {e}")
finally:
    # Verbindung beenden
    if 'ftp' in locals():
        ftp.quit()
