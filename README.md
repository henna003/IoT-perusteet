# IoT Perusteet
Tässä on koottuna IoT-perusteet kurssilla tehtyjä asioita. Harjoitukset on tehty wokwi-simulaattoorilla käyttäen Raspberry Pi Pico:n Micropython Pico W:tä. Kerätyt arvot on kerätty DHT22-anturin avulla ja data on lähetetty ThingSpeakin API:n kautta pilveen.

## Luento 1
- Blink the led
- Interrupt
- Traffic lights
- Weather Station

## Luento2
- Lcd näyttö
- Weather Station with backend
    - Tehty Wi-fillä toimiva IoT-järjestelmä, joka mittaa lämpötilaa DHT22-anturin avulla ja lähettää datan ThingSpeakin API:n kautta pilveen.

## Luento3
- server.js
    - Tehty RESTful API -palvelin Node.js:llä käyttäen Express.js-kirjastoa ja SQLite-tietokantaa.

## Luento4
- Webhook
    - Lähettää discordiin viestin, joka lähetetään postmanin kautta.
- Websocket
    - Tehty html-tiedosto, jonka kautta saadaan lähetettyä viesti, joka tulee takaisin.
- Fetch
    - Tehty html-tiedosto, jonka kautta saadaan näkyviin Thingspeak Api:ssa olevat arvot, jotka on aikaisemmin mitattu DHT22-anturin avulla ja lähetetty data ThingSpeakin API:n             kautta pilveen.
- GoogleChart
    - Aikaisemmin tehty IoT-järjestelmä, joka mittaa lämpötilaa ja ilmankosteutta DHT22-anturin avulla ja lähettää datan ThingSpeakin API:n kautta pilveen. Pilvessä olevat arvot            haetaan Google Charts pohjaiseen verkkosovellukseen, joka piirtää reaaliaikaisen graafin lämpötilalle ja kosteudelle.
- Weather Station with LCD
    - Toteutettu IoT-järjestelmä, joka mittaa lämpötilaa ja ilmankosteutta DHT22-anturin avulla ja lähettää kerätyt arvot pilvipalveluun ThingSpeak API:n kautta.                            Järjestelmä on toteutettu Wokwi-simulaattorissa ja siihen on liitetty myös I²C LCD-näyttö, joka näyttää reaaliaikaiset mittausarvot.


