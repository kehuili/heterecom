import java.util.ArrayList;

// this is a general node class for all types of nodes in the network
/*
 * member classes are
 * movie type 0
 * actor type 1
 * genre type 2
 * director type 3
 * */
public abstract class SimNode {

	private int id;
	private String data;
	private ArrayList<SimNode> neighbors = new ArrayList<SimNode>();
	
	public SimNode(String id, String data){
		int idint = Integer.parseInt(id);
		this.id = idint;
		this.data = data;
	}
	
	// getters
	public int getId(){return this.id;}
	public String getData(){return this.data;}
	public ArrayList<SimNode> getNeighbors(){return this.neighbors;}
	
	
	// setters
	public void setId(String id){
		int idint = Integer.parseInt(id);
		this.id = idint;
	}
	
	public void setData(String data){
		this.data = data;
	}
	
	public void setNeighbors(SimNode node){
		this.neighbors.add(node);
	}
}
