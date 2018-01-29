
public class GenreNode extends SimNode{
	private int type;
	
	public GenreNode(String id, String data){
		super(id, data);
		this.type = 2;
	}
	
	public int getType(){return this.type;}

}
