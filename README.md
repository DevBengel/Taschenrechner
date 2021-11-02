# Taschenrechner-App
(ohne Zusätze läuft diese nach Start unter http://localhost:5000)

Normales Aufrufen der Website gibt "Hello World" aus.

Zur Addition (Link + /add) muss via HTTP POST eine JSON-Datei der Form ```{"zahleins":5,"zahlzwei":8}``` übergeben werden - z.B. über POSTMAN API.

Der Statusaufruf (Link + /status) gibt die eigene IP-Adresse aus.

## Beschreibung der Pipeline:
1.  __Build__: Docker-Image „taschenrechner“ wird aus Dockerfile generiert. Es enthält Python, Requirements und die Taschenrechner-App, diese wird über main.py gestartet.
2.  __Static Code__:
    *   Run_unittest: Es wird ein Taschenrechner-Container gestartet und in diesem Tests zur Funktion der Software durchgeführt -> ob hello world ausgegeben wird, ob die Addition funktioniert, ob die Ausgabe der IP-Adresse über Status stimmt. Der Container wird anschließend geschlossen.
    *   Run_style: Es wird ein Style-Container gestartet, der nur Python & die Requirements enthält. Die main.py wird in den Unterordner /code kopiert und dort auf Stilchecks bzgl. Python untersucht. Anschließend wird der Container geschlossen. Hier werden auch Artifacts ausgegeben.
3.  __Prepare Systemtest__: 
    *   Prep-lb: Es wird sich in einer privaten Docker Registry angemeldet und dort ein Image unter dem Namen „registry-cido.experteach.demo:1234/root/application/lb“ hochgeladen: das Image enthält einen NGinx-Webserver mit zugehörigem Configfile. Es handelt sich um einen Loadbalancer.
    *   Prep-app: Gleiches Spiel wie vorher nur diesmal wird das Image mit der TR-App als „registry-cido.experteach.demo:1234/root/application/app“ hochgeladen.
4.  __System_test__: Es wird ein Docker-Netzwerk aus 3 Containern gestartet -> unter 172.20.20.10 wird der Loadbalancer gestartet, unter 172.20.20.101 und .102 wird jeweils die TR-App gestartet. Anschließend wird getestet, ob die Hello-World-, Additions- & Status-Funktion auch über den Loadbalancer klappen. Anschließend werden alle Container wieder gestoppt.
5.  __Deploy__: 
    * es wird ein Namespace mit Namen „apptaschen“ angelegt 
    * Secret wird zum Login auf die Registry hinterlegt
    * Service wird konfiguriert
    * Deployment mit 2 TR-Apps, Container wird vom privaten Registry geladen
    * Deployment der Running Config von Kubernetes wird mit aktuellem Datum versehen, damit Kubernetes die aktuellen Image-Änderungen auch übernimmt und neu deployed.
