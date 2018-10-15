import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;


enum GuessResult{
    Hot,
    Equal,
    Cold,
    FirstGuess
}

public class Game{
    /*
        for home work 1.4.34
    */
    public int N;
    public int SecretNumber;
    private int LastGuess;

    public Game(int N)
    {
        this.N = N;
        this.SecretNumber = StdRandom.uniform(N-1);
        this.LastGuess = -1;
    }

    public GuessResult Guess(int guess)
    {
        if (guess == this.SecretNumber) return GuessResult.Equal;
        if (this.LastGuess == -1) 
        {
            this.LastGuess = guess;
            return GuessResult.FirstGuess;
        }

        int lastDiff = Math.abs(this.LastGuess - this.SecretNumber);
        this.LastGuess = guess;
        int nowDiff = Math.abs(guess - this.SecretNumber);
        if (nowDiff > lastDiff) return GuessResult.Cold;
        else                    return GuessResult.Hot;
    }

    public void Restart()
    {
        this.LastGuess = -1;
    }

    public static void main(String[] args)
    {
        Game game = new Game(10);
        int tryTimes = 0;
        int hi = game.N;
        int lo = 1;
        while(lo <= hi)
        {
            int mid = lo + (hi - lo) / 2;
            GuessResult guessResult = game.Guess(lo);
            tryTimes++;

            if (guessResult == GuessResult.Equal)
            {
                StdOut.println("secret number is: " + lo);
                StdOut.println("use times is: " + tryTimes);
                break;
            }

            guessResult = game.Guess(hi);
            tryTimes++;
            if (guessResult == GuessResult.Equal)
            {
                StdOut.println("secret number is: " + hi);
                StdOut.println("use times is: " + tryTimes);
                break;
            }
            else if (guessResult == GuessResult.Hot) lo = mid;
            else                                     hi = mid;
        }
    }
}