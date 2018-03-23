CP=cython3
CPFLAGS=-I../gui -I../decoder -I../tables -3 --cplus
CC=g++
CFLAGS=   -I/usr/include/python3.5m -I/usr/include/x86_64-linux-gnu/python3.5m
GETFLAGS=$(pkg-config --libs --cflags python3)
LDFLAGS= -lpython3.5m

EXEC=Chrono

OBJS=	obj/__main__.o \
		obj/decoder/cano.o \
		obj/decoder/simulator.o \
		obj/decoder/tagV3.o \
		obj/gui/MainWindow.o \
		obj/gui/Set_RacerTp.o \
		obj/gui/Ui_MainWindow.o \
		obj/gui/Ui_set_RaceLen.o \
		obj/gui/Ui_Set_RacerTp.o \
		obj/tables/T_Concurrents.o \
		obj/tables/T_Marques.o \
		obj/tables/T_ModelCourses.o \
		obj/tables/T_Pays.o \
		obj/tables/T_Ville.o \
		obj/db.o \
		obj/decoder_task.o \
		obj/Globals.o \
		obj/manage.o \
		obj/manageRace.o \
		obj/Preferences.o \
		obj/receive.o

all: $(EXEC)

Chrono: $(OBJS)

	$(CC) -o Chrono  $(LDFLAGS) $(OBJS)

clean:
	rm -rf *.o

mrproper: clean
	rm -rf $(EXEC)

__main__.cc: ../__main__.py
	$(CP) $(CPFLAGS) -o __main__.cc   ../__main__.py --embed

obj/__main__.o: __main__.cc
	$(CC) -o obj/__main__.o -c __main__.cc $(CFLAGS)

#../console/best_lap.py
#../console/read_tp.py
#../console/receive.py
decoder/cano.cc:			../decoder/cano.py
	$(CP) $(CPFLAGS) -o decoder/cano.cc   ../decoder/cano.py

obj/decoder/cano.o: decoder/cano.cc
	$(CC) -o obj/decoder/cano.o -c decoder/cano.cc $(CFLAGS)

decoder/simulator.cc: 		../decoder/simulator.py
	$(CP) $(CPFLAGS) -o decoder/simulator.cc   ../decoder/simulator.py

obj/decoder/simulator.o: decoder/simulator.cc
	$(CC) -o obj/decoder/simulator.o -c decoder/simulator.cc $(CFLAGS)

decoder/tagV3.cc:			../decoder/tagV3.py
	$(CP) $(CPFLAGS) -o decoder/tagV3.cc   ../decoder/tagV3.py

obj/decoder/tagV3.o: decoder/tagV3.cc
	$(CC) -o obj/decoder/tagV3.o -c decoder/tagV3.cc $(CFLAGS)

gui/MainWindow.cc:			../gui/MainWindow.py
	$(CP) $(CPFLAGS) -o gui/MainWindow.cc   ../gui/MainWindow.py

obj/gui/MainWindow.o: gui/MainWindow.cc
	$(CC) -o obj/gui/MainWindow.o -c gui/MainWindow.cc $(CFLAGS)

gui/Set_RacerTp.cc:			../gui/Set_RacerTp.py
	$(CP) $(CPFLAGS) -o gui/Set_RacerTp.cc   ../gui/Set_RacerTp.py

obj/gui/Set_RacerTp.o: gui/Set_RacerTp.cc
	$(CC) -o obj/gui/Set_RacerTp.o -c gui/Set_RacerTp.cc $(CFLAGS)

gui/Ui_MainWindow.cc:		../gui/Ui_MainWindow.py
	$(CP) $(CPFLAGS) -o gui/Ui_MainWindow.cc   ../gui/Ui_MainWindow.py

obj/gui/Ui_MainWindow.o: gui/Ui_MainWindow.cc
	$(CC) -o obj/gui/Ui_MainWindow.o -c gui/Ui_MainWindow.cc $(CFLAGS)

gui/Ui_set_RaceLen.cc:		../gui/Ui_set_RaceLen.py
	$(CP) $(CPFLAGS) -o gui/Ui_set_RaceLen.cc   ../gui/Ui_set_RaceLen.py

