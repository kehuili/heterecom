import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		Network movieNet = new Network(new File("movie.txt"), new File("actor.txt"), 
				new File("director.txt"), new File("genre.txt"), new File("relation.txt"));
		movieNet.connect();
		
		movieNet.calculatePXY_APTPA(2); 
		movieNet.calculatePXX_APTPA();
		
		ArrayList<MovieNode> similarMovies = movieNet.PathSim_APTPA();
		for(int i = 0; i < 10; i++){
			int n = similarMovies.size();
			System.out.println(similarMovies.get(n - i - 1).getData() + '\t' + similarAuthors.get(n-i-1).get_sim_APTPA());
		}
		
	}
}

