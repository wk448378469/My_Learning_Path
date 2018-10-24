package facade;

public class HomeTheaterTestDrive {
    public static void main(String[] args){
        Amplifier amplifier = new Amplifier("Top-O-Line Amplifier");
        Tuner tuner = new Tuner("Top-O-Line AM/FM Tuner", amplifier);
        DvdPlayer dvdPlayer = new DvdPlayer("Top-O-Line DVD Player", amplifier);
        CdPlayer cdPlayer = new CdPlayer("Top-O-Line CD Player", amplifier);
        Projector projector = new Projector("Top-O-Line Projector", dvdPlayer);
        TheaterLights lights = new TheaterLights("Theater Ceiling Lights");
        Screen screen = new Screen("Theater Screen");
        PopcornPopper popper = new PopcornPopper("Popcorn Popper");

        HomeTheaterFacade homeTheaterFacade = new HomeTheaterFacade(amplifier, tuner, dvdPlayer, cdPlayer, projector, screen, lights, popper);

        homeTheaterFacade.watchMovie("F***************k");
        homeTheaterFacade.endMovie();

        homeTheaterFacade.listenToCd("Kamikaze");
        homeTheaterFacade.endCd();
    }
}
