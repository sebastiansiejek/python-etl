Celem zadania jest napisanie aplikacji, która:

wczyta dane z plików zawierających dane dotyczące artystów, ich utworów oraz odsłuchań,
przekształci dane w taki sposób by można było je umieścić w bazie danych (np. SQlite),
wypisze na standardowe wyjście informacje, takie jak: artysta z największą liczbą odsłuchań, 5 najpopularniejszych utworów oraz czas przetwarzania danych.
Źródło danych:

plik unique_tracks.txt - zawiera dane w następującym formacie: identyfikator wykonania<SEP>identyfikator utworu<SEP>nazwa artysty<SEP>tytuł utworu<LF> i można go pobrać z https://softmaz.xyz/wsb/rsc/unique_tracks.zip
plik triplets_sample_20p.txt - zawiera dane w następującym formacie: identyfikator użytkownika<SEP>identyfikator utworu<SEP>datę odsłuchania<LF> i można pobrać go z https://softmaz.xyz/wsb/rsc/triplets_sample_20p.zip.
Program nie może wczytywać całych plików do pamięci. Mijałoby się to z celem zadania. Można wykorzystywać dowolne biblioteki. Program ma tworzyć nową bazę SQLite i wstawiać do niej dane. Odpowiedzi na pytania mają być wyświetlone w konsoli. Odpowiedzi mogą być zarówno generowane przez odpowiednie zapytanie SQL jak i poprzez odpowiedni skrypt pythona.

Ocenie będzie podlegała również jakość kodu i jego zgodność ze standardem PEP8. Rozwiązanie należy przesłać w postaci kodu źródłowego (jeden lub więcej plików) a także pliku requirements.txt, zawierającego informacje o pakietach koniecznych do uruchomienia. Brak tego pliku oznaczać będzie, że projekt uruchamiany będzie tylko z biblioteką standardową. Programy, które nie zadziałają, otrzymują 0 punktów. Całość projektu należy spakować do archiwum.

Składowe oceny: 20% zgodność ze standardem PEP8, 40% ładowanie danych do bazy, 40% udzielenie odpowiedzi na pytania. Zgodność ze standardem oceniana jest poprzez pylint (i jego punktacja jest odpowiednio skalowana).

`pip freeze > requirments.txt`