obj/gui/Ui_set_RaceLen.o: gui/Ui_set_RaceLen.cc
	$(CC) -o obj/gui/Ui_set_RaceLen.o -c gui/Ui_set_RaceLen.cc $(CFLAGS)

gui/Ui_Set_RacerTp.cc:		../gui/Ui_Set_RacerTp.py
	$(CP) $(CPFLAGS) -o gui/Ui_Set_RacerTp.cc   ../gui/Ui_Set_RacerTp.py

obj/gui/Ui_Set_RacerTp.o: gui/Ui_Set_RacerTp.cc
	$(CC) -o obj/gui/Ui_Set_RacerTp.o -c gui/Ui_Set_RacerTp.cc $(CFLAGS)

tables/T_Concurrents.cc:		../tables/T_Concurrents.py
	$(CP) $(CPFLAGS) -o tables/T_Concurrents.cc   ../tables/T_Concurrents.py

obj/tables/T_Concurrents.o: tables/T_Concurrents.cc
	$(CC) -o obj/tables/T_Concurrents.o -c tables/T_Concurrents.cc $(CFLAGS)

tables/T_Marques.cc:		../tables/T_Marques.py
	$(CP) $(CPFLAGS) -o tables/T_Marques.cc   ../tables/T_Marques.py

obj/tables/T_Marques.o: tables/T_Marques.cc
	$(CC) -o obj/tables/T_Marques.o -c tables/T_Marques.cc $(CFLAGS)

tables/T_ModelCourses.cc:	../tables/T_ModelCourses.py
	$(CP) $(CPFLAGS) -o tables/T_ModelCourses.cc   ../tables/T_ModelCourses.py

obj/tables/T_ModelCourses.o: tables/T_ModelCourses.cc
	$(CC) -o obj/tables/T_ModelCourses.o -c tables/T_ModelCourses.cc $(CFLAGS)

tables/T_Pays.cc:			../tables/T_Pays.py
	$(CP) $(CPFLAGS) -o tables/T_Pays.cc   ../tables/T_Pays.py

obj/tables/T_Pays.o: tables/T_Pays.cc
	$(CC) -o obj/tables/T_Pays.o -c tables/T_Pays.cc $(CFLAGS)

tables/T_Ville.cc:			../tables/T_Ville.py
	$(CP) $(CPFLAGS) -o tables/T_Ville.cc   ../tables/T_Ville.py

obj/tables/T_Ville.o: tables/T_Ville.cc
	$(CC) -o obj/tables/T_Ville.o -c tables/T_Ville.cc $(CFLAGS)

db.cc:					../db.py
	$(CP) $(CPFLAGS) -o db.cc   ../db.py

obj/db.o: db.cc
	$(CC) -o obj/db.o -c db.cc $(CFLAGS)

decoder_task.cc:			../decoder_task.py
	$(CP) $(CPFLAGS) -o decoder_task.cc   ../decoder_task.py

obj/decoder_task.o: decoder_task.cc
	$(CC) -o obj/decoder_task.o -c decoder_task.cc $(CFLAGS)

Globals.cc:				../Globals.py
	$(CP) $(CPFLAGS) -o Globals.cc   ../Globals.py

obj/Globals.o: Globals.cc
	$(CC) -o obj/Globals.o -c Globals.cc $(CFLAGS)

manage.cc:				../manage.py
	$(CP) $(CPFLAGS) -o manage.cc   ../manage.py

obj/manage.o: manage.cc
	$(CC) -o obj/manage.o -c manage.cc $(CFLAGS)

manageRace.cc:				../manageRace.py
	$(CP) $(CPFLAGS) -o manageRace.cc   ../manageRace.py

obj/manageRace.o: manageRace.cc
	$(CC) -o obj/manageRace.o -c manageRace.cc $(CFLAGS)

Preferences.cc:			../Preferences.py
	$(CP) $(CPFLAGS) -o Preferences.cc   ../Preferences.py

obj/Preferences.o: Preferences.cc
	$(CC) -o obj/Preferences.o -c Preferences.cc $(CFLAGS)


#../raceTask.py
receive.cc:				../receive.py
	$(CP) $(CPFLAGS) -o receive.cc   ../receive.py

obj/receive.o: receive.cc
	$(CC) -o obj/receive.o -c receive.cc $(CFLAGS)

