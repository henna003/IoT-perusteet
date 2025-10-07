# IoT Perusteet
Tässä on koottuna IoT-perusteet kurssilla tehtyjä asioita. Harjoitukset on tehty Wokwi-simulaattorilla käyttäen Raspberry Pi Pico:n Micropython Pico W:tä. Arvot on kerätty DHT22-anturin avulla ja data on lähetetty ThingSpeakin API:n kautta pilveen.

## Luento 1
- Blink the led
  - Kun painetaan nappia, led-valo syttyy. Muuten led-valo on sammunut.
- Interrupt
  - Valo syttyy kun pico laitetaan päälle, satunnaisen ajan kuluttua valo            sammuu. Jonka jälkeen käyttäjä reagoi mahdollisimman nopeasti nappia             painamalla ja näkee kuinka kauan oli reagointiaika millisekunneissa.
- Traffic lights
  - Liikennevalot, eli punainen, keltainen ja vihreä led-valo syttyvät               vuorotellen. Kun painetaan nappia, vihreä valo pysyy päällä niin kauan           kun nappi on pohjassa.
- Weather Station
  - DHT22-anturin avulla mitataan lämpötilaa.

## Luento2
- Lcd-näyttö
    - Lcd-näytölle ilmestyy sille syötetty teksti.
- Weather Station with backend
    - Tehty Wi-fillä toimiva IoT-järjestelmä, joka mittaa lämpötilaa DHT22-            anturin avulla ja lähettää datan ThingSpeakin API:n kautta pilveen.

## Luento3
- server.js
    - Tehty RESTful API -palvelin Node.js:llä käyttäen Express.js-kirjastoa ja         SQLite-tietokantaa.

## Luento4
- Webhook
    - Toteutettu Discordiin, jossa webhook vastaanottaa viestejä. Viesti               lähetetään Postmanin kautta tekemällä HTTP POST -pyyntö webhook-URL:iin.
- Websocket
    - Toteutettu HTML-sivun kautta, jossa on WebSocket-yhteys palvelimeen.             Käyttäjä voi lähettää viestin HTML-sivulla olevaan tekstikenttään. Viesti        lähetetään WebSocketin kautta palvelimelle ja palautuu takaisin samalle          sivulle.
- Fetch
    - Tehty html-tiedosto, jonka kautta saadaan näkyviin Thingspeak Api:ssa            olevat arvot, jotka on aikaisemmin mitattu DHT22-anturin avulla ja               lähetetty data ThingSpeakin API:n kautta pilveen.
- GoogleChart
    - Aikaisemmin tehty IoT-järjestelmä, joka mittaa lämpötilaa ja                     ilmankosteutta DHT22-anturin avulla ja lähettää datan ThingSpeakin               API:n kautta pilveen. Pilvessä olevat arvot haetaan Google Charts                pohjaiseen verkkosovellukseen, joka piirtää reaaliaikaisen graafin               lämpötilalle ja ilmankosteudelle.
- Weather Station with LCD
    - Toteutettu IoT-järjestelmä, joka mittaa lämpötilaa ja ilmankosteutta             DHT22-anturin avulla ja lähettää kerätyt arvot pilvipalveluun ThingSpeak         API:n kautta. Järjestelmä on toteutettu Wokwi-simulaattorissa ja                 siihen on liitetty myös I²C LCD-näyttö, joka näyttää                             reaaliaikaiset mittausarvot.


