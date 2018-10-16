package observer;

public class WeatherStation {
    public static void main(String[] agrs){
        WeatherData weatherData = new WeatherData();

        ForecastDisplay forecastDisplay = new ForecastDisplay(weatherData);
        StatisticsDisplay statisticsDisplay = new StatisticsDisplay(weatherData);
        CurrentConditionsDisplay currentConditionsDisplay =
                new CurrentConditionsDisplay(weatherData);

        weatherData.setMeasurements(80, 65, 30.4f);
        System.out.println("\n");
        weatherData.setMeasurements(82, 63, 24.9f);
        System.out.println("\n");
        weatherData.setMeasurements(89, 62, 32.1f);
    }
}
