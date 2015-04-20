# cifu-archive
Python script to make a local mirror of Cifu's jazz radio shows.

### Introduction
The majority of Juan Claudio Cifuentes' body of work in advocating for Jazz in Spain is currently available in RTVE's Alacarta streaming service. All rights remain reserved to RTVE:

* http://www.rtve.es/alacarta/audios/jazz-porque-si/
* http://www.rtve.es/alacarta/audios/a-todo-jazz/

Should Alacarta ever stop offering such podcasts, this script ensures that his work is persisted and freely available for all Jazz lovers, forever. It will need around 150GB of available disk space.

It will synthesise filenames using a combination of radio show name, date (when available) and title (preserving UTF-8 character encoding). The script will by default spawn 8 worker threads to download shows in parallel.

### File list
* atj-2008-08-28-A todo jazz - 280808.mp3
* atj-2008-09-06-Primera hora - 060908.mp3
* atj-2008-09-06-Segunda hora - 060908.mp3
* atj-2008-09-13-Primera hora - 130908.mp3
* atj-2008-09-13-Segunda hora - 130908.mp3
* atj-2008-09-20-Primera hora - 200908.mp3
* atj-2008-09-20-Segunda hora - 200908.mp3
* atj-2008-09-27-Primera hora - 270908.mp3
* atj-2008-10-04-Primera hora - 041008.mp3
* atj-2008-10-04-Segunda hora - 041008.mp3
* atj-2008-10-11-Primera hora - 111008.mp3
* atj-2008-10-11-Segunda hora - 111008.mp3
* atj-2008-10-18-Primera hora - 181008.mp3
* atj-2008-10-18-Segunda hora - 181008.mp3
* atj-2008-10-25-Primera hora - 251008.mp3
* atj-2008-10-25-Segunda hora - 251008.mp3
* atj-2008-11-08-Primera hora - 081108.mp3
* atj-2008-11-15-Primera hora - 151108.mp3
* atj-2008-11-15-Segunda hora - 151108.mp3
* atj-2008-11-22-A todo jazz - 221108.mp3
* atj-2008-11-29-Primera hora - 291108.mp3
* atj-2008-11-29-Segunda hora - 291108.mp3
* atj-2008-12-06-Primera hora - 061208.mp3
* atj-2008-12-06-Segunda hora - 061208.mp3
* atj-2008-12-13-A todo jazz - 131208.mp3
* atj-2008-12-19-A todo jazz - 201208.mp3
* atj-2008-12-27-A todo jazz - 271208.mp3
* atj-2009-01-02-A todo jazz - 030109.mp3
* atj-2009-01-10-A todo jazz - 100109.mp3
* atj-2009-01-11-A todo jazz - 110109.mp3
* atj-2009-01-17-A todo jazz - 170109.mp3
* atj-2009-01-18-A todo jazz - 180109.mp3
* atj-2009-01-24-A todo jazz - 240109.mp3
* atj-2009-01-25-A todo jazz - 250109.mp3
* atj-2009-01-31-A todo jazz - 310109.mp3
* atj-2009-02-01-A todo jazz - 010209.mp3
* atj-2009-02-07-A todo jazz - 070209.mp3
* atj-2009-02-08-A todo jazz - 080209.mp3
* atj-2009-02-14-A todo jazz - 140209.mp3
* atj-2009-02-15-A todo jazz - 150209.mp3
* atj-2009-02-21-A todo jazz - 210209.mp3
* atj-2009-02-22-A todo jazz - 220209.mp3
* atj-2009-02-28-A todo jazz - 280209.mp3
* atj-2009-03-01-A todo jazz - 010309.mp3
* atj-2009-03-07-A todo jazz - 070309.mp3
* atj-2009-03-08-A todo jazz - 080309.mp3
* atj-2009-03-14-A todo jazz - 140309.mp3
* atj-2009-03-15-A todo jazz - 150309.mp3
* atj-2009-03-21-A todo jazz - 210309.mp3
* atj-2009-03-22-A todo jazz - 220309.mp3
* atj-2009-03-28-A todo jazz - 280309.mp3
* atj-2009-03-29-A todo jazz - 290309.mp3
* atj-2009-04-06-A todo jazz - 040509.mp3
* atj-2009-04-11-A todo jazz - 110409.mp3
* atj-2009-04-12-A todo jazz - 120409.mp3
* atj-2009-04-18-A todo jazz - 180409.mp3
* atj-2009-04-19-A todo jazz - 190409.mp3
* atj-2009-04-25-A todo jazz - 250409.mp3
* atj-2009-04-26-A todo jazz - 260409.mp3
* atj-2009-05-02-A todo jazz - 020509.mp3
* atj-2009-05-03-A todo jazz - 030509.mp3
* atj-2009-05-09-A todo jazz - 090509.mp3
* atj-2009-05-10-A todo jazz - 100509.mp3
* atj-2009-05-16-A todo jazz - 160509.mp3
* atj-2009-05-17-A todo jazz - 170509.mp3
* atj-2009-05-23-A todo jazz - 230509.mp3
* atj-2009-05-24-A todo jazz - 240509.mp3
* atj-2009-05-30-A todo jazz - 300509.mp3
* atj-2009-05-31-A todo jazz - 310509.mp3
* atj-2009-06-06-A todo jazz - 060609.mp3
* atj-2009-06-07-A todo jazz - 070609.mp3
* atj-2009-06-13-A todo jazz - 130609.mp3
* atj-2009-06-14-A todo jazz - 140609.mp3
* atj-2009-06-20-A todo jazz - 200609.mp3
* atj-2009-06-27-A todo jazz - 270609.mp3
* atj-2009-06-28-A todo jazz - 280609.mp3
* atj-2009-07-04-A todo jazz - 040709.mp3
* atj-2009-07-05-A todo jazz - 050709.mp3
* atj-2009-07-11-A todo jazz - 110709.mp3
* atj-2009-07-12-A todo jazz - 120709.mp3
* atj-2009-07-18-A todo jazz - 180709.mp3
* atj-2009-07-19-A todo jazz - 190709.mp3
* atj-2009-07-25-A todo jazz - 250709.mp3
* atj-2009-07-26-A todo jazz - 260709.mp3
* atj-2009-08-01-A todo jazz - 010809.mp3
* atj-2009-08-02-A todo jazz - 020809.mp3
* atj-2009-08-15-A todo jazz - 150809.mp3
* atj-2009-08-16-A todo jazz - 160809.mp3
* atj-2009-08-22-A todo jazz - 220809.mp3
* atj-2009-08-23-A todo jazz - 230809.mp3
* atj-2009-08-29-A todo jazz - 290809.mp3
* atj-2009-08-30-A todo jazz - 300809.mp3
* atj-2009-09-05-A todo jazz - 050909.mp3
* atj-2009-09-06-A todo jazz - 060909.mp3
* atj-2009-09-12-A todo jazz - 120909.mp3
* atj-2009-09-13-A todo jazz - 130909.mp3
* atj-2009-09-19-A todo jazz - 190909.mp3
* atj-2009-09-20-A todo jazz - 200909.mp3
* atj-2009-09-26-A todo jazz - 260909.mp3
* atj-2009-09-27-A todo jazz - 270909.mp3
* atj-2009-10-03-A todo jazz - 031009.mp3
* atj-2009-10-04-A todo jazz - 041009.mp3
* atj-2009-10-10-A todo jazz - 101009.mp3
* atj-2009-10-11-A todo jazz - 111009.mp3
* atj-2009-10-17-A todo jazz - 171009.mp3
* atj-2009-10-18-A todo jazz - 181009.mp3
* atj-2009-10-24-A todo jazz - 241009.mp3
* atj-2009-10-25-A todo jazz - 251009.mp3
* atj-2009-10-31-A todo jazz - 311009.mp3
* atj-2009-11-01-A todo jazz - 011109.mp3
* atj-2009-11-07-A todo jazz - 071109.mp3
* atj-2009-11-08-A todo jazz - 081109.mp3
* atj-2009-11-14-A todo jazz - 141109.mp3
* atj-2009-11-15-A todo jazz - 151109.mp3
* atj-2009-11-21-A todo jazz - 211109.mp3
* atj-2009-11-22-A todo jazz - 221109.mp3
* atj-2009-11-28-A todo jazz - 281109.mp3
* atj-2009-11-29-A todo jazz - 291109.mp3
* atj-2009-12-05-A todo jazz - 051209.mp3
* atj-2009-12-06-A todo jazz - 061209.mp3
* atj-2009-12-12-A todo jazz - 121209.mp3
* atj-2009-12-13-A todo jazz - 131209.mp3
* atj-2009-12-19-A todo jazz - 191209.mp3
* atj-2009-12-20-A todo jazz - 201209.mp3
* atj-2009-12-26-A todo jazz - 261209.mp3
* atj-2009-12-27-A todo jazz - 271209.mp3
* atj-2010-01-02-A todo jazz - 020110.mp3
* atj-2010-01-03-A todo jazz - 030110.mp3
* atj-2010-01-09-A todo jazz - 090110.mp3
* atj-2010-01-10-A todo jazz - 100110.mp3
* atj-2010-01-16-A todo jazz - 160110.mp3
* atj-2010-01-17-A todo jazz - 170110.mp3
* atj-2010-01-23-A todo jazz - 230110.mp3
* atj-2010-01-24-A todo jazz - 240110.mp3
* atj-2010-01-30-A todo jazz - 300110.mp3
* atj-2010-01-31-A todo jazz - 310110.mp3
* atj-2010-02-06-A todo jazz - 060210.mp3
* atj-2010-02-07-A todo jazz - 070210.mp3
* atj-2010-02-13-A todo jazz - 130210.mp3
* atj-2010-02-14-A todo jazz - 140210.mp3
* atj-2010-02-20-A todo jazz - 200210.mp3
* atj-2010-02-21-A todo jazz - 210210.mp3
* atj-2010-02-27-A todo jazz - 270210.mp3
* atj-2010-02-28-A todo jazz - 280210.mp3
* atj-2010-03-06-A todo jazz - 060310.mp3
* atj-2010-03-07-A todo jazz - 070310.mp3
* atj-2010-03-13-A todo jazz - 130310.mp3
* atj-2010-03-20-A todo jazz - 200310.mp3
* atj-2010-03-21-A todo jazz - 210310.mp3
* atj-2010-03-27-A todo jazz - 270310.mp3
* atj-2010-03-28-A todo jazz - 280310.mp3
* atj-2010-04-03-A todo jazz - 030410.mp3
* atj-2010-04-04-A todo jazz - 040410.mp3
* atj-2010-04-10-A todo jazz - 100410.mp3
* atj-2010-04-11-A todo jazz - 110410.mp3
* atj-2010-04-17-A todo jazz - 170410.mp3
* atj-2010-04-18-A todo jazz - 180410.mp3
* atj-2010-04-24-A todo jazz - 240410.mp3
* atj-2010-04-25-A todo jazz - 250410.mp3
* atj-2010-05-01-A todo jazz - 010510.mp3
* atj-2010-05-02-A todo jazz - 020510.mp3
* atj-2010-05-08-A todo jazz - 080510.mp3
* atj-2010-05-09-A todo jazz - 090510.mp3
* atj-2010-05-16-A todo jazz - 160510.mp3
* atj-2010-05-22-A todo jazz - 220510.mp3
* atj-2010-05-23-A todo jazz - 230510.mp3
* atj-2010-05-29-A todo jazz - 290510.mp3
* atj-2010-05-30-A todo jazz - 300510.mp3
* atj-2010-06-05-A todo jazz - 050610.mp3
* atj-2010-06-06-A todo jazz - 060610.mp3
* atj-2010-06-12-A todo jazz - 120610.mp3
* atj-2010-06-13-A todo jazz - 130610.mp3
* atj-2010-06-19-A todo jazz - 190610.mp3
* atj-2010-06-26-A todo jazz - 260610.mp3
* atj-2010-06-27-A todo jazz - 270610.mp3
* atj-2010-07-03-A todo jazz - 030710.mp3
* atj-2010-07-04-A todo jazz - 040710.mp3
* atj-2010-07-10-A todo jazz - 100710.mp3
* atj-2010-07-11-A todo jazz - 110710.mp3
* atj-2010-07-17-A todo jazz - 170710.mp3
* atj-2010-07-18-A todo jazz - 180710.mp3
* atj-2010-07-24-A todo jazz - 240710.mp3
* atj-2010-07-25-A todo jazz - 250710.mp3
* atj-2010-07-31-A todo jazz - 310710.mp3
* atj-2010-08-01-A todo jazz - 010810.mp3
* atj-2010-08-07-A todo jazz - 070810.mp3
* atj-2010-08-08-A todo jazz - 080810.mp3
* atj-2010-08-14-A todo jazz - 140810.mp3
* atj-2010-08-15-A todo jazz - 150810.mp3
* atj-2010-08-21-A todo jazz - 210810.mp3
* atj-2010-08-22-A todo jazz - 220810.mp3
* atj-2010-08-28-A todo jazz - 280810.mp3
* atj-2010-08-29-A todo jazz - 290810.mp3
* atj-2010-09-04-A todo jazz - 040910.mp3
* atj-2010-09-05-A todo jazz - 050910.mp3
* atj-2010-09-11-A todo jazz - 110910.mp3
* atj-2010-09-12-A todo jazz - 120910.mp3
* atj-2010-09-18-A todo jazz - 190910.mp3
* atj-2010-09-19-A todo jazz - 190910.mp3
* atj-2010-09-25-A todo jazz - 250910.mp3
* atj-2010-09-26-A todo jazz - 260910.mp3
* atj-2010-10-02-A todo jazz - 021010.mp3
* atj-2010-10-03-A todo jazz - 031010.mp3
* atj-2010-10-09-A todo jazz - 091010.mp3
* atj-2010-10-10-A todo jazz - 101010.mp3
* atj-2010-10-16-A todo jazz - 161010.mp3
* atj-2010-10-17-A todo jazz - 171010.mp3
* atj-2010-10-23-A todo jazz - 231010.mp3
* atj-2010-10-24-A todo jazz - 241010.mp3
* atj-2010-10-30-A todo jazz - 301010.mp3
* atj-2010-10-31-A todo jazz - 311010.mp3
* atj-2010-11-06-A todo jazz - 061110.mp3
* atj-2010-11-07-A todo jazz - 071110.mp3
* atj-2010-11-13-A todo jazz - 131110.mp3
* atj-2010-11-14-A todo jazz - 141110.mp3
* atj-2010-11-20-A todo jazz - 201110.mp3
* atj-2010-11-21-A todo jazz - 211110.mp3
* atj-2010-11-27-A todo jazz - 271110.mp3
* atj-2010-11-28-A todo jazz - 281110.mp3
* atj-2010-12-04-A todo jazz - 041210.mp3
* atj-2010-12-05-A todo jazz - 051210.mp3
* atj-2010-12-11-A todo jazz - 111210.mp3
* atj-2010-12-12-A todo jazz - 121210.mp3
* atj-2010-12-18-A todo jazz - 181210.mp3
* atj-2010-12-19-A todo jazz - 191210.mp3
* atj-2010-12-25-A todo jazz - 251210.mp3
* atj-2010-12-26-A todo jazz - 261210.mp3
* atj-2011-01-01-A todo jazz - 010111.mp3
* atj-2011-01-02-A todo jazz - 020111.mp3
* atj-2011-01-08-A todo jazz - 080111.mp3
* atj-2011-01-09-A todo jazz - 090111.mp3
* atj-2011-01-15-A todo jazz - 150111.mp3
* atj-2011-01-16-A todo jazz - 160111.mp3
* atj-2011-01-22-A todo jazz - 220111.mp3
* atj-2011-01-23-A todo jazz - 230111.mp3
* atj-2011-01-29-A todo jazz - 290111.mp3
* atj-2011-01-30-A todo jazz - 300111.mp3
* atj-2011-02-05-A todo jazz - 050211.mp3
* atj-2011-02-06-A todo jazz - 060211.mp3
* atj-2011-02-12-A todo jazz - 120211.mp3
* atj-2011-02-13-A todo jazz - 130211.mp3
* atj-2011-02-19-A todo jazz - 190211.mp3
* atj-2011-02-20-A todo jazz - 200211.mp3
* atj-2011-02-26-A todo jazz - 260211.mp3
* atj-2011-02-27-A todo jazz - 270211.mp3
* atj-2011-03-05-Jazzmen - 050311.mp3
* atj-2011-03-06-Milestones.mp3
* atj-2011-03-12-A todo jazz - Charlie Parker: Bird Lives!! [1] - 120311.mp3
* atj-2011-03-13-A todo jazz - Charlie Parker: Bird Lives!! [2] - 130311.mp3
* atj-2011-03-19-Charles Lloyd. Una leyenda todavía.mp3
* atj-2011-03-26-Stan Kenton Orchestra.mp3
* atj-2011-03-27-Charles Lloyd (y 2).mp3
* atj-2011-04-02-Jazz desde Chile.mp3
* atj-2011-04-03-Sassy, The Divine.mp3
* atj-2011-04-09-Return To Forever cabalga de nuevo.mp3
* atj-2011-04-10-Encuentro de gigantes en Copenhague.mp3
* atj-2011-04-16-Max Roach, una actuación memorable.mp3
* atj-2011-04-17-Tres Big Bands, Tres....mp3
* atj-2011-04-23-Un concierto hasta hoy inédito.mp3
* atj-2011-04-24-Guitarristas de aquí y de allá.mp3
* atj-2011-04-30-Retornamos con "Return...".mp3
* atj-2011-05-01-Encuentro de gigantes (2):.mp3
* atj-2011-05-07-John Coltrane: My Favorite Things.mp3
* atj-2011-05-08-Recordando a Booker Little.mp3
* atj-2011-05-14-Encuentro de gigantes (3).mp3
* atj-2011-05-21-Charlie Parker y Miles Davis.mp3
* atj-2011-05-22-Bebop y Gigantes del Jazz.mp3
* atj-2011-05-28-Un saxo, una trompeta, un trombón.mp3
* atj-2011-05-29-Recordando a Red Rodney.mp3
* atj-2011-06-04-Gil Evans, un arreglista....mp3
* atj-2011-06-05-Gil Evans: "New Bottle, Old Wine".mp3
* atj-2011-06-12-Great Jazz Standards.mp3
* atj-2011-06-18-Saxo tenores. Ella y otros.mp3
* atj-2011-06-19-Disco recomendado: "Monk's Dream".mp3
* atj-2011-06-26-"Saxophone Colossus", histórico.mp3
* atj-2011-07-02-Woody Herman-1964 ¡Vaya banda!.mp3
* atj-2011-07-03-Stan Getz con cuerdas. "Focus".mp3
* atj-2011-07-09-Disco recomendado: "Criss Cross".mp3
* atj-2011-07-10-Lee Morgan "The Sidewinder".mp3
* atj-2011-07-16-El joven McCoy Tyner.mp3
* atj-2011-07-17-Una buena sesión. 'Prez And Teddy'.mp3
* atj-2011-07-23-Ellington, Piano In The Background.mp3
* atj-2011-07-24-Viaje a la Costa Oeste.mp3
* atj-2011-07-31-Joe Henderson.mp3
* atj-2011-08-06-Joe Henderson 2ª parte.mp3
* atj-2011-08-07-Baker y Pepper de nuevo.mp3
* atj-2011-08-13-Herbie Hancock "Maiden Voyage".mp3
* atj-2011-08-14-Lee Konitz en directo: 1959.mp3
* atj-2011-08-20-Big Bands y tríos.mp3
* atj-2011-08-21-Jazz piano tríos de aquí.mp3
* atj-2011-08-27-Cerrando el 'Sueño de Monk'.mp3
* atj-2011-08-28-The Modern Jazz Quartet.mp3
* atj-2011-09-03-Herbie Hancock. "Empyrean Isles".mp3
* atj-2011-09-04-El joven McCoy Tyner (2).mp3
* atj-2011-09-10-E = MC2 = Count Basie Orchestra.mp3
* atj-2011-09-11-Gil Evans - Jazz Standards [3].mp3
* atj-2011-09-17-Un "west coaster" emblemático.mp3
* atj-2011-09-18-Hubbard vs Morgan.mp3
* atj-2011-09-24-La Big Band de Duke Pearson.mp3
* atj-2011-09-25-La Big Band de Duke Pearson, 2.mp3
* atj-2011-10-01-The Modern Jazz Quartet: Primeros...mp3
* atj-2011-10-02-McCoy Tyner: "A la tercera...".mp3
* atj-2011-10-08-Shorty Rogers. "West Coast Jazz".mp3
* atj-2011-10-09-Freddie Hubbard y Lee Morgan.mp3
* atj-2011-10-15-Miles Davis &The Modern Jazz Giants.mp3
* atj-2011-10-16-"Out Of The Cool".mp3
* atj-2011-10-22-Seguimos repasando a Duke Pearson.mp3
* atj-2011-10-23-Un gran disco de 1959: "The Fox".mp3
* atj-2011-10-30-Bud Powell, "Live in Lausanne".mp3
* atj-2011-11-05-Shorty Rogers Big Bands.mp3
* atj-2011-11-06-Miles Davis con Thelonious Monk.mp3
* atj-2011-11-12-Duke Pearson, compositor magnífico.mp3
* atj-2011-11-13-Bud Powell - gira europea '62.mp3
* atj-2011-11-19-Cannonball Adderley.mp3
* atj-2011-11-26-A la Costa Oeste con Shorty Rogers.mp3
* atj-2011-11-27-"Money Jungle": disco irrepetible.mp3
* atj-2011-12-03-Miscelánea de jazz.mp3
* atj-2011-12-04-Solo trompetas, por favor....mp3
* atj-2011-12-10-Scott LaFaro-No hubo otro como él.mp3
* atj-2011-12-11-Scott LaFaro (2)-Una carrera demasi.mp3
* atj-2011-12-17-Scott LaFaro-El trío de Bill Evans.mp3
* atj-2011-12-18-Scott LaFaro. Cap. 4.mp3
* atj-2011-12-24-París 1958 (1).mp3
* atj-2011-12-25-París 1958 (2).mp3
* atj-2011-12-31-Art Blakey & The Jazz Messengers.mp3
* atj-2012-01-01-Charles Tolliver en vivo.mp3
* atj-2012-01-07-The Modern Jazz Quartet - "Fontessa.mp3
* atj-2012-01-08-Chick Corea: Sus discos como líder.mp3
* atj-2012-01-14-The Tough Tenors live at Minton's.mp3
* atj-2012-01-15-The Tough Tenors live at Minton's.mp3
* atj-2012-01-21-Getz y Corea, juntos otra vez.mp3
* atj-2012-01-22-Shorty Rogers 1957.mp3
* atj-2012-01-28-Montreux Summit (1ª parte).mp3
* atj-2012-01-29-Montreux Summit (2ª parte).mp3
* atj-2012-02-04-Duke Pearson :"Sweet Honey Bee".mp3
* atj-2012-02-05-Duke Pearson en 1967.mp3
* atj-2012-02-11-Pat Martino en directo (2000).mp3
* atj-2012-02-12-Clark Terry y su banda (1974).mp3
* atj-2012-02-18-Miles Davis en París - 1967 (1).mp3
* atj-2012-02-19-Miles Davis en París - 1967 (2).mp3
* atj-2012-02-25-Lee Morgan "The Rumproller" (1965).mp3
* atj-2012-02-26-John Coltrane "Africa Brass" (1961).mp3
* atj-2012-03-03-El legendario trío de Bill Evans.mp3
* atj-2012-03-04-Bill Evans Trío - Vanguard 1961 (2).mp3
* atj-2012-03-10-Bill Evans Trío - Vanguard 1961 (3).mp3
* atj-2012-03-11-Bill Evans Trío - Vanguard 1961 (4).mp3
* atj-2012-03-17-Louie Bellson's Big Band.mp3
* atj-2012-03-18-Joe Morello: "It's About Time".mp3
* atj-2012-03-24-Miscelánea de discos de jazz.mp3
* atj-2012-03-31-De Pepper Adams a Thelonious Monk.mp3
* atj-2012-04-01-Sonny Rollins: cuartetos con J.Hall.mp3
* atj-2012-04-07-Jazz misceláneo.mp3
* atj-2012-04-08-Los quintetos HendersonDorham.mp3
* atj-2012-04-14-Steve Lacy y la música de Monk (1).mp3
* atj-2012-04-15-Steve Lacy y la música de Monk (2).mp3
* atj-2012-04-21-En la variedad está el jazz....mp3
* atj-2012-04-22-John Coltrane - "Africa" (2).mp3
* atj-2012-04-28-Mingus, Mingus, Mingus.....mp3
* atj-2012-04-29-The Jackie Mac Attack.mp3
* atj-2012-05-05-Sonny Rollins & Jim Hall.mp3
* atj-2012-05-06-Joe Henderson llegó a Nueva York.mp3
* atj-2012-05-12-El tintero del jazz.mp3
* atj-2012-05-13-Seguimos con el "tintero del jazz".mp3
* atj-2012-05-19-Otro "Jazz en el tintero".mp3
* atj-2012-05-20-Seguimos con Scott LaFaro.mp3
* atj-2012-05-26-Mal Waldron en París.mp3
* atj-2012-05-27-Jam-session con Dizzy.mp3
* atj-2012-06-02-Jam-session en el Vanguard (2).mp3
* atj-2012-06-03-"Jazz en el tintero" (cont.).mp3
* atj-2012-06-09-Pat Metheny Trio de gira (1).mp3
* atj-2012-06-10-Pat Metheny Trío de gira (2).mp3
* atj-2012-06-16-Dave Holland Octet.mp3
* atj-2012-06-17-McCoy Tyner "Enlightenment".mp3
* atj-2012-06-23-Jazz en el tintero (cont.).mp3
* atj-2012-06-24-Jazz en el tintero (cont.).mp3
* atj-2012-06-30-El Príncipe del Jazz Francés.mp3
* atj-2012-07-01-Art Farmer Quintet at Boomers.mp3
* atj-2012-07-07-Dizzy Gillespie at Carnegie Hall.mp3
* atj-2012-07-08-Horace Silver Quintet.mp3
* atj-2012-07-14-Stan Getz "El Maestro".mp3
* atj-2012-07-15-Otra entrega del "Montreux Summit".mp3
* atj-2012-07-21-El incombustible Roy Haynes.mp3
* atj-2012-07-22-El Renacimiento de Blue Note (1).mp3
* atj-2012-07-28-El Renacimiento de Blue Note (2).mp3
* atj-2012-07-29-El Renacimiento de Blue Note (3).mp3
* atj-2012-08-04-Count Basie en Las Vegas.mp3
* atj-2012-08-05-Dizzy Gillespie en París-1960.mp3
* atj-2012-08-11-Joe HendersonKenny Dorham.mp3
* atj-2012-08-12-Un trío de superlujo.mp3
* atj-2012-08-18-Thelonious Monk & Johnny Griffin 1.mp3
* atj-2012-08-19-Cannonball Adderley Sextet (1).mp3
* atj-2012-08-25-Wynton Kelly Trío con Hank Mobley 1.mp3
* atj-2012-08-26-Wynton Kelly Trío con Hank Mobley 2.mp3
* atj-2012-09-01-Jim Hall Trío.mp3
* atj-2012-09-02-Thelonious Monk & Johnny Griffin, 2.mp3
* atj-2012-09-08-Cannonball Adderley Sextet (2).mp3
* atj-2012-09-09-McCoy Tyner Quintet "Atlantis".mp3
* atj-2012-09-15-Scott LaFaro 1961.Grab. inéditas.mp3
* atj-2012-09-16-Dizzy Gillespie Quintet 1961.mp3
* atj-2012-09-22-Jazz en el tintero - Suma....mp3
* atj-2012-09-23-Jazz en el tintero - ...y sigue.mp3
* atj-2012-09-29-Impulse cabalga de nuevo.mp3
* atj-2012-09-30-Seguimos con Impulse.mp3
* atj-2012-10-06-Thelonious Monk Quartet en directo.mp3
* atj-2012-10-07-El tandem DorhamHenderson.mp3
* atj-2012-10-13-De nuevo con Jim Hall.mp3
* atj-2012-10-14-"Jazz en el tintero" - suma y sigue.mp3
* atj-2012-10-20-Tres discos de jazz, tres.mp3
* atj-2012-10-21-Cuando Jean-Luc Ponty llegó a EEUU.mp3
* atj-2012-10-27-Solo tríos, por favor....mp3
* atj-2012-10-28-El tintero no se seca... nunca....mp3
* atj-2012-11-03-Más tríos... pero distintos.mp3
* atj-2012-11-04-Joe Henderson y sus chicas.mp3
* atj-2012-11-10-Coltrane Live at The Vanguard (1).mp3
* atj-2012-11-11-Coltrane Live at The Vanguard (2).mp3
* atj-2012-11-17-Entrevista a Jorge Pardo.mp3
* atj-2012-11-18-Coltrane Live at The Vanguard (3).mp3
* atj-2012-11-24-Coltrane Live at The Vanguard (4).mp3
* atj-2012-11-25-Inédito:Getz en Nalen (Suecia) 1959.mp3
* atj-2012-12-01-The Cannonball Adderley Sextet 1962.mp3
* atj-2012-12-02-Christian Chevallier 1955.mp3
* atj-2012-12-08-J. Coltrane en el Village Vanguard.mp3
* atj-2012-12-09-Goodbye, Mr. Brubeck....mp3
* atj-2012-12-15-Ella Fitzgerald: The First Lady.mp3
* atj-2012-12-16-Ella and Louis: "Porgy And Bess".mp3
* atj-2012-12-22-J. Coltrane en el Village Vanguard.mp3
* atj-2012-12-23-Pierre Michelot Big Band.mp3
* atj-2012-12-29-Pat Martino Live at "Blues Alley".mp3
* atj-2012-12-30-Trompeta Toccata.mp3
* atj-2013-01-05-Marty Paich Big Band.mp3
* atj-2013-01-06-Cannonball Adderley Sextet.mp3
* atj-2013-01-12-Dave Brubeck Quartet.mp3
* atj-2013-01-13-John Coltrane en directo.mp3
* atj-2013-01-19-The Jazz Messengers in Paris - 1958.mp3
* atj-2013-01-20-Ese viejo "tintero"....mp3
* atj-2013-01-26-Milestone Jazz Stars in concert (1).mp3
* atj-2013-01-27-Milestone Jazz Stars in concert (2).mp3
* atj-2013-02-02-Woody Herman en San Francisco [1].mp3
* atj-2013-02-03-Woody Herman en San Francisco [2].mp3
* atj-2013-02-09-Homenaje a un gran jazzman (1).mp3
* atj-2013-02-10-Homenaje a un gran jazzman (2).mp3
* atj-2013-02-16-Jazz en el Tintero.mp3
* atj-2013-02-17-The Dave Brubeck Quartet.mp3
* atj-2013-02-23-Marty Paich Big Band.mp3
* atj-2013-02-24-Hal Galper - Un pianista diferente.mp3
* atj-2013-03-02-Un gran subestimado del jazz.mp3
* atj-2013-03-03-Hank Mobley- Cosecha 1960.mp3
* atj-2013-03-09-Jazz de hoy en Nueva York.mp3
* atj-2013-03-10-Donald Byrd en el "Chat Qui Pêche".mp3
* atj-2013-03-16-All Night Long.mp3
* atj-2013-03-17-All Day Long.mp3
* atj-2013-03-23-Jazz en el tintero.mp3
* atj-2013-03-24-Stan Getz Quartet live in Zurich.mp3
* atj-2013-03-30-Cannonball Adderley Sextet in Lugan.mp3
* atj-2013-03-31-Sonny Rollins live in San Francisco.mp3
* atj-2013-04-06-Dave Brubeck Quartet. Primeros años.mp3
* atj-2013-04-13-Hank Mobley - 19601961.mp3
* atj-2013-04-14-Hank Mobley 1961.mp3
* atj-2013-04-20-Jazz en el Tintero.mp3
* atj-2013-04-21-Bill Carrothers Trio live.mp3
* atj-2013-04-27-A Buck Clayton jam-session (1).mp3
* atj-2013-04-28-A Buck Clayton jam-session (2).mp3
* atj-2013-05-04-Dave Brubeck Quartet - 1954.mp3
* atj-2013-05-05-Hank Mobley - 1961.mp3
* atj-2013-05-11-The Flail - live at "Small's".mp3
* atj-2013-05-12-A Buck Clayton Jam Session (3).mp3
* atj-2013-05-18-Donald Byrd live (1).mp3
* atj-2013-05-19-Donald Byrd live (2).mp3
* atj-2013-05-25-Miles Davis: Aniversario (1).mp3
* atj-2013-05-26-Miles Davis: Aniversario (2).mp3
* atj-2013-06-01-Jazz en el tintero.mp3
* atj-2013-06-02-Dave Bubeck Quartet.mp3
* atj-2013-06-08-Cannonball in Japan.mp3
* atj-2013-06-09-Donald Byrd en París.mp3
* atj-2013-06-15-Dizzy Gillespie Duets.mp3
* atj-2013-06-16-Dizzy & the two Sonnys.mp3
* atj-2013-06-22-Jazz en el tintero.mp3
* atj-2013-06-23-Eddie DavisJohnny Griffin.mp3
* atj-2013-06-29-A Night At The Village Vanguard.mp3
* atj-2013-06-30-John Coltrane.mp3
* atj-2013-07-06-Una leyenda: Frank Morgan (1).mp3
* atj-2013-07-07-Una leyenda: Frank Morgan [2].mp3
* atj-2013-07-13-The Jazz Messengers in Europe (1).mp3
* atj-2013-07-14-The Jazz Messengers in Europe (2).mp3
* atj-2013-07-27-Recordemos a Wilbur Harden (1).mp3
* atj-2013-07-28-Recordemos a Wilbur Harden (2).mp3
* atj-2013-08-03-Un gran pianista: Kenny Drew.mp3
* atj-2013-08-04-Kenny Drew Trío - Una joya.mp3
* atj-2013-08-10-Louie Bellson.mp3
* atj-2013-08-11-For Musicians Only.mp3
* atj-2013-08-17-Cannonball Adderley Sextet.mp3
* atj-2013-08-18-Wilbur Harden y John Coltrane.mp3
* atj-2013-08-24-Terry Gibbs Dreamband (1).mp3
* atj-2013-08-25-Terry Gibbs Dreamband (2).mp3
* atj-2013-08-31-Kenny Barron Quintet.mp3
* atj-2013-09-01-Kenny Burrell.mp3
* atj-2013-09-07-The CD Players.mp3
* atj-2013-09-08-Clifford BrownMax Roach Q..mp3
* atj-2013-09-14-Bill Charlap Trío en el Vanguard.mp3
* atj-2013-09-15-Lester Young en Boston.mp3
* atj-2013-09-21-"The Five Peace Band" 1.mp3
* atj-2013-09-22-"The Five Peace Band" 2.mp3
* atj-2013-09-28-Duke Pearson Big Band live (1).mp3
* atj-2013-09-29-Duke Pearson Big Band live (2).mp3
* atj-2013-10-06-Jazz en el tintero.mp3
* atj-2013-10-12-Jazz en el Tintero.mp3
* atj-2013-10-13-London Jazz Festival 2011.mp3
* atj-2013-10-19-Jam Session con Buck Clayton.mp3
* atj-2013-10-20-Estrenos en A Todo Jazz.mp3
* atj-2013-10-26-Woody Shaw Quintet Live (1).mp3
* atj-2013-10-27-Woody Shaw Quintet Live (2).mp3
* atj-2013-11-02-Jazz en el tintero.mp3
* atj-2013-11-03-Jazz en el tintero.mp3
* atj-2013-11-09-The Five Peace Band.mp3
* atj-2013-11-10-The Jazztet at Newport.mp3
* atj-2013-11-16-Ahmad Jamal live at The Alhambra 1.mp3
* atj-2013-11-17-Ahmad Jamal live at The Alhambra 2.mp3
* atj-2013-11-24-Buck Clayton Jam Session 5.mp3
* atj-2013-11-30-Kenny ClarkeF. Boland Big Band 1.mp3
* atj-2013-12-01-Kenny ClarkeF. Boland Big Band 2.mp3
* atj-2013-12-07-Stan Getz en Harlem de Estocolmo 1.mp3
* atj-2013-12-08-Stan Getz en Harlem de Estocolmo 2.mp3
* atj-2013-12-14-Jazz en el tintero.mp3
* atj-2013-12-15-Jazz en el tintero.mp3
* atj-2013-12-21-Mulgrew Miller Trio at Yoshi's (1).mp3
* atj-2013-12-22-Mulgrew Miller Trio at Yoshi's (2).mp3
* atj-2013-12-28-Cedar Walton Quartet live (1977).mp3
* atj-2013-12-29-Terry Gibbs Big Band (1961).mp3
* atj-2014-01-04-Enrico Pieranunzi.mp3
* atj-2014-01-05-Dexter Gordon. Zurich 1975.mp3
* atj-2014-01-11-Jazz en el tintero.mp3
* atj-2014-01-12-Jazz en el tintero.mp3
* atj-2014-01-19-Art Pepper en directo - 1976.mp3
* atj-2014-01-25-The Giants of Jazz gira - 1971 (1).mp3
* atj-2014-01-26-The Giants of Jazz gira - 1971 (2).mp3
* atj-2014-02-01-Gary Burton & Pat Metheny Q. live.mp3
* atj-2014-02-02-Ivo Sans cuarteto en Barcelona.mp3
* atj-2014-02-08-Chris Potter cuarteto en directo.mp3
* atj-2014-02-09-Jazz en el tintero.mp3
* atj-2014-02-15-Jazz En El tintero 2.mp3
* atj-2014-02-16-Jazz En El tintero 3.mp3
* atj-2014-02-23-Albert Bover Trío desde Bilbao.mp3
* atj-2014-03-01-Kenny Barron Quintet.mp3
* atj-2014-03-02-Jazz en el tintero.mp3
* atj-2014-03-09-Woody Shaw Quintet live (3).mp3
* atj-2014-03-15-Jazz desde Dinamarca.mp3
* atj-2014-03-22-Bent Jaedig Quartet (2).mp3
* atj-2014-03-23-MulliganDesmond Quartet - 1957.mp3
* atj-2014-03-29-Jazz en el tintero.mp3
* atj-2014-03-30-Horace Silver 1962.mp3
* atj-2014-04-05-San Francisco Jazz Collective.mp3
* atj-2014-04-06-Kenny Dorham - 1962.mp3
* atj-2014-04-12-Jazz desde Chile.mp3
* atj-2014-04-13-Ahmad Jamal Trio - 1962.mp3
* atj-2014-04-19-Dexter Gordon - Zurich 1975 (2).mp3
* atj-2014-04-20-Dexter Gordon - Zurich 1975 (3).mp3
* atj-2014-04-27-Newport in New York 1972.mp3
* atj-2014-05-03-Jazz En El Tintero.mp3
* atj-2014-05-04-Pat Martino - 1968.mp3
* atj-2014-05-10-Dexter GordonBooker Ervin: Duelo de gigantes.mp3
* atj-2014-05-11-Miles Davis quinteto en Suiza.mp3
* atj-2014-05-17-Pat Martino Trío [2].mp3
* atj-2014-05-18-Buck Clayton Jam Sessions.mp3
* atj-2014-05-24-Art Farmer "Modern Art".mp3
* atj-2014-05-25-Mulgrew Miller Trío - Live at Yoshi's (3).mp3
* atj-2014-05-31-Count Basie en Europa (1).mp3
* atj-2014-06-01-Count Basie en Europa (2).mp3
* atj-2014-06-07-Ben & Dex en Baden.mp3
* atj-2014-06-08-Mulligan en Europa [1960].mp3
* atj-2014-06-14-Jazz en el tintero I.mp3
* atj-2014-06-15-Jazz en el tintero II.mp3
* atj-2014-06-21-Descanse en paz Horace Silver (1928-2014) [1].mp3
* atj-2014-06-22-Descanse en paz Horace Silver (1928-2014) [2].mp3
* atj-2014-06-29-Clark Terry Quintet.mp3
* atj-2014-07-05-Newport In New York 1972.mp3
* atj-2014-07-06-Jazz en el tintero.mp3
* atj-2014-07-12-Lee Morgan Clifford Jordan Quintet.mp3
* atj-2014-07-13-Max Roach Quintet live in Europe.mp3
* atj-2014-07-26-Woody Herman Big Band 1963.mp3
* atj-2014-07-27-Sonny Rollins Quartet.mp3
* atj-2014-08-02-PernalSzkil Quintet - Getxo 2013.mp3
* atj-2014-08-03-Un disco del gran Freddie Hubbard.mp3
* atj-2014-08-09-Kevin Eubanks en directo.mp3
* atj-2014-08-10-Jim Hall in Tokio.mp3
* atj-2014-08-16-MulliganDesmond de nuevo.mp3
* atj-2014-08-17-Max Roach Quintet live (2).mp3
* atj-2014-08-23-J. J. Johnson Sextet.mp3
* atj-2014-08-24-TatumWebster - Mejor imposible.mp3
* atj-2014-08-30-Blakey y los Tres Ratones Ciegos (1).mp3
* atj-2014-08-31-Blakey y los Tres Ratones Ciegos (2).mp3
* atj-2014-09-06-Woody Herman de nuevo.mp3
* atj-2014-09-07-Harold Land ¿The Fox¿.mp3
* atj-2014-09-13-Jessica Williams, la pianista [1].mp3
* atj-2014-09-14-Jessica Williams, la pianista [2].mp3
* atj-2014-09-21-Desmond y Mulligan-Nuevos duos.mp3
* atj-2014-09-27-Newport In New York 1972 (3).mp3
* atj-2014-09-28-Newport In New York 1972 (4).mp3
* atj-2014-10-05-John Lewis - un minimalista exquisito.mp3
* atj-2014-10-11-Jazz en el Tintero.mp3
* atj-2014-10-12-Jazz en el Tintero.mp3
* atj-2014-10-18-Jazz en el tintero.mp3
* atj-2014-10-19-Jazz en el tintero.mp3
* atj-2014-10-25-Jazz en el tintero.mp3
* atj-2014-10-26-Jazz en el tintero.mp3
* atj-2014-11-02-Rodney Green Quartet live.mp3
* atj-2014-11-08-Un magnífico contrabajista: Red Mitchell.mp3
* atj-2014-11-09-Jazz en el tintero.mp3
* atj-2014-11-15-Jazz en el tintero.mp3
* atj-2014-11-16- Tommy Flanagan. Un caballero del teclado.mp3
* atj-2014-11-22-Wes Montgomery en Paris.mp3
* atj-2014-11-23-Jazz en el tintero.mp3
* atj-2014-11-29-Stan Getz Quintet.mp3
* atj-2014-11-30-Happy Birthday, Mr. Sheldon!.mp3
* atj-2014-12-06-Dave Brubeck Quartet live.mp3
* atj-2014-12-07-Jazz en el tintero.mp3
* atj-2014-12-14-Wes Montgomery en París.mp3
* atj-2014-12-20-The Jazz Messengers at Birdland (1) - 1960.mp3
* atj-2014-12-21-The Jazz Messengers at Birdland (2) - 1960.mp3
* atj-2014-12-27-Bill Evans en Madrid (1979) [1].mp3
* atj-2014-12-28-Bill Evans en Madrid (1979) [2].mp3
* atj-2015-01-03-Valery Ponomarev at Sweet Basil.mp3
* atj-2015-01-04-John McLaughlin en Japón.mp3
* atj-2015-01-10-Max Roach-Maestro de la batería.mp3
* atj-2015-01-11-The Very Tall Band-1998.mp3
* atj-2015-01-17-Cedar Walton en directo.mp3
* atj-2015-01-18-Wes Montgomery en París, 1965.mp3
* atj-2015-01-24-Jay Jay Johnson at the Vanguard.mp3
* atj-2015-01-25-Stan Getz Quintet live in Boston.mp3
* atj-2015-01-31-Jazz en el tintero.mp3
* atj-2015-02-01-Jazz en el tintero 2.mp3
* atj-2015-02-07-Jazz en el tintero 3.mp3
* atj-2015-02-08-Jazz en el tintero 4.mp3
* atj-2015-02-14-John McLaughlin in Tokio (2).mp3
* atj-2015-02-15-Jazz En El Tintero.mp3
* atj-2015-02-22-Jazz en el Tintero.mp3
* atj-2015-02-28-Jazz En El Tintero: Cedar Walton (2).mp3
* atj-2015-03-01-Jazz En El Tintero: Cedar Walton (3).mp3
* atj-2015-03-07-Charles Tolliver, trompetista emérito (1).mp3
* atj-2015-03-08-Charles Tolliver, trompetista emérito (2).mp3
* atj-2015-03-14-A todo jazz - Lionel Hampton.mp3
* atj-2015-03-14-Charles Tolliver en concierto.mp3
* atj-2015-03-14-Charlie Parker.mp3
* atj-2015-03-14-George Benson.mp3
* atj-2015-03-14-JJ Johnson en el Village Vanguard.mp3
* atj-2015-03-14-Lester Young en concierto.mp3
* atj-2015-03-14-Lester Young.mp3
* atj-2015-03-14-Long Tall Dexter.mp3
* atj-2015-03-14-Michael Brecker.mp3
* atj-2015-03-14-Oscar Peterson, Milt Jackson y Ray Brown.mp3
* atj-2015-03-14-Thad Jones en directo.mp3
* atj-2015-03-14-Wynton Kelly.mp3
* atj-2015-03-21-George Benson.mp3
* atj-2015-03-22-Zoot Sims.mp3
* jpqs-2008-10-13-Carsten Daerr - 131008.mp3
* jpqs-2008-10-20-Tineke Postma - 201008.mp3
* jpqs-2008-10-22-Dizzy Gillespie - 221008.mp3
* jpqs-2008-10-24-Cab Calloway - 241008.mp3
* jpqs-2008-10-27-Illmieki - 271008.mp3
* jpqs-2008-10-29-Charlie Parker - 291008.mp3
* jpqs-2008-11-03-Big Band de Jimmy Heath - 031108.mp3
* jpqs-2008-11-05-Manny Albam - 051108.mp3
* jpqs-2008-11-07-Benny Carter - 071108.mp3
* jpqs-2008-11-10-Noticias y novedades - 101108.mp3
* jpqs-2008-11-12-Jazz porque Sí - 121108.mp3
* jpqs-2008-11-14-Muggsy Spanier - 141108.mp3
* jpqs-2008-11-17-Marvin Stamm - 171108.mp3
* jpqs-2008-11-19-J.J Johnson - 191108.mp3
* jpqs-2008-11-21-Coleman Hawkins - 211108.mp3
* jpqs-2008-11-24-Música Escandinava - 241108.mp3
* jpqs-2008-11-26-Charlie Parker - 261108.mp3
* jpqs-2008-11-28-Duke Ellington - 281108.mp3
* jpqs-2008-12-01-Jean-Marie Machado - 011208.mp3
* jpqs-2008-12-30-Duke Ellington - 301208.mp3
* jpqs-2009-01-08-François Bourassa - 080109.mp3
* jpqs-2009-01-12-Emil Viklický - 120109.mp3
* jpqs-2009-01-19-Herb Geller I - 190109.mp3
* jpqs-2009-01-26-Herb Geller - 260109.mp3
* jpqs-2009-01-28-Charlie Parker - 280109.mp3
* jpqs-2009-02-02-Rob McConnell - 020209.mp3
* jpqs-2009-02-04-Mel Lewis - 040209.mp3
* jpqs-2009-02-06-Bunny Berigan - 060209.mp3
* jpqs-2009-02-09-Slovenia Big Band - 090209.mp3
* jpqs-2009-02-11-Art Farmer - 110209.mp3
* jpqs-2009-02-13-Cab Calloway - 130209.mp3
* jpqs-2009-02-16-Yellowjackets - 160209.mp3
* jpqs-2009-02-18-Harold Land - 180209.mp3
* jpqs-2009-02-20-Beny Carter - 200209.mp3
* jpqs-2009-02-23-Slovenia Big Band - 230209.mp3
* jpqs-2009-02-25-Charlie Parker - 250209.mp3
* jpqs-2009-02-27-Duke Ellington - 270209.mp3
* jpqs-2009-03-02-Colin Towns - 020309.mp3
* jpqs-2009-03-04-Barney Wilen - 040309.mp3
* jpqs-2009-03-06-Muggsy Spanier - 060309.mp3
* jpqs-2009-03-09-Slovenia Big Band - 090309.mp3
* jpqs-2009-03-11-Clifford Brown - 110309.mp3
* jpqs-2009-03-13-Jimmy Archey - 130309.mp3
* jpqs-2009-03-16-Tommy Flanagan - 160309.mp3
* jpqs-2009-03-18-John Coltrane - 180309.mp3
* jpqs-2009-03-20-Duke Ellington - 200309.mp3
* jpqs-2009-03-23-Anne Guus Teerhuis - 230309.mp3
* jpqs-2009-03-25-Charlie Parker - 250309.mp3
* jpqs-2009-03-27-Ben Webster - 270309.mp3
* jpqs-2009-03-30-Émile Parisien - 300309.mp3
* jpqs-2009-04-01-Dizzy Gillespie - 010409.mp3
* jpqs-2009-04-03-Fats Waller - 030409.mp3
* jpqs-2009-04-06-Wolfgang Schlüter - 060409.mp3
* jpqs-2009-04-08-Jackie McLean - 080409.mp3
* jpqs-2009-04-10-Joe 'King' Oliver - 100409.mp3
* jpqs-2009-04-13-Dave Holland - 130409.mp3
* jpqs-2009-04-15-Jay Jay Johnson - 150409.mp3
* jpqs-2009-04-17-Fletcher Henderson - 170409.mp3
* jpqs-2009-04-20-Bob Brookmeyer - 200409.mp3
* jpqs-2009-04-22-Miles Davis - 220409.mp3
* jpqs-2009-04-24-Duke Ellington - 240409.mp3
* jpqs-2009-04-27-Martial Solal - 270409.mp3
* jpqs-2009-04-29-Charlie Parker - 290409.mp3
* jpqs-2009-05-01-Count Basie - 010509.mp3
* jpqs-2009-05-04-Eric Le Lann - 040509.mp3
* jpqs-2009-05-04-Herbie Man - 010709.mp3
* jpqs-2009-05-08-Django Reinhardt - 080509.mp3
* jpqs-2009-05-11-Laïka Fatien - 110509.mp3
* jpqs-2009-05-13-Chet Baker - 130509.mp3
* jpqs-2009-05-15-Billie Holiday - 150509.mp3
* jpqs-2009-05-18-Gustav Brom Big Band - 180509.mp3
* jpqs-2009-05-18-Maria Schneider - 100809.mp3
* jpqs-2009-05-20-Gigi Gryce - 200509.mp3
* jpqs-2009-05-22-Bunny Berigan - 220509.mp3
* jpqs-2009-05-25-Bruno Régnier - 250509.mp3
* jpqs-2009-07-03-Muggsy Spanier - 030709.mp3
* jpqs-2009-07-06-Regina Carter - 060709.mp3
* jpqs-2009-07-08-Milt Jackson - 080709.mp3
* jpqs-2009-07-10-Jelly Roll Morton - 100709.mp3
* jpqs-2009-07-13-Regina Carter - 130709.mp3
* jpqs-2009-07-15-Philly Joe Jones - 150709.mp3
* jpqs-2009-07-17-Jimmy Archey - 170709.mp3
* jpqs-2009-07-20-Hard Groove Quartet - 200709.mp3
* jpqs-2009-07-22-Sonny Stitt - 220709.mp3
* jpqs-2009-07-24-Fats Waller - 240709.mp3
* jpqs-2009-07-27-Jiannis Pavlidis - 270709.mp3
* jpqs-2009-07-29-Charlie Parker - 290709.mp3
* jpqs-2009-07-31-Duke Ellington - 310709.mp3
* jpqs-2009-08-03-Chuck Manning - 030809.mp3
* jpqs-2009-08-05-Art Farmer - 050809.mp3
* jpqs-2009-08-12-Clifford Brown - 120809.mp3
* jpqs-2009-08-14-Jazz Porque Sí- Fletcher Henderson-140809.mp3
* jpqs-2009-08-17-Jazz porque si- Concierto Cuarteto Peter Asplund- 170809.mp3
* jpqs-2009-08-19-Jazz porque sí- Bill Harris- 190809.mp3
* jpqs-2009-08-21-Jazz Porque Sí- Count Basie- 210809.mp3
* jpqs-2009-08-24-Torbjörn Zetterberg -240809.mp3
* jpqs-2009-08-26-Charlie Parker - 260809.mp3
* jpqs-2009-08-28-Duke Ellington - 280809.mp3
* jpqs-2009-09-02-Horace Silver - 020909.mp3
* jpqs-2009-09-14-Bobo Stenson - 140909.mp3
* jpqs-2009-09-21-Norrbotten Big Band - 210909.mp3
* jpqs-2009-10-02-Cab Calloway - 021009.mp3
* jpqs-2009-10-05-Norrbotten Big Band - 051009.mp3
* jpqs-2009-10-07-Dizzy Gillespie - 071009.mp3
* jpqs-2009-10-07-Jazz porque Sí - 1111009.mp3
* jpqs-2009-10-09-Benny Carter - 091009.mp3
* jpqs-2009-10-09-Jazz porque Sí - 091009.mp3
* jpqs-2009-10-12-Tim Hagans - 121009.mp3
* jpqs-2009-10-14-Jackie McLean - 141009.mp3
* jpqs-2009-10-16-Muggsy Spanier - 161009.mp3
* jpqs-2009-10-19-Kari Heinilä - 191009.mp3
* jpqs-2009-10-21-Jazz porque Sí - 211009.mp3
* jpqs-2009-10-23-Jazz porque Sí - 231009.mp3
* jpqs-2009-10-26-Jazz porque Sí - 261009.mp3
* jpqs-2009-10-28-Jazz porque Sí - 281009.mp3
* jpqs-2009-10-30-Jazz porque Sí - 301009.mp3
* jpqs-2009-11-02-Jazz Orchestra de Zagreb - 021109.mp3
* jpqs-2009-11-04-Gigi Gryce - 041109.mp3
* jpqs-2009-11-06-Jazz porque Sí - 0611009.mp3
* jpqs-2009-11-16-Jazz porque Sí - 161109.mp3
* jpqs-2009-11-18-Dexter Gordon - 181109.mp3
* jpqs-2009-11-20-Count Basie - 201109.mp3
* jpqs-2009-11-23-Points Quartet - 231109.mp3
* jpqs-2009-12-02-Wynton Kelly - 021209.mp3
* jpqs-2009-12-04-Django Reinhardt - 041209.mp3
* jpqs-2009-12-07-Marianne Trude - 071209.mp3
* jpqs-2009-12-11-Donald Byrd - 111209.mp3
* jpqs-2009-12-14-Ron Carter - 141209.mp3
* jpqs-2009-12-21-Ron Carter - 211209.mp3
* jpqs-2010-01-04-Infinite Quintet - 040110.mp3
* jpqs-2010-01-11-Infinite Quintet - 110110.mp3
* jpqs-2010-01-13-Michael Brecker - 130110.mp3
* jpqs-2010-01-15-Cab Calloway - 150110.mp3
* jpqs-2010-01-20-Jazz porque sí - 200110.mp3
* jpqs-2010-01-22-Benny Carter - 220110.mp3
* jpqs-2010-01-25-Jazz porque Sí - 250110.mp3
* jpqs-2010-01-27-Charlie Parker - 270110.mp3
* jpqs-2010-01-29-Jazz porque Sí - 290110.mp3
* jpqs-2010-02-01-Wark - 010210.mp3
* jpqs-2010-02-03-Art Farmer - 030210.mp3
* jpqs-2010-02-05-Los Firehouse - 050210.mp3
* jpqs-2010-02-08-European Jazz Orchestra - 080210.mp3
* jpqs-2010-02-10-Clifford Brown - 100210.mp3
* jpqs-2010-02-12-Muggsy Spanier - 120210.mp3
* jpqs-2010-02-15-S. Shterev - 150210.mp3
* jpqs-2010-02-17-Thelonious Monk - 170210.mp3
* jpqs-2010-02-19-Jimmy Archey - 190210.mp3
* jpqs-2010-02-22-Trompetista Roy Hargrove - 220210.mp3
* jpqs-2010-02-24-Charlie Parker - 240210.mp3
* jpqs-2010-02-26-Duke Ellington - 260210.mp3
* jpqs-2010-03-01-Roy Hargrove - 010310.mp3
* jpqs-2010-03-03-John Coltrane - 030310.mp3
* jpqs-2010-03-05-Fats Waller - 050310.mp3
* jpqs-2010-03-08-Eric Vloeimans - 080310.mp3
* jpqs-2010-03-10-Dizzy Gillespie - 100310.mp3
* jpqs-2010-03-12-Hnos Henderson - 120310.mp3
* jpqs-2010-03-15-Árpád Oláh - 150310.mp3
* jpqs-2010-03-19-Count Basie - 190310.mp3
* jpqs-2010-03-22-Tony Lakatos - 220310.mp3
* jpqs-2010-03-24-Jay Jay Johnson - 240310.mp3
* jpqs-2010-03-26-Duke Ellington - 260310.mp3
* jpqs-2010-03-29-Sharp Nine - 290310.mp3
* jpqs-2010-03-31-Charlie Parker - 310310.mp3
* jpqs-2010-04-02-Django Reinhardt - 020410.mp3
* jpqs-2010-04-05-James Carter - 050410.mp3
* jpqs-2010-04-07-Gerry Mulligan - 070410.mp3
* jpqs-2010-04-09-Billie Holiday - 090410.mp3
* jpqs-2010-04-12-James Carter - 120410.mp3
* jpqs-2010-04-14-Gigi Gryce - 140410.mp3
* jpqs-2010-04-16-Bessie Smith - 160410.mp3
* jpqs-2010-04-19-Tom Gibbs - 190410.mp3
* jpqs-2010-04-21-Dexter Gordon - 210410.mp3
* jpqs-2010-04-23-Louis Armstrong - 230410.mp3
* jpqs-2010-04-28-Charlie Parker - 280410.mp3
* jpqs-2010-04-30-Duke Ellington - 300410.mp3
* jpqs-2010-05-03-John Abercrombie, guitarrista.mp3
* jpqs-2010-05-05-Harold Land - 050510.mp3
* jpqs-2010-05-07-The Firehouse - 070510.mp3
* jpqs-2010-05-10-John Abercrombie - 100510.mp3
* jpqs-2010-05-12-Red Garland, pianista - 120510.mp3
* jpqs-2010-05-14-Sydney Bechet - 140510.mp3
* jpqs-2010-05-17-Chantal Gagné, pianista - 170510.mp3
* jpqs-2010-05-19-Lee Morgan, trompetista - 190510.mp3
* jpqs-2010-05-21-Bessie Smith - 210510.mp3
* jpqs-2010-05-24-Duke Ellington - 240510.mp3
* jpqs-2010-05-26-Charlie Parker - 260510.mp3
* jpqs-2010-05-28-Bunny Berigan - 280510.mp3
* jpqs-2010-05-31-Carla Bley - 310510.mp3
* jpqs-2010-06-02-Walter Davis Jr - 020610.mp3
* jpqs-2010-06-04-Cab Calloway - 040610.mp3
* jpqs-2010-06-07-Straight Ahead Quartet - 070610.mp3
* jpqs-2010-06-09-Manny Albam - 090610.mp3
* jpqs-2010-06-11-Frankie Trumbauer - 110610.mp3
* jpqs-2010-06-14-JonssonGröndal Quintet - 140610.mp3
* jpqs-2010-06-16-Tom Harrell - 160610.mp3
* jpqs-2010-06-18-Chick Webb - 180610.mp3
* jpqs-2010-06-21-Ari Bragi Karason - 210610.mp3
* jpqs-2010-06-23-Milt Jackson - 230610.mp3
* jpqs-2010-06-25-Duke Ellington - 250610.mp3
* jpqs-2010-06-28-Danish Radio Big Band - 280610.mp3
* jpqs-2010-06-30-Charlie Parker - 300610.mp3
* jpqs-2010-07-02-Benny Carter - 020710.mp3
* jpqs-2010-07-05-Jérôme Sabbagh - 050710.mp3
* jpqs-2010-07-07-Fats Navarro - 070710.mp3
* jpqs-2010-07-09-Muggsy Spanier - 090710.mp3
* jpqs-2010-07-12-Jean-Michel Pilc - 120710.mp3
* jpqs-2010-07-14-Art Farmer - 140710.mp3
* jpqs-2010-07-16-Jimmy Archey - 160710.mp3
* jpqs-2010-07-19-Sylvain Cathala - 190710.mp3
* jpqs-2010-07-21-Clifford Brown - 210710.mp3
* jpqs-2010-07-23-Claude Luter - 230710.mp3
* jpqs-2010-07-26-Maciej Sikala - 260710.mp3
* jpqs-2010-07-28-Charlie Parker - 280710.mp3
* jpqs-2010-07-30-Duke Ellington - 300710.mp3
* jpqs-2010-08-02-Igor Butman - 020810.mp3
* jpqs-2010-08-04-John Coltrane - 040810.mp3
* jpqs-2010-08-06-The Firehouse - 060810.mp3
* jpqs-2010-08-09-Igor Butman - 090810.mp3
* jpqs-2010-08-11-Dizzy Gillespie - 110810.mp3
* jpqs-2010-08-13-Fats Waller - 130810.mp3
* jpqs-2010-08-16-Mal Waldron - 160810.mp3
* jpqs-2010-08-18-Jackie McLean - 180810.mp3
* jpqs-2010-08-20-Fletcher Henderson - 200810.mp3
* jpqs-2010-08-23-Mario Stanchev - 230810.mp3
* jpqs-2010-08-25-Charlie Parker - 250810.mp3
* jpqs-2010-08-27-Duke Ellington - 270810.mp3
* jpqs-2010-08-30-Jussi Lehtonen - 300810.mp3
* jpqs-2010-09-01-Art Pepper - 010910.mp3
* jpqs-2010-09-03-Count Basie - 030910.mp3
* jpqs-2010-09-06-T. European Jazz Quartet - 060910.mp3
* jpqs-2010-09-08-Jay Jay Johnson - 080910.mp3
* jpqs-2010-09-10-Django Reinhardt - 100910.mp3
* jpqs-2010-09-13-Reykjavik Big Band - 130910.mp3
* jpqs-2010-09-15-Bill Evans - 150910.mp3
* jpqs-2010-09-17-Billie Holiday - 170910.mp3
* jpqs-2010-09-20-Kestutis Vaiginis - 200910.mp3
* jpqs-2010-09-22-Gigi Gryce - 220910.mp3
* jpqs-2010-09-24-Duke Ellington -240910.mp3
* jpqs-2010-09-29-Charlie Parker - 290910.mp3
* jpqs-2010-10-01-Bunny Berigan - 011010.mp3
* jpqs-2010-10-06-Harold Land - 061010.mp3
* jpqs-2010-10-08-Louis Armstrong - 081010.mp3
* jpqs-2010-10-13-Terry Gibbs - 131010.mp3
* jpqs-2010-10-15-Cab Calloway - 151010.mp3
* jpqs-2010-10-20-Dexter Gordon - 201010.mp3
* jpqs-2010-10-22-Benny Carter - 221010.mp3
* jpqs-2010-10-25-HFM Jazz Orchestra - 251010.mp3
* jpqs-2010-10-27-Charlie Parker - 271010.mp3
* jpqs-2010-10-29-Duke Ellington - 291010.mp3
* jpqs-2010-11-01-Chris Potter - 011110.mp3
* jpqs-2010-11-03-Eddie Davis - 031110.mp3
* jpqs-2010-11-05-Art Tatum - 051110.mp3
* jpqs-2010-11-10-Monográfico Lee Morgan - 101110.mp3
* jpqs-2010-11-12-Manny Albam - 171110.mp3
* jpqs-2010-11-12-Muggsy Spanier - 121110.mp3
* jpqs-2010-11-12-Tommy Flanagan - 151110.mp3
* jpqs-2010-11-19-Fats Waller - 191110.mp3
* jpqs-2010-11-24-Charlie Parker - 241110.mp3
* jpqs-2010-11-26-Duke Ellington - 261110.mp3
* jpqs-2010-12-01-Wynton Kelly - 011210.mp3
* jpqs-2010-12-03-Fletcher Henderson - 031210.mp3
* jpqs-2010-12-08-Jimmy Smith - 081210.mp3
* jpqs-2010-12-10-The Firehouse - 101210.mp3
* jpqs-2010-12-13-Harry Waters - 131210.mp3
* jpqs-2010-12-15-The Modern Jazz Quartet - 151210.mp3
* jpqs-2010-12-17-Claude Luter - 171210.mp3
* jpqs-2010-12-22-Art Farmer - 221210.mp3
* jpqs-2010-12-24-Count Basie - 241210.mp3
* jpqs-2010-12-29-Charlie Parker - 291210.mp3
* jpqs-2010-12-31-Duke Ellington - 311210.mp3
* jpqs-2011-01-05-Clifford Brown - 050111.mp3
* jpqs-2011-01-07-Django Reinhardt - 070111.mp3
* jpqs-2011-01-10-Jef Neve - 100111.mp3
* jpqs-2011-01-12-John Coltrane - 120111.mp3
* jpqs-2011-01-14-Billie Holiday - 140111.mp3
* jpqs-2011-01-19-Dizzy Gillespie - 190111.mp3
* jpqs-2011-01-21-Bunny Berigan - 210111.mp3
* jpqs-2011-01-24-Ralph Peterson - 240111.mp3
* jpqs-2011-01-26-Charlie Parker - 260111.mp3
* jpqs-2011-01-28-Duke Ellington - 280111.mp3
* jpqs-2011-02-02-Jackie McLean - 0202011.mp3
* jpqs-2011-02-04-Louis Armstrong - 040211.mp3
* jpqs-2011-02-09-Jay Jay Johnson - 090211.mp3
* jpqs-2011-02-11-Cab Calloway - 110211.mp3
* jpqs-2011-02-16-Gigi Gryce - 160211.mp3
* jpqs-2011-02-18-Benny Carter - 180211.mp3
* jpqs-2011-02-23-Clifford Brown - 230211.mp3
* jpqs-2011-02-25-Duke Ellington - 250211.mp3
* jpqs-2011-03-02-Philly Joe Jones - 020311.mp3
* jpqs-2011-03-04-Muggsy Spanier - 040311.mp3
* jpqs-2011-03-11-Fats Waller - 110311.mp3
* jpqs-2011-03-16-Dexter Gordon - 160311.mp3
* jpqs-2011-03-18-Fletcher Henderson - 180311.mp3
* jpqs-2011-03-23-Lee Morgan - 230311.mp3
* jpqs-2011-03-25-Duke Ellington - 250311.mp3
* jpqs-2011-03-28-Concierto de Kenny Barron.mp3
* jpqs-2011-03-30-Thelonious Monk en grabaciones de 1.mp3
* jpqs-2011-04-06-Randy Weston en su 85º cumpleaños.mp3
* jpqs-2011-04-08-Claude Luter.mp3
* jpqs-2011-04-13-Milt Jackson y John Lewis.mp3
* jpqs-2011-04-15-Count Basie, en grabaciones del año.mp3
* jpqs-2011-04-20-Art Farmer con grabaciones de 1979.mp3
* jpqs-2011-04-22-Django Reinhardt.mp3
* jpqs-2011-04-27-Thelonious Monk.mp3
* jpqs-2011-04-29-Duke Ellington, grabaciones de 1958.mp3
* jpqs-2011-05-04-Clifford Brown.mp3
* jpqs-2011-05-06-Billie Holiday (1937-1939).mp3
* jpqs-2011-05-11-John Coltrane, en 1958.mp3
* jpqs-2011-05-13-Bunny Berigan, trompetistadirector.mp3
* jpqs-2011-05-18-Dizzy Gillespie 1952.mp3
* jpqs-2011-05-20-Louis Armstrong 1952 y 1953.mp3
* jpqs-2011-05-25-Thelonious Monk 1947 y 1948.mp3
* jpqs-2011-05-27-Duke Ellington 1958.mp3
* jpqs-2011-06-01-Jackie McLean.mp3
* jpqs-2011-06-03-Cab Calloway.mp3
* jpqs-2011-06-08-Jay Jay Johnson 1957.mp3
* jpqs-2011-06-10-Benny Carter 1957 y 1958.mp3
* jpqs-2011-06-15-Ella Fitzgerald.mp3
* jpqs-2011-06-17-Muggsy Spanier (1953 y 1956).mp3
* jpqs-2011-06-22-Gigi Gryce, saxo alto.mp3
* jpqs-2011-06-24-Duke Ellington, en 1958.mp3
* jpqs-2011-07-06-Harold Land 1954 y 1955.mp3
* jpqs-2011-07-08-Fletcher Henderson.mp3
* jpqs-2011-07-13-Dexter Gordon con Tete Montoliu.mp3
* jpqs-2011-07-15-Claude Luter.mp3
* jpqs-2011-07-20-Lee Morgan.mp3
* jpqs-2011-07-22-Count Basie.mp3
* jpqs-2011-07-27-Thelonious Monk (1948-51).mp3
* jpqs-2011-07-29-Duke Ellington (1958).mp3
* jpqs-2011-08-03-Philly Joe Jones (1955).mp3
* jpqs-2011-08-05-Django Reinhardt (1939-1940).mp3
* jpqs-2011-08-10-Milt Jackson y John Lewis.mp3
* jpqs-2011-08-12-Billie Holiday.mp3
* jpqs-2011-08-17-Art Farmer.mp3
* jpqs-2011-08-19-Bunny Berigan.mp3
* jpqs-2011-08-24-Clifford Brown.mp3
* jpqs-2011-08-26-Duke Ellington.mp3
* jpqs-2011-08-31-Thelonious Monk (1951 y 1952).mp3
* jpqs-2011-09-02-Louis Armstrong (1953 y 1954).mp3
* jpqs-2011-09-07-Sonny Rollins.mp3
* jpqs-2011-09-09-Cab Calloway.mp3
* jpqs-2011-09-14-John Coltrane, grabaciones de 1958.mp3
* jpqs-2011-09-16-Benny Carter.mp3
* jpqs-2011-09-21-Dizzy Gillespie.mp3
* jpqs-2011-09-23-Fats Waller.mp3
* jpqs-2011-09-28-Homenaje a Miles Davis.mp3
* jpqs-2011-09-30-Duke Ellington, grabaciones del 59.mp3
* jpqs-2011-10-05-Booker Little.mp3
* jpqs-2011-10-07-Fletcher Henderson.mp3
* jpqs-2011-10-12-Jackie McLean.mp3
* jpqs-2011-10-14-Claude Luter.mp3
* jpqs-2011-10-19-Jay Jay Johnson.mp3
* jpqs-2011-10-21-Count Basie.mp3
* jpqs-2011-10-26-Thelonious Monk.mp3
* jpqs-2011-10-28-Duke Ellington, en 1959.mp3
* jpqs-2011-11-02-Phil Woods.mp3
* jpqs-2011-11-04-Django Reinhardt 1939 y 1940.mp3
* jpqs-2011-11-09-Gigi Gryce.mp3
* jpqs-2011-11-11-Billie Holiday (1939-1944).mp3
* jpqs-2011-11-16-En memoria de Roy Brooks.mp3
* jpqs-2011-11-18-Bunny Berigan, trompetista.mp3
* jpqs-2011-11-23-Harold Land (1955).mp3
* jpqs-2011-11-25-Duke Ellington (1959).mp3
* jpqs-2011-11-30-Thelonious Monk, en 1952 y 1953.mp3
* jpqs-2011-12-02-Louis Armstrong.mp3
* jpqs-2011-12-07-Dexter Gordon en 1964.mp3
* jpqs-2011-12-09-Cab Calloway.mp3
* jpqs-2011-12-14-Lee Morgan (1958 y 1959).mp3
* jpqs-2011-12-16-Turk Murphy.mp3
* jpqs-2011-12-21-Philly Joe Jones (1956).mp3
* jpqs-2011-12-23-Benny Carter.mp3
* jpqs-2011-12-28-Thelonious Monk (1953-54).mp3
* jpqs-2011-12-30-Duke Ellington (1959).mp3
* jpqs-2012-01-04-John McLaughlin.mp3
* jpqs-2012-01-06-Muggsy Spanier.mp3
* jpqs-2012-01-11-The Modern Jazz Quartet.mp3
* jpqs-2012-01-13-Fats Waller.mp3
* jpqs-2012-01-18-Art Farmer.mp3
* jpqs-2012-01-20-Fletcher Henderson.mp3
* jpqs-2012-01-25-Thelonious Monk.mp3
* jpqs-2012-01-27-Duke Ellington en 1959.mp3
* jpqs-2012-02-01-Clifford Brown (1953).mp3
* jpqs-2012-02-03-Claude Luter (1959 y 1971).mp3
* jpqs-2012-02-08-John Coltrane.mp3
* jpqs-2012-02-10-Count Basie.mp3
* jpqs-2012-02-15-Dizzy Gillespie, en 1952.mp3
* jpqs-2012-02-17-Django Reinhardt.mp3
* jpqs-2012-02-22-Jackie McLean (1956).mp3
* jpqs-2012-02-24-Duke Ellington (1959).mp3
* jpqs-2012-02-29-Thelonious Monk en 1954.mp3
* jpqs-2012-03-02-Charlie Christian (1939).mp3
* jpqs-2012-03-07-Jay Jay Johnson.mp3
* jpqs-2012-03-09-Billie Holiday.mp3
* jpqs-2012-03-14-Quincy Jones.mp3
* jpqs-2012-03-16-Cab Calloway.mp3
* jpqs-2012-03-21-Gigi Gryce.mp3
* jpqs-2012-03-23-Benny Carter.mp3
* jpqs-2012-03-28-Thelonious Monk.mp3
* jpqs-2012-03-30-Duke Ellington en 1958.mp3
* jpqs-2012-04-02-Buddy Rich y su big band.mp3
* jpqs-2012-04-04-Harold Land (1955 y 1956).mp3
* jpqs-2012-04-06-Fats Waller.mp3
* jpqs-2012-04-09-Kenny Barron.mp3
* jpqs-2012-04-11-Dexter Gordon con Tete Montoliu.mp3
* jpqs-2012-04-13-Fletcher Henderson.mp3
* jpqs-2012-04-16-Herbie Mann.mp3
* jpqs-2012-04-18-Lee Morgan.mp3
* jpqs-2012-04-20-Claude Luter.mp3
* jpqs-2012-04-23-Grant Stewart.mp3
* jpqs-2012-04-25-Thelonious Monk (1954).mp3
* jpqs-2012-04-27-Duke Ellington (1958).mp3
* jpqs-2012-04-30-Art Pepper.mp3
* jpqs-2012-05-02-Philly Joe Jones (1956).mp3
* jpqs-2012-05-04-Charlie Christian.mp3
* jpqs-2012-05-07-Lester Young (1956).mp3
* jpqs-2012-05-09-Stan Kenton.mp3
* jpqs-2012-05-11-Count Basie.mp3
* jpqs-2012-05-14-Woody Herman.mp3
* jpqs-2012-05-16-Wardell Gray (1948 y 1949).mp3
* jpqs-2012-05-18-Django Reinhardt (1940).mp3
* jpqs-2012-05-21-Miles Davis.mp3
* jpqs-2012-05-23-Modern Jazz Quartet.mp3
* jpqs-2012-05-25-Duke Ellington (1958).mp3
* jpqs-2012-05-28-Barney Wilen.mp3
* jpqs-2012-05-30-Thelonious Monk.mp3
* jpqs-2012-06-01-Billie Holiday.mp3
* jpqs-2012-06-04-Stan Getz.mp3
* jpqs-2012-06-06-Art Farmer (1989).mp3
* jpqs-2012-06-08-Cab Calloway (1944).mp3
* jpqs-2012-06-11-Woody Shaw.mp3
* jpqs-2012-06-13-Clifford Brown.mp3
* jpqs-2012-06-15-Benny Carter.mp3
* jpqs-2012-06-18-Dexter Gordon (1976).mp3
* jpqs-2012-06-20-John Coltrane.mp3
* jpqs-2012-06-22-Fats Waller.mp3
* jpqs-2012-06-25-J.L. Ponty, Eddy Louiss y D. Humair.mp3
* jpqs-2012-06-27-Discos variados.mp3
* jpqs-2012-06-29-Discos variados.mp3
* jpqs-2012-07-02-Shelly Manne.mp3
* jpqs-2012-07-04-Dizzy Gillespie en 1952.mp3
* jpqs-2012-07-06-Fletcher Henderson.mp3
* jpqs-2012-07-09-Don Byas.mp3
* jpqs-2012-07-11-Jackie McLean.mp3
* jpqs-2012-07-13-Charlie Christian.mp3
* jpqs-2012-07-16-Pat Metheny.mp3
* jpqs-2012-07-18-Jay Jay Johnson (1957).mp3
* jpqs-2012-07-20-Count Basie (1957).mp3
* jpqs-2012-07-23-Wynton Kelly.mp3
* jpqs-2012-07-27-Duke Ellington.mp3
* jpqs-2012-07-30-The Jazz Crusaders.mp3
* jpqs-2012-08-01-Wardell Gray.mp3
* jpqs-2012-08-03-Django Reinhardt.mp3
* jpqs-2012-08-06-Sonny Rollins.mp3
* jpqs-2012-08-08-Gigi Gryce.mp3
* jpqs-2012-08-10-Billie Holiday.mp3
* jpqs-2012-08-13-Dave Douglas.mp3
* jpqs-2012-08-15-Harold Land (1956).mp3
* jpqs-2012-08-17-Louis Armstrong (1954).mp3
* jpqs-2012-08-20-Chris Speed.mp3
* jpqs-2012-08-22-Dexter Gordon con Tete Montoliu.mp3
* jpqs-2012-08-24-Cab Calloway.mp3
* jpqs-2012-08-27-Concierto de Donat Fisch.mp3
* jpqs-2012-08-29-Thelonious Monk (1955-1956).mp3
* jpqs-2012-08-31-Duke Ellington (1959).mp3
* jpqs-2012-09-03-Concierto de Moncef Genou.mp3
* jpqs-2012-09-05-Lee Morgan.mp3
* jpqs-2012-09-07-Benny Carter.mp3
* jpqs-2012-09-10-Kurt Elling.mp3
* jpqs-2012-09-12-Philly Joe Jones.mp3
* jpqs-2012-09-14-Fats Waller.mp3
* jpqs-2012-09-17-Don Friedman.mp3
* jpqs-2012-09-19-Stan Kenton.mp3
* jpqs-2012-09-21-Charlie Christian.mp3
* jpqs-2012-09-24-Dave Douglas.mp3
* jpqs-2012-09-26-Thelonious Monk (1956).mp3
* jpqs-2012-09-28-Duke Ellington (1959).mp3
* jpqs-2012-10-01-Dave Holland.mp3
* jpqs-2012-10-03-John Coltrane (1958).mp3
* jpqs-2012-10-05-Count Basie (1957 y 1958).mp3
* jpqs-2012-10-08-Django Bates.mp3
* jpqs-2012-10-10-Milt Jackson y John Lewis.mp3
* jpqs-2012-10-12-Django Reinhardt (1940).mp3
* jpqs-2012-10-15-Karel Ruzicka.mp3
* jpqs-2012-10-17-Art Farmer (1989).mp3
* jpqs-2012-10-19-Billie Holiday (1952).mp3
* jpqs-2012-10-22-Karel Ruzicka.mp3
* jpqs-2012-10-24-Clifford Brown (1953).mp3
* jpqs-2012-10-26-Duke Ellington (1959).mp3
* jpqs-2012-10-29-Abdullah Ibrahim.mp3
* jpqs-2012-10-31-Thelonious Monk (1956).mp3
* jpqs-2012-11-02-Louis Armstrong (1954 y 1955).mp3
* jpqs-2012-11-05-Andy Emler.mp3
* jpqs-2012-11-12-Concierto de Gwilym Simcock.mp3
* jpqs-2012-11-16-Benny Carter (1961).mp3
* jpqs-2012-11-19-Nils Wülker.mp3
* jpqs-2012-11-21-Jay Jay Johnson (1957).mp3
* jpqs-2012-11-23-Fats Waller (1934 y 1935).mp3
* jpqs-2012-11-26-Jukka Eskola.mp3
* jpqs-2012-11-28-Thelonious Monk.mp3
* jpqs-2012-11-30-Duke Ellington (1959 y 1960).mp3
* jpqs-2012-12-03-Gilad Hekselman y Mark Turner.mp3
* jpqs-2012-12-05-Wardell Gray.mp3
* jpqs-2012-12-07-Charlie Christian.mp3
* jpqs-2012-12-10-Ronnie Cuber.mp3
* jpqs-2012-12-12-Wardell Gray (1950).mp3
* jpqs-2012-12-14-Count Basie (1958).mp3
* jpqs-2012-12-17-Florian Weber.mp3
* jpqs-2012-12-19-Harold Land (1956 y 1957).mp3
* jpqs-2012-12-21-Django Reinhardt (1941).mp3
* jpqs-2012-12-24-Concierto de Lou Donaldson.mp3
* jpqs-2012-12-26-Thelonious Monk.mp3
* jpqs-2012-12-28-Duke Ellington.mp3
* jpqs-2012-12-31-Miloslav Suchomel.mp3
* jpqs-2013-01-04-Billie Holiday (1952).mp3
* jpqs-2013-01-07-Jarek Bothur y Piotr Baron.mp3
* jpqs-2013-01-09-Dexter Gordon (1964).mp3
* jpqs-2013-01-11-Louis Armstrong (1955).mp3
* jpqs-2013-01-14-John Scofield en Praga.mp3
* jpqs-2013-01-16-Spike Robinson.mp3
* jpqs-2013-01-18-Cab Calloway.mp3
* jpqs-2013-01-21-Eric Barret.mp3
* jpqs-2013-01-23-Lee Morgan.mp3
* jpqs-2013-01-25-Duke Ellington (1960).mp3
* jpqs-2013-01-28-Concierto UER:Raise Four.mp3
* jpqs-2013-01-30-Thelonious Monk (1957).mp3
* jpqs-2013-01-31-Benny Carter (1961).mp3
* jpqs-2013-02-04-Concierto de Paul Lay.mp3
* jpqs-2013-02-06-Philly Joe Jones.mp3
* jpqs-2013-02-08-Fats Waller.mp3
* jpqs-2013-02-11-Concierto UER: Olivier Temime.mp3
* jpqs-2013-02-13-Stan Kenton (1945).mp3
* jpqs-2013-02-15-Charlie Christian (1941).mp3
* jpqs-2013-02-18-Wanja Slavin.mp3
* jpqs-2013-02-20-The Modern Jazz Quartet.mp3
* jpqs-2013-02-22-Duke Ellington.mp3
* jpqs-2013-02-25-François Corneloup.mp3
* jpqs-2013-02-27-Thelonious Monk (1957).mp3
* jpqs-2013-03-01-Count Basie.mp3
* jpqs-2013-03-04-Stéphane Kerecki.mp3
* jpqs-2013-03-06-Charles Tolliver.mp3
* jpqs-2013-03-08-Django Reinhardt (1940 - 1941).mp3
* jpqs-2013-03-11-Marc Ducret.mp3
* jpqs-2013-03-13-Terence Blanchard.mp3
* jpqs-2013-03-15-Billie Holiday (1952).mp3
* jpqs-2013-03-18-Christophe Monniot.mp3
* jpqs-2013-03-20-Gil Evans.mp3
* jpqs-2013-03-22-Louis Armstrong.mp3
* jpqs-2013-03-25-Antonio Ciacca.mp3
* jpqs-2013-03-27-Thelonious Monk (1957).mp3
* jpqs-2013-03-29-Terry , Golsen , Ferguson ....mp3
* jpqs-2013-04-01-Nathalie Loriers.mp3
* jpqs-2013-04-03-Bill Potts.mp3
* jpqs-2013-04-05-Cab Calloway.mp3
* jpqs-2013-04-08-Maxime Bender.mp3
* jpqs-2013-04-10-Art Farmer.mp3
* jpqs-2013-04-12-Lionel Hampton.mp3
* jpqs-2013-04-15-Ambrose Akinmusire.mp3
* jpqs-2013-04-17-Joe Romano.mp3
* jpqs-2013-04-19-Benny Carter (1962).mp3
* jpqs-2013-04-22-Uri Caine.mp3
* jpqs-2013-04-24-Thelonious Monk.mp3
* jpqs-2013-04-26-Duke Ellington.mp3
* jpqs-2013-04-29-Stéphane Belmondo.mp3
* jpqs-2013-05-01-Clifford Brown.mp3
* jpqs-2013-05-03-Fats Waller.mp3
* jpqs-2013-05-06-Rhoda Scott.mp3
* jpqs-2013-05-08-John Coltrane (1958).mp3
* jpqs-2013-05-10-Charlie Christian (1941).mp3
* jpqs-2013-05-13-UER: Belgrade Jazz Trio.mp3
* jpqs-2013-05-15-Dizzy Gillespie.mp3
* jpqs-2013-05-17-Count Basie.mp3
* jpqs-2013-05-20-Homenaje a Gil Evans.mp3
* jpqs-2013-05-22-Jackie McLean.mp3
* jpqs-2013-05-24-Django Reinhardt.mp3
* jpqs-2013-05-27-Sambeat, Colina y Miralta.mp3
* jpqs-2013-05-29-Thelonious Monk y Gerry Mulligan.mp3
* jpqs-2013-05-31-Duke Ellington & Louis Armstrong.mp3
* jpqs-2013-06-03-Rainer Tempel.mp3
* jpqs-2013-06-05-Jay Jay Johnson.mp3
* jpqs-2013-06-07-Billie Holiday.mp3
* jpqs-2013-06-10-Gil Evans.mp3
* jpqs-2013-06-12-Wardell Gray.mp3
* jpqs-2013-06-17-Nighthawks.mp3
* jpqs-2013-06-21-Cab Calloway (1949-1954).mp3
* jpqs-2013-06-24-Músicos de jazz españoles.mp3
* jpqs-2013-06-26-Thelonious Monk.mp3
* jpqs-2013-06-28-Duke Ellington.mp3
* jpqs-2013-07-01-Concierto de Martin Tingvall.mp3
* jpqs-2013-07-03-Harold Land.mp3
* jpqs-2013-07-05-Harry James.mp3
* jpqs-2013-07-08-Anne Paceo y Sean Levitt.mp3
* jpqs-2013-07-12-Jimmie Lunceford.mp3
* jpqs-2013-07-15-Kçstutis Vaiginis.mp3
* jpqs-2013-07-17-Nick Brignola.mp3
* jpqs-2013-07-19-Benny Carter.mp3
* jpqs-2013-07-24-Charles McPherson.mp3
* jpqs-2013-07-26-Duke Ellington (1961).mp3
* jpqs-2013-07-29-Stefano Bollani.mp3
* jpqs-2013-07-31-Thelonious Monk (1957).mp3
* jpqs-2013-08-02-Fats Waller (1935).mp3
* jpqs-2013-08-05-John Scofield.mp3
* jpqs-2013-08-07-Lee Morgan.mp3
* jpqs-2013-08-09-Charlie Christian.mp3
* jpqs-2013-08-12-Progressive Patriots.mp3
* jpqs-2013-08-14-Philly Joe Jones.mp3
* jpqs-2013-08-16-Count Basie.mp3
* jpqs-2013-08-19-Sébastien Texier.mp3
* jpqs-2013-08-21-Stan Kenton.mp3
* jpqs-2013-08-23-Bob Crosby.mp3
* jpqs-2013-08-26-Jazzworkers' Quintet.mp3
* jpqs-2013-08-28-Thelonious Monk.mp3
* jpqs-2013-08-30-Duke Ellington.mp3
* jpqs-2013-09-02-Patrice Caratini.mp3
* jpqs-2013-09-04-The Modern Jazz Quartet.mp3
* jpqs-2013-09-06-Django Reinhardt.mp3
* jpqs-2013-09-09-Philippe Macé.mp3
* jpqs-2013-09-11-Art Farmer.mp3
* jpqs-2013-09-13-Billie Holiday.mp3
* jpqs-2013-09-16-PRYSM.mp3
* jpqs-2013-09-18-Clifford Brown.mp3
* jpqs-2013-09-20-Ben Webster.mp3
* jpqs-2013-09-25-Thelonious Monk.mp3
* jpqs-2013-09-27-Duke Ellington.mp3
* jpqs-2013-09-30-En memoria de François Chassagnite.mp3
* jpqs-2013-10-02-John Coltrane (1958).mp3
* jpqs-2013-10-04-Louis Armstrong (1955).mp3
* jpqs-2013-10-07-Concierto UER: Denis Charolles.mp3
* jpqs-2013-10-09-Yusef Lateef.mp3
* jpqs-2013-10-11-Fats Waller.mp3
* jpqs-2013-10-14-Jacques Schwarz-Bart.mp3
* jpqs-2013-10-16-Art Blakey.mp3
* jpqs-2013-10-21-UER: Jacques Schwarz-Bart (2).mp3
* jpqs-2013-10-23-Gary McFarland (1933-1971).mp3
* jpqs-2013-10-25-Duke Ellington (1962).mp3
* jpqs-2013-10-28-Concierto UER: Emile Parisien.mp3
* jpqs-2013-11-01-Charlie Christian.mp3
* jpqs-2013-11-04-Django Bates.mp3
* jpqs-2013-11-08-Count Basie.mp3
* jpqs-2013-11-11-Sebastian Gille.mp3
* jpqs-2013-11-13-Jackie McLean.mp3
* jpqs-2013-11-15-Django Reinhardt.mp3
* jpqs-2013-11-18-Concierto UER: Paul Zauner.mp3
* jpqs-2013-11-20-Jay Jay Johnson.mp3
* jpqs-2013-11-22-Billie Holiday.mp3
* jpqs-2013-11-25-Concierto de Donny McCaslin.mp3
* jpqs-2013-11-29-Duke Ellington.mp3
* jpqs-2013-12-02-Donny McCaslin.mp3
* jpqs-2013-12-04-Jim Hall.mp3
* jpqs-2013-12-06-Louis Armstrong.mp3
* jpqs-2013-12-09-Inner Spaces.mp3
* jpqs-2013-12-11-McCoy Tyner.mp3
* jpqs-2013-12-13-Benny Carter.mp3
* jpqs-2013-12-16-Scott Colley.mp3
* jpqs-2013-12-18-Wardell Gray.mp3
* jpqs-2013-12-20-Fats Waller.mp3
* jpqs-2013-12-23-Uri Caine.mp3
* jpqs-2013-12-25-Thelonious Monk (1958).mp3
* jpqs-2013-12-27-Duke Ellington (1962).mp3
* jpqs-2013-12-30-Conciertos UER: Donat Fisch.mp3
* jpqs-2014-01-01-Jay Jay Johnson (1957).mp3
* jpqs-2014-01-03-Charlie Christian (1940).mp3
* jpqs-2014-01-06-Concierto de Hilaria Kramer.mp3
* jpqs-2014-01-08-Harold Land.mp3
* jpqs-2014-01-10-Count Basie.mp3
* jpqs-2014-01-13-UER: Ravi Coltrane.mp3
* jpqs-2014-01-15-Dexter Gordon (1965).mp3
* jpqs-2014-01-17-Django Reinhardt (1943 y 1944).mp3
* jpqs-2014-01-20-Bobby Broom.mp3
* jpqs-2014-01-22-Lee Morgan.mp3
* jpqs-2014-01-24-Billie Holiday.mp3
* jpqs-2014-01-27-Concierto de Jim Rotondi.mp3
* jpqs-2014-01-29-Thelonious Monk.mp3
* jpqs-2014-01-31-Duke Ellington.mp3
* jpqs-2014-02-03-Concierto UER.mp3
* jpqs-2014-02-05-Philly Joe Jones (1956).mp3
* jpqs-2014-02-07-Louis Armstrong (1955).mp3
* jpqs-2014-02-10-Herb Geller.mp3
* jpqs-2014-02-12-Stan Kenton.mp3
* jpqs-2014-02-14-Benny Carter (1967).mp3
* jpqs-2014-02-17-Jellyfish Jazz Orchestra.mp3
* jpqs-2014-02-19-The Modern Jazz Quartet.mp3
* jpqs-2014-02-21-Fats Waller.mp3
* jpqs-2014-02-24-Kenny Garrett.mp3
* jpqs-2014-02-26-Thelonious Monk (1958).mp3
* jpqs-2014-02-28-Duke Ellington (1962).mp3
* jpqs-2014-03-03-Kenny Garrett.mp3
* jpqs-2014-03-05-Art Farmer (1977).mp3
* jpqs-2014-03-07-Charlie Christian.mp3
* jpqs-2014-03-10-Hayden Chisholm (1ª parte).mp3
* jpqs-2014-03-12-Charlie Parker.mp3
* jpqs-2014-03-14-Count Basie.mp3
* jpqs-2014-03-17-Hayden Chisholm.mp3
* jpqs-2014-03-19-Lennie Tristano.mp3
* jpqs-2014-03-21-Django Reinhardt (1944-1945).mp3
* jpqs-2014-03-24-Takeo Moriyama.mp3
* jpqs-2014-03-26-Thelonious Monk (1958).mp3
* jpqs-2014-03-28-Duke Ellington (1962).mp3
* jpqs-2014-03-31-Concierto de Fumio Itabashi.mp3
* jpqs-2014-04-02-Buddy Rich.mp3
* jpqs-2014-04-04-Billie Holiday.mp3
* jpqs-2014-04-07-Timo Lassy.mp3
* jpqs-2014-04-09-Clifford Brown (1954).mp3
* jpqs-2014-04-11-Louis Armstrong.mp3
* jpqs-2014-04-14-Kevin Dean.mp3
* jpqs-2014-04-16-John Coltrane (1958).mp3
* jpqs-2014-04-18-Benny Carter (1975).mp3
* jpqs-2014-04-21-Concierto de Boyan Vodenitcharov.mp3
* jpqs-2014-04-23-Red Garland.mp3
* jpqs-2014-04-25-Duke Ellington.mp3
* jpqs-2014-04-28-Concierto UER: Dave Douglas.mp3
* jpqs-2014-04-30-Thelonious Monk.mp3
* jpqs-2014-05-02-Fats Waller.mp3
* jpqs-2014-05-05-Dave Douglas.mp3
* jpqs-2014-05-07-Dizzy Gillespie (1953).mp3
* jpqs-2014-05-09-Charlie Christian.mp3
* jpqs-2014-05-12-Concierto de Rembrandt Frerichs.mp3
* jpqs-2014-05-14-Jackie McLean.mp3
* jpqs-2014-05-16-Count Basie.mp3
* jpqs-2014-05-19-Jazz Baltica Ensemble.mp3
* jpqs-2014-05-21-Jay Jay Johnson (1958).mp3
* jpqs-2014-05-23-Django Reinhardt (1945).mp3
* jpqs-2014-05-26-The Bad Plus.mp3
* jpqs-2014-05-28-Thelonious Monk (1959).mp3
* jpqs-2014-05-30-Duke Ellington (1962).mp3
* jpqs-2014-06-02-Concierto de Samúel Jón Samúelsson.mp3
* jpqs-2014-06-04-Wardell Gray (1921-1955).mp3
* jpqs-2014-06-06-Billie Holiday (1915-1959).mp3
* jpqs-2014-06-09-Samúel Jón Samúelsson (2).mp3
* jpqs-2014-06-11-Shelly Manne.mp3
* jpqs-2014-06-13-Benny Goodman.mp3
* jpqs-2014-06-16-Max Von Mosch.mp3
* jpqs-2014-06-18-Harold Land.mp3
* jpqs-2014-06-20-Louis Armstrong.mp3
* jpqs-2014-06-23-Concierto UER: Rudresh Mahanthappa.mp3
* jpqs-2014-06-27-Duke Ellington.mp3
* jpqs-2014-06-30-Gran orquesta de jazz de la Radio Búlgara.mp3
* jpqs-2014-07-02-Ahmad Jamal.mp3
* jpqs-2014-07-04-Benny Carter (1907-2003).mp3
* jpqs-2014-07-07-Concierto UER: Ondrej Stveracek. 1ª parte.mp3
* jpqs-2014-07-09-Dexter Gordon (1965).mp3
* jpqs-2014-07-11-Fats Waller (1936).mp3
* jpqs-2014-07-14-Concierto UER: Ondrej Stveracek.mp3
* jpqs-2014-07-16-Dizzy Gillespie (1953).mp3
* jpqs-2014-07-18-Charlie Christian.mp3
* jpqs-2014-07-21-Enrico Pieranunzi en concierto (1ª parte).mp3
* jpqs-2014-07-23-Richie Kamuca.mp3
* jpqs-2014-07-25-Duke Ellington: "Money Jungle".mp3
* jpqs-2014-07-28-Concierto UER: Enrico Pieranunzi.mp3
* jpqs-2014-07-30-Thelonious Monk (1959).mp3
* jpqs-2014-08-01-Count Basie.mp3
* jpqs-2014-08-04-Cuarteto de Jiri Stivin.mp3
* jpqs-2014-08-06-Lee Morgan.mp3
* jpqs-2014-08-08-Django Reinhardt.mp3
* jpqs-2014-08-11-Edward Maclean.mp3
* jpqs-2014-08-13-Mulgrew Miller.mp3
* jpqs-2014-08-15-Billie Holiday en el Carnegie Hall de Nueva York.mp3
* jpqs-2014-08-18-Concierto UER: Kari Ikonen.mp3
* jpqs-2014-08-20-Thad Jones (1923-1986).mp3
* jpqs-2014-08-22-Louis Armstrong (1901-1971).mp3
* jpqs-2014-08-25-Anna-Lena Schnabel.mp3
* jpqs-2014-08-27-Thelonious Monk (1959).mp3
* jpqs-2014-08-29-Duke Ellington (1962).mp3
* jpqs-2014-09-01-Conicerto de la UER: Omer Klein (2014).mp3
* jpqs-2014-09-03-Philly Joe Jones.mp3
* jpqs-2014-09-05-Benny Carter.mp3
* jpqs-2014-09-08-Bill Frisell.mp3
* jpqs-2014-09-10-Stan Kenton (1912-1979).mp3
* jpqs-2014-09-12-Thomas "Fats" Waller (1904-1943).mp3
* jpqs-2014-09-15-Jack DeJohnette (1942).mp3
* jpqs-2014-09-17-John Lewis.mp3
* jpqs-2014-09-19-Charlie Christian.mp3
* jpqs-2014-09-22-Christoph Spangenberg.mp3
* jpqs-2014-09-24-Thelonious Monk (1917-1982).mp3
* jpqs-2014-09-26-Duke Ellington.mp3
* jpqs-2014-09-29-Medeski, Martin & Wood.mp3
* jpqs-2014-10-01-Lester Young (1909-1959).mp3
* jpqs-2014-10-06-Dave Holland.mp3
* jpqs-2014-10-08-Harry Edison.mp3
* jpqs-2014-10-13-Terry Gibbs.mp3
* jpqs-2014-10-15-Count Basie (1904-1984).mp3
* jpqs-2014-10-20-Art Farmer.mp3
* jpqs-2014-10-22-Django Reinhardt (1910-1953).mp3
* jpqs-2014-10-27-Thelonious Monk (1917-1982).mp3
* jpqs-2014-10-29-Duke Ellington (1962).mp3
* jpqs-2014-11-03-Eddie Davis.mp3
* jpqs-2014-11-05-Billie Holiday (1957).mp3
* jpqs-2014-11-10-Clifford Brown (1954).mp3
* jpqs-2014-11-12-Buck Clayton.mp3
* jpqs-2014-11-17-John Coltrane (1958).mp3
* jpqs-2014-11-19-Tommy Dorsey.mp3
* jpqs-2014-11-24-Thelonious Monk.mp3
* jpqs-2014-11-26-Duke Ellington (1962).mp3
* jpqs-2014-12-01-Dizzy Gillespie.mp3
* jpqs-2014-12-03-Las Boswell Sisters.mp3
* jpqs-2014-12-08-Jimmy Smith.mp3
* jpqs-2014-12-10-Louis Armstrong.mp3
* jpqs-2014-12-15-Jackie McLean.mp3
* jpqs-2014-12-17-Benny Carter.mp3
* jpqs-2014-12-22-Jay Jay Johnson.mp3
* jpqs-2014-12-24-Fats Waller (1936-1937).mp3
* jpqs-2014-12-29-Thelonious Monk.mp3
* jpqs-2014-12-31-Duke Ellington.mp3
* jpqs-2015-01-05-Charles Mingus.mp3
* jpqs-2015-01-07-Lester Young.mp3
* jpqs-2015-01-12-Wardell Gray.mp3
* jpqs-2015-01-14-Count Basie.mp3
* jpqs-2015-01-19-J.R. Monterose.mp3
* jpqs-2015-01-21-Benny Goodman.mp3
* jpqs-2015-01-26-Thelonious Monk.mp3
* jpqs-2015-01-28-Duke Ellington.mp3
* jpqs-2015-02-02-Stan Getz.mp3
* jpqs-2015-02-04-Django Reinhardt.mp3
* jpqs-2015-02-09-Harold Land.mp3
* jpqs-2015-02-11-Billie Holiday (1957).mp3
* jpqs-2015-02-16-Louie Bellson (1924-2009).mp3
* jpqs-2015-02-18-Benny Carter (1980).mp3
* jpqs-2015-02-23-Thelonious Monk (1917-1982).mp3
* jpqs-2015-02-25-Duke Ellington (1899-1974).mp3
* jpqs-2015-03-02-Dexter Gordon.mp3
* jpqs-2015-03-04-Fats Waller.mp3
* jpqs-2015-03-09-Lee Morgan.mp3
* jpqs-2015-03-11-Coleman Hawkins.mp3
* jpqs-2015-03-16-Philly Joe Jones.mp3
* jpqs-2015-03-18-Lester Young.mp3
* jpqs-2015-03-30-Thelonious Monk (1917-1982).mp3
* jpqs-2015-04-06-Gerry Mulligan (1927-1996).mp3
* jpqs-2015-04-27-Thelonious Monk (1963).mp3
* jpqs-NA-este lunes-The Modern Jazz Quartet (1960).mp3
* jpqs-NA-pasado lunes-Horace Silver (1928-2014).mp3

### Caveats
* For the sake of simplicity, the cleanup of temporary files (*.tmp) must be performed manually.
* The script is idempotent in that it will not download files already on disk based on their filenames, no checksumming is performed
* The script is not flushing podcasts to disk in chunks, it'll fit it all in RAM

### Acknowledgments
* Juan Claudio "Cifu" Cifuentes (Paris, 1941 - Madrid, 2015). Love and respect. Rest in Peace.
