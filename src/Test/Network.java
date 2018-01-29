import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class Network {
	private HashMap<Integer, MovieNode> movies = new HashMap<Integer, MovieNode>();
	private HashMap<Integer, ActorNode> actors = new HashMap<Integer, ActorNode>();
	private HashMap<Integer, GenreNode> genres = new HashMap<Integer, GenreNode>();
	private HashMap<Integer, DirectorNode> directors = new HashMap<Integer, DirectorNode>();
	private ArrayList<String[]> relations = new ArrayList<String[]>();
	
	public Network(File movieFile, File actorFile, File genreFile, File directorFile, File relationFile) throws IOException{
		ArrayList<String[]> movieList = TextParser.splitFile(movieFile);
		ArrayList<String[]> actorList = TextParser.splitFile(actorFile);
		ArrayList<String[]> genreList = TextParser.splitFile(genreFile);
		ArrayList<String[]> directorList = TextParser.splitFile(directorFile);
		this.relations = TextParser.splitFile(relationFile);
		
		this.movies = TextParser.movieList2Table(movieList);
		this.actors = TextParser.actorList2Table(actorList);
		this.genres = TextParser.genreList2Table(genreList);
		this.directors = TextParser.directorList2Table(directorList);
	}
	
	public void connect(){
		for(String[] relation : relations){
			int actorID = Integer.valueOf(relation[0]); 
			ActorNode actor = actors.get(actorID);
			Integer key = new Integer(relation[1]); 
			if(movies.containsKey(key) && movies.get(key).getType() == 0){ 
				MovieNode movie = movies.get(key);
				actor.setNeighbors(movie);
				movie.setNeighbors(actor);
			}
			else if(genres.containsKey(key) && genres.get(key).getType() == 2){ 
				GenreNode genre = genres.get(key);
				genre.setNeighbors(actor);
				actor.setNeighbors(genre);
			}
			else if(directors.containsKey(key) && directors.get(key).getType() == 3){ 
				DirectorNode director = directors.get(key);
				director.setNeighbors(actor);
				actor.setNeighbors(director);
			}
		}
	}
	
	public void calculatePXY_APVPA(Integer xid){
		MovieNode x = movies.get(xid);
		ArrayList<SimNode> xneighbors = x.getNeighbors();
		for(SimNode aneighbor : xneighbors){ 
			if(aneighbor instanceof ActorNode){ 
				ArrayList<SimNode> pneighbors = aneighbor.getNeighbors();
				for(SimNode pneighbor : pneighbors){
					if(pneighbor instanceof GenreNode){ 
						ArrayList<SimNode> vneighbors = pneighbor.getNeighbors();
						for(SimNode vneighbor : vneighbors){
							if(vneighbor instanceof ActorNode){ 
								ArrayList<SimNode> prneighbors = vneighbor.getNeighbors();
								for(SimNode prneighbor : prneighbors){
									if(prneighbor instanceof MovieNode){ 
										((MovieNode) prneighbor).incrementOPath();
									}
								} 
							}
						} 
					}
				} 
			}
		} 
	}
	
	public void calculatePXX_APVPA(Integer xid){
		MovieNode x = movies.get(xid);
		ArrayList<SimNode> xneighbors = x.getNeighbors();
		for(SimNode aneighbor : xneighbors){ 
			if(aneighbor instanceof ActorNode){ 
				ArrayList<SimNode> pneighbors = aneighbor.getNeighbors();
				for(SimNode pneighbor : pneighbors){
					if(pneighbor instanceof GenreNode){ 
						ArrayList<SimNode> vneighbors = pneighbor.getNeighbors();
						for(SimNode vneighbor : vneighbors){
							if(vneighbor instanceof ActorNode){ 
								ArrayList<SimNode> prneighbors = vneighbor.getNeighbors();
								for(SimNode prneighbor : prneighbors){
									if(prneighbor.equals(x)){ 
										x.incrementSPath();
									}
								} 
							}
						} 
					}
				} 
			}
		} 
	}
	
	
	public void calculatePXX_APVPA(){
		for(MovieNode movie : movies.values()){
			calculatePXX_APVPA(movie.getId());
		}
	}
	
	public ArrayList<MovieNode> PathSim_APVPA(){
		MovieNode x = movies.get(2); 
		int pxx = x.getSPath();
		ArrayList<MovieNode> ret = new ArrayList<MovieNode>(); 
		for(MovieNode movie : movies.values()){
			int dividend = 2 * movie.getOPath();
			int divisor = pxx + movie.getSPath();
			double sim = divisor == 0 ? 0 : ((double)dividend / divisor);
			movie.set_sim_APVPA(sim);
			ret.add(movie);
		}
		Collections.sort(ret);
		return ret;
	}
	
	public void calculatePXY_APTPA(Integer xid){
		MovieNode x = movies.get(xid);
		ArrayList<SimNode> xneighbors = x.getNeighbors();
		for(SimNode aneighbor : xneighbors){ 
			if(aneighbor instanceof ActorNode){ 
				ArrayList<SimNode> pneighbors = aneighbor.getNeighbors();
				for(SimNode pneighbor : pneighbors){
					if(pneighbor instanceof DirectorNode){
						ArrayList<SimNode> vneighbors = pneighbor.getNeighbors();
						for(SimNode vneighbor : vneighbors){
							if(vneighbor instanceof ActorNode){
								ArrayList<SimNode> prneighbors = vneighbor.getNeighbors();
								for(SimNode prneighbor : prneighbors){
									if(prneighbor instanceof MovieNode){ 
										((MovieNode) prneighbor).incrementOPath();
									}
								} 
							}
						} 
					}
				} 
			}
		} 
	}
	
	public void calculatePXX_APTPA(Integer xid){
		MovieNode x = movies.get(xid);
		ArrayList<SimNode> xneighbors = x.getNeighbors();
		for(SimNode aneighbor : xneighbors){
			if(aneighbor instanceof ActorNode){ 
				ArrayList<SimNode> pneighbors = aneighbor.getNeighbors();
				for(SimNode pneighbor : pneighbors){
					if(pneighbor instanceof DirectorNode){ 
						ArrayList<SimNode> vneighbors = pneighbor.getNeighbors();
						for(SimNode vneighbor : vneighbors){
							if(vneighbor instanceof ActorNode){
								ArrayList<SimNode> prneighbors = vneighbor.getNeighbors();
								for(SimNode prneighbor : prneighbors){
									if(prneighbor.equals(x)){ 
										x.incrementSPath();
									}
								} 
							}
						} 
					}
				} 
			}
		} 
	}
	
	
	public void calculatePXX_APTPA(){
		for(MovieNode movie : movies.values()){
			calculatePXX_APTPA(movie.getId());
		}
	}
	
	public ArrayList<MovieNode> PathSim_APTPA(){
		MovieNode x = movies.get(2); 
		int pxx = x.getSPath();
		ArrayList<MovieNode> ret = new ArrayList<MovieNode>(); 
		for(MovieNode movie : movies.values()){
			int dividend = 2 * movie.getOPath();
			int divisor = pxx + movie.getSPath();
			double sim = divisor == 0 ? 0 : ((double)dividend / divisor);
			movie.set_sim_APTPA(sim);
			ret.add(movie);
		}
		Collections.sort(ret);
		return ret;
	}
	
}





